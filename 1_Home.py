import streamlit as st

st.set_page_config(
    page_title="PIPS",
    page_icon="🔓",
)

st.title("Prompt Injection Prevention System (PIPS)")

st.markdown("""
## TLDR
- **Purpose**: Protect AI models from jailbreaks without compromising performance.
- **Key to Success**: Use few-shot examples of jailbreak attempts in the system prompt and update it with new attempts in real-time.
""") 

st.markdown("---")

st.markdown("""
## System Overview:
- **Purpose**: The Prompt Injection Prevention System (PIPS) is engineered to protect AI models from prompt injection attacks by identifying and blocking attempts to insert malicious instructions into the system prompt.
- **Independent Operation**: PIPS functions independently from the main AI model, providing an additional layer of security without interfering with the model's primary functionalities.
- **Comprehensive Inspection**: Each incoming prompt, along with the conversation history, is meticulously analyzed by PIPS to determine its validity and to identify any potential injection attempts.
- **Detection Criteria**: Leveraging advanced analysis parameters from `prompts.py`, PIPS evaluates queries based on factors such as instruction overrides, malicious intent, sensitive information extraction, unauthorized access attempts, and obfuscation techniques.
- **Response Mechanism**: Upon detecting a suspicious prompt, PIPS instructs the main model to refuse the request. The refusal can vary in intensity depending on the severity of the detected threat, ensuring appropriate handling of different risk levels.
- **Continuous Updating**: PIPS is regularly updated with new detection patterns and mitigation strategies to counter evolving adversarial attacks, ensuring robust and adaptive protection.
- **Advantages Over Traditional Methods**: Unlike methods that rely solely on finetuning refusal statements within the model, PIPS offers a dynamic and maintainable approach to preventing prompt injections, enhancing security without compromising model performance.
- **Transparency and Privacy**: PIPS maintains user privacy by not exposing sensitive information or the specifics of detected injection attempts, ensuring that the system remains secure and confidential.
""")
st.markdown("---")
st.markdown("""## Tips
- **Use Few-Shot Examples**: PIPS is most effective when integrated with few-shot examples of jailbreak attempts within the system prompt. This enhances the model's ability to recognize and block malicious inputs.
- **Continuous Monitoring and Updating**: Regularly monitor jailbreak attempts and update the system prompts with successful or near-successful attempts. This ongoing process allows PIPS to adapt and improve its detection capabilities over time.
- **Diversity of Examples**: Incorporate a wide variety of jailbreak examples to cover different attack vectors and techniques. This diversity ensures that PIPS can handle a broad spectrum of adversarial attempts.
- **Regular System Prompt Reviews**: Periodically review and refine the system prompts based on the latest threat patterns identified by PIPS. This ensures that the security measures remain robust against evolving attacks.
""")
st.markdown("---")
st.markdown(""" ## Findings
- The **PIPS** has demonstrated vulnerabilities where it can be bypassed through prompt injection attacks. While attempts to jailbreak PIPS often result in responses that are malformed and not parsable by the code, preventing malicious prompts from reaching the main AI model, it is not entirely foolproof.
- PIPS exhibits a high degree of sensitivity to updates in the underlying AI models. This poses challenges in maintaining its effectiveness post-model updates. In practical applications, a PIPS will require fine-tuning to avoid inconsistencies when the underlying model is updated. During testing, updates caused unpredictable false negative rates, undermining the system's reliability.
- Initially, using `<sandbox>` tags with a random code (e.g., `<sandbox_12345>`) effectively isolated user prompts from the rest of the input, preventing adversarial instruction attempts. However, this approach eventually complicated the queries, leading to numerous false positives. This method is currently under review and has been temporarily removed.
""")

st.markdown("---")
st.markdown(""" ## Successful Jailbreakers

1. Discord: whathefun (Locpet)
2. Discord: sidfeels (Sid ᶻᵒⁿᵉᵈᵒᵗ)
3. Discord: c1j4 (Wizard Toad)

Their attempts were effectively mitigated by incorporating them into the PIPS system prompt within the examples section. However, these specific prompts are excluded from the current system prompt to maintain user privacy.
""")

st.markdown("""
**Note**: This version of the PIPS will be significantly easier to jailbreak than the version used in the challenge. This is solely because of the examples provided to the model and the model used this site serves as a demonstration.
""") 

st.link_button("Try it out!", "https://prompt-injection-prevention-system.streamlit.app/Chat")

st.sidebar.markdown("---")
st.sidebar.markdown("Version: 6")
st.sidebar.markdown("Created by [@brianbellX](https://x.com/brianbellX)")
st.sidebar.markdown("Discord: Jerry5555")
st.sidebar.markdown("---")
st.sidebar.markdown("## Developer Notes")
st.sidebar.markdown("No prompts or conversations are stored. Error messages and conversation context are sent to discord via webhook only to monitor performance of the PIPS.")
