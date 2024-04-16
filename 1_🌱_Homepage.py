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

col1, col2 = st.columns(2)
col1.write(
    """
    
    The "Deep Learning and Machine Learning Integration: A Comprehensive Approach to Automated Crop Health Assessment Using CNN, ANN, and SVM" project aims to revolutionize crop health assessment in agriculture through cutting-edge technology and advanced machine learning techniques. By leveraging Convolutional Neural Networks (CNN), Artificial Neural Networks (ANN), and Support Vector Machines (SVM), the project endeavors to automate the process of evaluating crop health, thereby enhancing agricultural practices and promoting sustainability.
    
    """
)
col2.image("screenshots/Pepper_ss.jpeg")
col2.image("screenshots/Pepper_ss1.jpeg")