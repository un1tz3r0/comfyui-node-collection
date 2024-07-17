from PIL import Image
from io import BytesIO
import folder_paths as comfy_paths
import hashlib
import numpy as np
import os
import requests
import torch

class cstr(str):
    class color:
        END = '\33[0m'
        BOLD = '\33[1m'
        ITALIC = '\33[3m'
        UNDERLINE = '\33[4m'
        BLINK = '\33[5m'
        BLINK2 = '\33[6m'
        SELECTED = '\33[7m'

        BLACK = '\33[30m'
        RED = '\33[31m'
        GREEN = '\33[32m'
        YELLOW = '\33[33m'
        BLUE = '\33[34m'
        VIOLET = '\33[35m'
        BEIGE = '\33[36m'
        WHITE = '\33[37m'

        BLACKBG = '\33[40m'
        REDBG = '\33[41m'
        GREENBG = '\33[42m'
        YELLOWBG = '\33[43m'
        BLUEBG = '\33[44m'
        VIOLETBG = '\33[45m'
        BEIGEBG = '\33[46m'
        WHITEBG = '\33[47m'

        GREY = '\33[90m'
        LIGHTRED = '\33[91m'
        LIGHTGREEN = '\33[92m'
        LIGHTYELLOW = '\33[93m'
        LIGHTBLUE = '\33[94m'
        LIGHTVIOLET = '\33[95m'
        LIGHTBEIGE = '\33[96m'
        LIGHTWHITE = '\33[97m'

        GREYBG = '\33[100m'
        LIGHTREDBG = '\33[101m'
        LIGHTGREENBG = '\33[102m'
        LIGHTYELLOWBG = '\33[103m'
        LIGHTBLUEBG = '\33[104m'
        LIGHTVIOLETBG = '\33[105m'
        LIGHTBEIGEBG = '\33[106m'
        LIGHTWHITEBG = '\33[107m'

        @staticmethod
        def add_code(name, code):
            if not hasattr(cstr.color, name.upper()):
                setattr(cstr.color, name.upper(), code)
            else:
                raise ValueError(f"'cstr' object already contains a code with the name '{name}'.")

    def __new__(cls, text):
        return super().__new__(cls, text)

    def __getattr__(self, attr):
        if attr.lower().startswith("_cstr"):
            code = getattr(self.color, attr.upper().lstrip("_cstr"))
            modified_text = self.replace(f"__{attr[1:]}__", f"{code}")
            return cstr(modified_text)
        elif attr.upper() in dir(self.color):
            code = getattr(self.color, attr.upper())
            modified_text = f"{code}{self}{self.color.END}"
            return cstr(modified_text)
        elif attr.lower() in dir(cstr):
            return getattr(cstr, attr.lower())
        else:
            raise AttributeError(f"'cstr' object has no attribute '{attr}'")

    def print(self, **kwargs):
        print(self, **kwargs)

TEXT_TYPE = "STRING"
class BrevLoadImage:
    def __init__(self):
        self.input_dir = comfy_paths.input_directory

    @classmethod
    def INPUT_TYPES(cls):
        return {
                "required": {
                    "image_path": ("STRING", {"default": './ComfyUI/input/example.png', "multiline": False}),
                    "RGBA": (["false","true"],),
                },
                "optional": {
                    "filename_text_extension": (["true", "false"],),
                }
            }

    RETURN_TYPES = ("IMAGE", "MASK", TEXT_TYPE)
    RETURN_NAMES = ("image", "mask", "filename_text")
    FUNCTION = "load_image"

    CATEGORY = "BrevMage"

    def load_image(self, image_path, RGBA='false', filename_text_extension="true"):

        RGBA = (RGBA == 'true')

        if image_path.startswith('http'):
            from io import BytesIO
            i = self.download_image(image_path)
        else:
            try:
                i = Image.open(image_path)
            except OSError:
                cstr(f"The image `{image_path.strip()}` specified doesn't exist!").error.print()
                i = Image.new(mode='RGB', size=(512, 512), color=(0, 0, 0))
        if not i:
            return

        # Update history
        # update_history_images(image_path)

        image = i
        if not RGBA:
            image = image.convert('RGB')
        image = np.array(image).astype(np.float32) / 255.0
        image = torch.from_numpy(image)[None,]

        if 'A' in i.getbands():
            mask = np.array(i.getchannel('A')).astype(np.float32) / 255.0
            mask = 1. - torch.from_numpy(mask)
        else:
            mask = torch.zeros((64, 64), dtype=torch.float32, device="cpu")

        if filename_text_extension == "true":
            filename = os.path.basename(image_path)
            print(filename)
        else:
            filename = os.path.splitext(os.path.basename(image_path))[0]
            print(filename)

        return (image, mask, filename)

    def download_image(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            img = Image.open(BytesIO(response.content))
            return img
        except requests.exceptions.HTTPError as errh:
            cstr(f"HTTP Error: ({url}): {errh}").error.print()
        except requests.exceptions.ConnectionError as errc:
            cstr(f"Connection Error: ({url}): {errc}").error.print()
        except requests.exceptions.Timeout as errt:
            cstr(f"Timeout Error: ({url}): {errt}").error.print()
        except requests.exceptions.RequestException as err:
            cstr(f"Request Exception: ({url}): {err}").error.print()

    @classmethod
    def IS_CHANGED(cls, image_path):
        if image_path.startswith('http'):
            return float("NaN")
        m = hashlib.sha256()
        with open(image_path, 'rb') as f:
            m.update(f.read())
        return m.digest().hex()
    
NODE_CLASS_MAPPINGS = {
    "BrevImage": BrevLoadImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BrevImage": "BrevImage Node"
}
