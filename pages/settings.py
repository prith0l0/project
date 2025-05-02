import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Settings - SafeHer",
    page_icon="⚙️",
    layout="wide"
)

# Custom CSS (same as app.py)
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
        }
        
        /* Settings page specific */
        .settings-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        .settings-section {
            margin-bottom: 1.5rem;
        }
        
        .switch-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 1rem;
        }
        
        .switch-label {
            display: flex;
            flex-direction: column;
        }
        
        .switch-description {
            font-size: 0.875rem;
            color: var(--neutral);
        }
    </style>
    """, unsafe_allow_html=True)

local_css()

# Sidebar - Navigation from app.py is not duplicated here for brevity
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield-with-cross.png", width=80)
    st.title("SafeHer")
    st.caption("Your personal safety companion")
    st.markdown("---")
    
    # Settings categories
    st.subheader("Categories")
    
    settings_categories = [
        "Account",
        "Privacy",
        "Notifications",
        "Emergency Settings",
        "App Preferences",
        "Help & Support"
    ]
    
    for category in settings_categories:
        st.button(category, use_container_width=True)
    
    st.markdown("---")
    if st.button("Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Main content
st.title("Settings")
st.markdown("Customize your SafeHer application preferences")

# Account settings
st.header("Account Settings")

with st.expander("Profile Information", expanded=True):
    col_prof1, col_prof2 = st.columns(2)
    
    with col_prof1:
        st.text_input("Full Name", value="Jane Doe")
        st.text_input("Email Address", value="jane.doe@example.com")
        st.text_input("Phone Number", value="+1 (555) 123-4567")
    
    with col_prof2:
        st.date_input("Date of Birth")
        st.selectbox("Country", ["United States", "Canada", "United Kingdom", "Australia", "Other"])
        st.text_input("City", value="San Francisco")
    
    profile_save = st.button("Save Profile Changes")
    if profile_save:
        st.success("Profile information updated successfully!")

with st.expander("Security", expanded=False):
    st.text_input("Current Password", type="password")
    st.text_input("New Password", type="password")
    st.text_input("Confirm New Password", type="password")
    
    password_button = st.button("Change Password")
    
    st.markdown("---")
    
    st.subheader("Two-Factor Authentication")
    st.checkbox("Enable Two-Factor Authentication", value=True)
    
    if st.button("Set Up Two-Factor Authentication"):
        st.info("Please check your email for instructions on setting up two-factor authentication.")

# Privacy settings
st.header("Privacy Settings")

with st.expander("Location Sharing", expanded=True):
    st.markdown("""
    <div class="settings-section">
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Location Sharing</strong></span>
                <span class="switch-description">Allow the app to access your location to provide safety features</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Background Location</strong></span>
                <span class="switch-description">Allow the app to track your location even when the app is closed</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Location History</strong></span>
                <span class="switch-description">Store your location history for safety purposes</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.select_slider(
        "Location Accuracy",
        options=["Low", "Medium", "High", "Precise"],
        value="High"
    )
    
    st.markdown("<p class='switch-description'>Higher accuracy provides better safety features but uses more battery</p>", unsafe_allow_html=True)
    
    st.button("Clear Location History")

