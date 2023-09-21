import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

# page_background="""
#     <style>
#     [data-testid='stAppViewContainer']{
#     background-image: url("https://images.unsplash.com/20/cambridge.JPG?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2047&q=80");
#     background-size: cover;
#     }
#     [data-testid='stHeader']{
#     background-image: url("https://images.unsplash.com/20/cambridge.JPG?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2047&q=80");
#     background-size: cover;
#     }
#     </style>
# """
# st.markdown(page_background,unsafe_allow_html=True)



st.title("Hey!")
st.title("Want to deep dive into what exactly are we trying to do?")


features= st.container()



with features:
    with st.expander("Click For Project Details"):
        st.markdown(
            '''
            <style>
            .streamlit-expanderHeader {
                background-color: #262730;
                color: white; # Adjust this for expander header color
            }
            .streamlit-expanderContent {
                background-color: 262730;
                color: white; # Expander content color
            }
            </style>
            ''',
            unsafe_allow_html=True
        )
        st.header("PROJECT DETAILS")
        st.markdown("* **Training:** Machine Learning In-House Internship 2023")
        st.markdown("* **Project Title:** Graduate Admission Prediction")
        st.markdown("* **Project Model:** Linear Regression")
        st.markdown("* **Branch:** CSE")
        st.markdown("* **Current Year of Study:** II")
        st.markdown("* **Team:**  Neha Agarwal, Nishtha Jain, Parishi Thada, Poorvanshi Kulshreshtha")
        st.markdown("             ")



    with st.expander("Objective"):
        st.write(
            """
            400 applicants have been surveyed as potential students for UCLA.
            The university weighs certain aspects of a student's education to determine their acceptance.
            The objective is to explore what kind of data is provided, determine the most important factors 
            that contribute to a student's chance of admission, 
            and select the most accurate model to predict the probability of admission.

            Applying for a master's degree is a very expensive and is a intensive work. 
            With this kernel, students will guess their capacities and 
            they will decide whether to apply for a master's degree or not.

            """
        )
    
    with st.expander("Know More About GRE Score"):
        st.write(
            """
            The Graduate Record Examination is a standarized exam, 
            often required for admission to graduate and MBA programs globally. 
            It's made up of three components:

            * Analytical Writing (Scored on a 0-6 scale in half-point increments)
            * Verbal Reasoning (Scored on a 130-170 scale)
            * Quantitative Reasoning (Scored on a 130-170 scale)

            In this dataset, the GRE Score is based on a maximum of 340 points. 
            The mean is 317 with a standard deviation of 11.5.

            """
        )
    with st.expander("Know More About TOEFL Score"):
        st.write(
            """
            The Test of English as a Foreign Language is a standarized 
            test for non-native English speakers that are choosing to
            enroll in English-speaking universities.

            The test  is split up into 4 sections:

            * Reading
            * Listening
            * Speaking
            * Writing

            All sections are scored out of 30, giving the exam a total score of 120 marks. 
            In this dataset, the TOEFL scores have a mean of 107 and a standard deviation of 6.

            """
        )
    with st.expander("Know More About SOL Score"):
        st.write(
            """
            Know More at: https://www.idp.com/india/study-abroad/letter-of-recommendation/

            
             """
        )
    with st.expander("Know More About LOR Score"):
        st.write(
            """
            Know More at: https://unicreds.com/sop

            
            """
        )
    with st.expander("References And Links"):
        st.write(
            """
            * Data specific for the University of California, Los Angeles (UCLA)
            * Know more at their site: https://www.ucla.edu/
            * Kaggle Predicting Graduate Admissions: https://www.kaggle.com/datasets/mohansacharya/graduate-admissions
            

            """
        )

    
    


