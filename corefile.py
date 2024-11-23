import streamlit as st

#navigating to two different pages

pg=st.navigation([st.Page("Home.py"), st.Page("Booking.py")])
pg.run()