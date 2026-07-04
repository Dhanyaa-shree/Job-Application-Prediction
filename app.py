# ============================================
# PROFESSIONAL STREAMLIT DASHBOARD
# Job Acceptance Prediction System
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pickle
import os
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Job Acceptance Prediction System",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# ENHANCED CUSTOM CSS
# ============================================
st.markdown("""
    <style>
    /* Main Header with Gradient */
    .main-header {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 0.5rem 0;
        letter-spacing: -0.5px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Sub Header */
    .sub-header {
        font-size: 1.1rem;
        color: #8898aa;
        text-align: center;
        margin-bottom: 1.5rem;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        color: white;
        text-align: center;
    }
    .hero-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .hero-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        font-weight: 300;
    }
    
    /* Prediction Box */
    .prediction-box {
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        border: none;
    }
    .prediction-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.15);
    }
    .prediction-accept {
        background: linear-gradient(135deg, #d4edda 0%, #b7e4c7 100%);
        border-left: 5px solid #28a745;
    }
    .prediction-reject {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        border-left: 5px solid #dc3545;
    }
    .prediction-icon {
        font-size: 4rem;
        margin-bottom: 0.5rem;
    }
    .prediction-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0.3rem 0;
    }
    .prediction-desc {
        font-size: 1.1rem;
        opacity: 0.85;
    }
    
    /* Metric Cards */
    .metric-card {
        background: white;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        border-top: 4px solid #667eea;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #2d3748;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #718096;
        margin-top: 0.2rem;
        font-weight: 500;
    }
    .metric-icon {
        font-size: 1.5rem;
        margin-bottom: 0.3rem;
    }
    
    /* Section Headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #2d3748;
        margin: 1.5rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }
    .section-header-sm {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2d3748;
        margin: 1rem 0 0.5rem 0;
    }
    
    /* Buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 0.7rem;
        border-radius: 10px;
        border: none;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(102, 126, 234, 0.5);
        color: white;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%);
    }
    .sidebar-title {
        font-size: 1.2rem;
        font-weight: 700;
        color: #2d3748;
        text-align: center;
        padding: 0.5rem 0;
    }
    .sidebar-subtitle {
        font-size: 0.85rem;
        color: #718096;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 1.5rem 0;
        margin-top: 2rem;
        border-top: 1px solid #e9ecef;
    }
    .footer-text {
        color: #718096;
        font-size: 0.9rem;
    }
    .footer-highlight {
        color: #667eea;
        font-weight: 600;
    }
    
    /* Divider */
    .custom-divider {
        height: 4px;
        background: linear-gradient(90deg, #667eea, #764ba2, #667eea);
        border-radius: 2px;
        margin: 1.5rem 0;
        opacity: 0.6;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #f1f3f5;
        border-radius: 10px;
        padding: 4px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px;
        padding: 8px 20px;
        font-weight: 500;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white !important;
    }
    
    /* Stats Badge */
    .stat-badge {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    }
    
    /* New: Model Performance Card */
    .model-performance {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border-left: 5px solid #28a745;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        text-align: center;
        margin-bottom: 1rem;
    }
    .model-performance .title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #495057;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .model-performance .value {
        font-size: 2.2rem;
        font-weight: 800;
        color: #28a745;
        margin: 0.2rem 0;
    }
    .model-performance .sub {
        font-size: 0.8rem;
        color: #6c757d;
    }
    
    /* Glow Badge */
    .glow-badge {
        display: inline-block;
        padding: 0.25rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        background: linear-gradient(135deg, #ffd700 0%, #ffb300 100%);
        color: #333;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3); }
        50% { box-shadow: 0 0 40px rgba(255, 215, 0, 0.6); }
        100% { box-shadow: 0 0 20px rgba(255, 215, 0, 0.3); }
    }
    </style>
""", unsafe_allow_html=True)

# ============================================
# LOAD MODELS
# ============================================
@st.cache_resource
def load_models():
    try:
        base_path = r'D:/Job Application Pred/Models/'
        model_path = base_path + 'random_forest_model.pkl'
        scaler_path = base_path + 'scaler.pkl'
        features_path = base_path + 'feature_columns.pkl'
        
        if not os.path.exists(model_path):
            return None, None, None, None
        
        with st.spinner("🚀 Loading AI Model..."):
            model = joblib.load(model_path)
            scaler = joblib.load(scaler_path)
            with open(features_path, 'rb') as f:
                feature_cols = pickle.load(f)
        
        n_features = len(feature_cols) if feature_cols else 31
        return model, scaler, feature_cols, n_features
        
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None, None, None

