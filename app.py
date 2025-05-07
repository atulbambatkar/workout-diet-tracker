import streamlit as st
import datetime

st.set_page_config(page_title="Workout & Diet Tracker", layout="centered")
st.title("🏋️ Workout & Diet Tracker")

# Sidebar navigation
menu = st.sidebar.radio("Go to", ["🏋️ Workout Tracker", "🍱 Budget Diet Plan", "📈 Weight Progress"])



# Initialize session state
if "workouts" not in st.session_state:
    st.session_state.workouts = []

# Workout Tracker Page
if menu == "🏋️ Workout Tracker":
    st.header("💪 Log Your Workout")
# Diet Plan Section
elif menu == "🍱 Budget Diet Plan":
    st.header("🍽️ ₹200 Monthly Diet Plan for Muscle Gain")
    st.markdown("""
    Here's a simple, protein-rich diet plan on a budget:

    - 🥚 **6 Eggs per day** → ₹5 x 30 = ₹150/month  
    - 🍌 **2 Bananas daily** → ₹1.5 x 30 = ₹45/month  
    - 🌾 **Roasted Chana (50g daily)** → ₹5/day = ₹150/month  
    - 🥛 **1 Glass milk alternate days** (Optional) → ₹100/month  

    ✅ *Total: Approx ₹200–₹250*  
    ✅ *Protein: 50–60g daily — enough for muscle gain!*

    💡 Drink 3L water, sleep 7–8 hours, and avoid sugar (you're already doing this 💪)
    """)
    import matplotlib.pyplot as plt

# Weight Tracker Section
elif menu == "📈 Weight Progress":
    st.header("📊 Track Your Weight Progress")

    # Initialize weight history
    if "weights" not in st.session_state:
        st.session_state.weights = []

    # Inputs
    weight = st.number_input("Enter your weight (kg)", min_value=20.0, max_value=200.0, step=0.5)
    weight_date = st.date_input("Date", datetime.date.today(), key="weight_date")

    if st.button("➕ Add Weight"):
        st.session_state.weights.append({
            "weight": weight,
            "date": weight_date
        })
        st.success("✅ Weight entry saved!")

    # Show history
    if st.session_state.weights:
        st.subheader("📅 Weight Log")
        for w in st.session_state.weights:
            st.write(f"{w['date']} - {w['weight']} kg")

        # Plotting
        dates = [w["date"] for w in st.session_state.weights]
        weights = [w["weight"] for w in st.session_state.weights]

        fig, ax = plt.subplots()
        ax.plot(dates, weights, marker='o', linestyle='-')
        ax.set_title("Your Weight Progress")
        ax.set_xlabel("Date")
        ax.set_ylabel("Weight (kg)")
        st.pyplot(fig)


    # Inputs
    workout_type = st.selectbox("Workout Type", ["Push", "Pull", "Legs", "Home Full Body", "Cardio"])
    duration = st.slider("Duration (minutes)", 10, 120, 30)
    workout_date = st.date_input("Workout Date", datetime.date.today())

    # Save workout
    if st.button("➕ Add Workout"):
        st.session_state.workouts.append({
            "type": workout_type,
            "duration": duration,
            "date": workout_date
        })
        st.success("✅ Workout saved!")

    # Show history
    if st.session_state.workouts:
        st.subheader("📅 Workout History")
        for i, w in enumerate(st.session_state.workouts):
            st.write(f"{i+1}. {w['date']} - {w['type']} for {w['duration']} minutes")
