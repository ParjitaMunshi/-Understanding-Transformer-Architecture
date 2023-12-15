import openai

# Replace 'YOUR_API_KEY' with your actual API key
api_key = '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'

# Initialize the OpenAI client
openai.api_key = api_key


# Define a prompt for text generation
prompt = "Translate the following English text to French:"

# Make a request to the API to generate text
response = openai.Completion.create(
    engine="text-davinci-002",  # Choose an appropriate engine
    prompt=prompt,
    max_tokens=50  # Adjust the token limit as needed
)

# Extract the generated response
generated_text = response.choices[0].text

# Print the generated text
print(generated_text)
