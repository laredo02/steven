
from ollama import chat, generate, ChatResponse 
from google import genai

response = generate(model='tinyllama:1.1b', prompt='Give me a steven hawking speech, in first person, as if you were him')
print(response.response)

