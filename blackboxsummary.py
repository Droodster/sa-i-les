import openai

# Initialize the OpenAI API client
openai.api_key = "your_openai_api_key_here"

def generate_summary(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate a summary of the following text: " + text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response["choices"][0]["text"]

about_us_page_content = "The about us page content goes here"
summary = generate_summary(about_us_page_content)
print(summary)
