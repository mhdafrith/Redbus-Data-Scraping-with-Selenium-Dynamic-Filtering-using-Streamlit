import streamlit as st
import streamlit as st

# Create 3 columns for images to appear side by side
col1, col2, col3 = st.columns(3)

# Display images in each column
with col1:
    st.image('/Users/mohamedafrith/Downloads/se.png',width=100)

with col2:
    st.image('/Users/mohamedafrith/Downloads/db2.jpg.webp', width=100)

with col3:
    st.image('/Users/mohamedafrith/Downloads/logo.svg', width=150)



st.title(':red[Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit]')#project title
st.header("Introduction:", divider='gray')#header
st.markdown('This project focuses on web scraping data from Redbus, a popular online bus ticket booking platform, using Selenium. The scraped data is then filtered dynamically using Streamlit, a Python framework for building interactive applications. The project aims to gather information like bus schedules, prices, and routes, and display it in a user-friendly manner.')
st.header('Approach:',divider="gray")
st.markdown("***Web Scraping:***  We use Selenium to automate browsing and extract real-time data from the Redbus website.")
st.markdown("***Dynamic Filtering:*** Streamlit is used to create an interactive dashboard where users can filter the data based on their preferences, such as bus timings or prices.")
st.markdown("***Data Storage:*** SQL is used to store the scraped data for further analysis or future use")
st.header("Skills Takeaway:",divider='gray')
st.markdown("***Web Scraping*** with Selenium to extract live data.")#text content
st.markdown("***Interactive UI*** creation using Streamlit for real-time filtering.")
st.markdown("***Database Handling*** with SQL for data storage and management.")
st.markdown("***Python Programming*** for automation and data processing.")
st.header("Result:" ,divider='gray')
st.markdown("The project allows users to view bus schedules and prices in an interactive interface, making it easier to compare options and book tickets efficiently. It also demonstrates how to use web scraping, filtering, and data storage together in a practical application.")