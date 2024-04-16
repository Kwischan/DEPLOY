import streamlit as st

st.set_page_config(
    page_title="Homepage",
    page_icon="🌱"
)

st.title("Homepage")
#sidebar
with st.sidebar:
    st.subheader('About Us', divider='gray')
    
    st.info(
        """
        Authors:
        
        Christian Jerome S. Detuya
        
        Albert James E. Mangcao
        
        Axel Bert E. Ramos
        
        """
        )
