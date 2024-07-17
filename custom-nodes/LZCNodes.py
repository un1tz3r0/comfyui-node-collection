from PIL import Image, ImageDraw, ImageFont
import torchvision.transforms as transforms
import numpy as np
from torchvision.transforms.functional import to_pil_image
import torch
import cv2 
import tensorflow as tf
import torchvision.transforms as transforms
from torchvision.utils import save_image
from  torchvision import utils as vutils
import folder_paths
import os

class make_transparentmask:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    "image1": ("IMAGE",),
                    "image2": ("IMAGE",),
                }   
        }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    CATEGORY = "Hayo_nodes"
    FUNCTION = "make_white_transparent"

    def tensor2pil(self,image):  
        return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
    
    def pil2tensor(self,image):
        return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
    
    def create_transparent_image(self, image1, image2):

        arr1 = np.array(image1)
        arr2 = np.array(image2)

        black_areas = np.all(arr1[:, :, :3] == 0, axis=-1)

        arr2[black_areas, 3] = 0

        result_img = Image.fromarray(arr2)

        return result_img

    def make_white_transparent(self, image1,image2):

        image = image2
        print(type(image1))
        print(image1.mode)
        image1 = self.tensor2pil(image1)
        print(type(image1))
        image1 = image1.convert("RGBA")
        print(image1.mode)

        print(type(image2))
        print(image2.mode)
        image2 = self.tensor2pil(image2)
        print(type(image2))
        image2 = image2.convert("RGBA")
        print(image2.mode)

        result_image = self.create_transparent_image(image1,image2)
        print(type(result_image))
        result_image_path = '/data/ComfyUI/custom_nodes/modified_image.png'
        result_image.save(result_image_path)
        image = self.pil2tensor(result_image)
        return (result_image,)

class LoadPILImage:
    @classmethod
    def INPUT_TYPES(s):
        input_dir = folder_paths.get_input_directory()
        files = [f for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]
        return {"required":
                    {"image": (sorted(files), {"image_upload": True})},
                }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ('image',)
    CATEGORY = "Hayo_nodes"

    FUNCTION = "load_PILimage"



    def load_PILimage(self, image):
        image_path = folder_paths.get_annotated_filepath(image)
        i = Image.open(image_path)
        return (i,)
    
class MergeImages:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image1": ("IMAGE",),
                "image2": ("IMAGE",),
            },
        }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ('merged_image',)
    CATEGORY = "Hayo_nodes"

    FUNCTION = "merge"

    sd15 = 512
    sdxl = 1024
    image_size = sdxl

    def get_image_channels(self,image_path):
        with Image.open(image_path) as img:
            if img.mode == 'RGBA':
                num_channels = 4
            elif img.mode == 'RGB':
                num_channels = 3
            return num_channels
        
    def image_mod_convert(self,img):
        image = img.convert("RGBA")
        return image
    
    def resize_and_pad(self,image_path):
        original_image = Image.open(image_path)
        new_image = Image.new("RGBA", (self.image_size, self.image_size), (0, 0, 0, 0))
        x = (self.image_size - original_image.width) // 2
        y = (self.image_size - original_image.height) // 2
        new_image.paste(original_image, (x, y), original_image)
        return new_image
    
    def image_merge(self,image1, image2):
        merged_image = Image.alpha_composite(image1, image2)
        return (merged_image)
    
    def image_mod_size_standard(self,image_path):
        image = Image.open(image_path)
        image_num = self.get_image_channels(image_path)
        if image_num == 3:
            image = self.image_mod_convert(image)
        if image.size[0] != self.image_size or image.size[1] != self.image_size:
            image = self.resize_and_pad(image_path)
        return image
    
    def tensor2pil(self,image):  
        return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
    
    def pil2tensor(self,image):
        return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

    def merge(self, image1, image2):

        print(f"type of image1 {type(image1)}")
        # print(image1.mode)
        # image1 = self.tensor2pil(image1)
        # print(type(image1))
        # image1 = image1.convert("RGBA")
        print(image1.mode)
        print(image1.size)

        print(f"type of image1 {type(image2)}")
        # print(image2.mode)
        # image2 = self.tensor2pil(image2)
        # print(type(image2))
        # image2 = image2.convert("RGBA")
        print(image2.mode)
        print(image2.size)

        # 确保两个图像的模式为RGBA
        if image1.mode != 'RGBA':
            image1 = image1.convert('RGBA')
        if image2.mode != 'RGBA':
            image2 = image2.convert('RGBA')

        # 创建一个新图像用于存储合并后的图像
        merged_image = Image.new('RGBA', image1.size)

        # 获取两个图像的像素数据
        pixels1 = image1.load()
        pixels2 = image2.load()
        pixels_merged = merged_image.load()



        

        for y in range(image1.size[1]):
            for x in range(image1.size[0]):
                if pixels1[x, y][3] != 0:  # 检查image1的像素是否不透明
                    pixels_merged[x, y] = pixels1[x, y]
                else:
                    pixels_merged[x, y] = pixels2[x, y]
                    
        # 保存和返回合并后的图像
        merged_image.save('/data/ComfyUI/custom_nodes/merged_image.png')
        print(type(merged_image))
        print(f"merged_image mode is: {merged_image.mode}")
        merged_image = self.pil2tensor(merged_image)

      
        # merged_image = Image.alpha_composite(image1, image2)
        # merged_image.save('/data/ComfyUI/custom_nodes/merged_image.png')
        # print(type(merged_image))
        # print(f"merged_image mode is :{merged_image.mode}")
        # merged_image = self.pil2tensor(merged_image)

        return (merged_image,)
    


