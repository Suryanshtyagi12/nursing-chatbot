import streamlit as st

# Page setup
st.set_page_config(page_title="🧑‍⚕️ Nursing Admission Assistant", page_icon="🩺")

# Custom CSS for better visibility
st.markdown("""
    <style>
    .main {
        background-color: #f6f6f6;
        color: #1c1c1c;
    }
    .stChatMessage.user {
        background-color: #dceeff;
        color: black;
        border-radius: 12px;
        padding: 12px;
    }
    .stChatMessage.assistant {
        background-color: #e0ffe0;
        color: black;
        border-radius: 12px;
        padding: 12px;
    }
    .stTextInput > label {
        font-weight: bold;
        color: #333333;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1 style='text-align: center; color:#1c1c1c;'>🩺 Nursing College Admission Assistant</h1>
<p style='text-align: center; font-size:18px;'>Hello! 😊 Kya aap Nursing College mein admission lena chahte hain?</p>
<hr>
""", unsafe_allow_html=True)

# Chat state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Keywords
negative_keywords = ["nahi", "no", "stop", "exit", "cancel", "leave", "baad mein", "chod do"]
positive_keywords = ["haan", "yes", "start", "ok", "batao", "bataye", "sure", "continue", "chalo"]
doubt_keywords = ["kya", "matlab", "confuse", "dubara", "repeat", "problem", "samajh", "meaning", "clarify"]
fees_keywords = ["fees", "kitna", "charge"]
hostel_keywords = ["hostel", "room", "stay"]
scholarship_keywords = ["scholarship", "chhatravritti", "labour", "govt"]
eligibility_keywords = ["eligible", "eligibility", "criteria", "qualification"]
location_keywords = ["location", "kaha", "delhi", "college"]
training_keywords = ["training", "hospital", "practical", "internship"]

# Response logic
def get_response(user_input):
    user_input = user_input.lower()

    if any(k in user_input for k in negative_keywords):
        return "Thik hai! Agar baad mein admission ya info chahiye ho, toh bina jhijhak poochhna 😊 Best wishes!"

    elif any(k in user_input for k in positive_keywords):
        return "Shandar! 😄 Chaliye aapka eligibility check karte hain. Kya aapne 12th mein Biology liya tha?"

    elif any(k in user_input for k in ["biology", "bio"]):
        return """✅ Great! Aap eligible ho agar:
• 12th with Biology  
• PNT Exam pass  
• Age 17–35 years  
Aapko program, fees ya hostel ke baare mein jaan’na hai?"""

    elif any(k in user_input for k in fees_keywords):
        return """💸 **Fees ka breakdown**:
• Tuition – ₹60,000  
• Bus – ₹10,000  
• **Total**: ₹70,000/year  
Installments:
1️⃣ ₹30,000 (admission)  
2️⃣ ₹20,000 (after Sem 1)  
3️⃣ ₹20,000 (after Sem 2)  
Aasaan tareeke se 3 parts mein pay kar sakte ho 😊"""

    elif any(k in user_input for k in hostel_keywords):
        return """🏠 **Hostel Facilities**:
• Neat & clean rooms  
• 24x7 water + electricity ⚡  
• CCTV security + Lady warden  
• Separate hostel for girls & boys  
Ghar jaisa safe environment milega 😇"""

    elif any(k in user_input for k in scholarship_keywords):
        return """🎁 **Scholarships Available**:
• Govt: ₹18,000 to ₹23,000/year  
• Labour Reg: ₹40,000 to ₹48,000/year  
Aap eligible ho toh kaafi kam fees lagegi! 🤝"""

    elif any(k in user_input for k in eligibility_keywords):
        return """✅ **Eligibility Criteria**:
• 12th (Science) with Biology  
• PNT Entrance Exam cleared  
• Age 17 to 35 years  
Aap eligible ho toh apply zaroor kariye 😊"""

    elif any(k in user_input for k in location_keywords):
        return """📍 **College Location**:
College is in Delhi – easily reachable by bus & metro  
Nearby hospitals for practical training  
Safe and central location 🚍"""

    elif any(k in user_input for k in training_keywords):
        return """🏥 **Hospital Training**:
Real practical training milegi in top hospitals:  
• Backundpur  
• Chartha  
• Ranchi  
Yeh training aapko professional bana degi 💉"""

    elif any(k in user_input for k in doubt_keywords):
        return """Koi stress nahi! Main aapko simple aur easy words mein samjhata hoon 👇
🎓 Course: B.Sc Nursing (4 years)  
✅ Eligibility: 12th with Biology + PNT exam pass + Age 17–35  
💸 Fees: ₹70,000/year  
🏠 Hostel: Safe & comfortable  
🧾 Scholarships: ₹18k–₹48k  
Aap aur kya jaanna chahenge? 😊"""

    else:
        return """Yeh raha aapke liye admission ka full info – ekdum simple aur clear way mein 👇
🎓 **Course**: B.Sc Nursing (4 years, full-time)  
✅ **Eligibility**: 12th with Biology + PNT pass + Age 17–35  
💸 **Fees**: ₹70k/year (₹60k tuition + ₹10k bus)  
🏠 **Hostel**: 24x7 water, light, CCTV, warden  
📍 **Location**: Delhi  
🏥 **Training**: Chartha, Ranchi, Backundpur  
🧾 **Scholarship**: ₹18k–₹48k  
📊 **Seats**: 60  
✅ Approved by INC (Delhi)
Aap kis topic ke baare mein poochhna chahenge? 😊"""

# Input and response
user_input = st.chat_input("Aapka sawal yahan likhiye...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
