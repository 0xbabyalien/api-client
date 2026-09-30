import os
from openai import OpenAI

# Retrieve the API key securely provided through GitHub Secrets
client = OpenAI(
    base_url="https://cleanapis.com/v1",
    api_key=os.environ.get("CLEAN_API_KEY")
)

response = client.chat.completions.create(
    model="claude-opus-5",  # The model you selected in Clean APIs
    messages=[{"role": "user", "content": "Hello from GitHub Actions!"}]
)

print(response.choices[0].message.content)