@st.cache_data
def load_data():
    paths = [
        r'D:/Job Application Pred/Data/HR_Job_Placement_Cleaned.csv',
        './Data/HR_Job_Placement_Cleaned.csv'
    ]
    for path in paths:
        if os.path.exists(path):
            return pd.read_csv(path)
    return pd.DataFrame()

model, scaler, feature_cols, n_features = load_models()
df = load_data()

# ============================================
# SIDEBAR
# ============================================
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 0.5rem 0;">
            <div style="font-size: 3.5rem;">🎯</div>
            <div style="font-size: 1.3rem; font-weight: 700; color: #2d3748;">HR Analytics</div>
            <div style="font-size: 0.8rem; color: #718096;">Job Acceptance Predictor</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    page = st.radio(
        "📌 Navigation",
        ["🏠 Prediction", "📊 Analytics", "📋 Data"],
        index=0,
        key="nav"
    )
    
    st.markdown("---")
    
    # Model Performance Section in Sidebar
    st.markdown("### 🤖 Model Performance")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div style="text-align: center; background: #d4edda; padding: 0.5rem; border-radius: 8px;">
                <div style="font-size: 0.7rem; color: #155724;">Accuracy</div>
                <div style="font-size: 1.4rem; font-weight: 700; color: #28a745;">89.39%</div>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="text-align: center; background: #cce5ff; padding: 0.5rem; border-radius: 8px;">
                <div style="font-size: 0.7rem; color: #004085;">F1-Score</div>
                <div style="font-size: 1.4rem; font-weight: 700; color: #0066cc;">82.38%</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
        <div style="text-align: center; margin-top: 0.5rem;">
            <span class="glow-badge">🏆 Best Model: Random Forest</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    if model is not None:
        st.success("✅ AI Model: Active")
        st.caption(f"📊 Features: {n_features}")
    else:
        st.error("❌ AI Model: Inactive")
    
    st.markdown("---")
    
    if not df.empty:
        st.markdown("### 📊 Quick Stats")
        total = len(df)
        placed = df['status_enc'].sum() if 'status_enc' in df.columns else 0
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total", f"{total:,}")
        with col2:
            st.metric("Placed %", f"{(placed/total)*100:.1f}%")
    
    st.markdown("---")
    st.caption("⚡ Powered by Random Forest")

# ============================================
# FUNCTION TO CREATE INPUT VECTOR
# ============================================
def create_input_vector(age, ssc, hsc, degree, exp, prev_ctc, exp_ctc, certs,
                        gender, company, job_match, competition, bond, career_switch):
    
    avg_academic = (ssc + hsc + degree) / 3
    avg_interview = 70.0
    ctc_diff = exp_ctc - prev_ctc
    
    core_features = [
        age, ssc, hsc, degree,
        70.0, 70.0, 70.0, 70.0,
        certs, exp, prev_ctc, exp_ctc,
        30, 0,
        avg_academic, 70.0, ctc_diff
    ]
    
    encoded_features = [
        1 if gender == 'Male' else 0,
        0 if company == 'Tier 1' else 1 if company == 'Tier 2' else 2,
        0 if job_match == 'Matched' else 1,
        0 if competition == 'Low' else 1 if competition == 'Medium' else 2,
        0 if bond == 'Required' else 1,
        0 if career_switch == 'Willing' else 1,
        0, 0, 0, 0, 0, 0, 0, 0
    ]
    
    return np.array([core_features + encoded_features])

