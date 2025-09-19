import streamlit as st
import requests

st.title("Qwen 챗봇 (Streamlit Client)")

with st.form("chat_form"):
    system_msg = st.text_area(
        "시스템 메시지 (역할 설명)", 
        value="",  
        placeholder="역할을 설명하는 시스템 메시지를 입력하세요."
    )
    user_msg = st.text_area(
        "사용자 메시지",
        value="",  
        placeholder="질문이나 요청을 입력하세요."
    )
    temperature = st.slider("응답 다양성 (temperature)", 0.1, 1.5, 0.7)
    submitted = st.form_submit_button("질문하기")

if submitted:
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg}
    ]

    url = "http://<COLAB_IP_OR_DOMAIN>:8000/generate/"
    # Replace <COLAB_IP_OR_DOMAIN> with your Colab server IP or tunneling URL (e.g. ngrok URL)

    payload = {
        "messages": messages,
        "temperature": temperature,
        "max_new_tokens": 256,
        "top_p": 0.95
    }

    with st.spinner("답변 생성 중..."):
        try:
            response = requests.post(url, json=payload, timeout=60)
            response.raise_for_status()
            answer = response.json().get("answer", "No answer returned.")
        except Exception as e:
            answer = f"Error contacting model server: {str(e)}"
        
    st.markdown("### 답변")
    st.write(answer)
