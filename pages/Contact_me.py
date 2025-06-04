import streamlit as st

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





















