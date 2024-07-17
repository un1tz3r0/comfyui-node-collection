import requests
import json
import os
from googletrans import Translator

class GoogleTranslator:
    """
   A Simple Translator using Google.
   The main purpose is to translate prompts from any source language to English, 
   but another destination languages can be set 
   (just a few by now but you can expand the selection if you wish)
   It works pretty well translatin prompting instructions to english.

    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING",
                        {
                            "multiline":True,
                        }),
                "translate_to": (["en", "pt","ru","es"], {
                    "default": "en",
                    "multiline":False 
                }),
                "print_to_screen": (["enable", "disable"],),
            },
        }

    RETURN_TYPES = ("STRING",)
    #RETURN_NAMES = ("image_output_name",)

    FUNCTION = "translate"

    CATEGORY = "SimpleTools"

    def translate(self, text, translate_to,print_to_screen):
        translator = Translator()
        result = translator.translate(text,dest=translate_to)
        translated = result.text

        if print_to_screen == "enable":
            print(f"""Your input contains:
                text: {text}
                translate_to: {translate_to}
                translated: {translated}
            """)
        return (translated,)



NODE_CLASS_MAPPINGS = {
    "GoogleTranslator": GoogleTranslator
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GoogleTranslator": "Simple Gooogle Translator Client"
}