with st.expander("Data Privacy", expanded=False):
    st.markdown("""
    <div class="settings-section">
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Incident Reporting Privacy</strong></span>
                <span class="switch-description">Share your reported incidents anonymously with the community</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Route History</strong></span>
                <span class="switch-description">Store history of routes you've taken</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Analytics</strong></span>
                <span class="switch-description">Share anonymous usage data to help improve the app</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.select_slider(
        "Data Retention Period",
        options=["1 Week", "1 Month", "3 Months", "6 Months", "1 Year"],
        value="3 Months"
    )
    
    col_privacy1, col_privacy2 = st.columns(2)
    
    with col_privacy1:
        st.button("Download My Data")
    
    with col_privacy2:
        st.button("Delete My Data", type="primary")

# Notification settings
st.header("Notification Settings")

with st.expander("Alert Notifications", expanded=True):
    st.markdown("""
    <div class="settings-section">
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Emergency Alerts</strong></span>
                <span class="switch-description">Receive alerts about emergencies in your area</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Incident Reports</strong></span>
                <span class="switch-description">Receive notifications about safety incidents near you</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Safety Tips</strong></span>
                <span class="switch-description">Receive periodic safety tips and reminders</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Community Alerts</strong></span>
                <span class="switch-description">Receive updates from community safety initiatives</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.slider("Notification Radius", min_value=0.5, max_value=10.0, value=2.0, step=0.5, help="Distance in miles for location-based notifications")
    
    st.selectbox("Quiet Hours", ["None", "10 PM - 7 AM", "11 PM - 6 AM", "12 AM - 5 AM", "Custom"])

with st.expander("Contact Notifications", expanded=False):
    st.markdown("""
    <div class="settings-section">
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Safety Check Reminders</strong></span>
                <span class="switch-description">Receive reminders to check in with your safety contacts</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Contact Updates</strong></span>
                <span class="switch-description">Notify me when my emergency contacts change their information</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Emergency settings
st.header("Emergency Settings")

with st.expander("Emergency Response", expanded=True):
    st.subheader("SOS Trigger Settings")
    
    st.markdown("""
    <p class="switch-description">Configure how the SOS emergency feature is triggered</p>
    """, unsafe_allow_html=True)
    
    col_sos1, col_sos2 = st.columns(2)
    
    with col_sos1:
        st.selectbox("SOS Button Press Type", ["Long Press (3 seconds)", "Triple Press", "Double Press", "Single Press"])
    
    with col_sos2:
        st.selectbox("Secondary Trigger Method", ["Power Button 5x", "Volume Buttons Pattern", "Shake Device", "None"])
    
    st.checkbox("Require confirmation before sending alerts", value=True)
    
    st.markdown("---")
    
    st.subheader("SOS Response Actions")
    
    st.markdown("""
    <div class="settings-section">
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Alert Emergency Contacts</strong></span>
                <span class="switch-description">Send alerts to your emergency contacts</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Contact Emergency Services</strong></span>
                <span class="switch-description">Automatically call emergency services (911)</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Record Audio</strong></span>
                <span class="switch-description">Start audio recording when SOS is triggered</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Record Video</strong></span>
                <span class="switch-description">Start video recording when SOS is triggered</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Siren Sound</strong></span>
                <span class="switch-description">Play a loud alarm sound</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with st.expander("Safety Check-ins", expanded=False):
    st.subheader("Scheduled Check-ins")
    
    st.markdown("""
    <p class="switch-description">Set up regular safety check-ins. If you don't respond to a scheduled check-in, alerts will be sent to your emergency contacts.</p>
    """, unsafe_allow_html=True)
    
    st.checkbox("Enable Scheduled Check-ins", value=False)
    
    check_in_frequency = st.selectbox(
        "Check-in Frequency",
        ["Daily", "Every 12 hours", "Every 6 hours", "Custom"]
    )
    
    if check_in_frequency == "Custom":
        st.number_input("Hours between check-ins", min_value=1, max_value=72, value=24)
    
    st.time_input("First check-in time")
    
    st.markdown("---")
    
    st.subheader("Journey Monitoring")
    
    st.markdown("""
    <p class="switch-description">The app will monitor your journey and request check-ins. If you don't respond, alerts will be sent.</p>
    """, unsafe_allow_html=True)
    
    st.checkbox("Enable Journey Monitoring", value=True)
    
    st.selectbox(
        "Check-in Method",
        ["PIN Entry", "Fingerprint/Face ID", "Button Press"]
    )
    
    st.slider("Grace Period (minutes)", min_value=1, max_value=30, value=5, help="Time allowed to respond to a check-in request before alerts are sent")

# App preferences
st.header("App Preferences")

with st.expander("Display Settings", expanded=True):
    st.selectbox("Theme", ["System Default", "Light Mode", "Dark Mode", "High Contrast"])
    
    st.selectbox("Color Scheme", ["Purple (Default)", "Blue", "Green", "Pink", "Orange"])
    
    st.slider("Text Size", min_value=1, max_value=5, value=3, help="1 is smallest, 5 is largest")
    
    st.checkbox("Enable Animations", value=True)
    
    st.markdown("---")
    
    st.subheader("Map Settings")
    
    st.selectbox("Default Map Type", ["Standard", "Satellite", "Hybrid", "Transit"])
    
    st.checkbox("Show Safety Ratings on Map", value=True)
    
    st.checkbox("Show Incident Reports on Map", value=True)
    
    st.slider("Map Detail Level", min_value=1, max_value=5, value=3, help="Higher values show more details but may be slower")

with st.expander("Route Settings", expanded=False):
    st.markdown("""
    <div class="settings-section">
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Default to Safest Routes</strong></span>
                <span class="switch-description">Prioritize safety over speed for route suggestions</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Avoid Low-Lit Areas</strong></span>
                <span class="switch-description">Avoid poorly lit areas when possible, especially at night</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Avoid Isolated Areas</strong></span>
                <span class="switch-description">Prefer routes through populated areas</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
        
        <div class="switch-container">
            <div class="switch-label">
                <span><strong>Avoid Areas with Recent Incidents</strong></span>
                <span class="switch-description">Reroute around areas with reported safety incidents</span>
            </div>
            <div>
                <input type="checkbox" checked>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.slider("Maximum Safety Detour", min_value=0, max_value=30, value=10, help="Maximum additional minutes for a safer route")
    
    st.selectbox("Preferred Transportation", ["Walking", "Public Transit", "Rideshare", "Driving"])

# Help and support
st.header("Help & Support")

col_help1, col_help2 = st.columns(2)

with col_help1:
    st.markdown("""
    <div class="settings-card">
        <h3 style="margin-top: 0;">Frequently Asked Questions</h3>
        <p>Find answers to common questions about using the SafeHer app.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
            View FAQs
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="settings-card">
        <h3 style="margin-top: 0;">Contact Support</h3>
        <p>Get help from our support team with any issues or questions.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
            Contact Support
        </button>
    </div>
    """, unsafe_allow_html=True)

with col_help2:
    st.markdown("""
    <div class="settings-card">
        <h3 style="margin-top: 0;">Tutorials & Guides</h3>
        <p>Learn how to use all features of the SafeHer app effectively.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
            View Tutorials
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="settings-card">
        <h3 style="margin-top: 0;">Report a Problem</h3>
        <p>Report bugs, issues, or suggestions to help improve the app.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
            Report Problem
        </button>
    </div>
    """, unsafe_allow_html=True)

# App information
st.markdown("""
<div class="settings-card">
    <h3 style="margin-top: 0;">About SafeHer</h3>
    
    <p><strong>Version:</strong> 1.0.0</p>
    <p><strong>Last Updated:</strong> April 15, 2025</p>
    
    <div style="margin: 1rem 0;">
        <a href="#" style="color: var(--primary); text-decoration: none; margin-right: 1rem;">Privacy Policy</a>
        <a href="#" style="color: var(--primary); text-decoration: none; margin-right: 1rem;">Terms of Service</a>
        <a href="#" style="color: var(--primary); text-decoration: none;">Licenses</a>
    </div>
    
    <button style="background-color: var(--neutral); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
        Log Out
    </button>
</div>
""", unsafe_allow_html=True)