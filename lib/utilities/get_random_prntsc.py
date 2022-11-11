from uuid import uuid4

def get_random_prntsc() -> str:
    """ 
    Generate a random image
    using uuid, and check if
    image exists or not in 
    prnt.sc
    """
    image_id = uuid4()
    
    img_id_str = str(image_id)
    # Get only first 6 characters from id
    id = img_id_str[0 : 6]
    url = f"http://prnt.sc/{id}"
    
    return url

    
