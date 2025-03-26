import streamlit as st

st.title("AI Webscraper")

url = st.text_input("Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website..")