import os
import openai

# Create, copy, and paste your API key here:
openai.api_key = "sk-123456789"

response = openai.Completion.create(model="text-davinci-003",prompt="2+2=",temperature=0, max_tokens=10)


#### Check out https://blog.finxter.com/openapi-cheat-sheet/