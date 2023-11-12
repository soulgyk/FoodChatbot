import re

def extract_session_id(session_str:str):
    match = re.search(r"/sessions/(.*?)/contexts/",session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string
    


def get_str_from_food_dict(food_dict: dict):
    return " , ".join([f"{int(value)} {key}" for key, value in food_dict.items()])

    
if __name__ == "__main__":

    print(extract_session_id("projects/mira-chatbot-nlkf/agent/sessions/3472484e-4987-e415-c023-b01922cbb9a0/contexts/ongoing-order"))