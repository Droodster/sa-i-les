import json
from langdetect import detect

def check_country(url):
    # detect the language of the website
    lang = detect(url)
    
    # load the list of countries and their corresponding language codes
    with open("countrylist.json", "r") as file:
        country_list = json.load(file)

    # search the list for a match with the detected language
    for country in country_list:
        if lang == country["code"]:
            return country["about_us"], country["contact_us"]
    
    # if no match is found, return default values
    return "About Us", "Contact Us"
