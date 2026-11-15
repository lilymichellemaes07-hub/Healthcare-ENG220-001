import streamlit as st
import pandas as pd
import plotly.express as px

# Page Title
st.sidebar.title("Healthcare Access Dashboard")

# Team Members
st.sidebar.markdown("""
### Group 18

- Lily Maes
- Aubriana Martinez
- Sam Martin
- Sam Esparza
""")

st.title("Healthcare Access in Cuba, New Mexico")

st.info(
  "Analyzing healthcare accessibility, insurance coverage, transportation barriers, and potiental solutions for residents of Cuba, New Mexico."
)

# Project Overview
st.header("Project Overview")

st.write("""
This project analyzes healthcare accessibility in Cuba, New Mexico. 
Our research focuses on healthcare services, insurance coverage, 
income levels, transportation barriers, and possible solutions 
to improve healthcare access in rural communities.
""")

# Healthcare Challenges
st.header("Healthcare Challenges")

st.write("""
- No full-service hospital in Cuba, NM
- Travel long distances for specialized care
- Transportation limitations
- Healthcare provider shortages
- Finanical and insurance barriers
""")

# Insurance Coverage Results
st.header("Insurance Coverage Results")

col1, col2, col3 = st.columns(3)
with col1:
  st.metric("Population Analyzed", "4,876")
with col2:
  st.metric(
    label = "Insured Residents", 
    value = "4313")
with col3:
  st.metric(
    label = "Uninsured Residents", 
    value = "563")

st.write("""
88.5% of residents have health insurance coverage,
while 11.5% remain uninsured.
""")

insurance_df = pd.DataFrame({
  "Category" : ["Insured", "Uninsured"],
  "Population" : [4313, 563]
})

fig = px.pie(
  insurance_df,
  values="Population",
  names="Category",
  title="Insurance Coverage Distribution",
  color="Category",
  color_discrete_map={
    "Insured" : "#A78BFA",
    "Uninsured" : "C4A1E8",
  }
)
st.plotly_chart(fig, use_container_width=True)


# Insurance by Age Group 
st.header("Insurance Coverage by Age Group")

age_data = pd.DataFrame({
  "Age Group": ["19-25", "26-34", "55-64"],
  "Percent Insured": [78.0, 79.2, 74.8]
})

st.bar_chart(age_data.set_index("Age Group"))

st.write("""
Residents ages 55-64 had the lowest insurance coverage rate.
Young adults, ages 19-25 and 26-34, also showed lower rates
of insurance compared to other age groups.
""")

# Income and Healthcare Access
st.header("Income and Healthcare Access")

income_data = pd.DataFrame({
  "Income Level": [
    "Below 138% Poverty", "138-399% Poverty",
    "400%+ Poverty" 
  ],
  "Percent Insured": [85.3, 91.0, 91.3]
})

st.bar_chart(income_data.set_index("Income Level"))

st.write("""
Our analysis found that lower income residents generally had
lower insurance coverage rates than higher income residents.
Financial barriers can make healthcare services more difficult
to access.
""")

# Key findings 
st.header("Key Findings")

st.write("""
- 11.5% of residents remain uninsured.
- Adults ages 55-64 had the lowest insurance coverage rate. 
- Lower income residents experienced lower insurance coverage.
- Transportation and distance continue to impact healthcare access.
""")
# Proposed Solutions 
st.header("Proposed Healthcare Access Platform")

st.subheader("Telehealth Appointments")
st.write("- Meet with healthcare providers virtually")
st.write("- Reduce travel time for routine appointments")

st.subheader("Appointment Scheduling")
st.write("- Book appointments online")
st.write("- Receive appointment reminders")

st.subheader("Transportation Resources")
st.write("- Directions to nearby clinics and hospitals")
st.write("- Contact information for local transportation services")
st.write("- Information about transportation assistance programs")

st.subheader("Pharmacy Communication")
st.write("- View pharmacy contact information and hours")
st.write("- Message local pharmacies")

st.subheader("Emergency Care Information")
st.write("- Closest hospitals and emergency rooms")
st.write("- Emergency phone numbers")
st.write("- Directions and destimated travel distances")

st.subheader("Community Resource Page")
st.write("- Insurance assistance information")
st.write("- Financial aid programs")
st.write("- Community health programs")

st.subheader("Health Education Resources")
st.write("- Vaccination information")
st.write("- Healthy lifestyle resources")

st.subheader("Health Reminders")
st.write("- Medication reminders")
st.write("- Appointment reminders")

# Conclusion
st.header("Conclusion")

st.write("""
Healthcare access remains a challenge for many residents of
Cuba, New Mexico. Transportation barrieres, provider shortages,
and insurance limitations can affect access to care.

By analyzing healthcare data and developing healthcare access
platform, our team hopes to identify solutions that improve 
communication, accessibility, and overall health outcomes for
the community.
""")

# Data Sources
st.header("Data Sources")

st.write("""
- U.S. Census Bureau
- American Community Survey (ACS)
- CDC PLACES
- New Mexico Department of Health
- New Mexico Human Services Department
""")



