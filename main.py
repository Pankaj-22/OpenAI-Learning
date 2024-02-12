import os
import openai

# Create, copy, and paste your API key here:
openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003",prompt="2+2=",temperature=0, max_tokens=10)


#### Check out https://blog.finxter.com/openapi-cheat-sheet/