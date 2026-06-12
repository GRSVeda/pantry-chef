# Pantry-Chef:AI-Powered Recipe Agent 🧑‍🍳
Pantry Chef is an intelligent AI assistant designed to minimize food waste by generating personalized, actionable recipes based on the ingredients currently available in your kitchen. This project is built using Generative AI (LLMs) to provide real-time, context-aware culinary guidance.
# 🚀 Problem Statement:
        Many individuals struggle to decide what to cook with the ingredients they have on hand, often leading to food waste and unnecessary grocery purchases. This project aims to simplify everyday cooking by providing a smart, efficient solution that turns available pantry items into practical meal solutions.  
# 🛠 Tech StackLanguage: 
    PythonAI Model: Llama-3.3-70b-versatile (via Groq API)Frontend
    StreamlitDeployment: Streamlit Community Cloud
# ✨ Key FeaturesSmart Ingredient Input: 
    Users can enter multiple ingredients to get tailored suggestions.  Dynamic Generation: The AI generates step-by-step cooking instructions adapted to specific ingredient limitations.  Personalization: The agent provides substitutions, cooking tips, and dietary adjustments based on user preferences.  
# ⚙️ How to Run LocallyClone the repository:Bashgit clone https://github.com/GRSVeda/pantry-chef.git
      Install dependencies:Bashpip install -r requirements.txt
      Set your API Key:Create a .env file or export your environment variable:Bashexport OPENAI_API_KEY='your_groq_api_key'
      Run the app:Bashstreamlit run app.py
# 🌐 Deployment:
    This application is deployed on Streamlit Community Cloud. For deployment, sensitive API keys are securely managed via the Secrets Management interface to ensure data privacy and security.
