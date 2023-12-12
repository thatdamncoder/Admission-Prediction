import streamlit as st

st.title("What works behind the scenes?")

tab1, tab2 ,tab3,tab4,tab5,tab6,tab7= st.tabs(["Training Code", 
                                     "Home.py Code",
                                     "Prediction.py Code",
                                     "Result.py Code",
                                     "About.py Code",
                                     "Code.py Code",
                                     "Dataset.py Code"])

with tab1:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("Python Training Code")
        with open("MLCode.txt",encoding="utf8") as f:
            code = f.read()
            st.code(code,language="python")

with tab2:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Home Page")
        with open("1_Home.py", encoding="utf8") as f:
            code = f.read()
            st.code(code)
   
with tab3:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Prediction Page")
        with open("pages/3_Prediction.py", encoding="utf8") as f:
            code = f.read()
            st.code(code)


with tab4:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Result Page")
        with open("pages/4_Result.py", encoding="utf8") as f:
            code = f.read()
            st.code(code)
            
with tab5:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The About Page")
        with open("pages/8_About.py", encoding="utf8") as f:
            code = f.read()
            st.code(code)

with tab6:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Code Page (you're on this page)")
        with open("pages/6_Code.py", encoding="utf8") as f:
            code = f.read()
            st.code(code)

with tab7:
    col1,col2=st.columns([1,3])
    with col1:
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    with col2:
        st.header("The Dataset Page")
        with open("pages/7_Dataset.py", encoding="utf8") as f:
            code = f.read()
            st.code(code)

