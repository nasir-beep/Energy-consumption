import streamlit as st
import pandas as pd
import joblib

# PAGE CONFIG
st.set_page_config(
    page_title="Energy AI",
    page_icon="⚡",
    layout="wide"
)

# LOAD MODEL
model = joblib.load("energy_model.pkl")
feature_names = joblib.load("feature_names.pkl")


try:
    target_encoder = joblib.load("target_encoder.pkl")
    encoder_exists = True
except:
    encoder_exists = False


# CUSTOM CSS
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


# HERO SECTION
st.markdown("Energy Consumption Platform")

st.markdown(
    "<p class='hero-text'>"
    "Predict energy consumption intelligently using machine learning and smart building indicators."
    "</p>",
    unsafe_allow_html=True
)

st.divider()


# SIDEBAR INPUTS
st.sidebar.header("Energy Inputs")

inputs = {}

for feature in feature_names:
    inputs[feature] = st.sidebar.number_input(
        feature,
        value=0.0
    )


# MAIN LAYOUT
left, right = st.columns([1,1])

# LEFT PANEL
with left:

    st.subheader("Building Information")

    input_df = pd.DataFrame([inputs])

    st.dataframe(
        input_df,
        use_container_width=True
    )

    predict_button = st.button("Predict Energy Class")

# RIGHT PANEL
with right:

    st.subheader("AI Prediction")

    if predict_button:

        prediction = model.predict(
            input_df[feature_names]
        )

        if encoder_exists:
            label = target_encoder.inverse_transform(prediction)[0]
        else:
            label = prediction[0]

        st.markdown(f"""
        <div class="prediction-card">
            <div class="small-text">
                Predicted Energy Consumption
            </div>
            <div class="big-result">
                {label}
            </div>
        </div>
        """, unsafe_allow_html=True)

    else:

        st.info(
            "Enter values in the sidebar and click Predict."
        )


# FOOTER
st.divider()

st.caption(
    "Energy AI Platform • Machine Learning Assignment • Streamlit Dashboard"
)