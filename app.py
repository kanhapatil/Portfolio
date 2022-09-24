from PIL import Image
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

embed_component= {'linkedin':"""<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
        <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="kanha-patil-969884218" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/kanha-patil-969884218?trk=profile-badge"></a></div>"""}

with st.sidebar:
    components.html(embed_component['linkedin'],height=310)

with st.sidebar:
    st.image("GH.png", width=50)
    st.markdown("[Click Me](https://github.com/kanhapatil)")

st.sidebar.caption("**Wish to connect with me?**")
st.sidebar.write("📧: kanhap569@gmail.com")

# Summary 
st.write("### Summary")
st.write("Hello I am Kanha,")
st.write("Intern in Data science and Machine learning i have been learning DS & ML since a year and currently looking out to internship to solve business problems using AI; Love to learn new things. Building machine learning model with highly accurate that will help to solve the client problem and grow the business !!")

# Personal Projects
st.write("### Personal Projects")
with st.expander("Exploratory Data Analysis"):
    st.write("""
        Exploratory data analysis on Olympics Dataset
        In this project i have perform Exploratory data analysis on
        Olympics data set.
        And created a streamlit website for better visualization and Country wise and player wise analysis and check the perfomance of each country in a perticular year. 
        Visit web app : https://kanhapatil-olympic-data-analysis-till-2016-app-9n9dyv.streamlitapp.com/
    """)
    st.image("Olympics.jpg", width=600)

with st.expander("Meteorological Dataset"):
    st.write("""
        EDA On Meteorological Data (Weather Dataset)
        This notebook contains Exploratary Data Analysis on Weather Dataset and creation of Dashboard using Pywedge 0.5.1.8 Python package. The dataset contains 96,453 entries and 12 attributes related to meteorological data.
        
        View Jupyter Notebook : https://github.com/kanhapatil/EDA-On-Meteorological-Dataset
    """)
    st.image("barplot_1.png", width=600)

# Skills and tool
st.write("### Skills & Tools ⚒️")
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("Data science")
with col2:
    st.button("Python")

with col3:
    st.button("SQL")
with col4:
    st.button("Numpy")
with col5:
    st.button("Pandas")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("Machine Le..")
with col2:
    st.button("Scikit-Learn")
with col3:
    st.button("EDA")
with col4:
    st.button("PCA")
with col5:
    st.button("Plotly")

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.button("Matplotlib")
with col2:
    st.button("Seaborn")
with col3:
    st.button("PyWedge")
with col4:
    st.button("Streamlit")


    

# Education
st.write("### Education 📖")

df = pd.read_csv("Book1.csv")
st.dataframe(df)

# Achievements 
st.write("### Achievements 🥇")
st.markdown("- **My GFG Profile :** https://auth.geeksforgeeks.org/user/kanhap569")
st.markdown("- **My HackerRank Profile :** https://www.hackerrank.com/kanhap569")


# My Daily routine as learning data science and machine learning
st.write("### Daily routine as learning Data Science & Machine Learning")
image = Image.open("flowchart.jpeg")
st.image(image, width=650)




