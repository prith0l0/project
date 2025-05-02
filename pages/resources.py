import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Safety Resources - SafeHer",
    page_icon="📚",
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
        
        /* Resources styling */
        .resource-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s ease;
        }
        
        .resource-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .resource-icon {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        .tag {
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 9999px;
            font-size: 0.75rem;
            background-color: var(--primary-light);
            color: white;
            margin-right: 0.25rem;
            margin-bottom: 0.25rem;
        }
        
        .article-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        
        .article-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .article-image {
            width: 100%;
            height: 150px;
            object-fit: cover;
        }
        
        .article-content {
            padding: 1rem;
        }
        
        .technique-card {
            background-color: var(--white);
            border-radius: 0.5rem;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
            border-left: 4px solid var(--primary);
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
    
    # Resource categories
    st.subheader("Categories")
    
    categories = [
        "All Resources",
        "Safety Organizations",
        "Self-Defense",
        "Mental Health",
        "Legal Resources",
        "Transportation",
        "Educational Content"
    ]
    
    selected_category = st.radio("Filter by category", categories)
    
    st.markdown("---")
    if st.button("Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Main content
st.title("Safety Resources")
st.markdown("Access important safety information, services, and educational content.")

# Search
search = st.text_input("Search Resources", placeholder="e.g., self-defense, counseling, legal aid...")

# Tabs for resource categories
tab1, tab2, tab3, tab4 = st.tabs(["Local Services", "Safety Articles", "Self-Defense", "Community Resources"])

with tab1:
    st.subheader("Local Safety Services")
    
    # Local services by category
    service_categories = [
        {
            "name": "Women's Shelters",
            "icon": "🏠",
            "services": [
                {"name": "Safe Haven Women's Center", "address": "123 Main St, San Francisco, CA", "phone": "(555) 123-4567", "hours": "24/7", "tags": ["shelter", "counseling", "crisis"]},
                {"name": "Women's Protection Alliance", "address": "456 Market St, San Francisco, CA", "phone": "(555) 987-6543", "hours": "Mon-Fri 9AM-8PM", "tags": ["shelter", "legal aid", "support groups"]},
                {"name": "Harmony House", "address": "789 Oak Ave, San Francisco, CA", "phone": "(555) 321-7654", "hours": "24/7", "tags": ["shelter", "family services", "childcare"]}
            ]
        },
        {
            "name": "Crisis Centers",
            "icon": "⚕️",
            "services": [
                {"name": "Bay Area Crisis Center", "address": "101 Pine St, San Francisco, CA", "phone": "(555) 111-2222", "hours": "24/7", "tags": ["crisis", "hotline", "counseling"]},
                {"name": "SF Emergency Support", "address": "202 Elm St, San Francisco, CA", "phone": "(555) 333-4444", "hours": "24/7", "tags": ["crisis", "temporary housing", "medical"]}
            ]
        },
        {
            "name": "Legal Aid",
            "icon": "⚖️",
            "services": [
                {"name": "Women's Legal Collective", "address": "303 Cedar Rd, San Francisco, CA", "phone": "(555) 555-6666", "hours": "Mon-Fri 9AM-5PM", "tags": ["legal", "restraining orders", "advocacy"]},
                {"name": "Bay Legal Aid", "address": "404 Redwood Blvd, San Francisco, CA", "phone": "(555) 777-8888", "hours": "Mon-Fri 8:30AM-5:30PM", "tags": ["legal", "immigration", "housing"]}
            ]
        },
        {
            "name": "Mental Health Services",
            "icon": "🧠",
            "services": [
                {"name": "Women's Wellness Center", "address": "505 Birch St, San Francisco, CA", "phone": "(555) 999-0000", "hours": "Mon-Sat 8AM-8PM", "tags": ["counseling", "therapy", "support groups"]},
                {"name": "Healing Paths Therapy", "address": "606 Willow Dr, San Francisco, CA", "phone": "(555) 222-3333", "hours": "Mon-Fri 9AM-7PM", "tags": ["therapy", "trauma", "PTSD"]}
            ]
        }
    ]
    
    for category in service_categories:
        st.markdown(f"""
        <h3>{category["icon"]} {category["name"]}</h3>
        """, unsafe_allow_html=True)
        
        for service in category["services"]:
            st.markdown(f"""
            <div class="resource-card">
                <h4 style="margin-top: 0;">{service["name"]}</h4>
                <p style="margin-bottom: 0.5rem;"><strong>Address:</strong> {service["address"]}</p>
                <p style="margin-bottom: 0.5rem;"><strong>Phone:</strong> {service["phone"]}</p>
                <p style="margin-bottom: 1rem;"><strong>Hours:</strong> {service["hours"]}</p>
                <div>
                    {' '.join([f'<span class="tag">{tag}</span>' for tag in service["tags"]])}
                </div>
                <div style="margin-top: 1rem;">
                    <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; margin-right: 0.5rem;">
                        Get Directions
                    </button>
                    <button style="background-color: transparent; border: 1px solid var(--primary); color: var(--primary); padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
                        Call
                    </button>
                </div>
            </div>
            """, unsafe_allow_html=True)

with tab2:
    st.subheader("Safety Articles & Guides")
    
    # Featured article
    st.markdown("""
    <div class="resource-card" style="border-left: 4px solid var(--primary);">
        <h3 style="margin-top: 0;">Featured: Personal Safety Planning</h3>
        <p>Creating a personal safety plan is an important step in enhancing your security. It helps you think through potentially dangerous situations and have a strategy ready.</p>
        
        <h4>Key Elements of a Safety Plan:</h4>
        <ol>
            <li>Identify safe places you can go in an emergency</li>
            <li>Create a network of trusted contacts</li>
            <li>Prepare an emergency bag with essentials</li>
            <li>Document important information</li>
            <li>Plan safe routes for daily activities</li>
        </ol>
        
        <a href="#" style="color: var(--primary); text-decoration: none; font-weight: bold;">Read the full guide →</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Articles grid
    st.markdown("### Latest Articles")
    
    articles = [
        {
            "title": "Situational Awareness: The Key to Personal Safety",
            "image": "https://images.pexels.com/photos/6964402/pexels-photo-6964402.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "summary": "Learn how to develop and maintain situational awareness to prevent potential threats.",
            "tags": ["safety tips", "prevention"]
        },
        {
            "title": "Digital Safety: Protecting Your Online Presence",
            "image": "https://images.pexels.com/photos/5380664/pexels-photo-5380664.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "summary": "Tips to safeguard your digital information and maintain privacy in the connected world.",
            "tags": ["online safety", "privacy"]
        },
        {
            "title": "Transportation Safety Guidelines for Women",
            "image": "https://images.pexels.com/photos/7289738/pexels-photo-7289738.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "summary": "Safety practices for various modes of transportation, from public transit to ridesharing.",
            "tags": ["transportation", "travel"]
        },
        {
            "title": "Understanding and Responding to Verbal Harassment",
            "image": "https://images.pexels.com/photos/7176319/pexels-photo-7176319.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "summary": "Strategies for handling verbal harassment in public spaces and the workplace.",
            "tags": ["harassment", "response"]
        },
        {
            "title": "Building Confidence Through Self-Defense Training",
            "image": "https://images.pexels.com/photos/8108086/pexels-photo-8108086.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "summary": "How self-defense training can empower you both physically and mentally.",
            "tags": ["self-defense", "empowerment"]
        },
        {
            "title": "Creating Safe Spaces: Community Initiatives",
            "image": "https://images.pexels.com/photos/6646918/pexels-photo-6646918.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "summary": "How communities are working together to create safer environments for women.",
            "tags": ["community", "initiatives"]
        }
    ]
    
    # Display articles in a grid
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    for i, article in enumerate(articles):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="article-card">
                <img src="{article["image"]}" alt="{article["title"]}" class="article-image">
                <div class="article-content">
                    <h4 style="margin-top: 0;">{article["title"]}</h4>
                    <p style="color: var(--neutral); margin-bottom: 1rem;">{article["summary"]}</p>
                    <div style="margin-bottom: 1rem;">
                        {' '.join([f'<span class="tag">{tag}</span>' for tag in article["tags"]])}
                    </div>
                    <a href="#" style="color: var(--primary); text-decoration: none; font-weight: bold;">Read article</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

with tab3:
    st.subheader("Self-Defense Techniques")
    
    # Introduction
    st.markdown("""
    <div class="resource-card">
        <p>Self-defense is about awareness, preparedness, and knowing techniques that can help you protect yourself in threatening situations. The techniques below are basic and can be learned by anyone, regardless of physical strength or prior training.</p>
        
        <div style="background-color: #FEF3C7; border-left: 4px solid #F59E0B; padding: 1rem; margin: 1rem 0; border-radius: 0.25rem;">
            <strong>Note:</strong> These techniques are meant for educational purposes only. For comprehensive self-defense training, consider taking a professional course.
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Basic techniques
    st.markdown("### Basic Self-Defense Techniques")
    
    techniques = [
        {
            "name": "The Palm Strike",
            "description": "A simple yet effective strike using the heel of your palm. Aim for the nose or chin, with your arm straight and using your body weight to add force.",
            "when_to_use": "When you need to create distance between yourself and an attacker",
            "key_points": ["Keep your hand open and fingers bent back", "Aim for vulnerable areas like the nose or chin", "Use your body weight to add power"]
        },
        {
            "name": "Elbow Strike",
            "description": "One of the strongest strikes, using your elbow to target an attacker's face, neck, or solar plexus.",
            "when_to_use": "When an attacker is very close and you cannot create distance",
            "key_points": ["Bend your arm and keep your fist close to your chest", "Turn your body into the strike for maximum impact", "Aim for vulnerable areas"]
        },
        {
            "name": "Knee Strike",
            "description": "A powerful strike using your knee to target the attacker's groin, thigh, or abdomen.",
            "when_to_use": "When an attacker is close and you need to create an opportunity to escape",
            "key_points": ["Grab the attacker's shoulders for balance", "Pull down while driving your knee upward", "Immediately follow with an escape"]
        },
        {
            "name": "Wrist Release",
            "description": "A technique to free yourself when someone grabs your wrist or arm.",
            "when_to_use": "When someone has grabbed your wrist or forearm",
            "key_points": ["Rotate your arm toward the attacker's thumb (the weakest part of their grip)", "Use a quick, forceful motion", "Step back as you break free"]
        }
    ]
    
    for technique in techniques:
        st.markdown(f"""
        <div class="technique-card">
            <h4 style="margin-top: 0;">{technique["name"]}</h4>
            <p>{technique["description"]}</p>
            
            <p><strong>When to use:</strong> {technique["when_to_use"]}</p>
            
            <p><strong>Key points:</strong></p>
            <ul>
                {' '.join([f'<li>{point}</li>' for point in technique["key_points"]])}
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Self-defense classes
    st.markdown("### Find Self-Defense Classes Near You")
    
    classes = [
        {"name": "Women's Self-Defense Workshop", "location": "Community Center, 123 Main St", "schedule": "Saturdays, 10AM-12PM", "cost": "Free"},
        {"name": "Krav Maga for Beginners", "location": "Urban Defense Studio, 456 Market St", "schedule": "Mon/Wed/Fri, 6PM-7:30PM", "cost": "$80/month"},
        {"name": "Safety Skills & Awareness", "location": "City College, Room 102", "schedule": "Tuesdays, 7PM-9PM", "cost": "$60 for 6 weeks"}
    ]
    
    for class_info in classes:
        st.markdown(f"""
        <div class="resource-card">
            <h4 style="margin-top: 0;">{class_info["name"]}</h4>
            <p><strong>Location:</strong> {class_info["location"]}</p>
            <p><strong>Schedule:</strong> {class_info["schedule"]}</p>
            <p><strong>Cost:</strong> {class_info["cost"]}</p>
            <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; margin-right: 0.5rem;">
                Register
            </button>
            <button style="background-color: transparent; border: 1px solid var(--primary); color: var(--primary); padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
                More Info
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Safety products
    st.markdown("### Recommended Safety Products")
    
    products_col1, products_col2, products_col3 = st.columns(3)
    
    with products_col1:
        st.markdown("""
        <div class="resource-card">
            <div class="resource-icon">🔊</div>
            <h4>Personal Alarm</h4>
            <p>A small device that emits a loud sound (130+ dB) when activated, attracting attention and deterring attackers.</p>
            <a href="#" style="color: var(--primary); text-decoration: none; font-weight: bold;">View recommendations</a>
        </div>
        """, unsafe_allow_html=True)
    
    with products_col2:
        st.markdown("""
        <div class="resource-card">
            <div class="resource-icon">📱</div>
            <h4>Safety Apps</h4>
            <p>Apps that provide quick access to emergency contacts, location sharing, and panic buttons.</p>
            <a href="#" style="color: var(--primary); text-decoration: none; font-weight: bold;">View recommendations</a>
        </div>
        """, unsafe_allow_html=True)
    
    with products_col3:
        st.markdown("""
        <div class="resource-card">
            <div class="resource-icon">🔦</div>
            <h4>Tactical Flashlights</h4>
            <p>Bright flashlights that can temporarily blind an attacker and can be used as a striking tool in emergencies.</p>
            <a href="#" style="color: var(--primary); text-decoration: none; font-weight: bold;">View recommendations</a>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.subheader("Community Safety Resources")
    
    # Neighborhood watch
    st.markdown("""
    <div class="resource-card">
        <h3 style="margin-top: 0;">🏘️ Neighborhood Watch Programs</h3>
        <p>Neighborhood Watch is a crime prevention program that encourages residents to work together to create safer communities.</p>
        
        <h4>Benefits:</h4>
        <ul>
            <li>Improved communication between residents and local law enforcement</li>
            <li>Greater awareness of suspicious activities</li>
            <li>Stronger sense of community and mutual support</li>
            <li>Reduced crime rates in participating neighborhoods</li>
        </ul>
        
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer; margin-right: 0.5rem;">
            Find a Program Near You
        </button>
        <button style="background-color: transparent; border: 1px solid var(--primary); color: var(--primary); padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Start a New Program
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    # Community initiatives
    st.markdown("### Community Safety Initiatives")
    
    initiatives_col1, initiatives_col2 = st.columns(2)
    
    with initiatives_col1:
        st.markdown("""
        <div class="resource-card">
            <h4 style="margin-top: 0;">SafeWalk Programs</h4>
            <p>Volunteer-based programs that provide walking escorts for individuals traveling alone at night, particularly on college campuses and in urban areas.</p>
            <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
                Find or Volunteer
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="resource-card">
            <h4 style="margin-top: 0;">Business Safe Havens</h4>
            <p>A network of businesses that agree to be safe spaces where individuals can seek temporary refuge if they feel unsafe or threatened.</p>
            <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
                View Participating Businesses
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    with initiatives_col2:
        st.markdown("""
        <div class="resource-card">
            <h4 style="margin-top: 0;">Community Safety Workshops</h4>
            <p>Educational workshops that teach personal safety, self-defense, and community building skills to residents.</p>
            <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
                Upcoming Workshops
            </button>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="resource-card">
            <h4 style="margin-top: 0;">Street Lighting Improvement Projects</h4>
            <p>Community initiatives to identify and improve poorly lit areas to enhance nighttime safety.</p>
            <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
                Report Poor Lighting
            </button>
        </div>
        """, unsafe_allow_html=True)
    
    # Community forums
    st.markdown("### Community Safety Forums")
    
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Upcoming Community Safety Meetings</h4>
        
        <table style="width: 100%; border-collapse: collapse; margin-bottom: 1rem;">
            <thead>
                <tr style="border-bottom: 1px solid #E5E7EB;">
                    <th style="text-align: left; padding: 0.5rem;">Event</th>
                    <th style="text-align: left; padding: 0.5rem;">Date & Time</th>
                    <th style="text-align: left; padding: 0.5rem;">Location</th>
                    <th style="text-align: left; padding: 0.5rem;">Action</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #E5E7EB;">
                    <td style="padding: 0.5rem;">District 5 Safety Town Hall</td>
                    <td style="padding: 0.5rem;">May 15, 2025 - 6:30 PM</td>
                    <td style="padding: 0.5rem;">Community Center, 123 Main St</td>
                    <td style="padding: 0.5rem;">
                        <button style="background-color: var(--primary); color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.8rem; cursor: pointer;">
                            RSVP
                        </button>
                    </td>
                </tr>
                <tr style="border-bottom: 1px solid #E5E7EB;">
                    <td style="padding: 0.5rem;">Women's Safety Workshop</td>
                    <td style="padding: 0.5rem;">May 20, 2025 - 5:00 PM</td>
                    <td style="padding: 0.5rem;">Public Library, 456 Oak St</td>
                    <td style="padding: 0.5rem;">
                        <button style="background-color: var(--primary); color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.8rem; cursor: pointer;">
                            RSVP
                        </button>
                    </td>
                </tr>
                <tr style="border-bottom: 1px solid #E5E7EB;">
                    <td style="padding: 0.5rem;">Neighborhood Watch Kickoff</td>
                    <td style="padding: 0.5rem;">May 27, 2025 - 7:00 PM</td>
                    <td style="padding: 0.5rem;">Westside Park Pavilion</td>
                    <td style="padding: 0.5rem;">
                        <button style="background-color: var(--primary); color: white; border: none; padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.8rem; cursor: pointer;">
                            RSVP
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

# Volunteer opportunities
st.subheader("Get Involved: Volunteer Opportunities")

volunteer_col1, volunteer_col2, volunteer_col3 = st.columns(3)

with volunteer_col1:
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Crisis Hotline Volunteer</h4>
        <p>Provide support to individuals in crisis situations through phone or text support.</p>
        <p><strong>Commitment:</strong> 4-8 hours weekly</p>
        <p><strong>Training:</strong> 40-hour program provided</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Apply
        </button>
    </div>
    """, unsafe_allow_html=True)

with volunteer_col2:
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Safety Workshop Facilitator</h4>
        <p>Lead or assist with safety education workshops in schools and community centers.</p>
        <p><strong>Commitment:</strong> 2-4 hours weekly</p>
        <p><strong>Training:</strong> 16-hour program provided</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Apply
        </button>
    </div>
    """, unsafe_allow_html=True)

with volunteer_col3:
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Safe Walk Volunteer</h4>
        <p>Accompany individuals who need to walk through areas where they feel unsafe.</p>
        <p><strong>Commitment:</strong> Flexible scheduling</p>
        <p><strong>Training:</strong> 8-hour program provided</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Apply
        </button>
    </div>
    """, unsafe_allow_html=True)

# Download resources
st.subheader("Downloadable Resources")

download_col1, download_col2 = st.columns(2)

with download_col1:
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Personal Safety Plan Template</h4>
        <p>A comprehensive template to help you create your own safety plan.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Download PDF
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Emergency Contact Card</h4>
        <p>Printable card to keep important emergency numbers with you at all times.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Download PDF
        </button>
    </div>
    """, unsafe_allow_html=True)

with download_col2:
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Safety Assessment Checklist</h4>
        <p>Evaluate the safety of your home, workplace, and daily routines.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Download PDF
        </button>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="resource-card">
        <h4 style="margin-top: 0;">Legal Rights Guide</h4>
        <p>Information about your legal rights related to safety, harassment, and protection.</p>
        <button style="background-color: var(--primary); color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.25rem; cursor: pointer;">
            Download PDF
        </button>
    </div>
    """, unsafe_allow_html=True)

# Feedback form
st.subheader("Suggest a Resource")

with st.form("suggest_resource_form"):
    st.markdown("Help us improve by suggesting resources that would be valuable to the community.")
    
    resource_name = st.text_input("Resource Name")
    resource_type = st.selectbox(
        "Resource Type",
        ["Organization", "Service", "Educational Content", "Tool/App", "Community Initiative", "Other"]
    )
    resource_description = st.text_area("Description", placeholder="Please describe this resource and why it would be helpful...")
    resource_contact = st.text_input("Contact Information (optional)", placeholder="Website, phone, or email")
    
    submit_resource = st.form_submit_button("Submit Suggestion")
    
    if submit_resource:
        if not resource_name or not resource_description:
            st.error("Please provide both a name and description for the resource.")
        else:
            st.success("Thank you for your suggestion! Our team will review it and consider adding it to our resources.")