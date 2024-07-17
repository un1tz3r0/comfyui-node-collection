import torch

import comfy.diffusers_convert
import comfy.samplers
import comfy.sd
import comfy.utils

import comfy.clip_vision

import comfy.model_management


def common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent, denoise=1.0, disable_noise=False, start_step=None, last_step=None, force_full_denoise=False):
    latent_image = latent["samples"]
    noise_mask = None
    device = comfy.model_management.get_torch_device()

    if disable_noise:
        noise = torch.zeros(latent_image.size(
        ), dtype=latent_image.dtype, layout=latent_image.layout, device=device)
    else:
        batch_index = 0
        if "batch_index" in latent:
            batch_index = latent["batch_index"]

        generator = torch.manual_seed(seed)
        for i in range(batch_index):
            noise = torch.randn([1] + list(latent_image.size())[1:], dtype=latent_image.dtype,
                                layout=latent_image.layout, generator=generator, device=device)
        noise = torch.randn(latent_image.size(), dtype=latent_image.dtype,
                            layout=latent_image.layout, generator=generator, device=device)

    if "noise_mask" in latent:
        noise_mask = latent['noise_mask']
        noise_mask = torch.nn.functional.interpolate(
            noise_mask[None, None,], size=(noise.shape[2], noise.shape[3]), mode="bilinear")
        noise_mask = noise_mask.round()
        noise_mask = torch.cat([noise_mask] * noise.shape[1], dim=1)
        noise_mask = torch.cat([noise_mask] * noise.shape[0])
        noise_mask = noise_mask.to(device)

    real_model = None
    comfy.model_management.load_model_gpu(model)
    real_model = model.model

    noise = noise.to(device)
    latent_image = latent_image.to(device)

    positive_copy = []
    negative_copy = []

    control_nets = []

    def get_models(cond):
        models = []
        for c in cond:
            if 'control' in c[1]:
                models += [c[1]['control']]
            if 'gligen' in c[1]:
                models += [c[1]['gligen'][1]]
        return models

    for p in positive:
        t = p[0]
        if t.shape[0] < noise.shape[0]:
            t = torch.cat([t] * noise.shape[0])
        t = t.to(device)
        positive_copy += [[t] + p[1:]]
    for n in negative:
        t = n[0]
        if t.shape[0] < noise.shape[0]:
            t = torch.cat([t] * noise.shape[0])
        t = t.to(device)
        negative_copy += [[t] + n[1:]]

    models = get_models(positive) + get_models(negative)
    comfy.model_management.load_controlnet_gpu(models)

    if sampler_name in comfy.samplers.KSampler.SAMPLERS:
        sampler = comfy.samplers.KSampler(real_model, steps=steps, device=device, sampler=sampler_name,
                                          scheduler=scheduler, denoise=denoise, model_options=model.model_options)
    else:
        # other samplers
        pass

    samples = sampler.sample(noise, positive_copy, negative_copy, cfg=cfg, latent_image=latent_image,
                             start_step=start_step, last_step=last_step, force_full_denoise=force_full_denoise, denoise_mask=noise_mask)
    samples = samples.cpu()
    for m in models:
        m.cleanup()

    out = latent.copy()
    out["samples"] = samples
    return (out, )


class KSampler:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {"model": ("MODEL",),
                 "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                 "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                 "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                 "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                 "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                 "positive": ("CONDITIONING", ),
                 "negative": ("CONDITIONING", ),
                 "latent_image": ("LATENT", ),
                 "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
                 }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"

    CATEGORY = "sampling"

    def sample(self, model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=1.0):
        return common_ksampler(model, seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise)


class KSamplerAdvanced:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                {"model": ("MODEL",),
                 "add_noise": (["enable", "disable"], ),
                 "noise_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                 "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                 "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                 "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                 "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                 "positive": ("CONDITIONING", ),
                 "negative": ("CONDITIONING", ),
                 "latent_image": ("LATENT", ),
                 "start_at_step": ("INT", {"default": 0, "min": 0, "max": 10000}),
                 "end_at_step": ("INT", {"default": 10000, "min": 0, "max": 10000}),
                 "return_with_leftover_noise": (["disable", "enable"], ),
                 }}

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "sample"

    CATEGORY = "sampling"

    def sample(self, model, add_noise, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, start_at_step, end_at_step, return_with_leftover_noise, denoise=1.0):
        force_full_denoise = True
        if return_with_leftover_noise == "enable":
            force_full_denoise = False
        disable_noise = False
        if add_noise == "disable":
            disable_noise = True
        return common_ksampler(model, noise_seed, steps, cfg, sampler_name, scheduler, positive, negative, latent_image, denoise=denoise, disable_noise=disable_noise, start_step=start_at_step, last_step=end_at_step, force_full_denoise=force_full_denoise)


NODE_CLASS_MAPPINGS = {
    "KSamplerGPU": KSampler,
    "KSamplerAdvancedGPU": KSamplerAdvanced,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    # Sampling
    "KSamplerGPU": "KSampler GPU",
    "KSamplerAdvancedGPU": "KSampler (Advanced) GPU",
}
