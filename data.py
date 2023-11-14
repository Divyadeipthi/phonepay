#pip install mysql-connector-python
#pip install streamlit plotly mysql-connector-python
#pip install streamlit
#pip install streamlit_extras

import mysql.connector
import pandas as pd
import numpy as np
#import psycopg2
import json
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
    options = ["About","Home","Analysis","Basic insights"],
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
        st.title(':violet[PHONEPE PULSE DATA VISUALISATION]')
        st.subheader(':blue[Phonepe Pulse]:')
        st.write("PhonePe  is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
        st.markdown("## :violet[Done by] : Divya")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
    with col2:
        st.video("C:/Users/user/Downloads/pulse-video.mp4")
    st.write("----")





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





# ANALYSIS TAB

if SELECT == "Analysis":
    st.title(':violet[ANALYSIS]')
    st.subheader('Analysis done on the basis of All India ,States and Top categories between 2018 and 2022')
    select = option_menu(None,
                         options=["INDIA", "STATES" ],
                         default_index=0,
                         orientation="horizontal",
                         styles={"container": {"width": "100%"},
                                   "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px"},
                                   "nav-link-selected": {"background-color": "#6F36AD"}})
    if select == "INDIA":
        tab1, tab2 = st.tabs(["TRANSACTION","USER"])

# TRANSACTION TAB
        with tab1:
            col1, col2, col3 = st.columns(3)
            with col1:
                in_tr_yr = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022'), key='in_tr_yr')
            with col2:
                in_tr_qtr = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'), key='in_tr_qtr')
            with col3:
                in_tr_tr_typ = st.selectbox('**Select Transaction type**',
                                            ('Recharge & bill payments', 'Peer-to-peer payments',
                                             'Merchant payments', 'Financial Services', 'Others'), key='in_tr_tr_typ')

# SQL Query

# Transaction Analysis bar chart query
            cursor.execute(
                f"SELECT States,Transacion_amount FROM agg_trans WHERE 	Years = '{in_tr_yr}' AND Quaters = '{in_tr_qtr}' AND Transacion_type = '{in_tr_tr_typ}';")
            in_tr_tab_qry_rslt = cursor.fetchall()
            df_in_tr_tab_qry_rslt = pd.DataFrame(np.array(in_tr_tab_qry_rslt), columns=['States', 'Transacion_amount'])
            df_in_tr_tab_qry_rslt1 = df_in_tr_tab_qry_rslt.set_index(pd.Index(range(1, len(df_in_tr_tab_qry_rslt) + 1)))

# Transaction Analysis table query
            cursor.execute(
                f"SELECT States,Transacion_count, Transacion_amount FROM agg_trans WHERE Years = '{in_tr_yr}' AND Quaters = '{in_tr_qtr}' AND Transacion_type = '{in_tr_tr_typ}';")
            in_tr_anly_tab_qry_rslt = cursor.fetchall()
            df_in_tr_anly_tab_qry_rslt = pd.DataFrame(np.array(in_tr_anly_tab_qry_rslt),
                                                      columns=['States', 'Transaction_count', 'Transaction_amount'])
            df_in_tr_anly_tab_qry_rslt1 = df_in_tr_anly_tab_qry_rslt.set_index(
                pd.Index(range(1, len(df_in_tr_anly_tab_qry_rslt) + 1)))


# Total Transaction Amount table query
            cursor.execute(
                f"SELECT SUM(Transacion_amount), AVG(Transacion_amount) FROM agg_trans WHERE Years = '{in_tr_yr}' AND Quaters = '{in_tr_qtr}' AND Transacion_type = '{in_tr_tr_typ}';")
            in_tr_am_qry_rslt = cursor.fetchall()
            df_in_tr_am_qry_rslt = pd.DataFrame(np.array(in_tr_am_qry_rslt), columns=['Total', 'Average'])
            df_in_tr_am_qry_rslt1 = df_in_tr_am_qry_rslt.set_index(['Average'])

 # Total Transaction Count table query
            cursor.execute(
                f"SELECT SUM(Transacion_count), AVG(Transacion_count) FROM agg_trans WHERE Years = '{in_tr_yr}' AND Quaters = '{in_tr_qtr}' AND Transacion_type = '{in_tr_tr_typ}';")
            in_tr_co_qry_rslt = cursor.fetchall()
            df_in_tr_co_qry_rslt = pd.DataFrame(np.array(in_tr_co_qry_rslt), columns=['Total', 'Average'])
            df_in_tr_co_qry_rslt1 = df_in_tr_co_qry_rslt.set_index(['Average'])

# GEO VISUALISATION
# Drop a State column from df_in_tr_tab_qry_rslt
            df_in_tr_tab_qry_rslt.drop(columns=['States'], inplace=True)
            # Clone the gio data
            url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
            response = requests.get(url)
            data1 = json.loads(response.content)

