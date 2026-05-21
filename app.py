# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle
# import plotly.express as px
# import plotly.graph_objects as go
# from streamlit_option_menu import option_menu
# from datetime import datetime

# # =========================================================
# # PAGE CONFIG
# # =========================================================

# st.set_page_config(
#     page_title="AI Churn Prediction",
#     page_icon="🚀",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # =========================================================
# # CUSTOM CSS
# # =========================================================

# st.markdown("""
# <style>

# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

# html, body, [class*="css"]  {
#     font-family: 'Poppins', sans-serif;
# }

# .main {
#     background: linear-gradient(135deg,#050816,#0f172a,#111827);
#     color: white;
# }

# /* Glass Cards */

# .glass {
#     background: rgba(255,255,255,0.07);
#     border-radius: 20px;
#     padding: 25px;
#     backdrop-filter: blur(14px);
#     border: 1px solid rgba(255,255,255,0.1);
#     box-shadow: 0 8px 32px rgba(0,0,0,0.3);
# }

# /* Title */

# .main-title {
#     text-align: center;
#     font-size: 55px;
#     font-weight: 700;
#     background: linear-gradient(to right,#38bdf8,#8b5cf6,#ec4899);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
#     margin-bottom: 10px;
# }

# .subtitle {
#     text-align:center;
#     color:#cbd5e1;
#     font-size:18px;
#     margin-bottom:30px;
# }

# /* Buttons */

# .stButton>button {
#     width: 100%;
#     border-radius: 14px;
#     height: 3.5em;
#     border: none;
#     font-size: 18px;
#     font-weight: 600;
#     background: linear-gradient(90deg,#06b6d4,#3b82f6,#8b5cf6);
#     color: white;
#     transition: 0.4s ease;
# }

# .stButton>button:hover {
#     transform: scale(1.03);
#     box-shadow: 0 0 20px rgba(59,130,246,0.6);
# }

# /* Metrics */

# .metric-card {
#     background: rgba(255,255,255,0.05);
#     padding: 25px;
#     border-radius: 20px;
#     text-align: center;
#     border: 1px solid rgba(255,255,255,0.08);
# }

# .metric-card h1 {
#     color: #38bdf8;
#     font-size: 42px;
# }

# /* Sidebar */

# section[data-testid="stSidebar"] {
#     background: #0f172a;
# }

# /* Inputs */

# .stSelectbox div[data-baseweb="select"] {
#     background-color: rgba(255,255,255,0.08);
#     border-radius: 12px;
# }

# .stNumberInput input {
#     background-color: rgba(255,255,255,0.08);
# }

# </style>
# """, unsafe_allow_html=True)

# # =========================================================
# # LOAD DATA
# # =========================================================

# @st.cache_data
# def load_data():
#     return pd.read_csv("customer_churn_prediction_dataset.csv")

# data = load_data()

# # =========================================================
# # LOAD MODEL
# # =========================================================

# @st.cache_resource
# def load_model():
#     with open("Logistic_model.pkl", "rb") as file:
#         return pickle.load(file)

# model = load_model()

# # =========================================================
# # SIDEBAR
# # =========================================================

# with st.sidebar:

#     st.markdown("## 🚀 AI Navigation")

#     selected = option_menu(
#         menu_title=None,
#         options=["Dashboard","Predict","Analytics"],
#         icons=["house","robot","bar-chart"],
#         default_index=0,
#         styles={
#             "container": {
#                 "padding": "0!important",
#                 "background-color": "#0f172a",
#             },
#             "icon": {
#                 "color": "#38bdf8",
#                 "font-size": "18px"
#             },
#             "nav-link": {
#                 "font-size": "16px",
#                 "padding": "12px",
#                 "margin": "8px",
#                 "border-radius": "12px",
#                 "--hover-color": "#1e293b",
#             },
#             "nav-link-selected": {
#                 "background": "linear-gradient(90deg,#06b6d4,#8b5cf6)"
#             },
#         }
#     )

#     st.markdown("---")
#     st.info(f"🕒 {datetime.now().strftime('%d %B %Y')}")

# # =========================================================
# # HEADER
# # =========================================================

# st.markdown('<div class="main-title">⚡ AI Customer Churn Prediction</div>', unsafe_allow_html=True)

# st.markdown(
#     '<div class="subtitle">Smart • Interactive • Beautiful Machine Learning Dashboard</div>',
#     unsafe_allow_html=True
# )

# # =========================================================
# # DASHBOARD
# # =========================================================

