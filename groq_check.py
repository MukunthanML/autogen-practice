import groq

client = groq.Client(api_key="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")

try:
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # Change if needed
        messages=[{"role": "user", "content": "Hello, tell me joke"}]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print("Error:", e)

