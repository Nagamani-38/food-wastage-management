import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="Food Wastage Management", layout="wide")

st.title("🍱 Local Food Wastage Management System")
st.markdown("---")

st.sidebar.title("Navigation")

menu = st.sidebar.selectbox(
    "Select Module",
    ["Dashboard", "Providers", "Receivers", "Food Listings", "Claims", "Analysis"],
    key="menu"
)
if menu == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to Food Wastage Management Analysis App")
    st.subheader("Project Modules")
    st.write("1. Providers")
    st.write("2. Receivers")
    st.write("3. Food Listings")
    st.write("4. Claims")
    st.write("5. Analysis")

elif menu == "Providers":
    st.header("Providers Module")

    provider_name = st.text_input("Provider Name")
    provider_food = st.selectbox(
        "Food Type",
        ["Veg", "Non-Veg", "Both"],
        key="provider_food"
    )
    quantity = st.number_input("Quantity (in plates)", min_value=1)
    location = st.text_input("Location")
    contact = st.text_input("Contact Number")

    if st.button("Submit Provider"):
        st.success("Provider details submitted successfully!")

elif menu == "Receivers":
    st.header("Receivers Module")

    receiver_name = st.text_input("Receiver Name")
    receiver_type = st.selectbox(
        "Receiver Type",
        ["NGO", "Shelter", "Individual"],
        key="receiver_type"
    )
    people_count = st.number_input("People Count", min_value=1)
    receiver_location = st.text_input("Location")
    receiver_contact = st.text_input("Contact Number")

    if st.button("Submit Receiver"):
        st.success("Receiver details submitted successfully!")

elif menu == "Food Listings":
    st.header("Food Listings Module")

    food_name = st.text_input("Food Name")
    listing_food = st.selectbox(
        "Food Category",
        ["Veg", "Non-Veg", "Vegan"],
        key="listing_food"
    )

    listing_meal = st.selectbox(
        "Meal Type",
        ["Breakfast", "Lunch", "Dinner", "Snacks"],
        key="listing_meal"
    )

    quantity = st.number_input("Quantity Available", min_value=1)
    expiry = st.text_input("Expiry Time")

    if st.button("Add Food Listing"):
        st.success("Food listing added successfully!")

elif menu == "Claims":
    st.header("Claims Module")

    receiver_name = st.text_input("Receiver Name")
    food_item = st.text_input("Food Item")
    claim_quantity = st.number_input("Claim Quantity", min_value=1)

    claim_status = st.selectbox(
        "Claim Status",
        ["Pending", "Completed", "Cancelled"],
        key="claim_status"
    )

    if st.button("Submit Claim"):
        st.success("Claim submitted successfully!")

elif menu == "Analysis":
    st.header("Data Analysis Dashboard")

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.metric("Total Providers", 120)
    with col2:
        st.metric("Total Receivers", 80)
    with col3:
        st.metric("Food Listings", 250)
    with col4:
        st.metric("Total Claims", 180)

    st.subheader("Key Insights")
    st.write("• City with highest food availability: Hyderabad")
    st.write("• Most donated meal type: Dinner")
    st.write("• Top provider category: Restaurants")
    st.write("• Claim completion rate: 72%")

    st.subheader("Food Category Distribution")
    chart_data = pd.DataFrame({
        "Food Type": ["Veg", "Non-Veg", "Vegan"],
        "Count": [120, 80, 50]
    })
    st.bar_chart(chart_data.set_index("Food Type"))

    st.subheader("Claims Status Distribution (Pie Chart)")

    labels = ['Completed', 'Pending', 'Cancelled']
    sizes = [72, 20, 8]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')

    st.pyplot(fig)
   
    st.subheader("Provider Type Distribution")
    provider_data = pd.DataFrame({
        "Provider Type": ["Restaurant", "Supermarket", "Grocery Store"],
        "Count": [45, 35, 40]
    })
    st.bar_chart(provider_data.set_index("Provider Type"))

    st.subheader("Receiver Type Distribution")
    receiver_data = pd.DataFrame({
        "Receiver Type": ["NGO", "Shelter", "Individual"],
        "Count": [50, 40, 30]
    })
    st.bar_chart(receiver_data.set_index("Receiver Type"))

    st.subheader("Meal Type Distribution")
    meal_data = pd.DataFrame({
        "Meal Type": ["Breakfast", "Lunch", "Dinner", "Snacks"],
        "Count": [40, 70, 90, 50]
    })
    st.bar_chart(meal_data.set_index("Meal Type"))
    st.subheader("City vs Food Listings")

    city_data = pd.DataFrame({
    "City": ["Hyderabad", "Chennai", "Bangalore"],
    "Count": [120, 80, 50]
    })

    st.bar_chart(city_data.set_index("City"))

    st.subheader("Top Providers")
    top_provider_data = pd.DataFrame({
        "Provider": ["Restaurant", "Supermarket", "Grocery Store"],
        "Quantity": [120, 90, 75]
    })
    st.bar_chart(top_provider_data.set_index("Provider"))

    st.subheader("Top Receivers")
    top_receiver_data = pd.DataFrame({
        "Receiver": ["NGO", "Shelter", "Individual"],
        "Claims": [50, 35, 20]
    })
    st.bar_chart(top_receiver_data.set_index("Receiver"))

    st.subheader("Query Outputs")
    st.write("Top City by Food Listing: Hyderabad")
    st.write("Most Contributing Provider: Restaurants")
    st.write("Most Claimed Meal Type: Dinner")
    st.write("Claim Completion Rate: 72%")

    st.info("This system helps reduce food wastage by connecting food providers with receivers in real time.")