# if selected == "Dashboard":

#     churn_rate = round(
#         (data['Churn'].value_counts(normalize=True).get('Yes',0))*100,
#         2
#     )

#     avg_charge = round(data['MonthlyCharges'].mean(),2)

#     avg_tenure = round(data['tenure'].mean(),2)

#     c1,c2,c3 = st.columns(3)

#     with c1:
#         st.markdown(f"""
#         <div class="metric-card">
#         <h3>📉 Churn Rate</h3>
#         <h1>{churn_rate}%</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     with c2:
#         st.markdown(f"""
#         <div class="metric-card">
#         <h3>💰 Avg Monthly Charges</h3>
#         <h1>${avg_charge}</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     with c3:
#         st.markdown(f"""
#         <div class="metric-card">
#         <h3>⏳ Avg Tenure</h3>
#         <h1>{avg_tenure}</h1>
#         </div>
#         """, unsafe_allow_html=True)

#     st.markdown("## 📊 Customer Insights")

#     col1,col2 = st.columns(2)

#     with col1:

#         fig = px.pie(
#             data,
#             names="Churn",
#             hole=0.6,
#             title="Customer Churn Distribution"
#         )

#         fig.update_layout(
#             template="plotly_dark",
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#         )

#         st.plotly_chart(fig,use_container_width=True)

#     with col2:

#         fig2 = px.histogram(
#             data,
#             x="MonthlyCharges",
#             color="Churn",
#             nbins=40,
#             title="Monthly Charges Distribution"
#         )

#         fig2.update_layout(
#             template="plotly_dark",
#             paper_bgcolor='rgba(0,0,0,0)',
#             plot_bgcolor='rgba(0,0,0,0)',
#         )

#         st.plotly_chart(fig2,use_container_width=True)

# # =========================================================
# # PREDICTION PAGE
# # =========================================================

# elif selected == "Predict":

#     st.markdown("## 🤖 Predict Customer Churn")

#     st.markdown("Fill customer details below 👇")

#     col1,col2,col3 = st.columns(3)

#     with col1:
#         gender = st.selectbox("Gender",["Male","Female"])
#         senior = st.selectbox("Senior Citizen",[0,1])
#         partner = st.selectbox("Partner",["Yes","No"])
#         dependents = st.selectbox("Dependents",["Yes","No"])
#         tenure = st.slider("Tenure",0,72,12)

#     with col2:
#         phone = st.selectbox("Phone Service",["Yes","No"])
#         internet = st.selectbox("Internet Service",["DSL","Fiber optic","No"])
#         security = st.selectbox("Online Security",["Yes","No"])
#         backup = st.selectbox("Online Backup",["Yes","No"])
#         support = st.selectbox("Tech Support",["Yes","No"])

#     with col3:
#         contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])
#         paperless = st.selectbox("Paperless Billing",["Yes","No"])
#         monthly = st.slider("Monthly Charges",0,200,75)
#         total = monthly * tenure

#     if st.button("🚀 Predict Churn"):

#         input_df = pd.DataFrame({

#             'gender':[gender],
#             'SeniorCitizen':[senior],
#             'Partner':[partner],
#             'Dependents':[dependents],
#             'tenure':[tenure],
#             'PhoneService':[phone],
#             'InternetService':[internet],
#             'OnlineSecurity':[security],
#             'OnlineBackup':[backup],
#             'TechSupport':[support],
#             'Contract':[contract],
#             'PaperlessBilling':[paperless],
#             'MonthlyCharges':[monthly],
#             'TotalCharges':[total]

#         })

#         try:

#             prediction = model.predict(input_df)[0]

#             probability = model.predict_proba(input_df)[0][1]

#             st.markdown("---")

#             if prediction == 1:

#                 st.error(f"⚠️ High Churn Risk : {probability*100:.2f}%")

#             else:

#                 st.success(f"✅ Customer Likely To Stay : {(1-probability)*100:.2f}%")

#             gauge = go.Figure(go.Indicator(
#                 mode="gauge+number",
#                 value=probability*100,
#                 title={'text': "Churn Probability"},
#                 gauge={
#                     'axis': {'range': [0,100]},
#                     'bar': {'color': "#06b6d4"},
#                     'steps': [
#                         {'range':[0,40],'color':'green'},
#                         {'range':[40,70],'color':'orange'},
#                         {'range':[70,100],'color':'red'},
#                     ]
#                 }
#             ))

