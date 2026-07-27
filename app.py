import streamlit as st
from src.agent import ask_agent

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="🌦️ Weather AI Assistant",
    page_icon="🌤️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background: linear-gradient(180deg,#0f172a,#1e293b,#334155);
    color:white;
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:white;
    margin-bottom:5px;
}

.sub-title{
    text-align:center;
    color:#cbd5e1;
    margin-bottom:25px;
}

.chat-container{
    max-width:850px;
    margin:auto;
}

.user-msg{
    background:#2563eb;
    color:white;
    padding:14px;
    border-radius:15px 15px 0px 15px;
    margin:12px 0;
    width:fit-content;
    max-width:80%;
    margin-left:auto;
    font-size:17px;
}

.bot-msg{
    background:#1e293b;
    color:white;
    padding:14px;
    border-radius:15px 15px 15px 0px;
    margin:12px 0;
    width:fit-content;
    max-width:80%;
    border:1px solid #475569;
    font-size:17px;
}

.stChatInput input{
    color:white !important;
    background:#1e293b !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<div class='main-title'>🌦️ Weather AI Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Ask me about the weather anywhere in the world.</div>", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT ----------------
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:

    if msg["role"] == "user":
        st.markdown(
            f"<div class='user-msg'>👤 {msg['content']}</div>",
            unsafe_allow_html=True
        )

    else:
        formatted_response = msg["content"].replace("\n", "<br>")

        st.markdown(
            f"<div class='bot-msg'>🤖 {formatted_response}</div>",
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- CHAT INPUT ----------------
prompt = st.chat_input("Ask about today's weather...")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.spinner("Checking weather..."):

        try:
            answer = ask_agent(prompt)

        except Exception as e:
            answer = f"Error : {e}"

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    st.rerun()