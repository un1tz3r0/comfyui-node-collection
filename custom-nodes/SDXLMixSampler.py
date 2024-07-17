
import comfy.samplers
import nodes
import latent_preview
import torch

class SDXLMixSampler:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required":
                    {
                        "base_model": ("MODEL",),
                        "ref_model": ("MODEL",),
                        "noise_seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                        "total_loop": ("INT", {"default": 1, "min": 1.0, "max": 200, "step": 1.0}),
                        "base_steps_percentage": ("FLOAT", {"default": 65.0, "min": 0.0, "max": 100.0, "step": 1.0}),
                        "mixing_steps": ("INT", {"default": 20, "min": 10.0, "step": 1.0}),
                        "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                        "sampler_name": (comfy.samplers.KSampler.SAMPLERS, ),
                        "scheduler": (comfy.samplers.KSampler.SCHEDULERS, ),
                        "base_positive": ("CONDITIONING", ),
                        "base_negative": ("CONDITIONING", ),
                        "refiner_positive": ("CONDITIONING", ),
                        "refiner_negative": ("CONDITIONING", ),
                        "latent_image": ("LATENT", ),
                        "denoise": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 1.0, "step": 0.1}),
                        "final_only": (["yes", "no"], {"default": "yes"}),
                        # "return_base_latent": (["disable", "enable"], {"default": "disable"}),
                        # "return_each_loop": (["disable", "enable"], {"default": "enable"}),
                        # "add_noise": (["enable", "disable"], ),
                        # "start_at_step": ("INT", {"default": 0, "min": 0, "max": 10000}),
                        # "end_at_step": ("INT", {"default": 10000, "min": 0, "max": 10000}),
                        # "return_with_leftover_noise": (["disable", "enable"], ),
                     }
                }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "SDXLMixSampler"

    CATEGORY = "JNode"

    def SDXLMixSampler(self, base_model,ref_model,noise_seed,total_loop,base_steps_percentage,mixing_steps,cfg,sampler_name,scheduler,base_positive,base_negative,refiner_positive,refiner_negative,latent_image,denoise,final_only):
        # loop = 1
        out = latent_image.copy()
        result = None

        print(f"Total loop: {int(total_loop)}")
        for loop_index in range(int(total_loop)):
            if final_only == "yes":
                if loop_index != int(total_loop)-1:
                    continue
            loop = loop_index+1
            print(f"loop: {int(loop)}")
            disable_noise = False
            total_steps = mixing_steps * loop
            # print(f"total_steps: {int(total_steps)}")
            # print(f"mixing_steps: {int(mixing_steps)}")
            # if total_steps > mixing_steps:
            #     loop = total_steps / mixing_steps

            for i in range(int(loop)):
                force_full_denoise = False
                # add_noise only at the first base modal
                if i == 0 and denoise == 1.0:
                    disable_noise = False
                # base 0,13
                base_start_at_step = int(i * mixing_steps)
                base_end_at_step = int(base_start_at_step) + int(mixing_steps * base_steps_percentage / 100)
                print(f"noise_seed: {noise_seed},total_steps: {total_steps},cfg: {cfg},sampler_name: {sampler_name},scheduler: {scheduler},disable_noise: {disable_noise},base_start_at_step: {base_start_at_step},base_end_at_step: {base_end_at_step},force_full_denoise: {force_full_denoise}")
                # print('latent_image',latent_image)
                base_result = nodes.common_ksampler(base_model, noise_seed, total_steps, cfg, sampler_name, scheduler, base_positive, base_negative, latent_image, denoise=denoise, disable_noise=disable_noise, 
                                            start_step=base_start_at_step, last_step=base_end_at_step, force_full_denoise=force_full_denoise)
                # print('base_result',base_result)
                latent_image = base_result[0]
                # base_latent = latent_image["samples"]

                # disable_noise after base model
                disable_noise = True

                if i == int(loop)-1:
                    force_full_denoise = True

                # result += (latent_image,)
                # refiner 13,20
                refiner_start_at_step = int(base_end_at_step)
                refiner_end_at_step = int((i+1) * mixing_steps)
                print(f"noise_seed: {noise_seed},total_steps: {total_steps},cfg: {cfg},sampler_name: {sampler_name},scheduler: {scheduler},disable_noise: {disable_noise},refiner_start_at_step: {refiner_start_at_step},refiner_end_at_step: {refiner_end_at_step},force_full_denoise: {force_full_denoise}")
                refiner_result = nodes.common_ksampler(ref_model, noise_seed, total_steps, cfg, sampler_name, scheduler, refiner_positive, refiner_negative, latent_image, denoise=denoise, disable_noise=disable_noise, 
                                            start_step=refiner_start_at_step, last_step=refiner_end_at_step, force_full_denoise=force_full_denoise)
                
                latent_image = refiner_result[0]
            if result is None:
                result = latent_image["samples"]
            else:
                result = torch.cat((result,latent_image["samples"]),0)
        
        
        out["samples"] = result
        return (out,)


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "SDXLMixSampler": SDXLMixSampler
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "JNode": "SDXLMixSampler"
}
