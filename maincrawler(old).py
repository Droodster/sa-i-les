import requests
from bs4 import BeautifulSoup
from input import get_website, get_keywords
from backupai import find_contact_page
from blackboxcontact import extract_contact_details
from blackboxsummary import generate_summary

def maincrawler():
    website = get_website()
    keywords = get_keywords()
    try:
        html = requests.get(website).content
        soup = BeautifulSoup(html, "html.parser")
        links = soup.find_all("a")
        contact_page = None
        about_page = None
        for link in links:
            for keyword in keywords:
                if keyword in link.text.lower():
                    if "contact" in link.text.lower():
                        contact_page = link["href"]
                    if "about" in link.text.lower():
                        about_page = link["href"]
        if not contact_page:
            contact_page = find_contact_page(website)
        if not about_page:
            # Add logic to find the "about us" page using backupai
            pass
        contact_details = extract_contact_details(contact_page)
        summary = generate_summary(about_page)
        print("Contact Details:", contact_details)
        print("Summary:", summary)
    except Exception as e:
        print("An error occured:", e)

if __name__ == "__main__":
    maincrawler()
