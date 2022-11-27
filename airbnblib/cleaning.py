import pandas as pd
import re

def bath_clean(string: str) -> dict:
    """Convert strings from `bathrooms_text` to counts and type   
    ### Parameters:
        `string`: the string we want to convert  
    ### Return:
        `dict[float, str]`: dictionary with the number of baths in a listing and the type of bath
    """
    bath_arr = string.lower().split(" ")
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

def amenities_clean(string: str) -> list[str]:
    """Converts the input string into list objects
        ### Input Parameters:
            `string (str)`: the string we want to convert
        ### Returns:
            `list_str (list[str])`: return a list converted from input string 
        """
    amenities_check = [['TV'], ['Free','Parking'], ['Grill'], ['WiFi']]
    list_str = string.lstrip('["').rstrip('"]').split('", "')
    new_list = [
        re.sub('[0-9]{4}', '', item.replace('\\u', '')) \
        .encode('utf8').decode('ascii', errors='ignore')
        for item in list_str
    ]
    for item in new_list:
        for check in amenities_check:
            check_str = " ".join(check)
            if all(word.lower() in item.lower() for word in check) and (check_str.lower() != item.lower()):
                new_list.remove(item)
                if check_str not in new_list:
                    new_list.append(check_str)
                break    
    return new_list

def amenities_freq(df_col: pd.DataFrame) -> pd.DataFrame:
    """Remove all values from every amenities list that is appears in less than 50% of listings
    ### Input Parameters:
        `df_col (pd.DataFrame)`: Input amenities DataFrame column
    ### Returns:
        `pd.DataFrame`: Output amenities DataFrame column
    """
    amenities_num = {"sum": 0}
    for row in df_col:
        for item in row:
            if item not in amenities_num:
                amenities_num[item] = 0
            amenities_num[item] += 1
    for row in df_col:
        for item in row:
            # Initial dataset contains 45,802 total listings 
            # --> any amenities that appears in less than 22,910 will be removed  
            if amenities_num[item] < 22901:
                row.remove(item)
    return df_col

def get_zip_code(lat_col: str, long_col: str) -> int:
    
    pass