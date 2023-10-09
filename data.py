#pip install mysql-connector-python
#pip install streamlit plotly mysql-connector-python
#pip install streamlit
#pip install streamlit_extras

import mysql.connector
import pandas as pd
#import psycopg2
import streamlit as st
import PIL
from PIL import Image
from streamlit_option_menu import option_menu
import plotly.express as px
import pandas as pd
import requests

# connect to the database
import mysql.connector

#mysql connection
conn = mysql.connector.connect(user='root', password='Mysql!@#$%', host='127.0.0.1', database="phonepay")

# create a cursor object
cursor = conn.cursor()

#with st.sidebar:
SELECT = option_menu(
    menu_title = None,
    options = ["About","Home","Basic insights","Contact"],
    icons =["bar-chart","house","toggles","at"],
    default_index=2,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100%"},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})

#---------------------Basic Insights -----------------#


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--",
               "Top 10 states based on year and amount of transaction",
               "List 10 states based on type and amount of transaction",
               "Top 5 Transaction_Type based on Transaction_Amount",
               "Top 5 States based on Year and RegisteredUser",
               "Top 5 brands based on User_count",
               "Top 10 Districts based on states and Count of transaction",
               "List 10 states based on year and amount of transaction",
               "Least 5 RegisteredUsers based on states and District",
               "Top 5 states based on year and count of transaction",
               "Top 10 brands based on User_count"]






    select = st.selectbox("Select the option", options)
    if select == "Top 10 states based on year and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT States,Years, SUM(Transaction_Amount) AS Total_Transaction_Amount FROM top_trans GROUP BY States, Years ORDER BY Total_Transaction_Amount DESC LIMIT 10");

        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Years', 'Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 states and amount of transaction")
            st.bar_chart(data=df, x="Transaction_Amount", y="States")



    elif select == "List 10 states based on type and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT States, SUM(Transaction_Count) as Total FROM top_trans GROUP BY States ORDER BY Total ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Total_Transaction'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 states based on type and amount of transaction")
            st.bar_chart(data=df, x="Total_Transaction", y="States")



    elif select == "Top 5 Transaction_Type based on Transaction_Amount":
        cursor.execute(
            "SELECT DISTINCT Transacion_type, SUM(Transacion_amount) AS Amount FROM agg_trans GROUP BY Transacion_type	ORDER BY Amount DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['Transacion_type', 'Transacion_amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 Transaction_type based on Transaction_amount")
            st.bar_chart(data=df, x="Transacion_type", y="Transacion_amount")


    elif select == "Top 5 States based on Year and RegisteredUser":
        cursor.execute(
            "SELECT DISTINCT States,Years, SUM(RegisteredUser) AS Users FROM map_user GROUP BY States,Years ORDER BY Users DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Years', 'RegisteredUser'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 RegisteredUsers based on states and District")
            st.bar_chart(data=df, x="RegisteredUser", y="States")




    elif select == "Top 5 brands based on User_count":
        cursor.execute(
            "SELECT DISTINCT User_brand, SUM(User_count) AS Users FROM agg_user  GROUP BY User_brand ORDER BY Users DESC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['User_brand', 'User_count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 brands based on User_count")
            st.bar_chart(data=df, x="User_count", y="User_brand")



    elif select == "Top 10 Districts based on states and Count of transaction":
        cursor.execute(
        "SELECT DISTINCT States,District_name,SUM(Hover_count) AS Counts FROM map_trans GROUP BY States,District_name ORDER BY Counts DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', ',District_name', 'Hover_count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 Districts based on states and Count of transaction")
            st.bar_chart(data=df, x="Hover_count", y=",District_name")


    elif select == "List 10 states based on year and amount of transaction":
        cursor.execute(
            "SELECT DISTINCT States,Years,SUM(Transaction_Amount) AS Amount FROM top_trans GROUP BY States,Years ORDER BY Amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['States','Years','Transaction_Amount'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("List 10 Districts based on states and amount of transaction")
            st.bar_chart(data=df, x="Transaction_Amount", y="States")




    elif select == "Least 5 RegisteredUsers based on states and District":
        cursor.execute(
            "SELECT DISTINCT States,District, SUM(RegisteredUser) AS Users FROM map_user GROUP BY States,District ORDER BY Users ASC LIMIT 5");
        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'District', 'RegisteredUser'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Least 5 RegisteredUsers based on states and District")
            st.bar_chart(data=df, x="RegisteredUser", y="States")


#9

    elif select == "Top 5 states based on year and count of transaction":
        cursor.execute(
            "SELECT DISTINCT States,Years, SUM(Transaction_Count) AS Total_Transaction_count FROM top_trans GROUP BY States, Years ORDER BY Total_Transaction_count DESC LIMIT 5");

        df = pd.DataFrame(cursor.fetchall(), columns=['States', 'Years', 'Transaction_Count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 5 states and amount of transaction")
            st.bar_chart(data=df, x="Transaction_Count", y="States")


    elif select == "Top 10 brands based on User_count":
        cursor.execute(
            "SELECT DISTINCT User_brand, SUM(User_count) AS Users FROM agg_user  GROUP BY User_brand ORDER BY Users DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(), columns=['User_brand', 'User_count'])
        col1, col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.title("Top 10 brands based on User_count")
            st.bar_chart(data=df, x="User_count", y="User_brand")


#----------------Home----------------------#
cursor = conn.cursor()

# execute a SELECT statement
cursor.execute("SELECT * FROM agg_trans")

# fetch all rows
rows = cursor.fetchall()

if SELECT == "Home":
    col1, col2, = st.columns(2)
    img=Image.open('C:/Users/user/Downloads/PhonePe_Logo.jpg')
    st.image(img)
    with col1:
        st.subheader(
            "PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video("C:/Users/user/Downloads/pulse-video.mp4")

    df = pd.DataFrame(rows, columns=['States', 'Years', 'Quarters', 'Transacion_type', 'Transacion_count',
                                     'Transacion_amount'])
    fig = px.choropleth(df, locations="States", scope="asia", color="States", hover_name="States",
                        title="Live Geo Visualization of India")
    st.plotly_chart(fig)


#----------------About-----------------------#

if SELECT == "About":
    col1,col2 = st.columns(2)
    with col1:
        st.video("C:/Users/user/Downloads/upi.mp4")
    with col2:
        st.image(Image.open("C:/Users/user/Downloads/future_of_payments_header.webp"),width = 400)
        st.write("---")
        st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and states-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    st.write("---")
    col1,col2 = st.columns(2)
    with col1:
        st.title("THE BEAT OF PHONEPE")
        st.write("---")
        st.subheader("Phonepe became a leading digital payments company")
        st.image(Image.open("C:/Users/user/Downloads/photo.webp"),width = 200)
        with open("C:/Users/user/Downloads/annual report.pdf","rb") as f:
            data = f.read()
        st.download_button("DOWNLOAD REPORT",data,file_name="annual report.pdf")
    with col2:
        st.image(Image.open("C:/Users/user/Downloads/about_phonepe.jpg"),width = 200)



####Contact
if SELECT == "Contact":
    Name = (f'{"Name :"}  {"Divya"}')
    mail = (f'{"Mail :"}  {"divyadeeksha278@gmail.com"}')
    description = "An Aspiring DATA-SCIENTIST..!"
    social_media = {
        "GITHUB": "https://github.com/Divyadeipthi",
        "LINKEDIN": "https://www.linkedin.com/feed/"}

    col1, col2, col3 = st.columns(3)
    col3.image(Image.open("C:/Users/user/Downloads/img/divya_img.jpg"), width=100)
    with col2:
        st.title('Phonepe Pulse data visualisation')
        st.write(
            "The goal of this project is to extract data from the Phonepe pulse Github repository, transform and clean the data, insert it into a MySQL database, and create a live geo visualization dashboard using Streamlit and Plotly in Python. The dashboard will display the data in an interactive and visually appealing manner, with at least 10 different dropdown options for users to select different facts and figures to display. The solution must be secure, efficient, and user-friendly, providing valuable insights and information about the data in the Phonepe pulse Github repository.")
        st.write("---")

    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")








