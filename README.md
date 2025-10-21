# SellWise: High-Conversion AI Marketing Copy Generator

SellWise is an LLM-driven application that automates and optimizes high-performing sales and marketing content. Using Google Gemini API, it generates product page copy, social media ads, and email subject lines to save time and boost conversions. The app allows customizing tone of voice: Professional, Witty & Fun, Sleek & Modern, or Informative.  

Features:
- Product Page Copy Generator: headlines, body copy, and SEO-focused bullet points.  
- Social Media Ad Copy Generator: punchy, platform-specific ad copy with multiple CTAs.  
- Email Subject Line Generator: 8 high-open-rate email subject lines focused on pain points or benefits.  
- Customizable Tone of Voice.  
- Powered by Google Gemini API.  

Project structure:
SellWise/
- app.py                  # Main Streamlit app
- requirements.txt        # Python dependencies
- .gitignore              # Ignore __pycache__ and .env
- scripts/
  - gemini_logic.py       # Gemini API logic and generation functions

Steps to run the project:
1. Clone the repository:
git clone https://github.com/<your-username>/SellWise.git
cd SellWise

2. Install dependencies:
pip install -r requirements.txt

3. Set up Gemini API key by creating a `.env` file in the root folder:
GEMINI_API_KEY="YOUR_API_KEY_HERE"

4. Run the app:
streamlit run app.py

5. Open your browser at http://localhost:8501/ to start using SellWise.
