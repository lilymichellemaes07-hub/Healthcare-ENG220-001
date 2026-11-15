import streamlit as st
import pandas as pd

# Page Title
st.title("Healthcare Access in Cuba, New Mexico")

# Project Overview
st.header("Project Overview")

st.write("""
This project analyzes healthcare accessibility in Cuba, New Mexico. 
Our research focuses on healthcare services, insurance coverage, 
income levels, transportation barriers, and possible solutions 
to improve healthcare access in rural communities.
""")

# Team Members
st.header("Team Members")

st.write("""
- Lily Maes
- Aubriana Martinez
- Sam Martin
- Sam Esparza
""")

# Insurance Coverage Results
st.header("Insurance Coverage Results")

col1, col2, col3 = st.columns(3)
with col1:
  st.metric("Population Analyzed", "4,876")
with col2:
  st.metric("Insured", "4313")
with col3:
  st.metric("Uninsured", "563")

st.write("""
88.5% of residents have health insurance coverage,
while 11.5% remain uninsured.
""")

# Insurance by Age Group 
st.header("Insurance Coverage by Age Group")

age_data = pd.DataFrame({
  "Age Group": ["19-25", "26-32", "55-64"],
  "Percent Insured": [78.0, 79.2, 74.8]
})


st.bar_chart(age_data.set_index("Age Group"))

st.header("Proposed Solutions")

st.write("""
Our team proposes a healthcare access platform that would help residents connect with healthcare resources.

Features Include:

Telehealth Appointments
- Meet with healthcare providers virtually
- Reduce travel time for routine appointments

Appointment Scheduling
- Book appointments online
- Receive appointment reminders

Transportation Resources
- Directions to nearby clincs and hospitals
- Contact information for local transportation services
- Information about transportation assistance programs

Pharmacy Communication
- View pharmacy contact information and hours
- Message local pharmacies

Emergency Care Information
- Closest hospitals and emergency rooms
- Emergency phone numbers
- Directions and estimated travel distances

Community Resource Page
- Insurance assistance information
- Financial aid programs
- Community health resources

Health Education Resources
- Vaccination information
- Healthy lifestyle resources

Health Reminders
- Medication reminders
- Appointment reminders
""")
