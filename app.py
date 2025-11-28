import random

import streamlit as st
from pandas import DataFrame

from data import CITY_DATA
from utils_pdf import build_itinerary_pdf

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------
st.set_page_config(
    page_title="TripWeave – Premium Micro-SaaS",
    page_icon="🧭",
    layout="wide",
)

# ----------------------------------------------------------
# NAV STATE
# ----------------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"


def go(page_name: str):
    st.session_state.page = page_name


page = st.session_state.page

# ----------------------------------------------------------
# DARK THEME CSS
# ----------------------------------------------------------
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* App background */
.stApp {
    background: radial-gradient(circle at top, #020617 0%, #020617 55%, #020617 100%);
}

/* Streamlit top header */
[data-testid="stHeader"] {
    background: #020617 !important;
}
[data-testid="stHeader"] * {
    color: #e5e7eb !important;
}

/* Typography defaults */
h1, h2, h3, h4, h5, h6, p, li, label, span {
    color: #e5e7eb;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: #020617 !important;
}
[data-testid="stSidebar"] * {
    color: #e5e7eb !important;
}

/* Sidebar inputs */
[data-testid="stSidebar"] input,
[data-testid="stSidebar"] textarea {
    background: #f9fafb !important;
    color: #111827 !important;
    border-radius: 10px !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div {
    background: #f9fafb !important;
    border-radius: 10px !important;
}
[data-testid="stSidebar"] .stSelectbox > div > div * {
    color: #111827 !important;
}

/* Sliders text */
[data-testid="stSidebar"] [data-baseweb="slider"] div {
    color: #e5e7eb !important;
}

/* Checkboxes text */
[data-testid="stSidebar"] [data-baseweb="checkbox"] * {
    color: #e5e7eb !important;
}

/* Glass card */
.glass {
    background: rgba(15,23,42,0.96);
    border-radius: 20px;
    padding: 24px 28px;
    border: 1px solid rgba(148,163,184,0.55);
    box-shadow: 0 18px 40px rgba(15,23,42,0.95);
}

/* Hero */
.hero {
    text-align: center;
    padding: 50px 24px 32px 24px;
}
.hero-title {
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(90deg,#38bdf8,#6366f1,#a855f7,#ec4899,#f59e0b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-subtitle {
    font-size: 18px;
    color: #cbd5e1 !important;
}

/* Section heading */
.section-heading {
    font-size: 22px;
    font-weight: 700;
    color: #f9fafb;
    margin-bottom: 0.7rem;
    border-bottom: 2px solid rgba(96,165,250,0.7);
    display: inline-block;
    padding-bottom: 4px;
}

/* Card titles */
.card-title {
    font-size: 24px;
    font-weight: 800;
    background: linear-gradient(90deg,#38bdf8,#6366f1,#a855f7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem;
}

/* Top nav buttons */
.nav-btn > button {
    width: 100%;
    border-radius: 999px;
    background: radial-gradient(circle at top left,#38bdf8,#1d4ed8);
    color: #e5e7eb;
    border: 1px solid rgba(148,163,184,0.7);
    font-weight: 600;
    padding: 0.55rem 0.9rem;
    font-size: 14px;
    box-shadow: 0 0 20px rgba(56,189,248,0.6);
}
.nav-btn > button:hover {
    background: radial-gradient(circle at top left,#60a5fa,#6366f1);
    color: white;
    transform: translateY(-1px);
}

/* Primary buttons */
.stButton > button {
    border-radius: 999px;
    background: linear-gradient(90deg,#38bdf8,#6366f1);
    color: white;
    padding: 0.7rem 1.8rem;
    font-weight: 700;
    border: none;
    box-shadow: 0 12px 30px rgba(37,99,235,0.55);
}
.stButton > button:hover {
    filter: brightness(1.08);
    transform: translateY(-2px) scale(1.01);
}

/* Download buttons */
.stDownloadButton > button {
    border-radius: 999px;
    background: linear-gradient(90deg,#3b82f6,#8b5cf6);
    color: white;
    padding: 0.6rem 1.6rem;
    font-weight: 700;
    border: none;
    box-shadow: 0 10px 26px rgba(59,130,246,0.6);
}
.stDownloadButton > button:hover {
    filter: brightness(1.08);
    transform: translateY(-1px);
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    background: rgba(15,23,42,0.96);
    border-radius: 20px;
    border: 1px solid rgba(148,163,184,0.55);
    box-shadow: 0 18px 40px rgba(15,23,42,0.95);
    padding: 10px;
}
thead th {
    color: #e5e7eb !important;
    background: #020617 !important;
}
tbody td {
    color: #e5e7eb !important;
}

/* Expander header */
.streamlit-expanderHeader {
    background-color: #0f172a !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
    border: 1px solid #334155 !important;
}

/* HTML details/summary fix */
details > summary {
    background-color: #0f172a !important;
    color: #e2e8f0 !important;
    border-radius: 10px !important;
    padding: 10px !important;
    border: 1px solid #334155 !important;
}
details[open] > summary {
    background-color: #1e293b !important;
}

/* Expander content */
.streamlit-expanderContent {
    background-color: #020617 !important;
    padding: 15px !important;
    border-radius: 12px !important;
}

/* Footer */
.footer {
    text-align: center;
    color: #9ca3af;
    padding: 28px 0 10px 0;
    margin-top: 32px;
    font-size: 13px;
    border-top: 1px solid rgba(55,65,81,0.9);
}
</style>
""",
    unsafe_allow_html=True,
)


# ----------------------------------------------------------
# TOP NAVIGATION ROW
# ----------------------------------------------------------
nav_cols = st.columns(4)
with nav_cols[0]:
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("🏠 Home", key="nav_home"):
        go("home")
    st.markdown("</div>", unsafe_allow_html=True)

with nav_cols[1]:
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("🧭 Trip Planner", key="nav_planner"):
        go("planner")
    st.markdown("</div>", unsafe_allow_html=True)

with nav_cols[2]:
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("💰 Pricing", key="nav_pricing"):
        go("pricing")
    st.markdown("</div>", unsafe_allow_html=True)

with nav_cols[3]:
    st.markdown('<div class="nav-btn">', unsafe_allow_html=True)
    if st.button("⭐ Testimonials", key="nav_testimonials"):
        go("testimonials")
    st.markdown("</div>", unsafe_allow_html=True)

page = st.session_state.page

# ----------------------------------------------------------
# HOME PAGE
# ----------------------------------------------------------
if page == "home":
    st.markdown(
        """
        <div class="hero">
            <div class="glass">
                <div class="hero-title">Plan Trips Smarter.</div>
                <p class="hero-subtitle">
                    TripWeave is a Micro-SaaS that builds realistic, energy-aware itineraries using your mood,
                    weather, budget, interests and real locations.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-heading">Why TripWeave?</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">⚡ TECE Engine</div>
                <p>Traveler Energy Curve Engine adapts your plan to morning, afternoon and evening energy levels.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">🌦 Weather-Smart</div>
                <p>Switches between indoor and outdoor options based on expected weather.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">📍 Real Locations</div>
                <p>Curated place lists for Bangalore, Hyderabad, Goa, Delhi, Mumbai and Chennai with Google Maps links.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    st.button("🚀 Start Planning", on_click=lambda: go("planner"))
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# PRICING PAGE
# ----------------------------------------------------------
elif page == "pricing":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">Pricing</div>
            <p class="hero-subtitle">
                Simple tiers for solo travelers, power users and teams. Pro unlocks more cities, deeper TECE tuning
                and agency features.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="glass" style="text-align:center;">
                <div class="card-title">Starter</div>
                <h3 style="color:#f9fafb;">₹0 / month</h3>
                <p>Up to 3 trips / month<br>TECE basic<br>6 curated cities</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="glass" style="text-align:center;">
                <div class="card-title">Pro</div>
                <h3 style="color:#f9fafb;">₹199 / month</h3>
                <p>Unlimited trips<br>Advanced TECE tuning<br>More cities & presets<br>PDF + export tools</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="glass" style="text-align:center;">
                <div class="card-title">Teams</div>
                <h3 style="color:#f9fafb;">₹499 / month</h3>
                <p>Workspaces for agencies<br>White-label branding<br>Priority support</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------
# TESTIMONIALS PAGE
# ----------------------------------------------------------
elif page == "testimonials":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">What users say</div>
            <p class="hero-subtitle">Early adopters of TripWeave.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">“Feels like a human planner.”</div>
                <p>My Bangalore weekend felt natural – forts in the morning, cafés when I was tired.</p>
                <p><b>- Priya, Student</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">“UI looks like a real startup.”</div>
                <p>Not a typical college project – I’d actually pay for this.</p>
                <p><b>- Akash, Developer</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">“Zero planning anxiety.”</div>
                <p>I just put my city, days and energy – TripWeave balanced everything automatically.</p>
                <p><b>- Sarah, Marketer</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">“Authentic Hyderabad experience!”</div>
                <p>Visited Secunderabad and Niloufer Cafe. Tried Irani chai and biscuits – TripWeave helped me plan it all.</p>
                <p><b>- Manthan Gupta</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------
# TRIP PLANNER PAGE
# ----------------------------------------------------------
elif page == "planner":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">Trip Planner</div>
            <p class="hero-subtitle">Powered by TECE – Traveler Energy Curve Engine.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------- SIDEBAR ----------
    with st.sidebar:
        st.markdown("## Trip Settings")
        destination = st.selectbox(
            "Choose your destination  ✨ Unlock more cities with Pro plan ✨",
            ["Bangalore", "Hyderabad", "Goa", "Delhi", "Mumbai", "Chennai"],
        )
        trip_days = st.slider("Trip length (days)", 1, 7, 2)
        total_budget = st.number_input("Total budget (₹)", 0, value=6000, step=500)
        travel_style = st.selectbox("Travel style", ["Saver", "Balanced", "Premium"])

        st.markdown("### Activities per day")
        activities_per_day = st.slider("How many activities per day?", 3, 6, 3)

        st.markdown("### Energy Curve (TECE)")
        energy_morning = st.select_slider(
            "Morning energy", ["Low", "Medium", "High"], "High"
        )
        energy_afternoon = st.select_slider(
            "Afternoon energy", ["Low", "Medium", "High"], "Medium"
        )
        energy_evening = st.select_slider(
            "Evening energy", ["Low", "Medium", "High"], "Medium"
        )

        st.markdown("### Interests")
        interest_culture = st.checkbox("Culture & Landmarks", True)
        interest_nature = st.checkbox("Nature / Parks / Beaches", True)
        interest_food = st.checkbox("Food & Cafes", True)
        interest_shopping = st.checkbox("Shopping & Bazaars", False)

        weather_pref = st.selectbox(
            "Weather context",
            ["Mixed / Don't know", "Mostly Sunny", "Mostly Rainy"],
        )

        generate = st.button("✨ Generate TECE Plan", use_container_width=True)

    # ---------- BACKEND HELPERS ----------
    def allowed_tags():
        tags = []
        if interest_culture:
            tags.append("Culture")
        if interest_nature:
            tags.append("Nature")
        if interest_food:
            tags.append("Food")
        if interest_shopping:
            tags.append("Shopping")
        return tags or ["Culture", "Nature", "Food"]

    def get_city_activities(city: str):
        return CITY_DATA.get(city.strip().lower(), [])

    chosen_today = {}  # day -> set of used place names

    def build_time_slots(n: int):
        if n == 3:
            return [
                ("Morning", energy_morning),
                ("Afternoon", energy_afternoon),
                ("Evening", energy_evening),
            ]
        elif n == 4:
            return [
                ("Early Morning", energy_morning),
                ("Late Morning", energy_morning),
                ("Afternoon", energy_afternoon),
                ("Evening", energy_evening),
            ]
        elif n == 5:
            return [
                ("Early Morning", energy_morning),
                ("Late Morning", energy_morning),
                ("Afternoon", energy_afternoon),
                ("Evening", energy_evening),
                ("Night", energy_evening),
            ]
        else:  # 6
            return [
                ("Early Morning", energy_morning),
                ("Morning", energy_morning),
                ("Noon", energy_afternoon),
                ("Afternoon", energy_afternoon),
                ("Evening", energy_evening),
                ("Night", energy_evening),
            ]

    def pick_activity(day, energy, time_of_day, activities):
        tags = allowed_tags()
        indoor_needed = (weather_pref == "Mostly Rainy") and time_of_day in [
            "Early Morning", "Morning", "Late Morning", "Noon", "Afternoon",
        ]

        # Filter by tags + weather
        filtered = [
            a
            for a in activities
            if a["tag"] in tags and (not indoor_needed or a["indoor"])
        ]
        if not filtered:
            filtered = list(activities)

        # Avoid repeating the same place in a single day
        used = chosen_today.get(day, set())
        filtered = [a for a in filtered if a["name"] not in used] or filtered

        # TECE intensity matching
        if energy == "High":
            energy_filtered = [
                a for a in filtered if a["intensity"] in ["High", "Medium"]
            ]
        elif energy == "Medium":
            energy_filtered = [
                a for a in filtered if a["intensity"] in ["Medium", "Low"]
            ]
        else:  # Low
            energy_filtered = [a for a in filtered if a["intensity"] == "Low"]

        if not energy_filtered:
            energy_filtered = filtered

        act = random.choice(energy_filtered)
        chosen_today.setdefault(day, set()).add(act["name"])
        return act

    def cost_multiplier():
        return {"Saver": 0.8, "Balanced": 1.0, "Premium": 1.4}[travel_style]

    def build_itinerary():
        acts = get_city_activities(destination)
        result = []
        mult = cost_multiplier()
        per_day = total_budget / trip_days if trip_days else 0
        slots = build_time_slots(activities_per_day)

        for day in range(1, trip_days + 1):
            chosen_today[day] = set()
            for time_label, energy in slots:
                act = pick_activity(day, energy, time_label, acts)

                final_cost = int(act["base_cost"] * mult)

                result.append(
                    {
                        "Day": day,
                        "Time": time_label,
                        "Energy": energy,
                        "Activity": act["name"],
                        "Category": act["tag"],
                        "Indoor / Outdoor": "Indoor" if act["indoor"] else "Outdoor",
                        "Estimated Cost (₹)": final_cost,
                        "Rating": act.get("rating", 4.5),
                        "Maps Link": act["map"],
                    }
                )

        return result, per_day

    # ---------- SUMMARY CARDS ----------
    c1, c2, c3 = st.columns([2, 1.5, 1.5])

    dataset_badge = (
        "<span style='display:inline-block;padding:4px 10px;border-radius:999px;"
        "background:#064e3b;color:#bbf7d0;font-size:12px;'>"
        "Real city dataset – using actual popular spots."
        "</span>"
        if destination.strip().lower() in CITY_DATA
        else "<span style='display:inline-block;padding:4px 10px;border-radius:999px;"
        "background:#7f1d1d;color:#fecaca;font-size:12px;'>"
        "Generic suggestions – dataset not yet curated."
        "</span>"
    )

    with c1:
        snapshot_html = f"""
        <div class="glass">
            <div class="card-title">📍 Trip Snapshot</div>
            <p><b>Destination:</b> {destination}</p>
            <p><b>Duration:</b> {trip_days} day(s)</p>
            <p><b>Budget:</b> ₹{total_budget}</p>
            <p><b>Style:</b> {travel_style}</p>
            <p><b>Activities/day:</b> {activities_per_day}</p>
            <p style="margin-top:8px;">{dataset_badge}</p>
        </div>
        """
        st.markdown(snapshot_html, unsafe_allow_html=True)

    with c2:
        tece_html = f"""
        <div class="glass">
            <div class="card-title">🔋 TECE Energy Curve</div>
            <p><b>Morning:</b> {energy_morning}</p>
            <p><b>Afternoon:</b> {energy_afternoon}</p>
            <p><b>Evening:</b> {energy_evening}</p>
            <p style="font-size:13px;margin-top:8px;">
                High energy → forts, walks, markets. Low energy → cafés, lakes, viewpoints.
            </p>
        </div>
        """
        st.markdown(tece_html, unsafe_allow_html=True)

    with c3:
        ctx_html = f"""
        <div class="glass">
            <div class="card-title">🌦️ Context & Interests</div>
            <p><b>Weather:</b> {weather_pref}</p>
            <p><b>Interests:</b> {', '.join(allowed_tags())}</p>
            <p style="font-size:13px;margin-top:8px;">
                Rainy weather prefers indoor activities especially in mornings and afternoons.
            </p>
        </div>
        """
        st.markdown(ctx_html, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- ITINERARY + MAPS + DOWNLOAD ----------
    if generate:
        schedule, per_day_budget = build_itinerary()
        df = DataFrame(schedule)

        # Main itinerary table
        st.markdown(
            '<div class="card-title">📅 TECE-Powered Itinerary</div>',
            unsafe_allow_html=True,
        )
        st.write(f"Estimated spend per day: **₹{int(per_day_budget)}**")

        df_display = df[
            [
                "Day",
                "Time",
                "Energy",
                "Activity",
                "Category",
                "Indoor / Outdoor",
                "Estimated Cost (₹)",
                "Rating",
            ]
        ]

        st.dataframe(df_display, use_container_width=True, height=350)

        st.markdown("<br>", unsafe_allow_html=True)

        # Google Maps links card
        items = []
        for _, row in df.iterrows():
            items.append(
                f"<li><b>Day {row['Day']} – {row['Time']} – {row['Activity']}</b> "
                f"(⭐ {row['Rating']}/5) → "
                f"<a href='{row['Maps Link']}' target='_blank'>Open Maps</a></li>"
            )
        links_html = (
            "<div class='glass'>"
            "<div class='card-title'>📍 Open in Google Maps</div>"
            "<ul>"
            + "".join(items)
            + "</ul></div>"
        )
        st.markdown(links_html, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- DAY-WISE HIGHLIGHTS (NO IMAGES) ----------
        st.markdown(
            "<div class='card-title'>✨ Day-wise Highlights</div>",
            unsafe_allow_html=True,
        )

        CATEGORY_ICON = {
            "Nature": "🌳",
            "Culture": "🏛️",
            "Food": "🍽️",
            "Shopping": "🛍️",
        }

        for day in sorted(df["Day"].unique()):
            with st.expander(f"Day {day} – Highlights"):
                day_df = df[df["Day"] == day].reset_index(drop=True)
                cols = st.columns(2)
                for idx, row in day_df.iterrows():
                    col = cols[idx % 2]
                    with col:
                        cat = row["Category"]
                        cat_icon = CATEGORY_ICON.get(cat, "📍")
                        io_icon = "🏠" if row["Indoor / Outdoor"] == "Indoor" else "🌤️"

                        st.markdown(
                            f"**{row['Time']} – {row['Activity']}**  \n"
                            f"{cat_icon} {cat} • {io_icon} {row['Indoor / Outdoor']}  \n"
                            f"💰 ₹{row['Estimated Cost (₹)']} • ⭐ {row['Rating']}/5"
                        )

        st.markdown("<br>", unsafe_allow_html=True)

        # ---------- TXT EXPORT ----------
        txt = ""
        txt += "==============================\n"
        txt += "   TRIPWEAVE – YOUR ITINERARY\n"
        txt += "==============================\n\n"
        txt += f"Destination: {destination}\n"
        txt += f"Days: {trip_days}\n"
        txt += f"Travel Style: {travel_style}\n"
        txt += f"Activities per day: {activities_per_day}\n"
        txt += f"Daily Budget Estimate: ₹{int(per_day_budget)}\n"
        txt += f"Weather Context: {weather_pref}\n"
        txt += (
            f"Energy Curve: Morning-{energy_morning} • "
            f"Afternoon-{energy_afternoon} • Evening-{energy_evening}\n\n"
        )

        day_counts = {}
        for row in schedule:
            d = row["Day"]
            day_counts[d] = day_counts.get(d, 0) + 1

        current_day = None
        for row in schedule:
            d = row["Day"]
            if d != current_day:
                if current_day is not None:
                    txt += "\n"
                current_day = d
                total_for_day = day_counts[d]
                txt += "------------------------------------\n"
                txt += f"DAY {d} – (Total Planned Activities: {total_for_day})\n"
                txt += "------------------------------------\n\n"

            icon = (
                "🌅"
                if "Morning" in row["Time"]
                else "🌤"
                if row["Time"] in ["Noon", "Afternoon"]
                else "🌙"
            )

            txt += f"{icon} {row['Time']} – {row['Energy']} Energy\n"
            txt += f"• Activity: {row['Activity']}\n"
            txt += f"• Category: {row['Category']}\n"
            txt += f"• Indoor/Outdoor: {row['Indoor / Outdoor']}\n"
            txt += f"• Estimated Cost: ₹{row['Estimated Cost (₹)']}\n"
            txt += f"• Rating: {row['Rating']}/5\n"
            txt += f"• Maps: {row['Maps Link']}\n\n"

        txt += "==========================\n"
        txt += "   END OF YOUR ITINERARY\n"
        txt += "==========================\n"
        txt += "Powered by TripWeave – Micro-SaaS Travel Planner\n"

        # Build PDF
        pdf_bytes = build_itinerary_pdf(
            schedule=schedule,
            destination=destination,
            trip_days=trip_days,
            travel_style=travel_style,
            per_day_budget=per_day_budget,
            weather_pref=weather_pref,
            energy_morning=energy_morning,
            energy_afternoon=energy_afternoon,
            energy_evening=energy_evening,
        )

        # Download section
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">📥 Download Itinerary</div>
                <p>Export your TECE-generated plan as a text file or a branded PDF.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        col_txt, col_pdf = st.columns(2)
        with col_txt:
            st.download_button(
                "Download itinerary (.txt)",
                txt,
                file_name="tripweave_itinerary.txt",
                mime="text/plain",
                key="download_itinerary_txt_btn",
            )
        with col_pdf:
            st.download_button(
                "Download itinerary (.pdf)",
                pdf_bytes,
                file_name="tripweave_itinerary.pdf",
                mime="application/pdf",
                key="download_itinerary_pdf_btn",
            )

    else:
        st.markdown(
            """
            <div class="glass">
                <div class="card-title">👋 Ready when you are</div>
                <p>Configure your trip in the sidebar and click <b>“✨ Generate TECE Plan”</b> to see your itinerary.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ----------------------------------------------------------
# FOOTER (all pages)
# ----------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        TripWeave · Micro-SaaS Travel Planner · Built as a founding-tech assignment demo.
    </div>
    """,
    unsafe_allow_html=True,
)
