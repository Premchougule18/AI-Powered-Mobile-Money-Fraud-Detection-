import streamlit as st

st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp{
background:#F4F7FE;
}

.main-title{
text-align:center;
font-size:45px;
font-weight:bold;
color:#1E3A8A;
}

.subtitle{
text-align:center;
font-size:18px;
color:#555;
}

.box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 5px 20px rgba(0,0,0,0.1);
margin-bottom:20px;
}

.stButton>button{
background:#2563EB;
color:white;
height:55px;
width:100%;
border-radius:10px;
font-size:18px;
font-weight:bold;
border:none;
}

.metric-box{
background:#2563EB;
padding:20px;
border-radius:15px;
text-align:center;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------

st.sidebar.title("🏦 AI Banking Dashboard")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💳 Fraud Detection",
        "📈 Analytics",
        "⚙ Settings"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("🟢 Model Status : Active")

st.sidebar.info("""
Model : XGBoost

Accuracy : 99.98%

Version : 1.0
""")

st.sidebar.markdown("---")

st.sidebar.write("Developed using")
st.sidebar.write("✔ Python")
st.sidebar.write("✔ Streamlit")
st.sidebar.write("✔ XGBoost")

# ---------------- Header ----------------

st.markdown("<h1 class='main-title'>🛡 AI Fraud Detection System</h1>", unsafe_allow_html=True)

st.markdown("<p class='subtitle'>Real-Time Mobile Money Fraud Detection</p>", unsafe_allow_html=True)

st.write("")

# ---------------- Cards ----------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='metric-box'>
    <h3>Accuracy</h3>
    <h2>99.98%</h2>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-box'>
    <h3>Precision</h3>
    <h2>99%</h2>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-box'>
    <h3>Recall</h3>
    <h2>79%</h2>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='metric-box'>
    <h3>Model</h3>
    <h2>XGBoost</h2>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ---------------- Form ----------------

left,right = st.columns(2)

with left:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("💰 Transaction Details")

    step = st.number_input("Step")

    transaction = st.selectbox(
        "Transaction Type",
        [
            "CASH_IN",
            "CASH_OUT",
            "TRANSFER",
            "PAYMENT",
            "DEBIT"
        ]
    )

    amount = st.number_input("Amount")

    oldbalanceOrg = st.number_input("Old Balance Origin")

    newbalanceOrig = st.number_input("New Balance Origin")

    st.markdown("</div>", unsafe_allow_html=True)

with right:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("🏦 Destination Details")

    oldbalanceDest = st.number_input("Old Balance Destination")

    newbalanceDest = st.number_input("New Balance Destination")

    isFlaggedFraud = st.selectbox(
        "Flagged Fraud",
        [0,1]
    )

    st.write("")
    st.write("")

    predict = st.button("🚀 Predict Transaction")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- Result ----------------

if predict:

    st.success("Prediction code goes here.")

    # Replace this with your model prediction

    st.metric("Fraud Probability","98%")

    st.metric("Prediction","Legitimate")