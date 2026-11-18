
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
name = st.text_input("Student Name", placeholder="akshata")

# Roll Number
roll_no = st.text_input("Roll Number", placeholder="xxxxxx")
year = st.text_input("Year", placeholder="3rd year")


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

    if not name.strip() or not roll_no.strip() or not usn.strip():
        st.warning("Please enter all student details.")

    else:
        st.success("Profile submitted successfully!")

        st.write("### Student Profile")

        st.write("AKSHATA:", html.escape(name))
        st.write("XXXXXX:", html.escape(roll_no))
        st.write("CSE:", department)
        st.write("3RD YEAR:", year)
