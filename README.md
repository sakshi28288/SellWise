# SellWise: High-Conversion AI Marketing Copy Generator

SellWise is an LLM-driven application that automates and optimizes high-performing sales and marketing content. Using Google Gemini API, it generates product page copy, social media ads, and email subject lines to save time and boost conversions. Features include generating attention-grabbing headlines, persuasive body copy, SEO-focused bullet points, punchy social media ads with multiple CTAs, and 8 high-open-rate email subject lines. The app also allows customizing tone of voice: Professional, Witty & Fun, Sleek & Modern, or Informative. All content is AI-powered via Google Gemini API.

Project structure:

SellWise/
│
├─ app.py                  # Main Streamlit app
├─ requirements.txt        # Python dependencies
├─ .gitignore              # Ignore __pycache__ and .env
└─ scripts/
   └─ gemini_logic.py      # Gemini API logic and generation functions

To get started, clone the repository:

git clone https://github.com/<your-username>/SellWise.git
cd SellWise

Install dependencies:

pip install -r requirements.txt

Set up your Gemini API key by creating a `.env` file in the root folder:

GEMINI_API_KEY="YOUR_API_KEY_HERE"

Run the app:

streamlit run app.py

Open your browser at http://localhost:8501/ to start using SellWise.


