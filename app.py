import streamlit as st
from openai import OpenAI

st.title("Pantry Chef 🧑‍🍳")
ingredients = st.text_input("Enter the ingredients you have (comma separated):")

if st.button("Generate Recipe"):
    # Note: Replace 'YOUR_API_KEY' with a free Groq or OpenAI API key
    client = OpenAI(api_key="YOUR_API_KEY", base_url="https://api.groq.com/openai/v1") 
    
    prompt = f"I have these ingredients: {ingredients}. Give me a simple recipe."
    
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write(response.choices[0].message.content)
