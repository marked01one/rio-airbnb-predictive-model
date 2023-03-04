# THIS LIBRARY IS MANDATORY FOR THE NOTEBOOKS TO FUNCTION
from geopy.geocoders import Nominatim
import pandas as pd
import re

geolocator = Nominatim(user_agent="rio_airbnb_predictive_model")

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
        num = num / 2

    if bath_type == "bath":
        bath_type = "private bath"
    
    return {
        "bathroom_num": num,
        "bathroom_type": bath_type,
    }

def all_amenities(df_col: pd.DataFrame) -> list[str]:
    out = set()
    for list in df_col.to_list():
        out.append(list)
    return out

def amenities_clean(string: str) -> list[str]:
    """Converts the input string into list objects
        ### Input Parameters:
            `string (str)`: the string we want to convert
        ### Returns:
            `list_str (list[str])`: return a list converted from input string 
    """
    amenities_check = [['TV'], ['Free','Parking'], ['Grill'], ['WiFi']]
    list_str = string.lstrip('["').rstrip('"]').split('", "')
    # new_list = [
    #     re.sub('[0-9]{4}', '', item.replace('\\u', '')) \
    #     .encode('utf8').decode('ascii', errors='ignore')
    #     for item in list_str
    # ]
    new_list = []
    for item in new_list:
        new_item = re.sub('[0-9]{4}', '', item.replace('\\u', '')).encode('utf8').decode('ascii', errors='ignore')

          
        for check in amenities_check:
            check_str = " ".join(check)
            
            if check_str.lower() in new_item.lower() and check_str not in new_list:
                new_list.append(check_str)
                break
            
            
            if all(word.lower() in new_item.lower() for word in check) and (check_str.lower() != new_item.lower()):
                new_list.remove(item)
                if check_str not in new_list:
                    new_list.append(check_str)
                break    
    return new_list

def get_zip_code(coordinates) -> int:
    try:
      return re.findall("[0-9]{5}", geolocator.reverse(coordinates).address)[-1]
    except IndexError:
      return 0
