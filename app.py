import streamlit as st
from openai import OpenAI

# Load API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.set_page_config(page_title="Ads Agent", page_icon="📊", layout="wide")
st.title("📊 AI Ads Analysis Agent")

# User input
analysis_prompt = st.text_area(
    "Enter your analysis prompt:",
    "Analyze current trends in digital advertising and suggest profitable niches."
)

if st.button("Run Analysis"):
    with st.spinner("🤖 Thinking..."):
        try:
            # OpenAI API call (new v1 format)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": analysis_prompt}],
            )

            # Extract the AI’s reply
            ai_reply = response.choices[0].message.content

            st.subheader("✅ AI Response")
            st.write(ai_reply)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
