# Imports
import time
import numpy as np
import plotly.express as px
import streamlit as st
import pandas as pd
data = pd.read_csv('data.csv')
# Title & Intro
st.title("Example EDA: Predicting Entrepreneurial Potential in Students")
st.header("For this EDA, I decided to explore the relationship between different qualities that make someone a good enrepreneur.")
# Head and Tail
st.write(data.head())
st.write("Above are the first five indexes of the dataset. The first entry is marked as zero due to something known as zero-based indexing.")
st.write(data.tail())
st.write("Above are the last five entries. We can see that the bottom row is the 218th index, meaning the dataset has 219 entries (don't forget zero-based indexing!)")
st.write(data.info())
st.write(data.describe())
st.write("The describe function gives all sorts of tidbits about the dataset, such as average, standard deviation, and max/min values.")
st.write(data.count())
st.write("This function counts the number of values for all variables in the dataset.")
fig_One = px.scatter(data, x = "SelfConfidence", y = "Perseverance")
st.dataframe(data)
st.write("This dataframe shows all entries in the dataset. Each index (row) is a person, and the columns are different qualities they have. Categories include EducationSector, IndividualProject, Age, Gender, City, Influenced, Perseverance, DesireToTakeInitiative, Competitiveness, SelfReliance, StrongNeedToAchieve, SelfConfidence, GoodPhysicalHealth, MentalDisorder, KeyTraits, ReasonsForLack, and y.")
# Graph 1
st.plotly_chart(fig_One)
st.write("A scatter plot marks specific coordinates in a dataset based on their variable values. In this graph, I asked the question, 'Does perseverance increase as self confidence increase?' The answer is yes, acoording to this dataset. The two variables have a positive correlation with one another. In real-world terms, people who have higher self-confidence generally work through their challenges and continue through hardships.")
fig_Two = px.bar(data, x = "EducationSector", y = "Competitiveness")
st.write("For my bar graph, I wanted to compare the major with how competitive students identified themselves as. Engineering well outranked the others, with Econ/Business being runner-up. The least compeitive majors were Language, Math, and Teaching.")
st.plotly_chart(fig_Two)
fig_Three = px.histogram(data, x = "StrongNeedToAchieve")
st.plotly_chart(fig_Three)
st.write("A histogram illustrates the frequency of values for a specific variable. In this case, the students ranked their need to achieve success. The number of students that reported a certain level continually increased from 1 through 5.")
fig_Four = px.scatter_matrix(data, dimensions = ["Age","SelfConfidence","SelfReliance","Competitiveness"])
st.plotly_chart(fig_Four)
st.write("A scatter matrix compares four variables at once, and produces sixteen graphs. My four in this case were Age, SelfConfidence, SelfReliance, and Competitiveness. Many of the graphs below don't show any correlation, but a few that do include SelfConfidence with SelfReliance, SelfConfidence with Competitiveness, and SelfReliance with Competitiveness. Age had no impact on any of the main entrepreneurial factors.")
st.header("To summarize, I'd say this dataset had both surprising and unsurprising results. Although there are certain factors that increase the odds of success, the data shows that potential is everywhere.")