# scripts/gemini_logic.py

import os
from dotenv import load_dotenv
from google import genai

# --- 1. Load Environment Variables ---
# This looks for the .env file in the root directory (SellWise)
load_dotenv()

# --- 2. Initialize Gemini Client ---
def initialize_gemini():
    """Initializes and returns the Gemini client."""
    
    # Get the API key from the environment variables
    # The key should be stored in your .env file as GEMINI_API_KEY="YOUR_KEY_HERE"
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        # Raise an error if the key isn't found, guiding the user to fix it
        raise ValueError(
            "GEMINI_API_KEY not found. Please create a .env file and add your key."
        )

    # Initialize the client with the key
    client = genai.Client(api_key=api_key)
    return client

# Note: The actual generation functions will go here in the next step.

# scripts/gemini_logic.py (Continuing from Step 3)

# ... (Existing code for load_dotenv and initialize_gemini) ...

# --- 3. System Instruction for Product Copy (The Core Prompt) ---

PRODUCT_COPY_SYSTEM_INSTRUCTION = """
You are a highly skilled, conversion-focused **AI Marketing Copywriter** named SellWise.
Your primary goal is to generate compelling, structured marketing copy for a product page.

Your response MUST be formatted strictly using **Markdown headings and bullet points** as follows:

# Product Headline
- A short, attention-grabbing headline (maximum 10 words) focused on the main benefit.

## Product Body Copy
- A 2-3 paragraph summary (maximum 100 words) that immediately addresses a pain point and positions the product as the unique solution. The copy must be persuasive and engaging.

### Key SEO/Benefit Bullet Points
- Generate exactly 5 compelling bullet points.
- Each bullet point must focus on a key feature AND translate it into a specific user benefit.
- Integrate relevant keywords naturally (based on the product name/description).
- Use a maximum of 15 words per bullet point.

---
**INPUT PARAMETERS:**
- Tone: {tone}
- Product: {product_name}
- Audience: {target_audience}
- Description/Features: {product_description}
---
"""
# scripts/gemini_logic.py (Continuing)

# ... (Existing code for initialize_gemini and PRODUCT_COPY_SYSTEM_INSTRUCTION) ...

# --- 4. Generation Function for Product Copy (P1) ---

def generate_product_copy(client, product_name, description, audience, tone):
    """
    Generates structured product page marketing copy using the Gemini API.
    
    Args:
        client (genai.Client): The initialized Gemini client.
        product_name (str): Name of the product.
        description (str): Detailed features/description.
        audience (str): Target demographic.
        tone (str): Desired tone of voice.

    Returns:
        str: The generated, formatted marketing copy.
    """

    # Format the system instruction with the dynamic user inputs
    system_prompt = PRODUCT_COPY_SYSTEM_INSTRUCTION.format(
        tone=tone,
        product_name=product_name,
        target_audience=audience,
        product_description=description
    )

    # The user prompt is minimal since the System Instruction does the heavy lifting
    user_prompt = f"Generate the full product copy suite for the product: {product_name}."

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', # Fast model, great for structured text generation
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7, # A bit creative, but still grounded
            )
        )
        return response.text
    
    except Exception as e:
        # In a real app, you might log this error. Here, we re-raise for Streamlit to catch.
        return f"Gemini API Error: {e}"

        # scripts/gemini_logic.py (New Content for P2)

# --- 5. System Instruction for Social Ad Copy (The Core Prompt) ---

