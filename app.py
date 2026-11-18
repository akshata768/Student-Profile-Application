import streamlit as st
import html

st.set_page_config(
    page_title="Student Profile Application",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Profile Application")
st.caption("Developed by AKSHATA")

st.info("Fill in your details and click View My Profile.")

# Student Name
name = st.text_input("Student Name", placeholder="Enter your name")

# Roll Number
roll_no = st.text_input("Roll Number", placeholder="Enter roll number")

# Department
department = st.selectbox(
    "Department",
    ["CSE", "ISE", "ECE", "EEE", "ME", "CIVIL", "AIML"]
)

# Current Year
year = st.radio(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

# View My Profile
if st.button("View My Profile"):

    if not name.strip() ==""or roll_no.strip() =="":
        st.warning("Please enter all student details.")

    else:
        st.success("Profile submitted successfully!")

        st.write("### Student Profile")

        st.write("Name:", html.escape(name))
        st.write("Roll Number:", html.escape(roll_no))
        st.write("Department:", department)
        st.write("Year:", year)
