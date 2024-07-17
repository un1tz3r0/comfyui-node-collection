
import os
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import json
import numpy as np
import folder_paths
import datetime


class IntToText:
    """
    This node convert int to float
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
            "int_val": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff, "defaultBehavior": "input"}),
        }
    }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "fun"
    CATEGORY = "alek"

    def fun(self, int_val):
        return (str(int_val),)


class SeedWithText:
    """
    This node generate seeds for the model
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "prefix": ("STRING", {"multiline": False, "default": "out", "defaultBehavior": "input"}),
                "seperator": ("STRING", {"multiline": False, "default": "_", "defaultBehavior": "input"}),
            }
        }

    RETURN_TYPES = ("INT", "STRING", "STRING")
    RETURN_NAMES = ("Seed", "Seed as Text", "File prefix")
    FUNCTION = "fun"
    CATEGORY = "alek"

    def fun(self, seed, prefix, seperator):
        return (seed, str(seed), f"{prefix}{seperator}{seed}")


class SaveImage:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()
        self.type = "output"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE", ),
                "filename_prefix": ("STRING", {"default": "ComfyUI"})
            },
            "hidden": {
                "prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO"
            },
        }

    RETURN_TYPES = ()
    FUNCTION = "save_images"

    OUTPUT_NODE = True

    CATEGORY = "alkemann"

    def save_images(self, images, filename_prefix="ComfyUI", prompt=None, extra_pnginfo=None):

        def get_next_number(directory):
            files = os.listdir(directory)
            highest_number = 0
            for file in files:
                parts = file.split('-')
                try:
                    num = int(parts[0])
                    if num > highest_number:
                        highest_number = num
                except ValueError:
                    # If it's not a number, skip this file
                    continue

            # Return the next number
            return highest_number + 1
        
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        full_output_folder = os.path.join(self.output_dir, today)
        subfolder = os.path.dirname(os.path.normpath(today))
        os.makedirs(full_output_folder, exist_ok=True)

        if os.path.commonpath((self.output_dir, os.path.abspath(full_output_folder))) != self.output_dir:
            print("Saving image outside the output folder is not allowed.")
            return {}

        counter = get_next_number(full_output_folder)

        results = list()
        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            metadata = PngInfo()
            if prompt is not None:
                metadata.add_text("prompt", json.dumps(prompt))
            if extra_pnginfo is not None:
                for x in extra_pnginfo:
                    metadata.add_text(x, json.dumps(extra_pnginfo[x]))

            file = f"{counter:05}-c-{filename_prefix}.png"
            img.save(os.path.join(full_output_folder, file), pnginfo=metadata, compress_level=4)
            results.append({
                "filename": file,
                "subfolder": full_output_folder,
                "type": self.type
            })
            counter += 1

        return { "ui": { "images": results } }

    
    
NODE_CLASS_MAPPINGS = {
    "Int to Text": IntToText,
    "Seed With Text": SeedWithText,
    "Save A1 Image": SaveImage
}
