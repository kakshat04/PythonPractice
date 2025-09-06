from openai import OpenAI

client = OpenAI(
    api_key="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"
)

messages = [
    {
        "role": "user",
        "content": (
            "Generate Test Cases for Contact Us page for https://webdriveruniversity.com/Contact-Us/contactus.html"
            "* All fields are mandatory: First Name, Last Name, Email Address, Comments"
            "* There is a SUBMIT Button."
            "* When all data is submitted successfully, it gives message 'Thank you for your message!'"
            "* Email must contain '@' & '.'"
            "* If wrong email given, following error message will be printed : 'Error: Invalid email address'"
            "* If any field is missing, following error message will be printed : 'Error: all fields are required'"
            "* There is a RESET button, that clears all entries"
        )
    }
]

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=messages,
    max_tokens=500
)

print(response.choices[0].message.content.strip())