import streamlit as st
from openai import OpenAI

# Set up the page title
st.set_page_config(page_title="Pantry Chef")
st.title("Pantry Chef 🧑‍🍳")
st.subheader("Turn your leftover ingredients into a delicious recipe!")

# Retrieve the secret key from the Streamlit cloud settings
try:
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    st.error("API Key not found. Please add 'OPENAI_API_KEY' to your Streamlit Secrets.")
    st.stop()

# Initialize the Groq client
client = OpenAI(
    api_key=api_key, 
    base_url="https://api.groq.com/openai/v1"
)

# User input
ingredients = st.text_input("Enter the ingredients you have (e.g., tomato, onion, egg):")

if st.button("Generate Recipe"):
    if not ingredients:
        st.warning("Please enter some ingredients first!")
    else:
        with st.spinner("Chef is cooking up a recipe..."):
            try:
                # Call the AI model
                response = client.chat.completions.create(
                    model="llama3-8b-8192",
                    messages=[
                        {"role": "system", "content": "You are a helpful cooking assistant. Suggest a simple recipe based on the provided ingredients."},
                        {"role": "user", "content": f"I have these ingredients: {ingredients}. Give me a recipe."}
                    ]
                )
                # Display the result
                st.markdown("### Your Recipe:")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
