import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page


result=st.session_state["result"]

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

if(result*100>=70.0):
    page_background="""
    <style>
        [data-testid='stAppViewContainer']{
        background-image: url("https://images.unsplash.com/photo-1583373834259-46cc92173cb7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8dW5pdmVyc2l0eSUyMGNhbXB1c3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=600&q=60");
        background-size: cover;
        }
        [data-testid='stHeader']{
        background-image: url("https://images.unsplash.com/photo-1583373834259-46cc92173cb7?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NXx8dW5pdmVyc2l0eSUyMGNhbXB1c3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=600&q=60");
        background-size: cover;
        }
    </style>
    """
    st.markdown(page_background,unsafe_allow_html=True)
    st.title("You're Almost There!")
    st.write("Predicted Percentage is")
    st.success("{:.2f}".format(result*100))
    st.balloons()
    st.balloons()
    st.balloons()
    st.toast("Whoopie!You've got a high chance!",icon="🎉")
    st.toast("Pack Your Bags!",icon="📒")


elif(result*100>=50.0 and result*100<70.0):
    page_background="""
        <style>
            [data-testid='stAppViewContainer']{
            background-image: url("https://images.unsplash.com/photo-1496482475496-a91f31e0386c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8aGlnaCUyMHRpZGVzJTIwb24lMjB0aGUlMjBiZWFjaHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=600&q=60");
            background-size: cover;
            }
            [data-testid='stHeader']{
            background-image: url("https://images.unsplash.com/photo-1496482475496-a91f31e0386c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8aGlnaCUyMHRpZGVzJTIwb24lMjB0aGUlMjBiZWFjaHxlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=600&q=60");
            background-size: cover;
            }
        </style>
    """
    st.markdown(page_background,unsafe_allow_html=True)
    st.write("Predicted Percentage is")
    st.success("{:.2f}".format(result*100))
    st.title("You've Got Some Chance!")
    st.balloons()
    st.toast("Hey! We'll Pray For You, Don't Lose Hope!")

elif(result*100<50.0 and result*100>30.0):
    page_background="""
        <style>
            [data-testid='stAppViewContainer']{
            background-image: url("https://images.unsplash.com/photo-1558021212-51b6ecfa0db9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c3R1ZHl8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=600&q=60");
            background-size: cover;
            }
            [data-testid='stHeader']{
            background-image: url("https://images.unsplash.com/photo-1558021212-51b6ecfa0db9?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c3R1ZHl8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=600&q=60");
            background-size: cover;
            }
        </style>
    """
    st.markdown(page_background,unsafe_allow_html=True)

    st.write("Predicted Percentage is")
    st.success("{:.2f}".format(result*100))
    st.title("May Be Destiny Has Other Plans!")
    st.subheader("Try Better Next Time!")
    st.toast("Maybe Grab A Coffee? It Makes You Feel Better!")

else:
    st.subheader("Your Result Will Be Displayed Here!")
    if st.button("Predict Now"):
        switch_page("Prediction")
    


        