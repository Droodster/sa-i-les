import requests
from bs4 import BeautifulSoup
from checkcountry import get_language

def maincrawler(url):
    # send a GET request to the website
    response = requests.get(url)

    # parse the response as HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # detect the language of the website
    lang = get_language(url)

    # extract the relevant information from the website
    about_us = soup.find("a", string=f"About Us ({lang})")
    contact_us = soup.find("a", string=f"Contact Us ({lang})")

    # return the results
    return (about_us, contact_us)
