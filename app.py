# app.py

import streamlit as st
import sys
# Add the 'scripts' directory to the path so we can import modules from it
sys.path.append('scripts') 

from gemini_logic import initialize_gemini
# We will create these functions later in gemini_logic.py
from gemini_logic import generate_product_copy 
from gemini_logic import generate_social_copy 
from gemini_logic import generate_email_subjects 


# --- 1. Page Configuration and Initialization ---
st.set_page_config(
    page_title="SellWise: AI Marketing Copy Generator",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.title("💡 SellWise: AI Marketing Copy Generator")

# Initialize the Gemini client and handle potential API key error
try:
    gemini_client = initialize_gemini()
except ValueError as e:
    st.error(str(e))
    st.stop() # Stop the app if the key is missing

# --- 2. Streamlit Tabs for Feature Organization ---
# Create the three tabs for our features
tab1, tab2, tab3 = st.tabs(
    ["📝 Product Page Copy", "📱 Social Ad Copy", "📧 Email Subject Lines"]
)


# --- 3. Content for Tab 1: Product Page Copy Generator (P1) ---
with tab1:
    st.header("Generate High-Converting Product Page Copy")
    st.markdown(
        "Enter the details of your product to generate a compelling Headline, Body Text, and SEO-focused Bullet Points."
    )

    # Use a Streamlit form to group inputs and prevent reruns on every keystroke
    with st.form("product_copy_form", clear_on_submit=False):
        
        # --- User Inputs ---
        product_name = st.text_input(
            "Product Name (e.g., 'Eco-Friendly Bamboo Toothbrush')",
            placeholder="A short, catchy name for your product",
        )
        
        product_description = st.text_area(
            "Detailed Product Description / Features",
            placeholder="List 3-5 core features, materials, and key benefits. Be descriptive!",
            height=150,
        )

        target_audience = st.text_input(
            "Target Audience",
            placeholder="e.g., 'Young professionals interested in sustainability'",
        )
        
        tone = st.selectbox(
            "Select the Tone of Voice",
            ["Professional", "Witty & Fun", "Sleek & Modern", "Informative"],
        )
        
        # The submit button for the form
        submitted = st.form_submit_button("Generate Copy with Gemini ✨")
        
        # --- Logic to handle form submission ---
        if submitted:
            if not all([product_name, product_description, target_audience]):
                st.warning("Please fill in the Product Name, Description, and Target Audience fields.")
            else:
                # Show a temporary status message while generating
                with st.spinner("🧠 SellWise is crafting your marketing copy..."): 
                    try:
                        result = generate_product_copy(
                            gemini_client, product_name, product_description, target_audience, tone
                        )
                        st.subheader("✅ Generated Product Copy")
                        # Use st.markdown to properly render the generated Markdown format
                        st.markdown(result)
                    except Exception as e:
                        st.error(f"An error occurred during generation: {e}")
                
                st.success("Form submitted. Now we need the generation function!")



# Tab 2: Social Ad Copy
with tab2:
    st.header("Generate Short Social Media Ad Copy")
    st.markdown(
        "Generate punchy ad copy and multiple Call-to-Action options for maximum engagement."
    )

    with st.form("social_copy_form", clear_on_submit=False):
        
        # --- User Inputs for P2 ---
        p2_product_description = st.text_area(
            "Product's Core Selling Points / Features",
            placeholder="Focus on 1-2 major benefits. E.g., 'Silent keys & long battery'",
            height=100,
        )

        p2_target_audience = st.text_input(
            "Target Audience / Buyer Persona",
            placeholder="e.g., 'Busy professionals stressed by office noise'",
        )
        
        platform = st.selectbox(
            "Target Social Platform",
            ["Instagram/Facebook (Visual & direct)", "TikTok (Casual & trendy)", "LinkedIn (Professional & polished)"],
        )
        
        # The submit button for the form
        p2_submitted = st.form_submit_button("Generate Social Ad Copy 🚀")
        
        # --- Logic to handle form submission ---
        if p2_submitted:
            if not all([p2_product_description, p2_target_audience]):
                st.warning("Please fill in the Product's Core Selling Points and Target Audience.")
            else:
                with st.spinner("🧠 SellWise is crafting high-impact ad copy..."): 
                    try:
                        p2_result = generate_social_copy(
                            gemini_client, 
                            p2_product_description, 
                            p2_target_audience, 
                            platform
                        )
                        st.subheader("✅ Generated Social Ad Copy & CTAs")
                        st.markdown(p2_result)
                    except Exception as e:
                        st.error(f"An error occurred during generation: {e}")
# Tab 3: Email Subject Lines
with tab3:
    st.header("Generate 'Pain Point' Email Subject Lines")
    st.markdown(
        "Get 8 subject lines designed to increase open rates by immediately addressing a customer's problem."
    )

    with st.form("email_subjects_form", clear_on_submit=False):
        
        # --- User Inputs for P3 ---
        main_product_benefit = st.text_input(
            "Main Product Benefit/Solution",
            placeholder="e.g., 'Eliminates background typing noise'",
        )

        key_customer_pain = st.text_area(
            "Key Customer Pain Point / Problem Solved",
            placeholder="e.g., 'Distraction from coworkers' noisy mechanical keyboards'",
            height=100,
        )
        
        email_tone = st.selectbox(
            "Select Email Tone",
            ["Direct & Urgent", "Empathetic & Helpful", "Curious & Intriguing"],
        )
        
        # The submit button for the form
        p3_submitted = st.form_submit_button("Generate Subject Lines 📧")
        
        # --- Logic to handle form submission ---
        if p3_submitted:
            if not all([main_product_benefit, key_customer_pain]):
                st.warning("Please fill in the Main Product Benefit and Key Customer Pain Point.")
            else:
                with st.spinner("🧠 SellWise is brainstorming high-open-rate subject lines..."): 
                    try:
                        p3_result = generate_email_subjects(
                            gemini_client, 
                            main_product_benefit, 
                            key_customer_pain, 
                            email_tone
                        )
                        st.subheader("✅ 8 High-Impact Subject Lines")
                        st.markdown(p3_result)
                    except Exception as e:
                        st.error(f"An error occurred during generation: {e}")