import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.markdown("""
<style>
/* Default sidebar width */
[data-testid="stSidebar"] {
    width: 200px !important;
    max-width: 200px !important;
}

/* Sidebar responsive for narrow screens */
@media (max-width: 800px) {
    [data-testid="stSidebar"] {
        width: 120px !important;
        max-width: 120px !important;
    }
}
</style>
""", unsafe_allow_html=True)
blog_link='https://stacksandsnacks.hashnode.dev'
st.markdown("<h1 style='text-align: center;'>Visky Krisztina</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

with col1:
    st.image("images/photo.png", width=400)

with col2:
    content = f""" 👋 Hey there! I’m Krisz — a curious human on a mission to master Python, one project (and occasional bug) at a time. 
         This portfolio is my digital playground, where I’ve documented the chaos, creativity, and caffeine-fueled projects I’ve built while learning to code. It is a simple page, I mostly focused on the projects not on the style itself. 
        💡 But here you’ll find projects of all shapes and sizes that have a mix of trial, error, and determination.  I will also try to record my journey in a "mom blog"-ish way, so you can read and laugh a bit: <a href="{blog_link}" target="_blank" style="text-decoration: none; font-weight: bold; color: #c59d5f;">Stacks & Snacks</a>.                                                                                                                                                                                                                                                                                                                
           Feel free to explore this page and the blog, and don’t hesitate to share your thoughts, feedback, or brilliant ideas — I’d love to hear what you think!
        And if something here catches your eye and you think I might be a good fit to help with your project, don’t be shy — reach out and let’s talk!
        🙏 Thanks for stopping by!"""

    st.markdown(
            f"""
            <div style="display: flex; align-items: center; height: 100%;">
                <div style="background-color: #f0f2f6; border-radius: 5px; text-align: justify; padding: 15px">
                    {content.replace('\n', '<br>')}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown("<h5 style='text-align: center;'>Below are some of the apps I’ve built with Python and its extended family — Django, Selenium, Streamlit, and a few cousins I met along the way 😄 </h5>", unsafe_allow_html=True)

st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)

col3, empty_col, col4 = st.columns([1.5, 0.2, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for idx, row in df.iterrows():
        if row.empty or str(row[0]).startswith('#'):
            continue
        if idx % 2 == 0:
           st.markdown(f"### {row['title']}")
           st.write(row["description"])
           st.image(f"images/{row['image']}", use_container_width=True)

           # Center the GitHub link
           st.markdown(
               f"""                                                                                                                     
               <div style="text-align: center;">                                                                                        
                   <a href="{row['url']}" target="_blank" style="text-decoration: none; font-weight: bold;">👉 Source code on GitHub</a> 
               </div>                                                                                                                   
               """,
               unsafe_allow_html=True
           )
           st.markdown("---")
           st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)


with col4:
    for idx, row in df.iterrows():
        if row.empty or str(row[0]).startswith('#'):
           continue
        if idx % 2 == 1:
            st.markdown(f"### {row['title']}")
            st.write(row["description"])
            st.image(f"images/{row['image']}", use_container_width=True)

            # Center the GitHub link
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <a href="{row['url']}" target="_blank" style="text-decoration: none; font-weight: bold;">👉 Source code on GitHub</a>
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown("---")
            st.markdown("<div style='margin-top: 50px;'></div>", unsafe_allow_html=True)
















