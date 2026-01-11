import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Patient Management System", layout="centered")

st.title("🏥 Patient Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["View All Patients", "View Patient", "Create Patient", "Update Patient", "Delete Patient","AI Health Advisor"]
)

# ---------------- VIEW ALL ----------------
if menu == "View All Patients":
    st.subheader("📋 All Patients")
    res = requests.get(f"{BASE_URL}/view")

    if res.status_code == 200:
        data = res.json()
        st.json(data)
    else:
        st.error("Failed to fetch data")

# ---------------- VIEW SINGLE ----------------
elif menu == "View Patient":
    st.subheader("🔍 View Patient Details")
    patient_id = st.text_input("Enter Patient ID")

    if st.button("Search"):
        res = requests.get(f"{BASE_URL}/patient/{patient_id}")

        if res.status_code == 200:
            st.json(res.json())
        else:
            st.error("Patient not found")

# ---------------- CREATE ----------------
elif menu == "Create Patient":
    st.subheader("➕ Create New Patient")

    with st.form("create_form"):
        pid = st.text_input("Patient ID")
        name = st.text_input("Name")
        city = st.text_input("City")
        age = st.number_input("Age", min_value=1)
        gender = st.selectbox("Gender", ["male", "female", "others"])
        height = st.number_input("Height (m)", min_value=0.1)
        weight = st.number_input("Weight (kg)", min_value=0.1)

        submit = st.form_submit_button("Create")

    if submit:
        payload = {
            "id": pid,
            "name": name,
            "city": city,
            "age": age,
            "gender": gender,
            "height": height,
            "weight": weight
        }

        res = requests.post(f"{BASE_URL}/create", json=payload)

        if res.status_code == 201:
            st.success("Patient created successfully 🎉")
        else:
            st.error(res.json()["detail"])

# ---------------- UPDATE ----------------
elif menu == "Update Patient":
    st.subheader("✏️ Update Patient")

    patient_id = st.text_input("Patient ID")

    with st.form("update_form"):
        name = st.text_input("Name (optional)")
        city = st.text_input("City (optional)")
        age = st.number_input("Age (optional)", min_value=0)
        height = st.number_input("Height (optional)", min_value=0.0)
        weight = st.number_input("Weight (optional)", min_value=0.0)

        submit = st.form_submit_button("Update")

    if submit:
        payload = {}

        if name: payload["name"] = name
        if city: payload["city"] = city
        if age > 0: payload["age"] = age
        if height > 0: payload["height"] = height
        if weight > 0: payload["weight"] = weight

        res = requests.put(f"{BASE_URL}/edit/{patient_id}", json=payload)

        if res.status_code == 200:
            st.success("Patient updated successfully ✅")
        else:
            st.error("Update failed")

# ---------------- DELETE ----------------
elif menu == "Delete Patient":
    st.subheader("🗑 Delete Patient")
    patient_id = st.text_input("Patient ID")

    if st.button("Delete"):
        res = requests.delete(f"{BASE_URL}/delete/{patient_id}")

        if res.status_code == 200:
            st.success("Patient deleted 🧹")
        else:
            st.error("Patient not found")


        
elif menu == "AI Health Advisor":
    st.subheader("🤖 AI Health Advisor")
    patient_id = st.text_input("Patient ID")

    if st.button("Get AI Advice"):
        res = requests.get(f"{BASE_URL}/ai/health-advice/{patient_id}")

        if res.status_code == 200:
            st.success("AI Analysis Completed")
            st.write(res.json()["ai_advice"])
        else:
            st.error("Patient not found")
        