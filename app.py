import streamlit as st
from groq import Groq

# Page configuration
st.set_page_config(page_title="Pantry Chef", page_icon="🍳", layout="centered")

st.title("🍳 Pantry Chef")
st.write("Generate recipes instantly based on the ingredients you have on hand!")

# Initialize Groq client using Streamlit Secrets
groq_api_key = st.secrets.get("GROQ_API_KEY")

if not groq_api_key:
    st.error("Groq API key not found! Please add it to your Streamlit Secrets.")
    st.stop()

client = Groq(api_key=groq_api_key)

# Active model identifier
MODEL_NAME = "llama-3.1-8b-instant"

# User input form
with st.form("recipe_form"):
    ingredients_input = st.text_input(
        "Enter ingredients (comma-separated):",
        placeholder="e.g., chicken, garlic, tomatoes, rice"
    )
    submitted = st.form_submit_button("Generate Recipe")

if submitted:
    if not ingredients_input.strip():
        st.warning("Please enter at least one ingredient.")
    else:
        with st.spinner("Cooking up a recipe..."):
            try:
                prompt = f"Create a delicious recipe using these ingredients: {ingredients_input}."
                
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model=MODEL_NAME,
                )
                
                recipe_result = chat_completion.choices[0].message.content
                
                st.success("Here is your recipe!")
                st.markdown(recipe_result)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
