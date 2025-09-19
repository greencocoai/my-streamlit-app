import streamlit as st
import requests

st.title("웅나미봇v1(실시간 안됨)")

with st.form("chat_form"):
    system_msg = st.text_area(
        "역할 설명 (ex) 당신은 세계최고의 기상청 날씨 전문가입니다.",
        value="",
        placeholder="역할을 설명하는 시스템 메시지를 입력하세요."
    )
    user_msg = st.text_area(
        "문의 (ex) 내일 서울 날씨는?",
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
    
    # Colab ngrok 터널링 URL로 교체 (예: "http://xxxxxx.ngrok.io")
    url = "https://f79bab9e1125.ngrok-free.app/generate/"  # 반드시 실제 ngrok URL로 교체

    payload = {
        "messages": messages,
        "temperature": temperature,
        "max_new_tokens": 256,
        "top_p": 0.95
    }
    with st.spinner("답변 생성 중..."):
        try:
            response = requests.post(url, json=payload, timeout=120)
            response.raise_for_status()
            answer = response.json().get("answer", "No answer returned.")
        except Exception as e:
            answer = f"Error contacting model server: {str(e)}"
    st.markdown("### 답변")
    st.write(answer)
