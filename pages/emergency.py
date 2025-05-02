import streamlit as st
import time
import pandas as pd
import folium
from streamlit_folium import folium_static
import random

# Page configuration
st.set_page_config(
    page_title="Emergency - SafeHer",
    page_icon="🆘",
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
        
        /* Emergency page specific */
        .emergency-actions {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        
        .emergency-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            border-left: 4px solid var(--danger);
        }
        
        .emergency-button {
            background-color: var(--danger);
            color: white;
            padding: 1.5rem;
            border-radius: 50%;
            font-size: 1.2rem;
            font-weight: bold;
            text-align: center;
            margin: 1rem auto;
            width: 200px;
            height: 200px;
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
        
        .option-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            cursor: pointer;
            transition: transform 0.2s ease;
        }
        
        .option-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
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
        
        .danger-button>button {
            background-color: var(--danger);
        }
        
        .danger-button>button:hover {
            background-color: #F87171;
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
    
    # Show emergency contacts
    st.subheader("Emergency Contacts")
    
    # Sample emergency contacts (in a real app, this would be fetched from a database)
    emergency_contacts = [
        {"name": "Mom", "phone": "+1 (555) 123-4567"},
        {"name": "Dad", "phone": "+1 (555) 765-4321"},
        {"name": "Local Police", "phone": "911"}
    ]
    
    for contact in emergency_contacts:
        st.markdown(f"**{contact['name']}**: {contact['phone']}")
    
    st.markdown("---")
    if st.button("Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Main content
st.title("Emergency Help")
st.markdown("Use this page to quickly get help in emergency situations.")

# Emergency type selection
emergency_type = st.radio(
    "What kind of emergency are you experiencing?",
    ["I feel unsafe", "I'm being followed", "Medical emergency", "Other emergency"]
)

# Location display
st.subheader("Your Current Location")

# Generate a random location near a city center for demo purposes
# In a real app, this would use the device's GPS coordinates
def get_current_location():
    # Sample coordinates (would be from GPS in a real app)
    return {"lat": 37.7749 + random.uniform(-0.01, 0.01), 
            "lon": -122.4194 + random.uniform(-0.01, 0.01)}

user_location = get_current_location()

# Create map
m = folium.Map(location=[user_location["lat"], user_location["lon"]], zoom_start=15)
folium.Marker(
    [user_location["lat"], user_location["lon"]], 
    popup="Your Location",
    icon=folium.Icon(color="red", icon="info-sign")
).add_to(m)

# Add simulated nearby help locations
help_locations = [
    {"name": "Police Station", "lat": user_location["lat"] + 0.007, "lon": user_location["lon"] - 0.005, "type": "police"},
    {"name": "Hospital", "lat": user_location["lat"] - 0.005, "lon": user_location["lon"] + 0.008, "type": "hospital"},
    {"name": "Women's Shelter", "lat": user_location["lat"] + 0.003, "lon": user_location["lon"] + 0.006, "type": "shelter"}
]

for location in help_locations:
    color = "blue" if location["type"] == "police" else "green" if location["type"] == "hospital" else "purple"
    icon = "info-sign" if location["type"] == "police" else "plus" if location["type"] == "hospital" else "home"
    
    folium.Marker(
        [location["lat"], location["lon"]], 
        popup=location["name"],
        icon=folium.Icon(color=color, icon=icon)
    ).add_to(m)

# Display map
folium_static(m, width=800, height=400)

# Address information
st.text_input("Confirm your address", "123 Main Street, San Francisco, CA 94105")

# Emergency action buttons
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="emergency-button" onclick="alert('SOS Alert Activated!')">
        SEND SOS ALERT
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='text-align: center;'>Alerts will be sent to all your emergency contacts</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3>Emergency Options</h3>", unsafe_allow_html=True)
    
    # Emergency options
    st.markdown("""
    <div class="option-card" onclick="alert('Calling 911...')">
        <h4 style="color: #EF4444;">🚨 Call 911</h4>
        <p>Directly call emergency services</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="option-card" onclick="alert('Texting trusted contacts...')">
        <h4 style="color: #7C3AED;">💬 Text Trusted Contacts</h4>
        <p>Send your location to trusted contacts</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="option-card" onclick="alert('Recording started...')">
        <h4 style="color: #10B981;">🎥 Record Surroundings</h4>
        <p>Start audio/video recording for evidence</p>
    </div>
    """, unsafe_allow_html=True)

# Safety instructions based on emergency type
st.subheader("Safety Instructions")

if emergency_type == "I feel unsafe":
    st.markdown("""
    <div class="emergency-card">
        <h4>If You Feel Unsafe:</h4>
        <ul>
            <li>Move to a well-lit, public area with other people if possible</li>
            <li>Call a trusted friend or family member and stay on the phone</li>
            <li>Enter a store, restaurant, or other business if one is nearby</li>
            <li>Be prepared to use your SOS alert if the situation escalates</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
elif emergency_type == "I'm being followed":
    st.markdown("""
    <div class="emergency-card">
        <h4>If You're Being Followed:</h4>
        <ul>
            <li>Change direction to confirm if someone is following you</li>
            <li>Do not go home - go to a public place like a store or police station</li>
            <li>Call someone you trust and tell them where you are</li>
            <li>Be loud and draw attention if approached</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
elif emergency_type == "Medical emergency":
    st.markdown("""
    <div class="emergency-card">
        <h4>For Medical Emergencies:</h4>
        <ul>
            <li>Call 911 immediately</li>
            <li>Stay on the line with emergency services</li>
            <li>If possible, send someone to the street to guide paramedics</li>
            <li>The app has sent your medical information to emergency services</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div class="emergency-card">
        <h4>General Emergency Guidelines:</h4>
        <ul>
            <li>Assess if you need immediate police, fire, or medical assistance</li>
            <li>Call 911 if the situation is life-threatening</li>
            <li>Stay calm and provide clear information about your emergency</li>
            <li>Follow instructions from emergency personnel</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Simulated emergency response
st.subheader("Emergency Response Status")

status_container = st.empty()

if st.button("Simulate Emergency Response", type="primary"):
    # Simulate emergency response timeline
    with status_container:
        status_placeholder = st.empty()
        progress_bar = st.progress(0)
        
        status_updates = [
            "Emergency alert activated...",
            "Sending your location to emergency contacts...",
            "Contacts notified successfully...",
            "Identifying nearest emergency services...",
            "Police station at 0.5 miles away notified...",
            "Response team dispatched to your location...",
            "Estimated arrival time: 4 minutes..."
        ]
        
        for i, update in enumerate(status_updates):
            status_placeholder.info(update)
            progress_value = (i + 1) / len(status_updates)
            progress_bar.progress(progress_value)
            time.sleep(1)  # Simulating time delay
        
        st.success("Emergency response initiated! Help is on the way. Stay on this page for updates.")