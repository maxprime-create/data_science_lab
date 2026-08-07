def create_character(character_name, strength, intelligence, charisma):
    # Validate character name
    if not isinstance(character_name, str):
        return "The character name should be a string."
    
    if character_name == "":
        return "The character should have a name."
    
    if len(character_name) > 10:
        return "The character name is too long."
    
    if " " in character_name:
        return "The character name should not contain spaces."
    
    # Validate stats are integers
    stats = [strength, intelligence, charisma]
    if not all(isinstance(stat, int) for stat in stats):
        return "All stats should be integers."
    
    # Validate stats are between 1 and 4
    if not all(1 <= stat <= 4 for stat in stats):
        if any(stat < 1 for stat in stats):
            return "All stats should be no less than 1."
        else:
            return "All stats should be no more than 4."
    
    # Validate sum of stats equals 7
    if sum(stats) != 7:
        return "The character should start with 7 points."
    
    # All validations passed, create character string
    full_dot = "●"
    empty_dot = "○"
    
    str_line = "STR " + full_dot * strength + empty_dot * (10 - strength)
    int_line = "INT " + full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_line = "CHA " + full_dot * charisma + empty_dot * (10 - charisma)
    
    return f"{character_name}\n{str_line}\n{int_line}\n{cha_line}"