#             gauge.update_layout(
#                 template="plotly_dark",
#                 paper_bgcolor='rgba(0,0,0,0)',
#                 font={'color':'white'}
#             )

#             st.plotly_chart(gauge,use_container_width=True)

#         except Exception as e:

#             st.error(f"Prediction Error : {e}")

# # =========================================================
# # ANALYTICS
# # =========================================================

# elif selected == "Analytics":

#     st.markdown("## 📈 Advanced Analytics")

#     c1,c2 = st.columns(2)

#     with c1:

#         fig3 = px.box(
#             data,
#             x="Churn",
#             y="MonthlyCharges",
#             color="Churn",
#             title="Monthly Charges vs Churn"
#         )

#         fig3.update_layout(
#             template="plotly_dark",
#             paper_bgcolor='rgba(0,0,0,0)'
#         )

#         st.plotly_chart(fig3,use_container_width=True)

#     with c2:

#         fig4 = px.scatter(
#             data,
#             x="tenure",
#             y="TotalCharges",
#             color="Churn",
#             size="MonthlyCharges",
#             title="Tenure vs Total Charges"
#         )

#         fig4.update_layout(
#             template="plotly_dark",
#             paper_bgcolor='rgba(0,0,0,0)'
#         )

#         st.plotly_chart(fig4,use_container_width=True)

#     st.markdown("## 🗂 Dataset Preview")

#     st.dataframe(data,use_container_width=True)

# # =========================================================
# # FOOTER
# # =========================================================

# st.markdown("---")

# st.markdown(
#     "<center>✨ Built with Streamlit • Plotly • Machine Learning ✨</center>",
#     unsafe_allow_html=True
# )




import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
from datetime import datetime
import joblib
import pickle

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AI Customer Churn Prediction",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

