import streamlit as st
import torch
from transformers import pipeline, BitsAndBytesConfig

# --- 모델 로드 (앱 실행 시 1회만 실행) ---
@st.cache_resource(show_spinner=True)
def load_model():
    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.bfloat16
    )
    pipe = pipeline(
        "text-generation",
        model="Qwen/Qwen2-7B-Instruct",
        model_kwargs={"quantization_config": quantization_config},
        dtype=torch.bfloat16,
        device_map="auto"
    )
    return pipe

pipe = load_model()

# --- 채팅 함수 ---
def chat(messages, temperature=0.7, max_new_tokens=256, top_p=0.95):
    prompt = pipe.tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    outputs = pipe(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        top_p=top_p
    )
    generated_text = outputs[0]["generated_text"]
    answer = generated_text[len(prompt):].strip()
    return answer

# --- UI ---
st.title("Qwen 챗봇 (Streamlit)")

with st.form("chat_form"):
    system_msg = st.text_area(
        "시스템 메시지 (역할 설명)", 
        value="",  # 기본 빈칸으로 변경
        placeholder="역할을 설명하는 시스템 메시지를 입력하세요."
    )
    user_msg = st.text_area(
        "사용자 메시지",
        value="",  # 기본 빈칸으로 변경
        placeholder="질문이나 요청을 입력하세요."
    )
    temperature = st.slider("응답 다양성 (temperature)", 0.1, 1.5, 0.7)
    submitted = st.form_submit_button("질문하기")

if submitted:
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": user_msg}
    ]
    with st.spinner("답변 생성 중..."):
        response = chat(messages, temperature=temperature)
    st.markdown("### 답변")
    st.write(response)
