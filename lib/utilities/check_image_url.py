
import requests
from bs4 import BeautifulSoup


def check_image_url(soup: BeautifulSoup, session: requests.Session) -> (str | None):
    """ 
    If the generated url is an
    invalid or deleted image, will return 
    None, else, the return is an img url.
    """

    try:
        # Find image html from html webpage
        img_url = soup.find_all('img', {'class': 'no-click screenshot-image'})[0]
        # Get image url
        img = img_url['src']
        # If image url is relative (//prnt.sc/123456)
        if img.startswith('//'):
            # Generate real url
            img = img.replace('//st', 'https://st')
        # Request image url
        

        with session.get(img) as response:
            # If image don't exists
            if response.status_code != 200:
                return None
            # If image exists
            else:
                # Default image links for deleted image
                screenshot_removed = "https://st.prntscr.com/2022/05/15/0209/img/0_173a7b_211be8ff.png"
                imgur_removed = "https://i.imgur.com/xm3PvCC.png"
                imgur_removed2 = "https://i.imgur.com/removed.png"
                # If image is one of those default deleted image
                if img == screenshot_removed or img == imgur_removed or img == imgur_removed2:
                    return None
                    
                else:
                    # Image bytes
                    img_content = response.content
                    # Bytes length
                    img_bytes = len(img_content)
                    # Default bytes for deleted image
                    if img_bytes == 503:
                        return None
                    # ? Return image if is not invalid of deleted.
                    return img
    # If the page is redirect and soup don't find
    # specified html elements
    except IndexError:
        return None    