.main {
    background: linear-gradient(135deg,#050816,#0f172a,#111827);
    color: white;
}

/* Title */

.main-title {
    text-align: center;
    font-size: 55px;
    font-weight: 700;
    background: linear-gradient(to right,#38bdf8,#8b5cf6,#ec4899);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 10px;
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

/* Buttons */

.stButton>button {
    width: 100%;
    border-radius: 14px;
    height: 3.5em;
    border: none;
    font-size: 18px;
    font-weight: 600;
    background: linear-gradient(90deg,#06b6d4,#3b82f6,#8b5cf6);
    color: white;
    transition: 0.4s ease;
}

.stButton>button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 20px rgba(59,130,246,0.6);
}

/* Metrics */

.metric-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(255,255,255,0.08);
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: #0f172a;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():

    try:
        data = pd.read_csv("customer_churn_prediction_dataset.csv")
        return data

    except Exception as e:

        st.error(f"❌ Dataset Loading Error: {e}")
        return None

data = load_data()

# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    # Try Joblib
    try:

        model = joblib.load("Logistic_model.pkl")

        st.success("✅ Model Loaded Successfully")

        return model

    except Exception as e1:

        # Try Pickle
        try:

            with open("Logistic_model.pkl", "rb") as file:
                model = pickle.load(file)

            st.success("✅ Model Loaded Successfully")

            return model

        except Exception as e2:

            st.error("❌ Model Loading Failed")

            st.write("### Possible Reasons")
            st.write("- Wrong Python Version")
            st.write("- Corrupted Model File")
            st.write("- Different sklearn Version")

            st.write("Joblib Error:", e1)
            st.write("Pickle Error:", e2)

            return None

model = load_model()

# Stop app if model failed
if model is None:
    st.stop()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## 🚀 Navigation")

    selected = option_menu(
        menu_title=None,
        options=["Dashboard","Predict","Analytics"],
        icons=["house","robot","bar-chart"],
        default_index=0,
        styles={
            "container": {
                "padding": "0!important",
                "background-color": "#0f172a",
            },
            "icon": {
                "color": "#38bdf8",
                "font-size": "18px"
            },
            "nav-link": {
                "font-size": "16px",
                "padding": "12px",
                "margin": "8px",
                "border-radius": "12px",
            },
            "nav-link-selected": {
                "background": "linear-gradient(90deg,#06b6d4,#8b5cf6)"
            },
        }
    )

    st.markdown("---")
    st.info(f"📅 {datetime.now().strftime('%d %B %Y')}")

# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">⚡ AI Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Interactive Machine Learning Dashboard</div>',
    unsafe_allow_html=True
)

# =========================================================
# DASHBOARD
# =========================================================

if selected == "Dashboard":

    if data is not None:

        churn_rate = round(
            (data['Churn'].value_counts(normalize=True).get('Yes',0))*100,
            2
        )

        avg_charge = round(data['MonthlyCharges'].mean(),2)

        avg_tenure = round(data['tenure'].mean(),2)

        c1,c2,c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class="metric-card">
            <h2>📉 Churn Rate</h2>
            <h1>{churn_rate}%</h1>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class="metric-card">
            <h2>💰 Avg Charges</h2>
            <h1>${avg_charge}</h1>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class="metric-card">
            <h2>⏳ Avg Tenure</h2>
            <h1>{avg_tenure}</h1>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("## 📊 Customer Analytics")

        col1,col2 = st.columns(2)

        with col1:

            fig = px.pie(
                data,
                names="Churn",
                hole=0.6,
                title="Customer Churn Distribution"
            )

            fig.update_layout(template="plotly_dark")

            st.plotly_chart(fig,use_container_width=True)

        with col2:

            fig2 = px.histogram(
                data,
                x="MonthlyCharges",
                color="Churn",
                nbins=40,
                title="Monthly Charges Distribution"
            )

            fig2.update_layout(template="plotly_dark")

            st.plotly_chart(fig2,use_container_width=True)

# =========================================================
# PREDICTION PAGE
# =========================================================

elif selected == "Predict":

    st.markdown("## 🤖 Predict Customer Churn")

    col1,col2,col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender",["Male","Female"])
        senior = st.selectbox("Senior Citizen",[0,1])
        tenure = st.slider("Tenure",0,72,12)

    with col2:
        partner = st.selectbox("Partner",["Yes","No"])
        internet = st.selectbox("Internet Service",["DSL","Fiber optic","No"])
        contract = st.selectbox("Contract",["Month-to-month","One year","Two year"])

    with col3:
        paperless = st.selectbox("Paperless Billing",["Yes","No"])
        monthly = st.slider("Monthly Charges",0,200,70)

    total = monthly * tenure

    if st.button("🚀 Predict Churn"):

        try:

            input_df = pd.DataFrame({

                'gender':[gender],
                'SeniorCitizen':[senior],
                'Partner':[partner],
                'tenure':[tenure],
                'InternetService':[internet],
                'Contract':[contract],
                'PaperlessBilling':[paperless],
                'MonthlyCharges':[monthly],
                'TotalCharges':[total]

            })

            prediction = model.predict(input_df)[0]

            if hasattr(model, "predict_proba"):

                probability = model.predict_proba(input_df)[0][1]

            else:

                probability = 0.5

            st.markdown("---")

            if prediction == 1:

                st.error(f"⚠️ High Churn Risk : {probability*100:.2f}%")

            else:

                st.success(f"✅ Customer Likely To Stay : {(1-probability)*100:.2f}%")

            gauge = go.Figure(go.Indicator(
                mode="gauge+number",
                value=probability*100,
                title={'text': "Churn Probability"},
                gauge={
                    'axis': {'range': [0,100]},
                    'bar': {'color': "#06b6d4"},
                    'steps': [
                        {'range':[0,40],'color':'green'},
                        {'range':[40,70],'color':'orange'},
                        {'range':[70,100],'color':'red'},
                    ]
                }
            ))

            gauge.update_layout(template="plotly_dark")

            st.plotly_chart(gauge,use_container_width=True)

        except Exception as e:

            st.error(f"❌ Prediction Error: {e}")

# =========================================================
# ANALYTICS
# =========================================================

elif selected == "Analytics":

    st.markdown("## 📈 Advanced Analytics")

    if data is not None:

        c1,c2 = st.columns(2)

        with c1:

            fig3 = px.box(
                data,
                x="Churn",
                y="MonthlyCharges",
                color="Churn",
                title="Monthly Charges vs Churn"
            )

            fig3.update_layout(template="plotly_dark")

            st.plotly_chart(fig3,use_container_width=True)

        with c2:

            fig4 = px.scatter(
                data,
                x="tenure",
                y="TotalCharges",
                color="Churn",
                size="MonthlyCharges",
                title="Tenure vs Total Charges"
            )

            fig4.update_layout(template="plotly_dark")

            st.plotly_chart(fig4,use_container_width=True)

        st.markdown("## 🗂 Dataset Preview")

        st.dataframe(data,use_container_width=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    "<center>✨ Built with Streamlit • Machine Learning • Plotly ✨</center>",
    unsafe_allow_html=True
)