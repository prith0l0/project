import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import random
import plotly.express as px
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Safe Routes - SafeHer",
    page_icon="🗺️",
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
        
        /* Route specific styling */
        .route-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }
        
        .route-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .safety-high {
            border-left: 4px solid var(--success);
        }
        
        .safety-medium {
            border-left: 4px solid var(--warning);
        }
        
        .safety-low {
            border-left: 4px solid var(--danger);
        }
        
        .safety-indicator {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: bold;
            color: white;
        }
        
        .safety-high-bg {
            background-color: var(--success);
        }
        
        .safety-medium-bg {
            background-color: var(--warning);
        }
        
        .safety-low-bg {
            background-color: var(--danger);
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
    
    # Route filters
    st.subheader("Route Preferences")
    
    transport_mode = st.selectbox(
        "Transportation Mode",
        ["Walking", "Public Transit", "Rideshare", "Driving"]
    )
    
    safety_priority = st.slider(
        "Safety Priority",
        min_value=1,
        max_value=5,
        value=4,
        help="Higher values prioritize safety over speed"
    )
    
    avoid_options = st.multiselect(
        "Areas to Avoid",
        ["Low-lit streets", "Areas with reported incidents", "Isolated paths", "Construction zones"],
        default=["Low-lit streets", "Areas with reported incidents"]
    )
    
    time_options = st.radio(
        "Time of Travel",
        ["Now", "Schedule for Later"]
    )
    
    if time_options == "Schedule for Later":
        scheduled_date = st.date_input("Date", datetime.now())
        scheduled_time = st.time_input("Time", datetime.now().time())
    
    st.markdown("---")
    if st.button("Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Main content
st.title("Safe Routes")
st.markdown("Plan your journey with the safest possible routes")

# Route planning
col1, col2 = st.columns([2, 1])

with col1:
    # Origin and destination inputs
    origin = st.text_input("Starting Point", "Current Location")
    destination = st.text_input("Destination", "")
    
    if st.button("Find Safe Routes", type="primary"):
        if not destination:
            st.error("Please enter a destination")
        else:
            # This would connect to a real routing API in an actual app
            # For demo purposes, we'll generate simulated routes
            
            # Sample coordinates for San Francisco
            start_lat, start_lon = 37.7749, -122.4194
            
            # Slightly offset end point for demo
            end_lat = start_lat + random.uniform(0.01, 0.03)
            end_lon = start_lon + random.uniform(0.01, 0.03)
            
            # Create map
            m = folium.Map(location=[(start_lat + end_lat) / 2, (start_lon + end_lon) / 2], zoom_start=13)
            
            # Add markers for start and end
            folium.Marker([start_lat, start_lon], popup="Start", icon=folium.Icon(color="green", icon="play")).add_to(m)
            folium.Marker([end_lat, end_lon], popup="Destination", icon=folium.Icon(color="red", icon="flag")).add_to(m)
            
            # Generate 3 alternative routes with different safety profiles
            routes = [
                {
                    "name": "Safest Route",
                    "safety_score": 95,
                    "duration": "18 mins",
                    "distance": "1.2 miles",
                    "color": "#10B981",  # Green
                    "waypoints": [
                        [start_lat, start_lon],
                        [start_lat + 0.005, start_lon + 0.005],
                        [start_lat + 0.01, start_lon + 0.01],
                        [start_lat + 0.015, start_lon + 0.015],
                        [end_lat, end_lon]
                    ]
                },
                {
                    "name": "Balanced Route",
                    "safety_score": 80,
                    "duration": "15 mins",
                    "distance": "1.0 miles",
                    "color": "#F59E0B",  # Amber
                    "waypoints": [
                        [start_lat, start_lon],
                        [start_lat + 0.008, start_lon + 0.003],
                        [start_lat + 0.012, start_lon + 0.008],
                        [end_lat, end_lon]
                    ]
                },
                {
                    "name": "Fastest Route",
                    "safety_score": 65,
                    "duration": "12 mins",
                    "distance": "0.8 miles",
                    "color": "#EF4444",  # Red
                    "waypoints": [
                        [start_lat, start_lon],
                        [start_lat + 0.015, start_lon + 0.005],
                        [end_lat, end_lon]
                    ]
                }
            ]
            
            # Add polylines for each route
            for route in routes:
                folium.PolyLine(
                    route["waypoints"],
                    color=route["color"],
                    weight=5,
                    opacity=0.7,
                    popup=f"{route['name']} - {route['duration']}"
                ).add_to(m)
            
            # Add simulated incident reports on the map
            incidents = [
                {"lat": start_lat + 0.012, "lon": start_lon + 0.003, "type": "harassment", "time": "2 days ago"},
                {"lat": start_lat + 0.008, "lon": start_lon + 0.007, "type": "theft", "time": "1 week ago"},
                {"lat": start_lat + 0.018, "lon": start_lon + 0.002, "type": "suspicious activity", "time": "3 days ago"}
            ]
            
            for incident in incidents:
                folium.CircleMarker(
                    location=[incident["lat"], incident["lon"]],
                    radius=5,
                    color="#EF4444",
                    fill=True,
                    fill_color="#EF4444",
                    popup=f"{incident['type']} reported {incident['time']}"
                ).add_to(m)
            
            # Display map
            folium_static(m, width=800, height=500)
            
            # Display route options
            st.subheader("Available Routes")
            
            for route in routes:
                safety_class = "safety-high" if route["safety_score"] >= 90 else "safety-medium" if route["safety_score"] >= 70 else "safety-low"
                safety_bg_class = "safety-high-bg" if route["safety_score"] >= 90 else "safety-medium-bg" if route["safety_score"] >= 70 else "safety-low-bg"
                
                st.markdown(f"""
                <div class="route-card {safety_class}">
                    <h3>{route["name"]}</h3>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span><strong>Duration:</strong> {route["duration"]}</span>
                        <span><strong>Distance:</strong> {route["distance"]}</span>
                        <span class="safety-indicator {safety_bg_class}">Safety: {route["safety_score"]}%</span>
                    </div>
                    <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
                        Select This Route
                    </button>
                </div>
                """, unsafe_allow_html=True)

with col2:
    st.subheader("Safety Information")
    
    # Time-based safety chart
    st.markdown("### Safety by Time of Day")
    
    # Create sample data for safety scores by hour
    hours = list(range(24))
    safety_scores = [
        95, 94, 92, 90, 85, 82, 78, 80,  # 12am-8am
        85, 88, 90, 92, 93, 94, 95, 95,  # 8am-4pm
        94, 93, 90, 88, 85, 82, 80, 78   # 4pm-12am
    ]
    
    time_safety_df = pd.DataFrame({
        "Hour": [f"{h:02d}:00" for h in hours],
        "Safety Score": safety_scores
    })
    
    fig = px.line(
        time_safety_df, 
        x="Hour", 
        y="Safety Score",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#7C3AED"]
    )
    
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=30, b=20),
        xaxis_title="",
        yaxis_title="",
        yaxis_range=[70, 100]
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Recent incidents in the area
    st.markdown("### Recent Incidents Nearby")
    
    incidents_data = [
        {"type": "Harassment", "location": "Main St & 5th Ave", "time": "2 days ago", "severity": "Medium"},
        {"type": "Theft", "location": "Central Park South", "time": "1 week ago", "severity": "Medium"},
        {"type": "Suspicious Activity", "location": "Broadway & 10th", "time": "3 days ago", "severity": "Low"}
    ]
    
    for incident in incidents_data:
        severity_class = "safety-high-bg" if incident["severity"] == "Low" else "safety-medium-bg" if incident["severity"] == "Medium" else "safety-low-bg"
        
        st.markdown(f"""
        <div style="margin-bottom: 0.5rem; padding: 0.5rem; background-color: var(--white); border-radius: 0.25rem; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
            <div style="display: flex; justify-content: space-between;">
                <span><strong>{incident["type"]}</strong></span>
                <span class="safety-indicator {severity_class}" style="font-size: 0.7rem;">{incident["severity"]}</span>
            </div>
            <div style="color: var(--neutral); font-size: 0.8rem;">
                {incident["location"]} • {incident["time"]}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Safety tips for the route
    st.markdown("### Safety Tips")
    
    st.markdown("""
    <div style="background-color: #EDE9FE; padding: 1rem; border-radius: 0.5rem; margin-top: 1rem;">
        <ul style="margin: 0; padding-left: 1.5rem;">
            <li>Stay on well-lit, populated streets when possible</li>
            <li>Share your route with a trusted contact</li>
            <li>Keep your phone charged and accessible</li>
            <li>Be aware of your surroundings</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Share route button
    st.markdown("### Share Your Route")
    
    col_share1, col_share2 = st.columns(2)
    
    with col_share1:
        st.button("Share Location", use_container_width=True)
    
    with col_share2:
        st.button("Track Journey", use_container_width=True)

# Features to improve safety
st.subheader("Enhanced Safety Features")

col_features1, col_features2, col_features3 = st.columns(3)

with col_features1:
    st.markdown("""
    <div class="route-card">
        <h4 style="color: var(--primary);">👥 Walking Buddy</h4>
        <p>Find other users traveling in the same direction to walk together.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
            Find a Buddy
        </button>
    </div>
    """, unsafe_allow_html=True)

with col_features2:
    st.markdown("""
    <div class="route-card">
        <h4 style="color: var(--primary);">🔊 Safety Alarm</h4>
        <p>Activate a loud safety alarm to deter potential threats and attract attention.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
            Set Up Alarm
        </button>
    </div>
    """, unsafe_allow_html=True)

with col_features3:
    st.markdown("""
    <div class="route-card">
        <h4 style="color: var(--primary);">🔍 Area Safety Reviews</h4>
        <p>Read and contribute safety reviews for specific streets and neighborhoods.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
            View Reviews
        </button>
    </div>
    """, unsafe_allow_html=True)

# Frequently traveled routes
st.subheader("Your Frequent Routes")

# Generate dummy frequent routes
frequent_routes = [
    {"name": "Home to Work", "safety": 92, "last_used": "Today"},
    {"name": "Home to Gym", "safety": 88, "last_used": "Yesterday"},
    {"name": "Home to Shopping Mall", "safety": 90, "last_used": "Last week"}
]

frequent_cols = st.columns(len(frequent_routes))

for i, route in enumerate(frequent_routes):
    safety_class = "safety-high-bg" if route["safety"] >= 90 else "safety-medium-bg" if route["safety"] >= 70 else "safety-low-bg"
    
    with frequent_cols[i]:
        st.markdown(f"""
        <div class="route-card">
            <h4>{route["name"]}</h4>
            <p><span class="safety-indicator {safety_class}">Safety: {route["safety"]}%</span></p>
            <p style="color: var(--neutral); font-size: 0.8rem;">Last used: {route["last_used"]}</p>
            <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; width: 100%;">
                Use Route
            </button>
        </div>
        """, unsafe_allow_html=True)