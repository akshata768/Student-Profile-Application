
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Profile Application",
    page_icon="🎓",
    layout="centered"
)

# Application title
st.title("🎓 Student Profile Application")

st.subheader("Developed by AKSHATA")

st.info("Fill in your details and click View My Profile.")

# Student name
name = st.text_input(
    "Student Name",
    placeholder="Enter your name"
)

# USN / Roll Number
roll_number = st.text_input(
    "USN / Roll Number",
    placeholder="Enter roll number"
)

# Department selection
department = st.selectbox(
    "Department",
    ["CSE", "ISE", "ECE", "EEE", "ME", "CIVIL", "AIML"]
)

# Current year
year = st.radio(
    "Current Year",
    ["1st Year", "2nd Year", "3rd Year", "4th Year"]
)

# View profile button
if st.button("View My Profile"):

    if name.strip() == "" or roll_number.strip() == "":
        st.warning("Please enter all student details.")

    else:
        st.success("Profile submitted successfully!")

        st.write("### Student Profile")

        st.write("**Name:**", name)
        st.write("**Roll Number:**", roll_number)
        st.write("**Department:**", department)
        st.write("**Year:**", year)
