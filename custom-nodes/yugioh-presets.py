# by Nicolai256 inspired by throttlekitty SDXLAspectRatio

class yugioh_Presets:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "CARD_NAME": ("STRING", {"default": "",}),
                    "EXTRA_PROMPT": ("STRING", {"default": 'glowing, yugioh style, yugioh monster, duel monster',}),
                    "CARD": ("STRING", {"default": '',}),
                    "main_Type": ([
                    "None",
                    "Dark", 
                    "Divine", 
                    "Earth", 
                    "Fire", 
                    "Light", 
                    "Water", 
                    "Wind"],),
                    "extra_Type": ([
                    "None",
                    "Dark", 
                    "Divine", 
                    "Earth", 
                    "Fire", 
                    "Light", 
                    "Water", 
                    "Wind"],),
                    "main_attributes": ([
                    "None",
                    "Aqua",
                    "Beast",
                    "Beast-Warrior",
                    "Cyberse",
                    "Dinosaur",
                    "Divine-Beast",
                    "Dragon",
                    "Fairy",
                    "Fiend",
                    "Fish",
                    "Insect",
                    "Machine",
                    "Plant",
                    "Psychic",
                    "Pyro",
                    "Reptile",
                    "Rock",
                    "Sea Serpent",
                    "Spellcaster",
                    "Thunder",
                    "Warrior",
                    "Winged Beast",
                    "Wyrm",
                    "Zombie"],
                    ),
                    "extra_attributes_1": ([
                    "None",
                    "Aqua",
                    "Beast",
                    "Beast-Warrior",
                    "Cyberse",
                    "Dinosaur",
                    "Divine-Beast",
                    "Dragon",
                    "Fairy",
                    "Fiend",
                    "Fish",
                    "Insect",
                    "Machine",
                    "Plant",
                    "Psychic",
                    "Pyro",
                    "Reptile",
                    "Rock",
                    "Sea Serpent",
                    "Spellcaster",
                    "Thunder",
                    "Warrior",
                    "Winged Beast",
                    "Wyrm",
                    "Zombie"],
                    ),
                    "extra_attributes_2": ([
                    "None",
                    "Aqua",
                    "Beast",
                    "Beast-Warrior",
                    "Cyberse",
                    "Dinosaur",
                    "Divine-Beast",
                    "Dragon",
                    "Fairy",
                    "Fiend",
                    "Fish",
                    "Insect",
                    "Machine",
                    "Plant",
                    "Psychic",
                    "Pyro",
                    "Reptile",
                    "Rock",
                    "Sea Serpent",
                    "Spellcaster",
                    "Thunder",
                    "Warrior",
                    "Winged Beast",
                    "Wyrm",
                    "Zombie"],
                    ),
                    "Level": ("INT", {"default": 7, "min": 1, "max": 9}),
                    "Attack": ("INT", {"default": 2600, "min": 0, "max": 5000}),
                    "Defense": ("INT", {"default": 1900, "min": 0, "max": 5000}),
                    "add_type_and_attribute_to_prompt": ([
                    "no", 
                    "yes"],),
            }
        }
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("PROMPT", "CARD")
    FUNCTION = "yugioh_Presets"
    CATEGORY = "utils"

    def yugioh_Presets(self, CARD_NAME, EXTRA_PROMPT, main_Type, extra_Type, main_attributes, extra_attributes_1, extra_attributes_2, Level, Attack, Defense, CARD, add_type_and_attribute_to_prompt):
        main_Type = main_Type
        extra_Type = extra_Type
        main_attributes = main_attributes
        extra_attributes_1 = extra_attributes_1
        extra_attributes_2 = extra_attributes_2
        Level = str(Level)
        Attack = str(Attack)
        Defense = str(Defense)
        if add_type_and_attribute_to_prompt == "yes":
            main_Type = "type: " + main_Type
            extra_Type = "type: " + extra_Type
            main_attributes = "Attribute: " + main_attributes
            extra_attributes_1 = "Attribute: " + extra_attributes_1
            extra_attributes_2 = "Attribute: " + extra_attributes_2
            Level = "level: " + str(Level)
            Attack = "Attack: " + str(Attack)
            Defense = "Defense: " + str(Defense)

        if main_Type == "None":
            main_Type = ""
        else:
            main_Type = " , " + main_Type

        if extra_Type == "None":
            extra_Type = ""
        else:
            extra_Type = " , " + extra_Type

        if main_attributes == "None":
            main_attributes = ""
        else:
            main_attributes = " , " + main_attributes

        if extra_attributes_1 == "None":
            extra_attributes_1 = ""
        else:
            extra_attributes_1 = " , " + extra_attributes_1

        if extra_attributes_2 == "None":
            extra_attributes_2 = ""
        else:
            extra_attributes_2 = " , " + extra_attributes_2  

        PROMPT = CARD_NAME + main_Type + extra_Type + main_attributes + extra_attributes_1  + extra_attributes_2 + " , " + str(Level) + " , " + str(Attack) + " , " + str(Defense) + " , " + EXTRA_PROMPT
        CARD = ""
        return(PROMPT, CARD)

            
NODE_CLASS_MAPPINGS = {
    "yugioh_Presets": yugioh_Presets
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "yugioh_Presets": "SDXL 1.0 yugioh Presets"
}