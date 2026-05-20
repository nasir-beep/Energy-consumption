import streamlit as st
import pandas as pd
import joblib

# Page configuration
st.set_page_config(
    page_title="Energy AI",
    page_icon="⚡",
    layout="wide"
)

# Load Model and features
model = joblib.load("energy_model.pkl")
feature_names = joblib.load("feature_names.pkl")


try:
    target_encoder = joblib.load("target_encoder.pkl")
    encoder_exists = True
except:
    encoder_exists = False


# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    color: white;
    font-size: 48px !important;
    font-weight: 700 !important;
}

.hero-text {
    color: #B0B3B8;
    font-size:18px;
}

.prediction-card {
    background: linear-gradient(135deg,#1f2937,#111827);
    padding: 30px;
    border-radius: 20px;
    border:1px solid #374151;
    text-align:center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

.big-result {
    font-size:40px;
    color:#00E5FF;
    font-weight:bold;
}

.small-text {
    color:#9CA3AF;
    font-size:16px;
}

.stButton>button {
    width:100%;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:600;
    background-color:#00C2FF;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# Hero section
st.markdown("Energy Consumption Platform")

st.markdown(
    "<p class='hero-text'>"
    "Predict energy consumption intelligently using machine learning and smart building indicators."
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# Sidebar inputs
st.sidebar.header("Energy Inputs")

temperature = st.sidebar.number_input(
    "Temperature",
    min_value=0.0,
    value=25.0
)

humidity = st.sidebar.number_input(
    "Humidity",
    min_value=0.0,
    value=50.0
)

square_footage = st.sidebar.number_input(
    "SquareFootage",
    min_value=0.0,
    value=1000.0
)

occupancy = st.sidebar.number_input(
    "Occupancy",
    min_value=0.0,
    value=5.0
)

renewable = st.sidebar.number_input(
    "RenewableEnergy",
    min_value=0.0,
    value=10.0
)

# Categorical inputs
hvac = st.sidebar.selectbox(
    "HVACUsage",
    ["Off", "On"]
)

lighting = st.sidebar.selectbox(
    "LightingUsage",
    ["Low", "Medium", "High"]
)

day = st.sidebar.selectbox(
    "DayOfWeek",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)

holiday = st.sidebar.selectbox(
    "Holiday",
    ["No", "Yes"]
)

# Manual encoding
hvac_map = {
    "Off": 0,
    "On": 1
}

lighting_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

day_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

holiday_map = {
    "No": 0,
    "Yes": 1
}

# Create input dataframe
input_df = pd.DataFrame({
    "Temperature": [temperature],
    "Humidity": [humidity],
    "SquareFootage": [square_footage],
    "Occupancy": [occupancy],
    "HVACUsage": [hvac_map[hvac]],
    "LightingUsage": [lighting_map[lighting]],
    "RenewableEnergy": [renewable],
    "DayOfWeek": [day_map[day]],
    "Holiday": [holiday_map[holiday]]
})

# Main layout
left, right = st.columns([1,1])

# Left panel
with left:

    st.subheader("Building Information")

    st.dataframe(
        input_df,
        use_container_width=True
    )

    predict_button = st.button(
        "Predict Energy Class"
    )

# Right panel
with right:

    st.subheader("AI Prediction")

    if predict_button:

        prediction = model.predict(
            input_df[feature_names]
        )

        pred_value = prediction[0]

        if pred_value == 1:
            label = "⚡ HIGH Energy Consumption"
        else:
            label = "🌱 LOW Energy Consumption"

        st.markdown(f"""
        <div class="prediction-card">
            <div class="small-text">
                Predicted Energy Consumption Class
            </div>
            <div class="big-result">
                {label}
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.info(
            "Enter building data in the sidebar and click Predict."
        )

# Footer
st.divider()

st.caption(
    "Energy Consumption Platform • Machine Learning Assignment • Streamlit Dashboard"
)