import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
#model = genai.GenerativeModel("gemini-pro")

def generate_description(product):
    prompt = f"""
Generate a short product marketing description for:
- Name: {product['name']}
- Price: ${product['price']}
- Battery Life: {product['battery_life']}
- Brand: {product['brand']}
- Specs: {product['specs']}

Make it appealing for remote work users.
"""
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"