# Extract state names and sort them in alphabetical order
            state_names_tra = [feature['properties']['ST_NM'] for feature in data1['features']]
            state_names_tra.sort()

            # Create a DataFrame with the state names column
            df_state_names_tra = pd.DataFrame({'States': state_names_tra})

            # Combine the Gio State name with df_in_tr_tab_qry_rslt
            df_state_names_tra['Transacion_amount'] = df_in_tr_tab_qry_rslt

            # convert dataframe to csv file
            df_state_names_tra.to_csv('State_trans.csv', index=False)
            # Read csv
            df_tra = pd.read_csv('State_trans.csv')
            # Geo plot
            fig_tra = px.choropleth(
                df_tra,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM', locations='States', color='Transacion_amount',
                color_continuous_scale='thermal', title='Transaction Analysis')
            fig_tra.update_geos(fitbounds="locations", visible=False)
            fig_tra.update_layout(title_font=dict(size=33), title_font_color='#AD71EF', height=800)
            st.plotly_chart(fig_tra, use_container_width=True)


# ---------   /   All India Transaction Analysis Bar chart  /  ----- #
            df_in_tr_tab_qry_rslt1['States'] = df_in_tr_tab_qry_rslt1['States'].astype(str)
            df_in_tr_tab_qry_rslt1['Transacion_amount'] = df_in_tr_tab_qry_rslt1['Transacion_amount'].astype(float)
            df_in_tr_tab_qry_rslt1_fig = px.bar(df_in_tr_tab_qry_rslt1, x='States', y='Transacion_amount',
                                                color='Transacion_amount', color_continuous_scale='thermal',
                                                title='Transaction Analysis Chart', height=700, )
            df_in_tr_tab_qry_rslt1_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
            st.plotly_chart(df_in_tr_tab_qry_rslt1_fig, use_container_width=True)

            # -------  /  All India Total Transaction calculation Table   /   ----  #
            st.header(':violet[Total calculation]')
            col4, col5 = st.columns(2)
            with col4:
                st.subheader(':violet[Transaction Analysis]')
                st.dataframe(df_in_tr_anly_tab_qry_rslt1)
            with col5:
                st.subheader(':violet[Transacion_amount]')
                st.dataframe(df_in_tr_am_qry_rslt1)
                st.subheader(':violet[Transacion_count]')
                st.dataframe(df_in_tr_co_qry_rslt1)

            # USER TAB
        with tab2:
            col1, col2 = st.columns(2)
            with col1:
                in_us_yr = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022'), key='in_us_yr')
            with col2:
                in_us_qtr = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'), key='in_us_qtr')

            # SQL Query

            # User Analysis Bar chart query
            cursor.execute(f"SELECT States, SUM(User_count) FROM agg_user WHERE Years = '{in_us_yr}' AND 	Quaters = '{in_us_qtr}' GROUP BY States;")
            in_us_tab_qry_rslt = cursor.fetchall()
            df_in_us_tab_qry_rslt = pd.DataFrame(np.array(in_us_tab_qry_rslt), columns=['States', 'User Count'])
            df_in_us_tab_qry_rslt1 = df_in_us_tab_qry_rslt.set_index(
            pd.Index(range(1, len(df_in_us_tab_qry_rslt) + 1)))

            # Total User Count table query
            cursor.execute(
                f"SELECT SUM(User_count), AVG(User_count) FROM agg_user WHERE Years = '{in_us_yr}' AND 	Quaters= '{in_us_qtr}';")
            in_us_co_qry_rslt = cursor.fetchall()
            df_in_us_co_qry_rslt = pd.DataFrame(np.array(in_us_co_qry_rslt), columns=['Total', 'Average'])
            df_in_us_co_qry_rslt1 = df_in_us_co_qry_rslt.set_index(['Average'])

            # GEO VISUALIZATION FOR USER

            # Drop a State column from df_in_us_tab_qry_rslt
            df_in_us_tab_qry_rslt.drop(columns=['States'], inplace=True)
            # Clone the gio data
            url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
            response = requests.get(url)
            data2 = json.loads(response.content)
            # Extract state names and sort them in alphabetical order
            state_names_use = [feature['properties']['ST_NM'] for feature in data2['features']]
            state_names_use.sort()
            # Create a DataFrame with the state names column
            df_state_names_use = pd.DataFrame({'States': state_names_use})
            # Combine the Gio State name with df_in_tr_tab_qry_rslt
            df_state_names_use['User Count'] = df_in_us_tab_qry_rslt
            # convert dataframe to csv file
            df_state_names_use.to_csv('State_user.csv', index=False)
            # Read csv
            df_use = pd.read_csv('State_user.csv')
            # Geo plot
            fig_use = px.choropleth(
                df_use,
                geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                featureidkey='properties.ST_NM', locations='States', color='User Count',
                color_continuous_scale='thermal', title='User Analysis')
            fig_use.update_geos(fitbounds="locations", visible=False)
            fig_use.update_layout(title_font=dict(size=33), title_font_color='#AD71EF', height=800)
            st.plotly_chart(fig_use, use_container_width=True)
            # ----   /   All India User Analysis Bar chart   /     -------- #
            df_in_us_tab_qry_rslt1['States'] = df_in_us_tab_qry_rslt1['States'].astype(str)
            df_in_us_tab_qry_rslt1['User Count'] = df_in_us_tab_qry_rslt1['User Count'].astype(int)
            df_in_us_tab_qry_rslt1_fig = px.bar(df_in_us_tab_qry_rslt1, x='States', y='User Count', color='User Count',
                                                color_continuous_scale='thermal', title='User Analysis Chart',
                                                height=700, )
            df_in_us_tab_qry_rslt1_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
            st.plotly_chart(df_in_us_tab_qry_rslt1_fig, use_container_width=True)

            # -----   /   All India Total User calculation Table   /   ----- #
            st.header(':violet[Total calculation]')

            col3, col4 = st.columns(2)
            with col3:
                st.subheader(':violet[User Analysis]')
                st.dataframe(df_in_us_tab_qry_rslt1)
            with col4:
                st.subheader(':violet[User Count]')
                st.dataframe(df_in_us_co_qry_rslt1)

 # STATE TAB
    if select == "STATES":
        tab3 ,tab4 = st.tabs(["TRANSACTION","USER"])

        # TRANSACTION TAB FOR STATE
        with tab3:
            col1, col2, col3 = st.columns(3)
            with col1:
                st_tr_st = st.selectbox('**Select State**', (
                    'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                    'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                    'haryana', 'himachal-pradesh',
                    'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                    'maharashtra', 'manipur',
                    'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                    'tamil-nadu', 'telangana',
                    'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'), key='st_tr_st')
            with col2:
                st_tr_yr = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022'), key='st_tr_yr')
            with col3:
                st_tr_qtr = st.selectbox('**Select Quarter**', ('1', '2', '3', '4'), key='st_tr_qtr')

                # SQL QUERY

        # Transaction Analysis bar chart query
        cursor.execute(f"SELECT Transacion_type, Transacion_amount FROM agg_trans WHERE States = '{st_tr_st}' AND Years = '{st_tr_yr}' AND Quaters = '{st_tr_qtr}';")
        st_tr_tab_bar_qry_rslt = cursor.fetchall()
        df_st_tr_tab_bar_qry_rslt = pd.DataFrame(np.array(st_tr_tab_bar_qry_rslt),columns=['Transaction_type', 'Transaction_amount'])
        df_st_tr_tab_bar_qry_rslt1 = df_st_tr_tab_bar_qry_rslt.set_index(
        pd.Index(range(1, len(df_st_tr_tab_bar_qry_rslt) + 1)))

        # Transaction Analysis table query
        cursor.execute(
            f"SELECT Transacion_type, Transacion_count, Transacion_amount FROM agg_trans WHERE States = '{st_tr_st}' AND Years = '{st_tr_yr}' AND Quaters = '{st_tr_qtr}';")
        st_tr_anly_tab_qry_rslt = cursor.fetchall()
        df_st_tr_anly_tab_qry_rslt = pd.DataFrame(np.array(st_tr_anly_tab_qry_rslt),
                                                  columns=['Transaction_type', 'Transaction_count',
                                                           'Transaction_amount'])
        df_st_tr_anly_tab_qry_rslt1 = df_st_tr_anly_tab_qry_rslt.set_index(
            pd.Index(range(1, len(df_st_tr_anly_tab_qry_rslt) + 1)))

        # Total Transaction Amount table query
        cursor.execute(
            f"SELECT SUM(Transacion_amount), AVG(Transacion_amount) FROM agg_trans WHERE States = '{st_tr_st}' AND Years = '{st_tr_yr}' AND Quaters= '{st_tr_qtr}';")
        st_tr_am_qry_rslt = cursor.fetchall()
        df_st_tr_am_qry_rslt = pd.DataFrame(np.array(st_tr_am_qry_rslt), columns=['Total', 'Average'])
        df_st_tr_am_qry_rslt1 = df_st_tr_am_qry_rslt.set_index(['Average'])

        # Total Transaction Count table query
        cursor.execute(
            f"SELECT SUM(Transacion_count), AVG(Transacion_count) FROM agg_trans WHERE States = '{st_tr_st}' AND Years ='{st_tr_yr}' AND Quaters = '{st_tr_qtr}';")
        st_tr_co_qry_rslt = cursor.fetchall()
        df_st_tr_co_qry_rslt = pd.DataFrame(np.array(st_tr_co_qry_rslt), columns=['Total', 'Average'])
        df_st_tr_co_qry_rslt1 = df_st_tr_co_qry_rslt.set_index(['Average'])

        # -----    /   State wise Transaction Analysis bar chart   /   ------ #

        df_st_tr_tab_bar_qry_rslt1['Transaction_type'] = df_st_tr_tab_bar_qry_rslt1['Transaction_type'].astype(str)
        df_st_tr_tab_bar_qry_rslt1['Transaction_amount'] = df_st_tr_tab_bar_qry_rslt1['Transaction_amount'].astype(
            float)
        df_st_tr_tab_bar_qry_rslt1_fig = px.bar(df_st_tr_tab_bar_qry_rslt1, x='Transaction_type',
                                                y='Transaction_amount', color='Transaction_amount',
                                                color_continuous_scale='thermal',
                                                title='Transaction Analysis Chart', height=500, )
        df_st_tr_tab_bar_qry_rslt1_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
        st.plotly_chart(df_st_tr_tab_bar_qry_rslt1_fig, use_container_width=True)

        # ------  /  State wise Total Transaction calculation Table  /  ---- #
        st.header(':violet[Total calculation]')

        col4, col5 = st.columns(2)
        with col4:
            st.subheader(':violet[Transaction Analysis]')
            st.dataframe(df_st_tr_anly_tab_qry_rslt1)
        with col5:
            st.subheader(':violet[Transaction Amount]')
            st.dataframe(df_st_tr_am_qry_rslt1)
            st.subheader(':violet[Transaction Count]')
            st.dataframe(df_st_tr_co_qry_rslt1)

    # USER TAB FOR STATE
        with tab4:
             col5, col6 = st.columns(2)
             with col5:
                 st_us_st = st.selectbox('**Select State**', (
                 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar',
                  'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                 'haryana', 'himachal-pradesh','jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                 'maharashtra', 'manipur','meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                 'tamil-nadu', 'telangana','tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal'), key='st_us_st')
             with col6:
                 st_us_yr = st.selectbox('**Select Year**', ('2018', '2019', '2020', '2021', '2022'), key='st_us_yr')

# SQL QUERY

 # User Analysis Bar chart query
             cursor.execute(f"SELECT Quaters, SUM(User_count) FROM agg_user WHERE States = '{st_us_st}' AND Years = '{st_us_yr}' GROUP BY Quaters;")
             st_us_tab_qry_rslt = cursor.fetchall()
             df_st_us_tab_qry_rslt = pd.DataFrame(np.array(st_us_tab_qry_rslt), columns=['Quaters', 'User Count'])
             df_st_us_tab_qry_rslt1 = df_st_us_tab_qry_rslt.set_index(
             pd.Index(range(1, len(df_st_us_tab_qry_rslt) + 1)))

        # Total User Count table query
             cursor.execute(f"SELECT SUM(User_count), AVG(User_count) FROM agg_user WHERE States = '{st_us_st}' AND Years = '{st_us_yr}';")
             st_us_co_qry_rslt = cursor.fetchall()
             df_st_us_co_qry_rslt = pd.DataFrame(np.array(st_us_co_qry_rslt), columns=['Total', 'Average'])
             df_st_us_co_qry_rslt1 = df_st_us_co_qry_rslt.set_index(['Average'])

        # -----   /   All India User Analysis Bar chart   /   ----- #
             df_st_us_tab_qry_rslt1['Quaters'] = df_st_us_tab_qry_rslt1['Quaters'].astype(int)
             df_st_us_tab_qry_rslt1['User Count'] = df_st_us_tab_qry_rslt1['User Count'].astype(int)
             df_st_us_tab_qry_rslt1_fig = px.bar(df_st_us_tab_qry_rslt1, x='Quaters', y='User Count', color='User Count',
                                            color_continuous_scale='thermal', title='User Analysis Chart',
                                            height=500, )
             df_st_us_tab_qry_rslt1_fig.update_layout(title_font=dict(size=33), title_font_color='#AD71EF')
             st.plotly_chart(df_st_us_tab_qry_rslt1_fig, use_container_width=True)

        # ------    /   State wise User Total User calculation Table   /   -----#
             st.header(':violet[Total calculation]')

             col3, col4 = st.columns(2)
             with col3:
                 st.subheader(':violet[User Analysis]')
                 st.dataframe(df_st_us_tab_qry_rslt1)
             with col4:
                 st.subheader(':violet[User Count]')
                 st.dataframe(df_st_us_co_qry_rslt1)




