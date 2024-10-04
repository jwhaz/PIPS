import streamlit as st
from prompts import pips_system_prompt, main_model_system_prompt

if "pips_system_prompt" not in st.session_state:
    st.session_state.pips_system_prompt = pips_system_prompt
if "main_model_system_prompt" not in st.session_state:
    st.session_state.main_model_system_prompt = main_model_system_prompt

new_pips_prompt = st.text_area("PIPS System Prompt", value=st.session_state.pips_system_prompt, height=300)

new_main_model_prompt = st.text_area("Main Model System Prompt", value=st.session_state.main_model_system_prompt, height=300)

if st.button("Save Changes"):
    st.session_state.pips_system_prompt = new_pips_prompt
    st.session_state.main_model_system_prompt = new_main_model_prompt
    st.success("Prompts updated successfully.")


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
