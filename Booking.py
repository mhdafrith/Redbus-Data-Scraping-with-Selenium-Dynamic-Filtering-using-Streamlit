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