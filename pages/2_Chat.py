import streamlit as st
from pips import (
    pips,
    process_pips_result,
)
from util import (
    generate_conversation_id,
)


if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = generate_conversation_id()
if "api_key" not in st.session_state:
    st.session_state.api_key = ""

st.session_state.api_key = st.sidebar.text_input("OpenAI API Key:", type="password")

if not st.session_state.api_key:
    st.sidebar.error("Please enter your API key to use the chat.")
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message gpt-4o-mini", max_chars=20000):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        pips_result, all_messages, result = pips()
    except Exception as e:
        pips_result = None
        all_messages = None
        result = None  # Ensure all variables are defined

    if st.session_state.messages:
        context = f"{st.session_state.messages[-1]['role']}: {st.session_state.messages[-1]['content']}"
    else:
        context = "" 
    process_pips_result(pips_result, prompt, context)

if len(st.session_state.messages) > 1:
    if st.button("Reset Conversation"):
        st.session_state.messages = []
        st.session_state.conversation_id = generate_conversation_id()
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.markdown("Version: 6")
st.sidebar.markdown("Created by [@brianbellX](https://x.com/brianbellX)")
st.sidebar.markdown("Discord: Jerry5555")
st.sidebar.markdown("---")
st.sidebar.markdown("When contacting support, please include your conversation ID.")
st.sidebar.markdown("Conversation ID:") 
st.sidebar.code(st.session_state.conversation_id)
st.sidebar.markdown("---")
st.sidebar.markdown("## Developer Notes")
st.sidebar.markdown("No prompts or conversations are stored. Error messages and conversation context are sent to discord via webhook only to monitor performance of the PIPS.")
