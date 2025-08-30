import streamlit as st
import requests
from bs4 import BeautifulSoup
import openai
import os

# --- Streamlit page setup ---
st.set_page_config(page_title="Ad Transparency AI Agent", layout="wide")
st.title("📊 Ad Transparency & Meta Ads Library Agent")

# --- OpenAI API key input (for AI analysis of ads) ---
openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

# --- User input ---
st.sidebar.header("Search Ads")
platform = st.sidebar.selectbox("Choose Platform", ["Google Ads Transparency", "Meta Ads Library"])
keyword = st.sidebar.text_input("Enter Keyword (e.g. insurance, shoes)")
search_btn = st.sidebar.button("🔍 Search Ads")

# --- Display area ---
if search_btn and keyword:
    st.info(f"Searching **{platform}** for ads related to: {keyword}")

    ads_data = []

    if platform == "Google Ads Transparency":
        # Fake example scraper for Google Ads Transparency
        url = f"https://adstransparency.google.com/?q={keyword}"
        st.write(f"🔗 Searching Google Ads Transparency: {url}")

        # Example placeholder result
        ads_data = [
            {
                "Advertiser": "Example Insurance Co",
                "Ad Copy": "Best car insurance in 2025! Save 30% today.",
                "Ad URL": "https://example.com/ad",
                "Landing Page": "https://example.com/landing",
                "Impressions": "120K",
                "Clicks": "8,500",
                "CTR": "7.1%",
                "Comments": "N/A"
            }
        ]

    elif platform == "Meta Ads Library":
        url = f"https://www.facebook.com/ads/library/?q={keyword}&active_status=all"
        st.write(f"🔗 Searching Meta Ads Library: {url}")

        # Example placeholder result
        ads_data = [
            {
                "Advertiser": "Nike",
                "Ad Copy": "Step into the future. Discover the new AirMax.",
                "Ad URL": "https://facebook.com/ad/12345",
                "Landing Page": "https://nike.com/airmax",
                "Impressions": "2.5M",
                "Clicks": "180K",
                "CTR": "7.2%",
                "Comments": "12,300"
            }
        ]

    # --- Display results ---
    if ads_data:
        for ad in ads_data:
            st.subheader(ad["Advertiser"])
            st.write(f"**Ad Copy:** {ad['Ad Copy']}")
            st.write(f"🔗 [Ad URL]({ad['Ad URL']}) | 🌍 [Landing Page]({ad['Landing Page']})")
            st.write(f"👁️ Impressions: {ad['Impressions']} | 🖱️ Clicks: {ad['Clicks']} | 📈 CTR: {ad['CTR']}")
            st.write(f"💬 Comments: {ad['Comments']}")
            st.markdown("---")

        # --- AI Analysis ---
        if openai.api_key:
            analysis_prompt = f"Analyze these ads for effectiveness:\n\n{ads_data}"
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": analysis_prompt}],
            )
            st.subheader("🤖 AI Insights")
            st.write(response["choices"][0]["message"]["content"])
        else:
            st.warning("No OpenAI API key found. Add it in Streamlit → Settings → Secrets.")
    else:
        st.error("No ads found. Try another keyword.")