SOCIAL_AD_SYSTEM_INSTRUCTION = """
You are a rapid, direct-response **AI Social Media Copywriter** named SellWise.
Your goal is to generate short, viral, and high-impact ad copy suitable for platforms like Instagram, Facebook, or TikTok.
The copy must immediately grab attention and clearly lead to a call-to-action.

Your response MUST be formatted strictly using **Markdown headings and a numbered list** as follows:

# Primary Ad Hook (Max 2 sentences)
- A punchy, urgent opening line that uses an emoji and addresses a common audience pain point.

## Ad Body Copy (Max 50 words)
- A brief, benefit-driven paragraph explaining how the product solves the pain point. Keep it concise for a mobile screen.

### Strong Call-to-Action Options (Generate exactly 5)
1. Generate an urgent CTA (e.g., "Shop Now").
2. Generate a benefit-focused CTA (e.g., "Claim Your Focus").
3. Generate a scarcity CTA (e.g., "Limited Stock").
4. Generate a discovery CTA (e.g., "Learn More").
5. Generate a curiosity CTA (e.g., "See Why Thousands Switched").

---
**INPUT PARAMETERS:**
- Platform: {platform}
- Target Audience: {target_audience}
- Description/Features: {product_description}
---
"""
# scripts/gemini_logic.py (New Content for P2)

# ... (Existing functions) ...

# --- 6. Generation Function for Social Ad Copy (P2) ---

def generate_social_copy(client, product_description, audience, platform):
    """
    Generates structured social media ad copy and multiple CTAs.
    
    Args:
        client (genai.Client): The initialized Gemini client.
        product_description (str): Detailed features/description.
        audience (str): Target demographic.
        platform (str): The social media platform (influences tone).

    Returns:
        str: The generated, formatted marketing copy.
    """

    # Format the system instruction with the dynamic user inputs
    system_prompt = SOCIAL_AD_SYSTEM_INSTRUCTION.format(
        platform=platform,
        target_audience=audience,
        product_description=product_description
    )

    # The user prompt is minimal
    user_prompt = "Generate the social media ad copy and CTA options based on the parameters provided."

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.8, # Slightly higher temperature for more creative ad hooks
            )
        )
        return response.text
    
    except Exception as e:
        return f"Gemini API Error: {e}"

# scripts/gemini_logic.py (New Content for P3)

# --- 7. System Instruction for Email Subject Lines (The Core Prompt) ---

EMAIL_SUBJECT_SYSTEM_INSTRUCTION = """
You are a highly efficient **AI Email Marketing Specialist** named SellWise.
Your task is to generate 8 high-open-rate subject lines for a product or service.
The primary strategy is to focus on a **clear pain point** or a **curiosity gap** related to the product's main benefit.

Your response MUST be formatted strictly as a **numbered list** of exactly 8 subject lines.
The subject lines should be short, impactful, and designed to maximize the email open rate.
For variety, ensure you include:
1.  One subject line using an emoji.
2.  One subject line posing a clear question.
3.  One subject line that creates urgency or scarcity.
4.  One subject line focused on a direct benefit (no pain point).

---
**INPUT PARAMETERS:**
- Product Benefit: {product_benefit}
- Pain Point: {pain_point}
- Tone: {tone}
---
"""

# scripts/gemini_logic.py (New Content for P3)

# ... (Existing functions) ...

# --- 8. Generation Function for Email Subject Lines (P3) ---

def generate_email_subjects(client, product_benefit, pain_point, tone):
    """
    Generates structured email subject lines using the Gemini API.
    
    Args:
        client (genai.Client): The initialized Gemini client.
        product_benefit (str): The main benefit the product offers.
        pain_point (str): The key problem the target audience faces.
        tone (str): Desired tone of voice.

    Returns:
        str: A numbered list of 8 generated email subject lines.
    """

    # Format the system instruction with the dynamic user inputs
    system_prompt = EMAIL_SUBJECT_SYSTEM_INSTRUCTION.format(
        product_benefit=product_benefit,
        pain_point=pain_point,
        tone=tone
    )

    # The user prompt is minimal
    user_prompt = "Generate the 8 high-converting email subject lines based on the pain point and benefit provided."

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=user_prompt,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.9, # Higher temperature for maximum creativity in subject lines
            )
        )
        return response.text
    
    except Exception as e:
        return f"Gemini API Error: {e}"

# Remember to save scripts/gemini_logic.py now!