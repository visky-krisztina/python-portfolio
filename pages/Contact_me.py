import streamlit as st
from send_email import send_mail

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

st.markdown("<h2 style='text-align: center;'>Reach out and let's talk!</h2>", unsafe_allow_html=True)

with st.form(key="email-form"):
    user_email = st.text_input("Your e-mail address: ")
    user_message = st.text_area("Your message: ")
    message = f"""\
Subject: E-mail from {user_email}

From: {user_email}
        {user_message}
    """
    submit_button = st.form_submit_button("Submit")
    if submit_button:
        send_mail(message)
        st.info("Your e-mail was sent successfully!")




















