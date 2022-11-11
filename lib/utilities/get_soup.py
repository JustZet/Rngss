from bs4 import BeautifulSoup
import requests

def get_soup(prntsc_url: str, session: requests.Session) -> BeautifulSoup:
    with session.get(prntsc_url) as response:
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        return soup