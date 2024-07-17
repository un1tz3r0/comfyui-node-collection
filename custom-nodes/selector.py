#

"""
@author:˶𝞢⤬⫒ⵖsᐼ˶
@title: Selector
@nickname: Selector
@project: "https://github.com/exdysa/comfyui-selector",
@description: Preset aspect ratios and inference parameters.
"""

import comfy.samplers

class selectah:
    
    # dimensions sourced from: https://arxiv.org/abs/2307.01952
    # & https://github.com/Stability-AI/generative-models
    RATIO = [
        ("1:1___SD 512x512", 512, 512),
        ("4:3___SD 682x512", 682, 512),
        ("3:2___SD 768x512", 768, 512),
        ("16:9__SD 910x512", 910, 512),
        ("1:85:1 SD 952x512", 952, 512),
        ("2:1___SD 1024x512", 1024, 512),
        ("1:1_SV3D 576x576", 576, 576),
        ("16:9_SVD 576x1024", 1024, 576),
        ("1:1__SD2 768x768", 768, 768),
        ("1:1___XL 1024x1024", 1024, 1024),
        ("16:15_XL 1024x960", 1024, 960),
        ("17:15_XL 1088x960", 1088, 960),
        ("17:14_XL 1088x896", 1088, 896),
        ("4:3___XL 1152x896", 1152, 896),
        ("18:13_XL 1152x832", 1152, 832),
        ("3:2___XL 1216x832", 1216, 832),
        ("5:3___XL 1280x768", 1280, 768),
        ("7:4___XL 1344x768", 1344, 768),
        ("21:11_XL 1344x704", 1344, 704),
        ("2:1___XL 1408x704", 1408, 704),
        ("23:11_XL 1472x704", 1472, 704),
        ("21:9__XL 1536x640", 1536, 640),
        ("5:2___XL 1600x640", 1600, 640),
        ("26:9__XL 1664x576", 1664, 576),
        ("3:1___XL 1728x576", 1728, 576),
        ("28:9__XL 1792x576", 1792, 576),
        ("29:8__XL 1856x512", 1856, 512),
        ("15:4__XL 1920x512", 1920, 512),
        ("31:8__XL 1984x512", 1984, 512),
        ("4:1___XL 2048x512", 2048, 512),
    ]

    @classmethod
    def INPUT_TYPES(cls):
        aspect_ratio_titles = [title for title, res1, res2 in cls.RATIO]
        rotation = ("landscape", "portrait")
        
        return {
            "required": {
                "aR": (aspect_ratio_titles,
                    {"default": ("1:1___XL 1024x1024")}),
                "rotation": (rotation,),
            },
            "optional": {
                "batch": 
                    ("INT", {"default": 1, "min": 1, "max": 10000,}),
                "steps": 
                    ("INT", {"default": 20, "min": 1, "max": 10000,}),
                "refiner_steps":
                    ("INT", {"default": 20, "min": 1, "max": 10000,}),
                "cfg": ("FLOAT",{
                         "default": 1.0,
                         "min": -10.0,
                         "max": 100.0,
                         "step": 0.1,
                         "round": 0.1,
                }),
                "refiner_cfg": ("FLOAT", {
                        "default": 1.0,
                        "min": -10.0,
                        "max": 100.0,
                        "step": 0.1,
                        "round": 0.1,
                }),
                "str_denoise": ("FLOAT", {
                        "default": 1.000,
                        "min": -10.000,
                        "max": 100.000,
                        "step": 0.001,
                        "round": 0.01,
                 }),
                "scale_factor": ("FLOAT", {
                        "default": 2.0,
                        "min": 1.0,
                        "max": 10.0,
                        "step": 0.1,
                        "round": 0.1,
                }),
                "sampler": (comfy.samplers.KSampler.SAMPLERS,),
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS,)
            }
        }   
    RETURN_TYPES = (
        "INT", "INT", "INT", "INT", "INT", "FLOAT",
        "FLOAT", "FLOAT", "FLOAT",comfy.samplers.KSampler.SAMPLERS,
        comfy.samplers.KSampler.SCHEDULERS,)
        
    RETURN_NAMES = (
        "WIDTH",
        "HEIGHT",
        "BATCH_SIZE",
        "STEPS",
        "REFINER_STEPS",
        "CFG",
        "REFINER_CFG",
        "STRENGTH",
        "SCALE",
        "SAMPLER",
        "SCHEDULER",
    )
    FUNCTION = "selectah"
    CATEGORY = "image"

    def selectah(self, aR, rotation, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale_factor, sampler, scheduler):
        for title, width, height in self.RATIO:
            if title == aR:
                if rotation == "portrait":
                    width, height = height, width  # Swap for portrait orientation
                return (width, height, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale_factor, sampler, scheduler)
        return (None, None, batch, steps, refiner_steps, cfg, refiner_cfg, str_denoise, scale_factor, sampler, scheduler)  # In case the aspect ratio is not found

NODE_CLASS_MAPPINGS = { "Selector": selectah, }
NODE_DISPLAY_NAME_MAPPINGS = { "Selector": "Selector...       ⠑⠭⠙⠽⠎⠁" }
