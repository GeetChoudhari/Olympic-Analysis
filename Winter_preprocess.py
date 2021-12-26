

import streamlit as st
import pandas as pd
import numpy as np
import win_helper
import winter_pr
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff


df = pd.read_csv("athlete_events.csv")
region_df = pd.read_csv("noc_regions.csv")


df = winter_pr.preprocess(df, region_df)


def Winter():

    header = st.container()
    info = st.container()

    with header:
        st.markdown(
            "<h1 style='text-align: center; color:blue ;'>Winter Olympics </h1>", unsafe_allow_html=True)

    with info:
        # ==================================================Options on Summer Olympics==============================================
        user = st.sidebar.radio(
            "Select an option",
            ("Medal Tally", "Overall Analysis",
             "Country-Wise Analysis")
        )
        st.markdown(
            "<h4 style='text-align: center ;'>The Olympic games were cancelled altogether because of World War I (1916) and World War II (1940 and 1944) The 1980 Summer Olympics boycott was one part of a number of actions initiated by the United States to protest against the Soviet invasion of Afghanistan.</h4>", unsafe_allow_html=True)
        if user == "Medal Tally":
            st.markdown(
                "<h3 color:yellow ;'>Medal Tally </h3>", unsafe_allow_html=True)

            years, country = win_helper.country_year_list(df)
            selected_year = st.sidebar.selectbox("Select Year", years)
            selected_country = st.sidebar.selectbox("Select Country", country)

            medal_tally = win_helper.fetch_medal_tally(
                df, selected_year, selected_country)
            if selected_year == 'Overall' and selected_country == 'Overall':
                st.title("Overall Medal Tally from 1924-2014")
            if selected_year != 'Overall' and selected_country == 'Overall':
                st.title("Medal Tally in " + str(selected_year) + " Olympics")
            if selected_year == 'Overall' and selected_country != 'Overall':
                st.title(selected_country + " overall performance")
            if selected_year != 'Overall' and selected_country != 'Overall':
                st.title(selected_country + " performance in " +
                         str(selected_year) + " Olympics")
            st.table(medal_tally)

        if user == "Overall Analysis":

            editions = df['Year'].unique().shape[0]
            cities = df['City'].unique().shape[0]
            sports = df['Sport'].unique().shape[0]
            events = df['Event'].unique().shape[0]
            athletes = df['Name'].unique().shape[0]
            nations = df['region'].unique().shape[0]

            st.markdown(
                "<h2 style='text-align: center; color:yellow ;'>Overall Analysis (1924-2014) </h2>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("Editions")
                st.title(editions)
            with col2:
                st.header("Hosts")
                st.title(cities)
            with col3:
                st.header("Sports")
                st.title(sports)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.header("Events")
                st.title(events)
            with col2:
                st.header("Nations")
                st.title(nations)
            with col3:
                st.header("Athletes")
                st.title(athletes)

            nations_over_time = win_helper.data_over_time(df, 'region')
            fig = px.bar(nations_over_time, x="Year",
                         y="region", barmode="group")
            fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.6)
            st.title("Participating Nations over the years")
            st.plotly_chart(fig)

            events_over_time = win_helper.data_over_time(df, 'Event')
            fig = px.bar(events_over_time, x="Year", y="Event")
            fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.6)
            st.title("Events over the years")
            st.plotly_chart(fig)

            athlete_over_time = win_helper.data_over_time(df, 'Name')
            fig = px.bar(athlete_over_time, x="Year", y="Name")
            fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.6)
            st.title("Athletes over the years")
            st.plotly_chart(fig)

            st.title("Most successful Athletes")
            sport_list = df['Sport'].unique().tolist()
            sport_list.sort()
            sport_list.insert(0, 'Overall')

            selected_sport = st.selectbox('Select a Sport', sport_list)
            x = win_helper.most_successful(df, selected_sport)
            st.table(x)

        if user == "Country-Wise Analysis":

            st.markdown(
                "<h2 style='text-align: center; color:yellow ;'>Country-Wise Analysis </h2>", unsafe_allow_html=True)
            country_list = df['region'].dropna().unique().tolist()
            country_list.sort()
            selected_country = st.sidebar.selectbox(
                'Select a Country', country_list)

            country_df = win_helper.yearwise_medal_tally(df, selected_country)
            fig = px.bar(country_df, x="Year", y="Medal")
            fig.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                              marker_line_width=1.5, opacity=0.6)

            st.title(selected_country + " Medal Tally over the years")
            st.plotly_chart(fig)

            st.title(selected_country + " excels in the following sports")
            pt = win_helper.country_event_heatmap(df, selected_country)
            if len(pt) == 0:
                st.write("No Result Found")
            else:
                fig, ax = plt.subplots(figsize=(20, 20))
                ax = sns.heatmap(pt, annot=True)
                st.pyplot(fig)

            st.title("Top 15 athletes of " + selected_country)
            top15_df = win_helper.most_successful_countrywise(
                df, selected_country)
            st.table(top15_df)
