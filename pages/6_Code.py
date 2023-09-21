import streamlit as st

st.title("What works behind the scenes?")

tab1, tab2 ,tab3,tab4,tab5,tab6,tab7= st.tabs(["Training Code", 
                                     "Streamlit Home.py Code",
                                     "Streamlit Prediction.py Code",
                                     "Streamlit Result.py Code",
                                     "Streamlit About.py Code",
                                     "Streamlit Code.py Code",
                                     "Streamlit Dataset.py Code"])

with tab1:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("Python Training Code")
        with open(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\MLCode.txt", "r") as f:
            code = f.read()
            st.code(code,language="python")

with tab2:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Home Page")
        with open(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\1_Home.py", "r") as f:
            code = f.read()
            st.code(code)
   
with tab3:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Prediction Page")
        with open(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\pages\3_Prediction.py", "r") as f:
            code = f.read()
            st.code(code)


with tab4:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Result Page")
        with open(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\pages\4_Result.py", "r") as f:
            code = f.read()
            st.code(code)
            
with tab5:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The About Page")
        with open(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\pages\8_About.py", "r") as f:
            code = f.read()
            st.code(code)

with tab6:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Code Page (you're on this page)")
        with open(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\pages\6_Code.py", "r") as f:
            code = f.read()
            st.code(code)

with tab7:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Dataset Page")
        with open(r"C:\Users\Dr. Vikash Thada\Documents\Admission Prediction\pages\7_Dataset.py", "r") as f:
            code = f.read()
            st.code(code)

