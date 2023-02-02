import requests
from bs4 import BeautifulSoup
import backupai
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

    # if the contact us link was not found, try to get it from the sitemap file
    if not contact_us:
        sitemap_file = 'sitemap.xml'
        _, contact_us_url = backupai.extract_info_from_sitemap(sitemap_file)
        if contact_us_url:
            response = requests.get(contact_us_url)
            soup = BeautifulSoup(response.text, "html.parser")
            contact_us = soup.find("a", string=f"Contact Us ({lang})")

    # return the results
    return (about_us, contact_us)
