# Step 1: Setup GROQ API key
import os
from dotenv import load_dotenv  # Load this to read .env file
from groq import Groq

load_dotenv()  # This reads variables from your .env file

api_key = os.getenv("GROQ_API_KEY") 


# Step 2: Convert image to required format
import base64

def encode_image(image_path):
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

# Step 3: Setup Multimodal LLM
query = "Is there something wrong with my face?"
model = "llama-3.2-90b-vision-preview"

# Passing the key from env

def analyze_image_with_query(query, model, encoded_image):
    client=Groq()  
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text", 
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion=client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content