import streamlit as st

#navigating to two different pages

pg=st.navigation([st.Page("Home.py"), st.Page("Booking.py")])
pg.run()

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
import streamlit as st
import pandas as pd
import mysql.connector

st.image("/Users/mohamedafrith/Downloads/rdc-redbus-logo.svg") #logo 
state=st.selectbox("Select the State",('Andhra Pradesh','Assam','Bihar','Chandigarh','Himachal Pradesh','Kerala','Punjab','Telangana','Goa','West Bengal'),index=None) #all 10 states

#reading the csv stored in the list
list_apsrtc=[]
df_apsrtc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_apsrtc.csv")
for i,r in df_apsrtc.iterrows():
    list_apsrtc.append(r["route_name"])

list_astc=[]
df_astc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_astc.csv")
for i,r in df_astc.iterrows():
    list_astc.append(r["route_name"])

list_bsrtc=[]
df_bsrtc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_bsrtc.csv")
for i,r in df_bsrtc.iterrows():
    list_bsrtc.append(r["route_name"])

list_cturtc=[]
df_cturtc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_cturtc.csv")
for i,r in df_cturtc.iterrows():
    list_cturtc.append(r["route_name"])

list_hrtc=[]
df_hrtc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_hrtc.csv")
for i,r in df_hrtc.iterrows():
    list_hrtc.append(r["route_name"])

list_krtc=[]
df_krtc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_krtc.csv")
for i,r in df_krtc.iterrows():
    list_krtc.append(r["route_name"])

list_pepsu=[]
df_pepsu=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_pepsu.csv")
for i,r in df_pepsu.iterrows():
    list_pepsu.append(r["route_name"])

list_tsrtc=[]
df_tsrtc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_tsrtc.csv")
for i,r in df_tsrtc.iterrows():
    list_tsrtc.append(r["route_name"])

list_ktcl=[]
df_ktcl=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_ktcl.csv")
for i,r in df_ktcl.iterrows():
    list_ktcl.append(r["route_name"])

list_wbtc=[]
df_wbtc=pd.read_csv("/Users/mohamedafrith/Desktop/redbus_project/df_wbtc.csv")
for i,r in df_wbtc.iterrows():
    list_wbtc.append(r["route_name"])

#ratings slider
ratings=st.select_slider("Ratings",('0 to 1','1 to 2','2 to 3','3 to 4','4 to 5'))

#fetching data through mysql database
#Andhra Pradesh
if state=="Andhra Pradesh":
    A=st.selectbox("Select the Route",list_apsrtc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))
    
    
   
    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{A}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{A}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{A}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{A}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{A}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)

#Assam
if state=="Assam":
    AS=st.selectbox("Select the Route",list_astc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{AS}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df_assam=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df_assam)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{AS}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df_assam=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df_assam)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{AS}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df_assam=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df_assam)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{AS}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df_assam=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df_assam)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{AS}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df_assam=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df_assam)

#Bihar
if state=="Bihar":
    B=st.selectbox("Select the Route",list_bsrtc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{B}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{B}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{B}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{B}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{B}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)


#Chandigarh
if state=="Chandigarh":
    C=st.selectbox("Select the Route",list_cturtc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{C}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{C}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{C}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{C}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{C}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)

#Himachal Pradesh
if state=="Himachal Pradesh":
    H=st.selectbox("Select the Route",list_hrtc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{H}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{H}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{H}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{H}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{H}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)


#Kerala
if state=="Kerala":
    K=st.selectbox("Select the Route",list_krtc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{K}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{K}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{K}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{K}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{K}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)

#Punjab
if state=="Punjab":
    P=st.selectbox("Select the Route",list_pepsu,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{P}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{P}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{P}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{P}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{P}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)


#Telangana
if state=="Telangana":
    T=st.selectbox("Select the Route",list_tsrtc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{T}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{T}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{T}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{T}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{T}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)

#Goa
if state=="Goa":
    G=st.selectbox("Select the Route",list_ktcl,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{G}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{G}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{G}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{G}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{G}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)

#West Bengal
if state=="West Bengal":
    W=st.selectbox("Select the Route",list_wbtc,index=None)
    timing=st.radio("Select the Departure Time",("'00:01:00' and '05:59:00'","'06:00:00' and '12:00:00'","'12:01:00' and '18:00:00'","'18:01:00' and '00.00:00'"))

    if ratings=='0 to 1':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '0.00' and '1.00' and departing_time between {timing} and route_name = '{W}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='1 to 2':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '1.01' and '2.00' and departing_time between {timing} and route_name = '{W}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='2 to 3':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '2.01' and '3.00' and departing_time between {timing} and route_name = '{W}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='3 to 4':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '3.01' and '4.00' and departing_time between {timing} and route_name = '{W}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)
    if ratings=='4 to 5':
        conn=mysql.connector.connect(host="localhost",user="root",password="24434244342",database="redbus_project")
        my_cursor=conn.cursor()
        query=f"select busname,bustype,departing_time,reaching_time,duration,star_rating,route_link from bus_data where star_rating between '4.01' and '5.00' and departing_time between {timing} and route_name = '{W}' order by departing_time asc;"
        my_cursor.execute(query)
        out=my_cursor.fetchall()
        df=pd.DataFrame(out,columns=['busname','bustype','departing_time','reaching_time','duration','star_rating','route_link'])
        st.write(df)