class tensor_trans_pil:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    "image1": ("IMAGE",),
                }   
        }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    CATEGORY = "Hayo_nodes"
    FUNCTION = "tensor_trans_pil"

    def tensor2pil(self,image):  
        return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
    
    def pil2tensor(self,image):
        return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)
    
    def tensor_trans_pil(self, image1):
        image1 = self.tensor2pil(image1)
        return (image1,)

class words_generatee:
    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    # "image": ("IMAGE",),
                    "text": ("STRING", {"default": '', "multiline": False}),
                }   
        }
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    CATEGORY = "Hayo_nodes"
    FUNCTION = "words_generatee"

    def pil2tensor(self,image):
        return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

    def generate_mask_image(self, text, font_path, font_size, width, height, output_path):

        image = Image.new(mode='RGBA', size=(width, height), color=(0, 0, 0, 0))
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(image)

        x = 50  # 起始位置的X坐标
        y = 50  # 起始位置的Y坐标
        for char in text:

            # 为每个字符创建一个单独的图像
            char_image = Image.new(mode='RGBA', size=(font_size+int(font_size/5), font_size+int(font_size/5)), color=(0, 0, 0, 0))
            char_draw = ImageDraw.Draw(char_image)
            char_draw.text((0, 0), char, font=font, fill=(255, 255, 255, 255))
            # 逆时针旋转45度
            char_image = char_image.rotate(45, expand=0)
            # 获取旋转后的字符尺寸
            rotated_width, rotated_height = char_image.size
            # 绘制旋转后的字符到主图像
            image.paste(char_image, (x, y), char_image)

            x += font_size      # 更新x坐标，使下一个字符横向绘制
            # y += font_size      # 更新y坐标，使下一个字符竖向绘制

        # image.save(output_path)
        # image = self.pil2tensor(image)
        print("111")
        print(type(image))
        return (image,)
    
    def words_generatee(self, text: str):

        text = "好说"
        font_path = "/data/ComfyUI/custom_nodes/字魂白鸽天行体.ttf"
        font_size = 128
        width = 1024
        height = 1024
        output_path = "/data/ComfyUI/custom_nodes/"

        image = Image.new(mode='RGBA', size=(width, height), color=(0, 0, 0, 0))
        font = ImageFont.truetype(font_path, font_size)
        draw = ImageDraw.Draw(image)

        x = 50  # 起始位置的X坐标
        y = 50  # 起始位置的Y坐标
        for char in text:

            # 为每个字符创建一个单独的图像
            char_image = Image.new(mode='RGBA', size=(font_size+int(font_size/5), font_size+int(font_size/5)), color=(0, 0, 0, 0))
            char_draw = ImageDraw.Draw(char_image)
            char_draw.text((0, 0), char, font=font, fill=(255, 255, 255, 255))
            # 逆时针旋转45度
            char_image = char_image.rotate(45, expand=0)
            # 获取旋转后的字符尺寸
            rotated_width, rotated_height = char_image.size
            # 绘制旋转后的字符到主图像
            image.paste(char_image, (x, y), char_image)

            x += font_size      # 更新x坐标，使下一个字符横向绘制
            # y += font_size      # 更新y坐标，使下一个字符竖向绘制
            # image.save(output_path)
        print("222")
        print(type(image))
        image = self.pil2tensor(image)
        return (image,)


NODE_CLASS_MAPPINGS = {
    "tensor_trans_pil": tensor_trans_pil,
    "make_transparentmask": make_transparentmask,
    "MergeImages": MergeImages,
    "words_generatee": words_generatee,
    "LoadPILImages":LoadPILImage
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "tensor_trans_pil": "tensor_trans_pil Node",
    "make_transparentmask": "Make Transparent mask Node",
    "MergeImages": "MergeImages Node",
    "words_generatee": "words_generatee Node",
    "LoadPILImages":"load_PIL image Node"
}