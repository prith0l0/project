import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Emergency Contacts - SafeHer",
    page_icon="📞",
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
        
        /* Contact specific styling */
        .contact-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .contact-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: var(--primary-light);
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            color: white;
            font-size: 1.25rem;
        }
        
        .contact-info {
            flex-grow: 1;
        }
        
        .contact-actions {
            display: flex;
            gap: 0.5rem;
        }
        
        .contact-action-button {
            background-color: transparent;
            border: none;
            cursor: pointer;
            padding: 0.5rem;
            border-radius: 0.25rem;
            color: var(--neutral);
            transition: background-color 0.2s;
        }
        
        .contact-action-button:hover {
            background-color: #F3F4F6;
        }
        
        .priority-contact {
            border-left: 4px solid var(--primary);
        }
        
        /* Form styling */
        .form-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
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
    
    # Emergency contact tips
    st.subheader("Contact Tips")
    
    st.markdown("""
    - Add at least 3 trusted emergency contacts
    - Include people who are typically available at different times
    - Make sure your contacts know they're on your emergency list
    - Regularly update contact information
    - Consider adding local emergency services
    """)
    
    st.markdown("---")
    if st.button("Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Main content
st.title("Emergency Contacts")
st.markdown("Manage the contacts who will be notified in case of an emergency.")

# Tabs for contact lists
tab1, tab2, tab3 = st.tabs(["Emergency Contacts", "Add New Contact", "Emergency Services"])

with tab1:
    st.subheader("Your Emergency Contacts")
    
    # Sample contacts data (in a real app, this would be stored in a database)
    contacts = [
        {"name": "Mom", "phone": "+1 (555) 123-4567", "relationship": "Family", "priority": True, "initials": "MO"},
        {"name": "Dad", "phone": "+1 (555) 765-4321", "relationship": "Family", "priority": True, "initials": "DA"},
        {"name": "Sarah (Roommate)", "phone": "+1 (555) 987-6543", "relationship": "Roommate", "priority": False, "initials": "SR"},
        {"name": "John (Friend)", "phone": "+1 (555) 345-6789", "relationship": "Friend", "priority": False, "initials": "JF"}
    ]
    
    if not contacts:
        st.warning("You don't have any emergency contacts yet. Add contacts to get help quickly in emergencies.")
    else:
        # Priority contacts first
        priority_contacts = [c for c in contacts if c["priority"]]
        other_contacts = [c for c in contacts if not c["priority"]]
        
        # Display priority contacts
        if priority_contacts:
            st.markdown("#### Priority Contacts")
            st.caption("These contacts will be notified first in case of emergency")
            
            for contact in priority_contacts:
                st.markdown(f"""
                <div class="contact-card priority-contact">
                    <div class="contact-avatar">{contact["initials"]}</div>
                    <div class="contact-info">
                        <h4 style="margin: 0;">{contact["name"]}</h4>
                        <div style="display: flex; gap: 1rem;">
                            <span style="color: var(--neutral); font-size: 0.9rem;">{contact["phone"]}</span>
                            <span style="color: var(--neutral); font-size: 0.9rem;">Relationship: {contact["relationship"]}</span>
                        </div>
                    </div>
                    <div class="contact-actions">
                        <button class="contact-action-button" title="Call">📞</button>
                        <button class="contact-action-button" title="Text">💬</button>
                        <button class="contact-action-button" title="Edit">✏️</button>
                        <button class="contact-action-button" title="Remove">❌</button>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Display other contacts
        if other_contacts:
            st.markdown("#### Other Contacts")
            
            for contact in other_contacts:
                st.markdown(f"""
                <div class="contact-card">
                    <div class="contact-avatar">{contact["initials"]}</div>
                    <div class="contact-info">
                        <h4 style="margin: 0;">{contact["name"]}</h4>
                        <div style="display: flex; gap: 1rem;">
                            <span style="color: var(--neutral); font-size: 0.9rem;">{contact["phone"]}</span>
                            <span style="color: var(--neutral); font-size: 0.9rem;">Relationship: {contact["relationship"]}</span>
                        </div>
                    </div>
                    <div class="contact-actions">
                        <button class="contact-action-button" title="Call">📞</button>
                        <button class="contact-action-button" title="Text">💬</button>
                        <button class="contact-action-button" title="Edit">✏️</button>
                        <button class="contact-action-button" title="Remove">❌</button>
                    </div>
                </div>
                """, unsafe_allow_html=True)
    
    # Emergency alert settings
    st.subheader("Emergency Alert Settings")
    
    st.markdown("""
    <div class="form-card">
        <h4 style="margin-top: 0;">Alert Message Template</h4>
        <p style="color: var(--neutral); margin-bottom: 1rem;">This message will be sent to your emergency contacts when you trigger an alert.</p>
        
        <textarea style="width: 100%; padding: 0.75rem; border-radius: 0.25rem; border: 1px solid #D1D5DB; margin-bottom: 1rem;" rows="3">🆘 EMERGENCY ALERT: I'm in an emergency situation and need help. My current location is: [LOCATION]. Please contact me immediately or call emergency services.</textarea>
        
        <div style="display: flex; justify-content: space-between; margin-bottom: 1rem;">
            <label style="display: flex; align-items: center; gap: 0.5rem;">
                <input type="checkbox" checked />
                <span>Include my current location</span>
            </label>
            
            <label style="display: flex; align-items: center; gap: 0.5rem;">
                <input type="checkbox" checked />
                <span>Include photo from camera</span>
            </label>
            
            <label style="display: flex; align-items: center; gap: 0.5rem;">
                <input type="checkbox" checked />
                <span>Include audio recording</span>
            </label>
        </div>
        
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Save Template
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # Notification settings
    st.markdown("""
    <div class="form-card">
        <h4 style="margin-top: 0;">Notification Settings</h4>
        
        <div style="margin-bottom: 1rem;">
            <label style="display: block; margin-bottom: 0.5rem;">Alert Method</label>
            <div style="display: flex; gap: 1rem;">
                <label style="display: flex; align-items: center; gap: 0.5rem;">
                    <input type="checkbox" checked />
                    <span>SMS Text</span>
                </label>
                
                <label style="display: flex; align-items: center; gap: 0.5rem;">
                    <input type="checkbox" checked />
                    <span>WhatsApp</span>
                </label>
                
                <label style="display: flex; align-items: center; gap: 0.5rem;">
                    <input type="checkbox" />
                    <span>Email</span>
                </label>
                
                <label style="display: flex; align-items: center; gap: 0.5rem;">
                    <input type="checkbox" checked />
                    <span>In-app notification</span>
                </label>
            </div>
        </div>
        
        <div style="margin-bottom: 1rem;">
            <label style="display: block; margin-bottom: 0.5rem;">Notification Frequency</label>
            <select style="width: 100%; padding: 0.5rem; border-radius: 0.25rem; border: 1px solid #D1D5DB;">
                <option>Send a single alert</option>
                <option selected>Repeat alert every 1 minute (3 times)</option>
                <option>Repeat alert every 2 minutes (5 times)</option>
                <option>Repeat alert until manually stopped</option>
            </select>
        </div>
        
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Save Settings
        </button>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.subheader("Add New Emergency Contact")
    
    with st.form("add_contact_form"):
        st.markdown("""
        <p style="color: var(--neutral);">Add trusted people who can help you in emergency situations. Make sure to inform them that they're on your emergency contacts list.</p>
        """, unsafe_allow_html=True)
        
        contact_name = st.text_input("Full Name", placeholder="e.g., Jane Smith")
        
        col1, col2 = st.columns(2)
        
        with col1:
            contact_phone = st.text_input("Phone Number", placeholder="e.g., +1 (555) 123-4567")
        
        with col2:
            contact_relationship = st.selectbox(
                "Relationship",
                ["Family", "Friend", "Roommate", "Coworker", "Neighbor", "Other"]
            )
        
        contact_priority = st.checkbox("Mark as priority contact", value=True, help="Priority contacts are notified first during emergencies")
        
        contact_notes = st.text_area("Notes (optional)", placeholder="Add any additional information about this contact...")
        
        st.markdown("### Communication Preferences")
        
        col_comm1, col_comm2 = st.columns(2)
        
        with col_comm1:
            contact_sms = st.checkbox("SMS Alerts", value=True)
            contact_whatsapp = st.checkbox("WhatsApp Alerts")
        
        with col_comm2:
            contact_call = st.checkbox("Phone Call", value=True)
            contact_email = st.checkbox("Email Alerts")
        
        if contact_email:
            contact_email_address = st.text_input("Email Address")
        
        submit_button = st.form_submit_button("Add Contact")
        
        if submit_button:
            if not contact_name or not contact_phone:
                st.error("Please provide both name and phone number for the contact.")
            else:
                st.success(f"Contact {contact_name} has been added to your emergency contacts.")
                st.balloons()

with tab3:
    st.subheader("Emergency Services")
    
    st.markdown("""
    <p style="color: var(--neutral);">Important local emergency services that can be contacted directly from the app during an emergency.</p>
    """, unsafe_allow_html=True)
    
    # Emergency services based on location
    emergency_services = [
        {"name": "Police", "number": "911", "icon": "🚓"},
        {"name": "Ambulance", "number": "911", "icon": "🚑"},
        {"name": "Fire Department", "number": "911", "icon": "🚒"},
        {"name": "Women's Crisis Hotline", "number": "1-800-799-7233", "icon": "☎️"},
        {"name": "Poison Control", "number": "1-800-222-1222", "icon": "⚕️"},
        {"name": "Mental Health Crisis Line", "number": "988", "icon": "🧠"}
    ]
    
    for service in emergency_services:
        st.markdown(f"""
        <div class="contact-card">
            <div style="font-size: 2rem; margin-right: 0.5rem;">{service["icon"]}</div>
            <div class="contact-info">
                <h4 style="margin: 0;">{service["name"]}</h4>
                <span style="color: var(--neutral); font-size: 0.9rem;">{service["number"]}</span>
            </div>
            <div class="contact-actions">
                <button class="contact-action-button" title="Call" style="font-size: 1.25rem;">📞</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Custom emergency service
    st.subheader("Add Custom Emergency Service")
    
    with st.form("add_service_form"):
        service_name = st.text_input("Service Name", placeholder="e.g., Campus Security")
        service_number = st.text_input("Phone Number", placeholder="e.g., (555) 123-4567")
        
        submit_service = st.form_submit_button("Add Service")
        
        if submit_service:
            if not service_name or not service_number:
                st.error("Please provide both name and phone number for the service.")
            else:
                st.success(f"{service_name} has been added to your emergency services.")

# Test emergency system
st.subheader("Test Emergency System")

st.markdown("""
<div class="form-card">
    <p>Test your emergency alert system to ensure everything works correctly when you need it. This will send a test message to your selected contact.</p>
    
    <div style="background-color: #FEF3C7; border-left: 4px solid #F59E0B; padding: 1rem; margin: 1rem 0; border-radius: 0.25rem;">
        <strong>Note:</strong> The test message will clearly indicate that this is only a test and not a real emergency.
    </div>
    
    <div style="margin-bottom: 1rem;">
        <label style="display: block; margin-bottom: 0.5rem;">Select Contact for Test</label>
        <select style="width: 100%; padding: 0.5rem; border-radius: 0.25rem; border: 1px solid #D1D5DB;">
            <option>Mom</option>
            <option>Dad</option>
            <option>Sarah (Roommate)</option>
            <option>John (Friend)</option>
        </select>
    </div>
    
    <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
        Send Test Alert
    </button>
</div>
""", unsafe_allow_html=True)

# Last test results
st.markdown("""
<div class="form-card">
    <h4 style="margin-top: 0;">Last Test Results</h4>
    
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 1rem;">
        <thead>
            <tr style="border-bottom: 1px solid #E5E7EB;">
                <th style="text-align: left; padding: 0.5rem;">Date</th>
                <th style="text-align: left; padding: 0.5rem;">Contact</th>
                <th style="text-align: left; padding: 0.5rem;">Status</th>
                <th style="text-align: left; padding: 0.5rem;">Response Time</th>
            </tr>
        </thead>
        <tbody>
            <tr style="border-bottom: 1px solid #E5E7EB;">
                <td style="padding: 0.5rem;">2025-03-15 10:45 AM</td>
                <td style="padding: 0.5rem;">Mom</td>
                <td style="padding: 0.5rem;"><span style="color: var(--success);">Delivered</span></td>
                <td style="padding: 0.5rem;">12 seconds</td>
            </tr>
            <tr style="border-bottom: 1px solid #E5E7EB;">
                <td style="padding: 0.5rem;">2025-02-28 03:30 PM</td>
                <td style="padding: 0.5rem;">Dad</td>
                <td style="padding: 0.5rem;"><span style="color: var(--success);">Delivered</span></td>
                <td style="padding: 0.5rem;">8 seconds</td>
            </tr>
        </tbody>
    </table>
</div>
""", unsafe_allow_html=True)