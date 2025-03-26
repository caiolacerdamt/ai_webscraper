import streamlit as st
from scrape import scrape_web

st.title("AI Webscraper")

url = st.text_input("Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website..")
    result = scrape_web(url)
    print(result)