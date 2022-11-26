def bath_clean(string: str) -> dict:
    """
    Convert strings from `bathrooms_text` to counts and type  
    
    ### Parameters:
        `string`: the string we want to convert
    """
    bath_arr = str(string).lower().split(" ")
    try:
        num = float(bath_arr[0])
    except ValueError:
        bath_arr = ["1"] + bath_arr
        num = round(float(bath_arr[0]), 1)
    bath_type = " ".join(bath_arr[1:]).rstrip("s")
    
    if 'half-' in bath_type:
        bath_type = bath_type.replace('half-', '')
        num += 0.5

    if bath_type == "bath":
        bath_type = "private bath"
    
    return {
        "bathroom_num": num,
        "bathroom_type": bath_type,
    }

