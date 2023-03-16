from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    """
    Add your code here or call it from here   
    """
    new_dict = {}
    for i in range(1, num+1):
        new_dict[i] = i*i
    return new_dict
