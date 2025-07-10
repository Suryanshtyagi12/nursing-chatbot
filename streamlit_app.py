import streamlit as st

# Streamlit Page Setup
st.set_page_config(page_title="🧑‍⚕️ Nursing Admission Assistant", page_icon="🩺")
st.markdown("""
    <style>
    .main {
        background-color: #e6f2ff;
        color: #0d1b2a;
    }
    .stChatMessage {
        background-color: #1e1e1e;
        color: yellow;
        padding: 12px;
        border-radius: 12px;
        margin-bottom: 8px;
        border: 1px solid #dddddd;
    }
    .stTextInput > label {
        font-weight: bold;
        color: #0d1b2a;
    }
    .css-1cpxqw2, .css-ffhzg2 {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='text-align: center; color: #003366;'>🩺 Nursing College Admission Assistant</h1>
<p style='text-align: center;'>Aapka AI Dost – Jo Nursing Admission ke har kadam mein aapki madad karega 💬</p>
<hr>
<p><b>Start by answering the question below (e.g., Haan, Nahi, Kya?) ya aap direct koi sawal bhi puchh sakte hain:</b></p>
<ul>
<li>"Fees kitni hai?"</li>
<li>"Scholarship milti hai kya?"</li>
<li>"Hostel facility hai?"</li>
<li>"Training kahan hoti hai?"</li>
</ul>
""", unsafe_allow_html=True)

# Keywords
positive_keywords = [
    "haan", "yes", "batao", "bataye", "ok", "okay", "start", "continue", "sure", "ji", "chalu", "h", "b", "tell", "poori", "details", "acha", "sahi",
    "theek hai", "ready", "next", "karna hai", "admission", "interested"
]
negative_keywords = [
    "nahi", "no", "stop", "exit", "cancel", "not interested", "leave", "band", "baad mein", "chod do", "nopes", "abhi nahi", "reject"
]
doubt_keywords = [
    "kya", "matlab", "confuse", "help", "repeat", "doubt", "issue", "samajh", "explain", "meaning", "dubara", "kaise", "clarify"
]

# Intent detection
def detect_intent(text):
    text = text.lower()
    if any(k in text for k in negative_keywords):
        return "negative"
    elif any(k in text for k in doubt_keywords):
        return "doubt"
    else:
        return "positive"

# Chat state
if "step" not in st.session_state:
    st.session_state.step = 0
if "messages" not in st.session_state:
    st.session_state.messages = []

# Question Chain
questions = [
    "Kya aap nursing college mein admission lena chahte hain?",
    "Great! Aapne 12th mein Biology liya tha kya?",
    "Perfect! Yeh B.Sc Nursing course full-time 4 saal ka hota hai. Aur detail chahiye?",
    "Fees ₹70,000 per year hoti hai: ₹60,000 tuition + ₹10,000 bus. Teen installment mein dena hota hai. Bataun kaise?",
    "Hostel mein 24x7 water, electricity, CCTV aur warden ki facility hai. Aur jaankari chahiye?",
    "College Delhi mein hai. Location aur aaspaas ke area ke baare mein jaankari chahiye?",
    "College Indian Nursing Council (INC) se recognize hai. Aur bataun?",
    "Clinical training Backundpur, Chartha aur Ranchi hospitals mein hoti hai. Puchhna chahenge details?",
    "Scholarship bhi milti hai ₹18k–48k tak (Govt & Labour Reg.). Aap eligible ho sakte hain! Puchhna chahenge eligibility?",
    "Total 60 seats hain. Eligibility: Biology in 12th, PNT exam pass, age 17–35. Apply karna chahenge?"
]

# Chat input
user_input = st.chat_input("Apna sawal ya jawab likhiye...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    intent = detect_intent(user_input)

    if intent == "negative":
        response = "Thik hai! Agar baad mein zarurat ho toh zaroor batana 😊"
    elif intent == "doubt":
        response = "Koi baat nahi! Main aapko simple shabdon mein fir se samjhata hoon: " + questions[st.session_state.step]
    else:
        if st.session_state.step < len(questions):
            response = questions[st.session_state.step]
            st.session_state.step += 1
        else:
            response = "Yeh thi sari jaankari! Agar kuch aur puchhna hai toh poochhiye. 🤓"

    st.session_state.messages.append({"role": "assistant", "content": response})

# Display conversation
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