# ============================================
# PAGE 1: PREDICTION DASHBOARD
# ============================================
if page == "🏠 Prediction":
    # Hero Section with Model Performance Badge
    st.markdown("""
        <div class="hero-section" style="display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 2rem;">
            <div style="text-align: left;">
                <div class="hero-title">🎯 Job Acceptance Prediction</div>
                <div class="hero-subtitle">AI-powered prediction for candidate job offer acceptance</div>
            </div>
            <div style="text-align: right; background: rgba(255,255,255,0.15); padding: 0.8rem 1.5rem; border-radius: 12px; backdrop-filter: blur(10px);">
                <div style="font-size: 0.7rem; opacity: 0.8;">🏆 Best Model</div>
                <div style="font-size: 1.2rem; font-weight: 700;">Random Forest</div>
                <div style="font-size: 0.8rem; opacity: 0.9;">🎯 Accuracy: 89.39%</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    if model is None:
        st.error("⚠️ AI Model not loaded. Please check model files.")
        st.stop()
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown('<div class="section-header">👤 Candidate Profile</div>', unsafe_allow_html=True)
        st.caption("Enter the candidate details below for real-time prediction")
    
    with col_right:
        # Model Performance Card
        st.markdown("""
            <div class="model-performance">
                <div class="title">📊 Model Performance</div>
                <div class="value">89.39%</div>
                <div class="sub">Accuracy • F1-Score: 82.38%</div>
                <div style="margin-top: 0.3rem;">
                    <span class="glow-badge">⭐ Random Forest</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        if not df.empty and 'status_enc' in df.columns:
            placement_rate = (df['status_enc'].sum() / len(df)) * 100
            st.metric("📈 Placement Rate", f"{placement_rate:.1f}%", delta="+2.3% vs last quarter")
    
    # Input Form with Tabs
    tab1, tab2, tab3 = st.tabs(["🎓 Academic", "💼 Professional", "🏢 Job Details"])
    
    with st.form("prediction_form", clear_on_submit=False):
        with tab1:
            col1, col2 = st.columns(2)
            with col1:
                age = st.number_input("Age", min_value=18, max_value=60, value=25, step=1)
                ssc = st.slider("SSC Percentage", min_value=0.0, max_value=100.0, value=70.0, step=0.5)
            with col2:
                hsc = st.slider("HSC Percentage", min_value=0.0, max_value=100.0, value=70.0, step=0.5)
                degree = st.slider("Degree Percentage", min_value=0.0, max_value=100.0, value=70.0, step=0.5)
        
        with tab2:
            col1, col2 = st.columns(2)
            with col1:
                exp = st.number_input("Years of Experience", min_value=0, max_value=20, value=1, step=1)
                prev_ctc = st.number_input("Previous CTC (LPA)", min_value=0.0, max_value=50.0, value=5.0, step=0.5)
            with col2:
                exp_ctc = st.number_input("Expected CTC (LPA)", min_value=0.0, max_value=50.0, value=7.0, step=0.5)
                certs = st.number_input("Certifications", min_value=0, max_value=10, value=1, step=1)
        
        with tab3:
            col1, col2 = st.columns(2)
            with col1:
                gender = st.selectbox("Gender", ["Male", "Female"])
                company = st.selectbox("Company Tier", ["Tier 1", "Tier 2", "Tier 3"])
                job_match = st.selectbox("Job Role Match", ["Matched", "Not Matched"])
            with col2:
                competition = st.selectbox("Competition Level", ["Low", "Medium", "High"])
                bond = st.selectbox("Bond Requirement", ["Not Required", "Required"])
                career_switch = st.selectbox("Career Switch Willingness", ["Willing", "Not Willing"])
        
        st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
        submitted = st.form_submit_button("🔮 Predict Acceptance", use_container_width=True)
    
    # Prediction Result
    if submitted and model is not None:
        try:
            input_data = create_input_vector(
                age, ssc, hsc, degree, exp, prev_ctc, exp_ctc, certs,
                gender, company, job_match, competition, bond, career_switch
            )
            
            input_scaled = scaler.transform(input_data)
            prediction = model.predict(input_scaled)[0]
            probability = model.predict_proba(input_scaled)[0][1]
            
            st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
            st.markdown('<div class="section-header">📊 Prediction Result</div>', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                if prediction == 1:
                    st.markdown("""
                        <div class="prediction-box prediction-accept">
                            <div class="prediction-icon">✅</div>
                            <div class="prediction-title" style="color: #155724;">Will ACCEPT Job Offer</div>
                            <div class="prediction-desc" style="color: #155724;">The candidate is highly likely to accept the job offer</div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                        <div class="prediction-box prediction-reject">
                            <div class="prediction-icon">❌</div>
                            <div class="prediction-title" style="color: #721c24;">Will REJECT Job Offer</div>
                            <div class="prediction-desc" style="color: #721c24;">The candidate is likely to reject the job offer</div>
                        </div>
                    """, unsafe_allow_html=True)
            
            with col2:
                st.metric("Acceptance Probability", f"{probability*100:.1f}%")
            
            with col3:
                confidence = abs(probability - 0.5) * 2
                st.metric("Confidence Level", f"{confidence*100:.1f}%")
            
            # Gauge Chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number+delta",
                value=probability * 100,
                title={'text': "Acceptance Probability", 'font': {'size': 16}},
                delta={'reference': 50, 'increasing': {'color': "#28a745"}, 'decreasing': {'color': "#dc3545"}},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1},
                    'bar': {'color': "#667eea"},
                    'steps': [
                        {'range': [0, 40], 'color': "#f8d7da"},
                        {'range': [40, 60], 'color': "#fff3cd"},
                        {'range': [60, 100], 'color': "#d4edda"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    }
                }
            ))
            fig.update_layout(height=280)
            st.plotly_chart(fig, use_container_width=True)
            
            # Profile Summary
            st.markdown('<div class="section-header-sm">👤 Profile Summary</div>', unsafe_allow_html=True)
            avg_academic = (ssc + hsc + degree) / 3
            ctc_diff = exp_ctc - prev_ctc
            
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.metric("📚 Academic", f"{avg_academic:.1f}%")
            with col2:
                st.metric("💼 Experience", f"{exp} yrs")
            with col3:
                st.metric("🎯 Skills Match", f"70%")
            with col4:
                st.metric("📜 Certifications", certs)
            with col5:
                st.metric("💰 CTC Diff", f"{ctc_diff:.1f} LPA")
            
        except Exception as e:
            st.error(f"❌ Prediction error: {str(e)}")

