import streamlit as st
from streamlit_option_menu import option_menu

st.title("🚀Vinsup Infotech")
# with st.sidebar:
#     st.header("Vinsup Infotech")
# st.write("# Vinsup Infotech") #bold(small)
# st.write("## Vinsup Infotech") #normal
# st.write(" _Vinsup Infotech_") #italic
# st.write(" - Vinsup Infotech")  #bulletin
# st.write(" 🚀_Vinsup Infotech_🚀") #emojies
# st.text_input("Enter your name")
# st.button("Submit")st
with st.sidebar:
    data = option_menu(
        menu_title = "Vinsup",
        options = ["Home" , "About" , "Contact"],
        icons = ["house", "people","phone"],


    )
if data == "Home":
    st.header("Registration Form")
    

    col1,col2 = st.columns(2)
    with col1:
       Name =  st.text_input("Enter your Name")
       Email = st.text_input("Enter your Email")
    with col2:
      Phone =   st.text_input("Enter your Number")
      Password =  st.text_input("Enter your Password")

    if st.button("Submit"):
        st.write(Name,Email,Phone,Password)
        st.success("Data Inserted Successfully")
        st.balloons()
       #  st.snow()
    st.metric(label="python",value=20,delta="20%")
    st.number_input("Integer" ,max_value=0)
    # st.radio("Select your Option", options=["male","female"])
    st.radio(label=":rainbow[Gender]", options=["male","female"])
    # st.selectbox(label="City",options=["Madurai","Chennai","Coimbatore"])
    st.multiselect(label="City",options=["Madurai","Chennai","Coimbatore"]) 
    st.slider("Number",0,100)  
    st.file_uploader("Upload")




elif data =="About":
    st.header("About Page")
elif data == "Contact":
    st.header("Contact Page")