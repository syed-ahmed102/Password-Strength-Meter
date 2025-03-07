import streamlit as st
import re
from passlib.context import CryptContext

# Configure password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Custom CSS for styling the strength meter
st.markdown(
    """
    <style>
        .weak { background-color: #ff4d4d; color: white; padding: 5px; border-radius: 5px; }
        .medium { background-color: #ffa500; color: white; padding: 5px; border-radius: 5px; }
        .strong { background-color: #4caf50; color: white; padding: 5px; border-radius: 5px; }
    </style>
    """,
    unsafe_allow_html=True
)

def check_strength(password):
    """Check password strength based on length & complexity."""
    if len(password) < 6:
        return "Weak", "weak"
    elif re.search(r"\d", password) and re.search(r"[A-Z]", password) and len(password) >= 8:
        return "Strong", "strong"
    elif len(password) >= 6:
        return "Medium", "medium"
    return "Weak", "weak"

st.title("🔐 Password Strength Meter")

password = st.text_input("Enter Password", type="password")

if password:
    strength, css_class = check_strength(password)
    st.markdown(f'<p class="{css_class}">Strength: {strength}</p>', unsafe_allow_html=True)
