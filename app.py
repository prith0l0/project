import streamlit as st
from PIL import Image
import base64
from streamlit_extras.switch_page_button import switch_page

# Page configuration
st.set_page_config(
    page_title="SafeHer - Women Safety App",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
def local_css():
    st.markdown("""
    <style>
        /* Main colors */
        :root {
            --primary: #7C3AED;
            --primary-light: #A78BFA;
            --secondary: #FDA4AF;
            --warning: #F59E0B;
            --danger: #EF4444;
            --success: #10B981;
            --neutral: #6B7280;
            --background: #F3F4F6;
            --white: #FFFFFF;
        }
        
        /* Base styling */
        .main {
            background-color: var(--background);
            padding: 1rem;
        }
        
        h1, h2, h3 {
            color: var(--primary);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        /* Custom components */
        .emergency-button {
            background-color: var(--danger);
            color: white;
            padding: 1.5rem;
            border-radius: 50%;
            font-size: 1.2rem;
            font-weight: bold;
            text-align: center;
            margin: 1rem auto;
            width: 150px;
            height: 150px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .emergency-button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }
        
        .card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .feature-icon {
            font-size: 2rem;
            color: var(--primary);
            margin-bottom: 0.5rem;
        }
        
        /* Sidebar styling */
        .sidebar .sidebar-content {
            background-color: var(--primary);
        }
        
        /* Button styling */
        .stButton>button {
            background-color: var(--primary);
            color: white;
            border: none;
            border-radius: 0.25rem;
            padding: 0.5rem 1rem;
            font-weight: bold;
        }
        
        .stButton>button:hover {
            background-color: var(--primary-light);
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield-with-cross.png", width=80)
    st.title("SafeHer")
    st.caption("Your personal safety companion")
    
    st.markdown("---")
    
    # Navigation
    st.subheader("Navigation")
    if st.button("🏠 Home", use_container_width=True):
        switch_page("app")
    if st.button("🆘 Emergency", use_container_width=True):
        switch_page("emergency")
    if st.button("🗺️ Safe Routes", use_container_width=True):
        switch_page("routes")
    if st.button("📞 Contacts", use_container_width=True):
        switch_page("contacts")
    if st.button("📊 Report Incident", use_container_width=True):
        switch_page("report")
    if st.button("📚 Resources", use_container_width=True):
        switch_page("resources")
    if st.button("⚙️ Settings", use_container_width=True):
        switch_page("settings")
        
    st.markdown("---")
    st.caption("© 2025 SafeHer App")
    st.caption("For Hackathon Demo Purposes")

# Main content
st.title("Welcome to SafeHer")
st.subheader("Your personal safety companion")

# Emergency button
st.markdown("""
<div class="emergency-button" onclick="alert('Emergency feature activated!')">
    SOS EMERGENCY
</div>
<p style="text-align: center; color: #6B7280;">Press in case of emergency</p>
""", unsafe_allow_html=True)

# Main features in columns
st.markdown("## Key Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="feature-icon">🆘</div>
        <h3>Emergency Alert</h3>
        <p>One-tap SOS alert that shares your location with emergency contacts and nearby authorities.</p>
        <br/>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="feature-icon">📞</div>
        <h3>Fake Call</h3>
        <p>Simulate an incoming call to help you exit uncomfortable situations safely.</p>
        <br/>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="feature-icon">🗺️</div>
        <h3>Safe Routes</h3>
        <p>Get navigation suggestions for safer routes based on community safety ratings and time of day.</p>
        <br/>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="feature-icon">👥</div>
        <h3>Trusted Contacts</h3>
        <p>Set up emergency contacts who will be notified with your location in case of distress.</p>
        <br/>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="feature-icon">📊</div>
        <h3>Incident Reporting</h3>
        <p>Report and view safety incidents in your area to stay informed about potential dangers.</p>
        <br/>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card">
        <div class="feature-icon">📚</div>
        <h3>Safety Resources</h3>
        <p>Access a directory of local safety resources including shelters, police stations, and hospitals.</p>
        <br/>
    </div>
    """, unsafe_allow_html=True)

# Statistics
st.markdown("## Safety Statistics")
stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)

with stats_col1:
    st.metric(label="Active Users", value="10,342", delta="↑ 15%")

with stats_col2:
    st.metric(label="Safe Routes Mapped", value="5,280", delta="↑ 8%")

with stats_col3:
    st.metric(label="Emergency Alerts", value="132", delta="-5%", delta_color="inverse")

with stats_col4:
    st.metric(label="Community Safety Score", value="93%", delta="↑ 3%")

# Testimonials
st.markdown("## User Testimonials")
testimonial_col1, testimonial_col2 = st.columns(2)

with testimonial_col1:
    st.markdown("""
    <div class="card" style="padding: 1.5rem;">
        <p style="font-style: italic;">"This app helped me navigate safely when I was traveling alone in a new city. The safe routes feature is incredibly useful!"</p>
        <p style="text-align: right; color: var(--primary); font-weight: bold;">- Sarah K.</p>
    </div>
    """, unsafe_allow_html=True)

with testimonial_col2:
    st.markdown("""
    <div class="card" style="padding: 1.5rem;">
        <p style="font-style: italic;">"The emergency alert feature gave me peace of mind when walking home late after work. Knowing help is just a button away makes all the difference."</p>
        <p style="text-align: right; color: var(--primary); font-weight: bold;">- Michelle T.</p>
    </div>
    """, unsafe_allow_html=True)

# Safety Tip of the Day
st.markdown("## Safety Tip of the Day")
st.markdown("""
<div class="card" style="background-color: #EDE9FE; border-left: 4px solid var(--primary); padding: 1.5rem;">
    <h3 style="margin-top: 0;">Trust Your Instincts</h3>
    <p>If a situation or person makes you feel uncomfortable, trust your gut feeling. Don't worry about being polite - your safety comes first. Create distance between yourself and the person or situation that is causing concern.</p>
</div>
""", unsafe_allow_html=True)

# App usage guide
with st.expander("How to Use SafeHer"):
    st.markdown("""
    ### Getting Started
    
    1. **Set Up Emergency Contacts**: Navigate to the Contacts page to add trusted people who will be notified in case of emergency.
    
    2. **Configure Your Profile**: Complete your profile with relevant health information that might be useful in emergencies.
    
    3. **Explore Safe Routes**: Before traveling to a new area, check the Safe Routes page to identify safer paths.
    
    4. **Learn Safety Tips**: Visit the Resources section to learn about personal safety strategies and self-defense techniques.
    
    ### In Case of Emergency
    
    - **SOS Button**: Press the large SOS button on the home screen to send alerts to your emergency contacts with your current location.
    
    - **Fake Call**: Use the fake call feature to simulate an incoming call and provide an excuse to leave uncomfortable situations.
    
    - **Report Incidents**: Help the community by reporting safety incidents you witness or experience.
    """)