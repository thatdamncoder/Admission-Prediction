import streamlit as st
from streamlit_option_menu import option_menu
import joblib
import json
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="TheGrads",page_icon="👨‍🎓",layout="wide")
st.title(" 👨‍🎓 TheGrads")
st.divider()


# page_background="""
#     <style>
#     [data-testid='stAppViewContainer']{
#     background-image: url("https://images.unsplash.com/20/cambridge.JPG?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2047&q=80");
#     background-size: cover;
#     }
#     </style>
#     """
# st.markdown(page_background,unsafe_allow_html=True)

# def rain_snow():    
#     rain(
#         emoji="⚪",
#         font_size=10,
#         falling_speed=200,
#         animation_length="infinite",
#     )


def load_lottiefile(filepath:str):
    with open(filepath,"r") as file:
        return json.load(file)
    

with st.container():
    # rain_snow()
    hi_col,animation_col=st.columns([1.5,1])
    hi_col.markdown("    ")   
    hi_col.subheader('Hi :wave:')
    hi_col.header('Your fav Uni awaits you! :rainbow:')
    hi_col.markdown("Tell us your examinations scores and we'll tell you if your dream is getting true!")
    hi_col.write(
        """
        Are you an undergraduate student with aspirations for higher education?
        Whether you're just curious or planning your future, **TheGrads** is here to help you 
        get a sneak peek into your admission possibilities. Our innovative platform uses 
        Machine Learning Algorithms to estimate your chances of getting
        admitted to various graduate programs!

        <- <- <- Open the sidebar to discover!
        

        """
    )
    lottie_animation=load_lottiefile(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\lottiefiles/BearRocket.json")
    with animation_col:
        st.lottie(
            lottie_animation,
            reverse=False,
            height=600,
            width=500,
            loop=True,
        )







