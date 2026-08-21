import streamlit as st

from modules.chatbot import generate_context_response
from modules.knowledge_base import load_faq, find_answer
from modules.intent import recognize_intent
from modules.confidence import calculate_confidence
from modules.speech import speech_to_text


# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="AI Customer Support Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# PROFESSIONAL UI / CSS
# =========================================================

st.markdown("""
<style>

    /* Main application */
    .stApp {
        background-color: #f6f8fc;
    }

    /* Main content */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    /* Header */
    .main-header {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        padding: 28px 32px;
        border-radius: 18px;
        margin-bottom: 25px;
        color: #4f46e5;
        box-shadow: 0 8px 25px rgba(79, 70, 229, 0.18);
    }

    .main-header h1 {
        color: white;
        margin: 0;
        font-size: 34px;
        font-weight: 700;
    }

    .main-header p {
        color: #eef2ff;
        margin-top: 8px;
        font-size: 16px;
    }

    /* Feature cards */
    .feature-card {
        background: white;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        margin-bottom: 10px;
        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.04);
    }

    .feature-card h4 {
        margin: 0;
        color: #1f2937;
    }

    .feature-card p {
        margin-top: 6px;
        color: #6b7280;
        font-size: 14px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: 1px solid #d1d5db;
        padding: 9px 15px;
        font-weight: 600;
    }

    /* Chat messages */
    [data-testid="stChatMessage"] {
        border-radius: 14px;
        margin-bottom: 10px;
    }

    /* Chat input */
    [data-testid="stChatInput"] {
        border-radius: 12px;
    }

    /* Status box */
    .status-box {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 16px;
        margin-top: 15px;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 13px;
        padding-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center;">
            <div style="font-size:48px;">🤖</div>
            <h2 style="margin-bottom:0;">Support Bot</h2>
            <p style="color:#6b7280;">AI Customer Support Assistant</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Language
    language = st.selectbox(
        "🌐 Select Language",
        [
            "English",
            "Urdu"
        ]
    )

    st.divider()

    # Voice input
    st.subheader("🎤 Voice Support")

    if st.button(
        "🎙️ Speak",
        use_container_width=True
    ):

        voice_text = speech_to_text()

        if voice_text:

            st.session_state.voice_question = voice_text
            st.rerun()

        else:

            st.warning(
                "Sorry, I could not understand your voice."
            )

    st.divider()

    # Clear chat
    if st.button(
        "🧹 Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()

    st.divider()

    # Features
    st.subheader("✨ Features")

    st.markdown(
        """
        <div class="feature-card">
            <h4>🧠 Natural Language</h4>
            <p>Understands customer questions.</p>
        </div>

        <div class="feature-card">
            <h4>💬 Context Awareness</h4>
            <p>Maintains conversation history.</p>
        </div>

        <div class="feature-card">
            <h4>📚 FAQ Knowledge Base</h4>
            <p>Provides answers from stored FAQs.</p>
        </div>

        <div class="feature-card">
            <h4>🎯 Intent Recognition</h4>
            <p>Identifies the customer's intent.</p>
        </div>

        <div class="feature-card">
            <h4>📊 Confidence Score</h4>
            <p>Shows answer confidence.</p>
        </div>

        <div class="feature-card">
            <h4>🌐 Multi-language</h4>
            <p>Supports English and Urdu.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.caption("Task 2 • Week 2")
    st.caption("AI Chatbot for Customer Support")



# =========================================================
# MAIN HEADER
# =========================================================

st.title("🤖 AI Customer Support Chatbot")

st.caption(
    "Intelligent customer support powered by NLP, "
    "FAQ matching, intent recognition and context-aware responses."
)

# =========================================================
# QUICK INFORMATION
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class="status-box">
            <b>🧠 NLP</b><br>
            <span style="color:#6b7280;">
                Natural Language Understanding
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


with col2:

    st.markdown(
        """
        <div class="status-box">
            <b>🎯 Intent Detection</b><br>
            <span style="color:#6b7280;">
                Understand customer intent
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


with col3:

    st.markdown(
        """
        <div class="status-box">
            <b>🌐 Language</b><br>
            <span style="color:#6b7280;">
                English + Urdu
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )


st.write("")


# =========================================================
# LOAD FAQ
# =========================================================

faq_data = load_faq()


# =========================================================
# CONVERSATION HISTORY
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# =========================================================
# WELCOME MESSAGE
# =========================================================

if len(st.session_state.messages) == 0:

    if language == "Urdu":

        welcome_message = (
            "Assalam-o-Alaikum! 👋\n\n"
            "Main aapka AI Customer Support Assistant hoon. "
            "Aap mujhse orders, refunds, payments, delivery "
            "aur customer support ke baare mein sawal kar sakte hain."
        )

    else:

        welcome_message = (
            "Hello! 👋\n\n"
            "I'm your AI Customer Support Assistant. "
            "You can ask me about orders, refunds, payments, "
            "delivery and customer support."
        )

    with st.chat_message("assistant"):

        st.write(welcome_message)


# =========================================================
# DISPLAY PREVIOUS MESSAGES
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# =========================================================
# TEXT INPUT
# =========================================================

user_question = st.chat_input(
    "💬 Type your question here..."
)


# =========================================================
# VOICE QUESTION
# =========================================================

if "voice_question" in st.session_state:

    user_question = st.session_state.voice_question

    del st.session_state.voice_question


# =========================================================
# PROCESS QUESTION
# =========================================================

if user_question:

    # -----------------------------------------------------
    # USER MESSAGE
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_question
        }
    )

    with st.chat_message("user"):

        st.write(user_question)


    # -----------------------------------------------------
    # INTENT RECOGNITION
    # -----------------------------------------------------

    intent, intent_score = recognize_intent(
        user_question
    )


    # -----------------------------------------------------
    # FAQ MATCHING
    # -----------------------------------------------------

    answer, score = find_answer(
        user_question,
        faq_data
    )


    # -----------------------------------------------------
    # CONFIDENCE SCORE
    # -----------------------------------------------------

    confidence, level, emoji = calculate_confidence(
        score
    )


    # -----------------------------------------------------
    # GENERATE RESPONSE
    # -----------------------------------------------------

    response = generate_context_response(
        user_question,
        st.session_state.messages,
        answer,
        language
    )


    # -----------------------------------------------------
    # ADD INTENT
    # -----------------------------------------------------

    if language == "Urdu":

        response += (
            f"\n\n**Intent:** `{intent}`"
        )

        response += (
            f"\n\n**Confidence Score:** "
            f"`{confidence:.0f}%` {emoji} **{level}**"
        )

    else:

        response += (
            f"\n\n**Intent:** `{intent}`"
        )

        response += (
            f"\n\n**Confidence Score:** "
            f"`{confidence:.0f}%` {emoji} **{level}**"
        )


    # -----------------------------------------------------
    # SAVE ASSISTANT RESPONSE
    # -----------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )


    # -----------------------------------------------------
    # DISPLAY ASSISTANT RESPONSE
    # -----------------------------------------------------

    with st.chat_message("assistant"):

        st.write(response)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        🤖 AI Customer Support Chatbot &nbsp;•&nbsp;
        Task 2 – Week 2 &nbsp;•&nbsp;
        Built with Python & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)