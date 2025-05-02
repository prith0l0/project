import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import random
from datetime import datetime, timedelta
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Report Incident - SafeHer",
    page_icon="📊",
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
        
        /* Incident report styling */
        .report-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        }
        
        .incident-type {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            font-weight: bold;
            color: white;
            margin-right: 0.5rem;
        }
        
        .harassment {
            background-color: #EF4444;
        }
        
        .suspicious {
            background-color: #F59E0B;
        }
        
        .theft {
            background-color: #10B981;
        }
        
        .assault {
            background-color: #7C3AED;
        }
        
        .other {
            background-color: #6B7280;
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
    
    # Incident filters
    st.subheader("Filter Incidents")
    
    incident_types = st.multiselect(
        "Incident Types",
        ["Harassment", "Suspicious Activity", "Theft", "Assault", "Other"],
        default=["Harassment", "Suspicious Activity", "Assault"]
    )
    
    time_period = st.selectbox(
        "Time Period",
        ["Last 24 hours", "Last week", "Last month", "Last 3 months", "All time"],
        index=1
    )
    
    radius = st.slider(
        "Distance (miles)",
        min_value=0.5,
        max_value=10.0,
        value=2.0,
        step=0.5
    )
    
    st.markdown("---")
    if st.button("Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Main content
st.title("Report & View Incidents")

# Tabs for viewing vs reporting
tab1, tab2 = st.tabs(["View Incidents", "Report an Incident"])

with tab1:
    st.subheader("Safety Incidents Near You")
    
    # Create map centered near user location
    user_lat, user_lon = 37.7749, -122.4194  # Sample coordinates for San Francisco
    
    m = folium.Map(location=[user_lat, user_lon], zoom_start=14)
    
    # Add marker for user's location
    folium.Marker(
        [user_lat, user_lon],
        popup="Your Location",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)
    
    # Add circle to show search radius
    folium.Circle(
        location=[user_lat, user_lon],
        radius=radius * 1609,  # Convert miles to meters
        color="#7C3AED",
        fill=True,
        fill_opacity=0.1
    ).add_to(m)
    
    # Generate sample incident data
    incidents = []
    
    incident_types_data = ["Harassment", "Suspicious Activity", "Theft", "Assault", "Other"]
    incident_colors = {"Harassment": "red", "Suspicious Activity": "orange", "Theft": "green", "Assault": "purple", "Other": "gray"}
    
    # Generate 15 random incidents
    for i in range(15):
        # Random position within radius
        angle = random.uniform(0, 360)
        distance = random.uniform(0, radius)
        
        # Convert polar to cartesian coordinates
        import math
        dx = distance * math.cos(math.radians(angle)) * 0.01
        dy = distance * math.sin(math.radians(angle)) * 0.01
        
        incident_lat = user_lat + dy
        incident_lon = user_lon + dx
        
        # Random incident type
        incident_type = random.choice(incident_types_data)
        
        # Random time within the last month
        days_ago = random.randint(0, 30)
        incident_time = datetime.now() - timedelta(days=days_ago)
        incident_time_str = incident_time.strftime("%Y-%m-%d %H:%M")
        
        # Description based on type
        descriptions = {
            "Harassment": ["Verbal harassment on the street", "Catcalling incident", "Following and verbal harassment"],
            "Suspicious Activity": ["Suspicious person loitering", "Someone following people", "Unusual behavior near ATM"],
            "Theft": ["Phone snatching incident", "Purse theft", "Attempted pickpocketing"],
            "Assault": ["Physical altercation", "Attempted assault", "Pushing incident"],
            "Other": ["Uncomfortable situation", "Unwanted approach", "Safety concern"]
        }
        
        description = random.choice(descriptions[incident_type])
        
        incidents.append({
            "type": incident_type,
            "lat": incident_lat,
            "lon": incident_lon,
            "time": incident_time,
            "time_str": incident_time_str,
            "description": description,
            "status": random.choice(["Verified", "Under Review", "Reported"])
        })
    
    # Sort by recency
    incidents.sort(key=lambda x: x["time"], reverse=True)
    
    # Add incident markers to map
    for incident in incidents:
        if incident["type"] in incident_types:
            color = incident_colors[incident["type"]]
            
            folium.CircleMarker(
                location=[incident["lat"], incident["lon"]],
                radius=8,
                color=color,
                fill=True,
                fill_color=color,
                fill_opacity=0.7,
                popup=f"{incident['type']}: {incident['description']} ({incident['time_str']})"
            ).add_to(m)
    
    # Display map
    folium_static(m, width=800, height=500)
    
    # Incident statistics
    st.subheader("Incident Statistics")
    
    # Create data for charts
    incident_counts = {}
    for type in incident_types_data:
        incident_counts[type] = len([i for i in incidents if i["type"] == type])
    
    # Incident type distribution
    incident_type_df = pd.DataFrame({
        "Incident Type": list(incident_counts.keys()),
        "Count": list(incident_counts.values())
    })
    
    fig1 = px.pie(
        incident_type_df,
        values="Count",
        names="Incident Type",
        title="Incident Types Distribution",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    
    fig1.update_traces(textposition='inside', textinfo='percent+label')
    fig1.update_layout(height=350)
    
    # Time-based incident trend
    # Group incidents by day
    from collections import defaultdict
    daily_counts = defaultdict(int)
    
    for incident in incidents:
        day = incident["time"].date()
        daily_counts[day] += 1
    
    # Sort days
    sorted_days = sorted(daily_counts.keys())
    
    time_df = pd.DataFrame({
        "Date": sorted_days,
        "Incidents": [daily_counts[day] for day in sorted_days]
    })
    
    fig2 = px.line(
        time_df,
        x="Date",
        y="Incidents",
        title="Incident Trend (Last 30 Days)",
        markers=True,
        line_shape="spline",
        color_discrete_sequence=["#7C3AED"]
    )
    
    fig2.update_layout(height=350)
    
    # Display charts in columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.plotly_chart(fig1, use_container_width=True)
    
    with col2:
        st.plotly_chart(fig2, use_container_width=True)
    
    # Recent incident list
    st.subheader("Recent Incidents")
    
    for incident in incidents[:10]:  # Show only the 10 most recent incidents
        if incident["type"] in incident_types:
            incident_class = incident["type"].lower().replace(" ", "-")
            
            st.markdown(f"""
            <div class="report-card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span class="incident-type {incident_class}">{incident["type"]}</span>
                        <span style="color: var(--neutral); font-size: 0.8rem;">{incident["time_str"]}</span>
                    </div>
                    <span style="background-color: #E5E7EB; padding: 0.2rem 0.5rem; border-radius: 9999px; font-size: 0.75rem;">
                        {incident["status"]}
                    </span>
                </div>
                <p style="margin-top: 0.5rem; margin-bottom: 0;">{incident["description"]}</p>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.subheader("Report a Safety Incident")
    st.markdown("Help improve community safety by reporting incidents. Your reports are anonymous by default.")
    
    # Report form
    with st.form("incident_report_form"):
        # Incident type selection
        incident_type = st.selectbox(
            "Incident Type",
            ["Harassment", "Suspicious Activity", "Theft", "Assault", "Other"]
        )
        
        # Description
        description = st.text_area("Description", placeholder="Describe what happened...")
        
        # Date and time
        col_date, col_time = st.columns(2)
        
        with col_date:
            incident_date = st.date_input("Date", datetime.now())
        
        with col_time:
            incident_time = st.time_input("Time", datetime.now().time())
        
        # Location
        st.markdown("### Location")
        
        use_current = st.checkbox("Use my current location", value=True)
        
        if not use_current:
            location_address = st.text_input("Address")
        else:
            location_address = "Current location"
        
        # Create map for location selection
        incident_map = folium.Map(location=[user_lat, user_lon], zoom_start=15)
        
        folium.Marker(
            [user_lat, user_lon],
            popup="Incident Location",
            icon=folium.Icon(color="red", icon="info-sign"),
            draggable=True
        ).add_to(incident_map)
        
        st.markdown("Drag the marker to the exact location of the incident")
        folium_static(incident_map, width=800, height=300)
        
        # Additional details
        st.markdown("### Additional Details")
        
        severity = st.select_slider(
            "Severity",
            options=["Low", "Medium", "High", "Critical"],
            value="Medium"
        )
        
        witnesses = st.checkbox("There were witnesses")
        
        reported_police = st.checkbox("Reported to police")
        
        if reported_police:
            police_report = st.text_input("Police Report Number (optional)")
        
        # Attachments
        st.markdown("### Attachments (optional)")
        
        photo_upload = st.file_uploader("Upload Photos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
        
        # Anonymity options
        st.markdown("### Privacy Options")
        
        anonymous = st.checkbox("Keep my report anonymous", value=True)
        
        if not anonymous:
            st.warning("Your username will be visible to other users if you uncheck this.")
        
        share_location = st.checkbox("Share precise location", value=True)
        
        if not share_location:
            st.info("Only the general area will be shown to other users.")
        
        # Submission
        submit_button = st.form_submit_button("Submit Report")
        
        if submit_button:
            if not description:
                st.error("Please provide a description of the incident.")
            else:
                st.success("Thank you for your report. It has been submitted and will help keep the community safer.")
                
                # Show next steps
                st.markdown("""
                ### Next Steps
                
                Your report will be:
                1. Reviewed by our safety team
                2. Added to the safety map if verified
                3. Used to improve safe routing for all users
                
                You can track the status of your report in your profile.
                """)