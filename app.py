import streamlit as st
from database import (
    run_query,
    ask_ai,
    generate_sql,
    DATABASE_SCHEMA,
    validate_sql,
    get_table_schema,
    execute_sql,
    generate_answer
)
st.set_page_config(
    page_title="Hospital Management System",
    page_icon="⚡",
    layout="wide"
)

st.title("Hospital Management System")
st.write(
    "Hospital analytics dashboard for monitoring patients, "
    "doctors, appointments, treatments, and billing."
)
st.header("Database Overview")

# KPI Cards
def get_count(table):
    query = f"""
        SELECT COUNT(*) AS total
        FROM {table};
        """
    result = run_query(query)
    return result.iloc[0]["total"]

total_patients = get_count("patients")
total_doctors = get_count("doctors")
total_treatments = get_count("treatments")
total_appointments = get_count("appointments")
total_billing = get_count("billing")

with st.container(border=True):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("Total Patients:", total_patients)
    with col2:
        st.metric("Total Doctors:", total_doctors)
    with col3:
        st.metric("Total Appointments:", total_appointments)
    with col4:
        st.metric("Total Treatments:", total_treatments)
    with col5:
        st.metric("Total Billing:", total_billing)

st.divider()

# Filters
st.subheader("Filters")

status_query = """
SELECT DISTINCT status
FROM appointments
ORDER BY status;
"""
status_result = run_query(status_query)
appointment_statuses = status_result["status"].tolist()

with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        status_filter = st.selectbox(
            "Appointment Status",
            ["All"] + appointment_statuses
        )

# Build WHERE clause with proper quoting
where_clause = ""

if status_filter != "All":
    where_clause = f"WHERE status = '{status_filter}'"

st.divider()

# Appointments Status
st.subheader("Appointment Status")

query = f"""
SELECT
    status AS "Appointment Status",
    COUNT(*) AS "Total Appointments"
FROM appointments
{where_clause}
GROUP BY status
ORDER BY "Total Appointments" DESC;
"""
appointment_status = run_query(query)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(
        appointment_status,
        use_container_width=True
    )

with col2:
    st.bar_chart(
        appointment_status,
        x="Appointment Status",
        y="Total Appointments"
    )

st.divider()

# Revenue Overview
st.subheader("Revenue Overview")

query = """
SELECT
    ROUND(COALESCE(SUM(amount), 0), 2) AS total_revenue
FROM billing;
"""
revenue = run_query(query)
total_revenue = revenue.iloc[0]["total_revenue"]

st.metric(
    "Total Revenue",
    f"${total_revenue:,.2f}"
)

query = """
SELECT
    payment_status AS "Payment Status",
    COUNT(*) AS "Number of Payments",
    ROUND(SUM(amount), 2) AS "Total Amount"
FROM billing
GROUP BY payment_status
ORDER BY "Total Amount" DESC;
"""
payment_status = run_query(query)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(
        payment_status,
        use_container_width=True
    )

with col2:
    st.bar_chart(
        payment_status,
        x="Payment Status",
        y="Total Amount"
    )

st.divider()

# Treatment Analysis
st.subheader("Treatment Analysis")

query = """
SELECT
    treatment_type AS "Treatment Type",
    COUNT(*) AS "Times Performed",
    ROUND(SUM(cost), 2) AS "Total Revenue"
FROM treatments
GROUP BY treatment_type
ORDER BY "Times Performed" DESC;
"""
treatments = run_query(query)

st.dataframe(
    treatments,
    use_container_width=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Most Frequently Performed")
    st.bar_chart(
        treatments,
        x="Treatment Type",
        y="Times Performed"
    )

with col2:
    st.markdown("### Revenue by Treatment")
    st.bar_chart(
        treatments,
        x="Treatment Type",
        y="Total Revenue"
    )

st.divider()

# Doctor Performance
st.subheader("Doctor Performance")

query = f"""
SELECT
    doctor_id AS "Doctor ID",
    COUNT(*) AS "Total Appointments"
FROM appointments
{where_clause}
GROUP BY doctor_id
ORDER BY "Total Appointments" DESC;
"""
doctor_performance = run_query(query)

st.dataframe(
    doctor_performance,
    use_container_width=True
)

st.bar_chart(
    doctor_performance,
    x="Doctor ID",
    y="Total Appointments"
)

st.divider()

# Patient Analysis
st.subheader("Patient Analysis")

query = f"""
SELECT
    patient_id AS "Patient ID",
    COUNT(*) AS "Total Appointments"
FROM appointments
{where_clause}
GROUP BY patient_id
ORDER BY "Total Appointments" DESC;
"""
patient_analysis = run_query(query)

st.dataframe(
    patient_analysis,
    use_container_width=True
)

st.bar_chart(
    patient_analysis.head(10),
    x="Patient ID",
    y="Total Appointments"
)
# Table Schema
st.subheader("Table Schema")
st.write(
    get_table_schema("patients")
)
st.write(
    get_table_schema("doctors")
)
st.write(
    get_table_schema("appointments")
)
st.write(
    get_table_schema("treatments")
)
st.write(
    get_table_schema("billing")
)


# AI Chat Assistant
st.divider()
st.subheader("🤖 AI Chat Assistant")
st.write("Ask questions about the hospital data.")

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
prompt = st.chat_input("Ask something about the hospital data...")
if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.write(prompt)
    sql = generate_sql(
        prompt,
        DATABASE_SCHEMA
    )
    if validate_sql(sql):
        result = execute_sql(sql)
        response = generate_answer(
            prompt,
            result
        )

    else:
        response = "I could not generate a valid database query."
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
    with st.chat_message("assistant"):
        st.write(response)
