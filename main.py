import streamlit as st
import pandas

st.set_page_config(layout="wide")
# Row 1: Title centered
st.markdown("<h1 style='text-align: center;'>Visky Krisztina</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.image("images/photo.png", width=400)

with col2:
    content = """
        👋 Hey there! I’m Krisz — a curious human on a mission to master Python, one project (and occasional bug) at a time. 
         This portfolio is my digital playground, where I’ve documented the chaos, creativity, and caffeine-fueled projects I’ve built while learning to code.  
        💡 You’ll find projects of all shapes and sizes and fueled by a mix of trial, error, and determination.
        Feel free to explore, and don’t hesitate to share your thoughts, feedback, or brilliant ideas — I’d love to hear what you think!
        And if something here catches your eye and you think I might be a good fit to help with your project, don’t be shy — reach out and let’s talk!
        🙏 Thanks for stopping by!       
   """
    st.info(content)
st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Below are some of the apps I’ve built with Python and its extended family — Django, Selenium, Streamlit, and a few cousins I met along the way 😄 </h5>", unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for idx, row in df.iterrows():
        if idx % 2 == 0:  # even index -> odd-numbered row (1st, 3rd, etc.)
            st.header(row["title"])
            st.write(row["description"])
            st.image("images/" + row["image"])
            st.write(f"[Source code on Github]({row['url']})")

with col4:
    for idx, row in df.iterrows():
        if idx % 2 == 1:  # odd index -> even-numbered row (2nd, 4th, etc.)
           st.header(row["title"])
           st.write(row["description"])
           st.image("images/" + row["image"])
           st.write(f"[Source code on Github]({row['url']})")   
