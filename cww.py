import streamlit as st
import resend


# Load your API key
resend.api_key = st.secrets["resend"]["api_key"]

# --- CSS for navbar ---
st.markdown("""
<style>
/* Make the navbar sticky */
.sticky-nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 999;
    background-color: white;
    padding: 10px 20px;
    border-bottom: 1px solid #ddd;
    display: flex;
    justify-content: left;
    gap: 40px;
    font-size: 24px;
    font-weight: bold;
}

/* Add padding to the main content */
.main .block-container {
    padding-top: 80px !important;
}

/* Navbar link styles */
.sticky-nav a {
    color: black;
    text-decoration: none;
}

.sticky-nav a:hover {
    text-decoration: underline;
}

/* Hide the default Streamlit header */
header[data-testid="stHeader"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# --- Navbar ---
st.markdown(
    """
    <div class="sticky-nav">
        <a href="https://betteranoopsshop.streamlit.app/" target="_blank">Shop</a>
    </div>
    """,
    unsafe_allow_html=True
)

st.image("image (6).png")
st.title("Carrie Wang")
st.write("Born in Taipei, shaped in Los Angeles — a city girl at heart. I connect ideas, people, and execution. I thrive in client-facing, fast-paced environments, that’s why I know how to keep both customers and vendors happy. I blend creative thinking with solution-oriented approaches, and even under high pressure, still am a happy team player.")
st.write("“For those who change fields every 3-4 years, they’re more likely to learn quickly in a short period of time. Because they constantly push themselves out of their comfort zone and must acquire new skills within a limited timeframe, they usually develop a steeper learning curve and achieve better work efficiency.” — Patty McCord (Former Netflix CTO)")
st.markdown("")
st.markdown("")

if "name" not in st.session_state:
    st.session_state.name = ""
if "email" not in st.session_state:
    st.session_state.email = ""
if "subject" not in st.session_state:
    st.session_state.subject = ""
if "message" not in st.session_state:
    st.session_state.message = ""


st.header("Contact")
st.subheader("Let's Connect")
name = st.text_input("Name", key="name")
email = st.text_input("Email", key="email")
subject = st.text_input("Subject", key="subject")
message = st.text_area("Message", key="message")





if st.button("Send Message"):
    if not name or not email or not message:
        st.warning("Please fill out all fields.")
    else:
        try:
            # Build the email
            params = {
                "from": "onboarding@resend.dev",
                "to":"hudsonk21r3@gmail.com",
                "subject": subject,
                "html": email + ": " + message
                }
            resend.Emails.send(params)
            st.success("✅ Email sent successfully!")
            name = ""

        except Exception as e:
            st.error(f"❌ Failed to send email: {e}")



st.markdown("")
st.markdown("""
<style>
.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    margin-top: 200px; /* pushes toward bottom if page is short */
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 6px; /* spacing between elements */
    padding: 10px 0;
    font-size: 16px;
    color: black;
}

.footer a {
    text-decoration: underline;
    color: black;
    font-weight: 500;
    transition: opacity 0.2s ease;
}

.footer a:hover {
    opacity: 0.6;
}

.footer span {
    color: black;
}

.footer .title {
    font-weight: 700;
    font-size: 20px; /* subheader size */
}
</style>

<div class="footer">
    <span class="title">BetteranOops than a whatIF&nbsp;&nbsp;&nbsp;</span>
    <a href="https://www.linkedin.com/in/carrie-w-77997484/" target="_blank">LinkedIn</a>
    <span>/</span>
    <a href="https://www.instagram.com/carrrieon/" target="_blank">Instagram</a>
    <span>&nbsp;&nbsp;Designed with Curiosity</span>
</div>
""", unsafe_allow_html=True)
