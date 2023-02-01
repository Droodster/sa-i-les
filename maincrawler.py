import requests
from bs4 import BeautifulSoup
from langdetect import detect
import openai

def extract_text(url):
    # send a GET request to the URL and retrieve the HTML content
    response = requests.get(url)
    html_content = response.text

    # use BeautifulSoup to extract the text from the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()

    return text

def summarize_with_openai(text):
    # replace with your own OpenAI API key
    openai.api_key = "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"

    # generate a summary of the text using OpenAI's GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='Please summarize this text: ' + text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text

def crawl_website(url):
    # initialize variables to store the text from each page
    front_page_text = ''
    about_us_text = ''
    contact_us_text = ''

    # extract text from the front page
    front_page_text = extract_text(url)

    # check the language of the front page
    front_page_language = detect(front_page_text)

    # search for the "About Us" and "Contact Us" pages
    if front_page_language == 'en':
        about_us_keywords = ['about us', 'about', 'team']
        contact_us_keywords = ['contact us', 'contact', 'reach out']
    else:
        # if the language is not English, you will need to specify keywords for the target language
        # or translate the English keywords to the target language
        about_us_keywords = []
        contact_us_keywords = []

    # find the links for the "About Us" and "Contact Us" pages on the front page
    soup = BeautifulSoup(front_page_text, 'html.parser')
    links = [link.get('href') for link in soup.find_all('a')]
    for link in links:
        link_text = link.lower()
        if any(keyword in link_text for keyword in about_us_keywords):
            about_us_url = link
        if any(keyword in link_text for keyword in contact_us_keywords):
            contact_us_url = link

    # extract text from the "About Us" and "Contact Us" pages
    try:
        about_us_text = extract_text(about_us_url)
    except:
        pass
    try:
        contact_us_text = extract_text(contact_us_url)
    except:
        pass

    # return the text from each page
    return front_page_text, about_us_text
