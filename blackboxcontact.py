import openai

# Initialize the OpenAI API client
openai.api_key = "your_openai_api_key_here"

def extract_contact_details(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Extract contact details from the following text: " + text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response["choices"][0]["text"]

contact_us_page_content = "The contact us page content goes here"
contact_details = extract_contact_details(contact_us_page_content)
print(contact_details)