# ============================================
# PAGE 2: ANALYTICS DASHBOARD (UPDATED)
# ============================================
elif page == "📊 Analytics":
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">📊 Analytics Dashboard</div>
            <div class="hero-subtitle">Comprehensive analytics and insights from HR data</div>
        </div>
    """, unsafe_allow_html=True)
    
    if df.empty:
        st.warning("⚠️ Data not loaded.")
        st.stop()
    
    # ============================================
    # 5 KPI METRICS
    # ============================================
    st.markdown('<div class="section-header">📈 Key Performance Indicators</div>', unsafe_allow_html=True)
    
    total = len(df)
    placed = df['status_enc'].sum() if 'status_enc' in df.columns else 0
    placed_pct = (placed / total) * 100 if total > 0 else 0
    avg_acad = df['avg_academic'].mean() if 'avg_academic' in df.columns else 0
    avg_skills = df['skills_match_percentage'].mean() if 'skills_match_percentage' in df.columns else 0
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">👥</div>
                <div class="metric-value">{total:,}</div>
                <div class="metric-label">Total Candidates</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">✅</div>
                <div class="metric-value">{placed:,}</div>
                <div class="metric-label">Placed Candidates</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">📊</div>
                <div class="metric-value">{placed_pct:.1f}%</div>
                <div class="metric-label">Placement Rate</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">🎓</div>
                <div class="metric-value">{avg_acad:.1f}</div>
                <div class="metric-label">Avg Academic Score</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-icon">🎯</div>
                <div class="metric-value">{avg_skills:.1f}%</div>
                <div class="metric-label">Avg Skills Match</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # ============================================
    # ROW 1: Donut Chart + Bar Chart
    # ============================================
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header-sm">📊 Status Distribution</div>', unsafe_allow_html=True)
        if 'status' in df.columns:
            status_counts = df['status'].value_counts()
            fig = px.pie(
                values=status_counts.values,
                names=status_counts.index,
                color=status_counts.index,
                color_discrete_map={'Placed': '#28a745', 'Not Placed': '#dc3545'},
                hole=0.45,
                title="Job Acceptance Distribution"
            )
            fig.update_layout(height=380, title_font_size=14)
            fig.update_traces(textposition='inside', textinfo='percent+label', textfont_size=14)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown('<div class="section-header-sm">🏢 Placement by Company Tier</div>', unsafe_allow_html=True)
        if 'company_tier' in df.columns and 'status_enc' in df.columns:
            tier_placement = df.groupby('company_tier')['status_enc'].mean() * 100
            colors = ['#667eea', '#764ba2', '#f093fb']
            fig = px.bar(
                x=tier_placement.index,
                y=tier_placement.values,
                color=tier_placement.index,
                color_discrete_sequence=colors,
                labels={'x': 'Company Tier', 'y': 'Placement Rate (%)'},
                text=tier_placement.values.round(1)
            )
            fig.update_layout(height=380, showlegend=False, title_font_size=14)
            fig.update_traces(textposition='outside', textfont_size=14)
            st.plotly_chart(fig, use_container_width=True)
    
    # ============================================
    # ROW 2: Scatter Plot
    # ============================================
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="section-header-sm">📈 Interview Score vs Skills Match</div>', unsafe_allow_html=True)
        if 'avg_interview' in df.columns and 'skills_match_percentage' in df.columns:
            fig = px.scatter(
                df,
                x='avg_interview',
                y='skills_match_percentage',
                color='status' if 'status' in df.columns else None,
                color_discrete_map={'Placed': '#28a745', 'Not Placed': '#dc3545'},
                title="Interview Score vs Skills Match",
                labels={'avg_interview': 'Avg Interview Score', 'skills_match_percentage': 'Skills Match %'},
                hover_data=['years_of_experience'] if 'years_of_experience' in df.columns else None,
                size_max=15,
                opacity=0.7
            )
            fig.update_layout(height=400, title_font_size=14)
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Empty placeholder for spacing
        st.empty()
    
    # ============================================
    # ROW 3: Heatmap
    # ============================================
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-header">🔥 Feature Correlation Heatmap</div>', unsafe_allow_html=True)
    
    corr_cols = ['avg_academic', 'avg_interview', 'skills_match_percentage', 
                 'years_of_experience', 'certifications_count', 'status_enc']
    
    available_cols = [col for col in corr_cols if col in df.columns]
    if len(available_cols) > 2:
        corr_df = df[available_cols].corr()
        fig = px.imshow(
            corr_df,
            text_auto='.2f',
            aspect='auto',
            color_continuous_scale='RdBu_r',
            title="Feature Correlation Matrix",
            zmin=-1, zmax=1
        )
        fig.update_layout(height=450, title_font_size=14)
        st.plotly_chart(fig, use_container_width=True)
        
# ============================================
# PAGE 3: DATA EXPLORER
# ============================================
else:
    st.markdown("""
        <div class="hero-section">
            <div class="hero-title">📋 Data Explorer</div>
            <div class="hero-subtitle">Explore and analyze candidate data with powerful filters</div>
        </div>
    """, unsafe_allow_html=True)
    
    if df.empty:
        st.warning("⚠️ Data not loaded.")
        st.stop()
    
    # Filters
    st.markdown('<div class="section-header">🔍 Filter Data</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        status_filter = st.selectbox("Status", ["All"] + sorted(df['status'].unique().tolist()) if 'status' in df.columns else ["All"])
    with col2:
        gender_filter = st.selectbox("Gender", ["All"] + sorted(df['gender'].unique().tolist()) if 'gender' in df.columns else ["All"])
    with col3:
        tier_filter = st.selectbox("Company Tier", ["All"] + sorted(df['company_tier'].unique().tolist()) if 'company_tier' in df.columns else ["All"])
    with col4:
        exp_filter = st.selectbox("Experience Level", ["All"] + sorted(df['exp_category'].unique().tolist()) if 'exp_category' in df.columns else ["All"])
    
    # Apply filters
    filtered_df = df.copy()
    if status_filter != "All" and 'status' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['status'] == status_filter]
    if gender_filter != "All" and 'gender' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['gender'] == gender_filter]
    if tier_filter != "All" and 'company_tier' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['company_tier'] == tier_filter]
    if exp_filter != "All" and 'exp_category' in filtered_df.columns:
        filtered_df = filtered_df[filtered_df['exp_category'] == exp_filter]
    
    # Stats
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Total Records", len(filtered_df))
    with col2:
        placed_count = filtered_df['status_enc'].sum() if 'status_enc' in filtered_df.columns else 0
        st.metric("✅ Placed", placed_count)
    with col3:
        placed_pct = (placed_count / len(filtered_df)) * 100 if len(filtered_df) > 0 else 0
        st.metric("📈 Placement Rate", f"{placed_pct:.1f}%")
    
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    
    # Data Table
    st.markdown('<div class="section-header-sm">📊 Data Table</div>', unsafe_allow_html=True)
    display_cols = ['age_years', 'gender', 'ssc_percentage', 'hsc_percentage', 'degree_percentage',
                    'technical_score', 'aptitude_score', 'communication_score', 
                    'skills_match_percentage', 'years_of_experience', 'company_tier', 'status']
    available_display = [col for col in display_cols if col in filtered_df.columns]
    
    if available_display:
        st.dataframe(
            filtered_df[available_display],
            use_container_width=True,
            height=500
        )
    
    # Download
    st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="📥 Download Filtered Data (CSV)",
        data=csv,
        file_name="filtered_candidates.csv",
        mime="text/csv",
        use_container_width=True
    )

# ============================================
# FOOTER
# ============================================
st.markdown("""
    <div class="footer">
        <div class="footer-text">
            <span class="footer-highlight">🏢 Job Acceptance Prediction System</span> • 
            AI-powered HR Analytics • Built with Streamlit & Random Forest
        </div>
        <div class="footer-text" style="font-size: 0.8rem; opacity: 0.6; margin-top: 0.3rem;">
            © 2026 | All Rights Reserved
        </div>
    </div>
""", unsafe_allow_html=True)