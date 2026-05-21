import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# Load images
logo = Image.open("images/logo.png")
house = Image.open("images/house.png")
high = Image.open("images/high.png")
low = Image.open("images/low.png")

# Page configuration
st.set_page_config(
    page_title="Energy Consumption Platform",
    page_icon=logo,
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

col1, col2 = st.columns([1,5])
with col1:
    st.image(logo, width=110)

with col2:
    st.title("Energy Consumption Platform")
    st.markdown(
        "<p class='hero-text'>"
        "Predict and manage energy consumption using machine learning and smart sustainability recommendations."
        "</p>",
        unsafe_allow_html=True
    )

st.divider()

# Sidebar inputs
st.sidebar.image(house, width=80)
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
    "HVAC Usage",
    ["Off", "On"]
)

lighting = st.sidebar.selectbox(
    "Lighting Usage",
    ["Low", "Medium", "High"]
)

day = st.sidebar.selectbox(
    "Day Of Week",
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
        "Predict Energy Consumption"
    )

# Right panel
with right:

    st.subheader("AI Prediction")

    if predict_button:

        prediction = model.predict(
            input_df[feature_names]
        )

        pred_value = prediction[0]

        # High energy prediction
        if pred_value == 1:

            st.image(high, width=120)

            st.markdown("""
            <div class="prediction-card">
                <div class="small-text">
                    Prediction Result
                </div>

                <div class="big-result">
                    HIGH Energy Consumption
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.warning("Recommended Actions")

            if hvac == "On":
                st.write("• Reduce or optimize HVAC usage")

            if lighting == "High":
                st.write("• Lower lighting intensity")

            if occupancy > 10:
                st.write("• Monitor occupancy-related demand")

            if renewable < 20:
                st.write("• Increase renewable energy contribution")

            st.write(
                "• Schedule heavy energy activities during off-peak periods"
            )

        # Low energy prediction
        else:

            st.image(low, width=120)

            st.markdown("""
            <div class="prediction-card">
                <div class="small-text">
                    Prediction Result
                </div>

                <div class="big-result">
                    LOW Energy Consumption
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.success("Energy Efficient Status")

            st.write(
                "• Current settings are energy efficient"
            )

            st.write(
                "• Maintain operating conditions"
            )

            st.write(
                "• Continue sustainability practices"
            )

    else:

        st.info(
            "Enter building information and click Predict."
        )

# Footer
st.divider()

st.caption(
    "Energy Consumption Platform • Machine Learning Assignment • Sustainability Decision Support System"
)