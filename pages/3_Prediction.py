import streamlit as st
import joblib
import time
from streamlit_option_menu import option_menu
from streamlit_toggle import st_toggle_switch
from streamlit_extras.let_it_rain import rain
from streamlit_extras.switch_page_button import switch_page
from sklearn.preprocessing import StandardScaler

page_bg="""
    <style>
    [data-testid='stAppViewContainer']{
    background-image: url("https://images.unsplash.com/photo-1602780374996-8c6499ce7420?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80");
    background-size: cover;
    }
    [data-testid='stHeader']{
    background-image: url("https://images.unsplash.com/photo-1602780374996-8c6499ce7420?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1974&q=80");
    background-size: cover;
    }
    </style>
"""
st.markdown(page_bg,unsafe_allow_html=True)


#with st.container():
#   selected= option_menu(
#        menu_title="Website",
#        options=["Home","Prediction","Result","About"],
#        default_index=1,
#        orientation="horizontal",
#    )
#    if selected=="Home":
#        switch_page("Home")
#    if selected=="Prediction":
#       switch_page("Prediction")
#    if selected=="Result":   
#        switch_page("Result") 
#    if selected=="About":
#        switch_page("About")


linreg=joblib.load('GAP LinReg')
scaler=joblib.load('Scaler')

st.title('Predicting Graduate Admissions')
st.write("Fill Your Entries And Press Enter To Apply")

gre=st.number_input('Enter Your GRE Score',min_value=0,max_value=340)
toefl=st.number_input('Enter Your TOEFL Score',min_value=0,max_value=120)
cgpa=st.number_input('Enter Your CGPA',min_value=0.0,max_value=10.0,format="%.2f")
sop=st.number_input('Enter Your SOP Score',min_value=0.0,max_value=5.0,format="%.2f")
lor=st.number_input('Enter Your LOR Score',min_value=0.0,max_value=5.0,format="%.2f")
univrat=st.slider('Select Your University Rating',min_value=1,max_value=4,value=2,step=1)
research=st.toggle(
    "Research Paper Published?",
    )
if research:
    research_encode=1
else:
    research_encode=0


scaled_input=scaler.transform([[gre,toefl,univrat,sop,lor,cgpa,research_encode]])

if "result" not in st.session_state:
    st.session_state["result"]=0

result=linreg.predict(scaled_input)[0]
st.session_state["result"]=result

calculate_prob_button=st.button("Probability of Admission")

if calculate_prob_button:
    text_progress_bar="Hold On! We're Computing..."
    progress_bar=st.progress(0,text=text_progress_bar)
    for time_progress in range(80):
        time.sleep(0.05)
        progress_bar.progress(time_progress+1,text=text_progress_bar)
    switch_page("Result")
  
        
    
