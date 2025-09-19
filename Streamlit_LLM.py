import streamlit as st
import requests

st.title("테스트봇v1(실시간 안됨)")

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


st.set_page_config(page_title="테스트봇v1 멀티페이지 앱", layout="wide")

# 사이드바 메뉴 이름 리스트 (원하는 만큼 추가)
page_names = [
    "챗봇",
    "문서 요약 및 검색",
    "동영상 음성 분리",
    "목소리 변조 모델 생성 및 변조",
    "음원 분리 및 음성 변조 노래 생성",
    "이미지 내 텍스트 인식 및 번역",
    "텍스트→이미지 생성 및 이미지 변형",
    "텍스트·이미지 기반 영상 생성"
]

# 사이드바 메뉴 선택 UI
page = st.sidebar.selectbox("기능 선택", page_names)

# 각 페이지별 함수 정의

def page_chatbot():
    st.title("챗봇 페이지")
    # 기존 챗봇 UI 코드 재사용 가능
    with st.form("chat_form"):
        system_msg = st.text_area(
            "역할 설명 (ex) 당신은 세계최고의 기상청 날씨 전문가입니다.",
            value="", placeholder="역할을 설명하는 시스템 메시지를 입력하세요."
        )
        user_msg = st.text_area(
            "문의 (ex) 내일 서울 날씨는?", value="", placeholder="질문이나 요청을 입력하세요."
        )
        temperature = st.slider("응답 다양성 (temperature)", 0.1, 1.5, 0.7)
        submitted = st.form_submit_button("질문하기")
    if submitted:
        messages = [
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ]
        url = "https://your-ngrok-url.ngrok-free.app/generate/"  # 여기에 실제 API 서버 주소 넣기
        payload = {
            "messages": messages,
            "temperature": temperature,
            "max_new_tokens": 256,
            "top_p": 0.95
        }
        with st.spinner("답변 생성 중..."):
            try:
                import requests
                response = requests.post(url, json=payload, timeout=120)
                response.raise_for_status()
                answer = response.json().get("answer", "No answer returned.")
            except Exception as e:
                answer = f"Error contacting model server: {e}"
        st.markdown("### 답변")
        st.write(answer)

def page_document_summary_search():
    st.title("문서 요약 및 검색 페이지")
    uploaded_file = st.file_uploader("텍스트, SRT, PDF 문서 업로드", type=['txt','srt','pdf'])
    if uploaded_file:
        # 문서의 내용을 추출해서 요약 및 검색 UI 구현
        st.write("문서 처리 및 요약 기능 개발 필요")
        # 예: 텍스트 -> 요약, 검색어 입력 -> 답변 출력 등

def page_video_audio_extraction():
    st.title("동영상 음성 파일/자막/무음영상 분리")
    video_file = st.file_uploader("동영상(mp4) 업로드", type=['mp4'])
    if video_file:
        st.write("동영상에서 음성(mp3), 자막(srt), 무음영상(mp4) 분리 기능 개발 필요")

def page_voice_modeling():
    st.title("목소리 모델 생성 및 변조")
    st.write("둘 이상의 목소리 파일 업로드 → 새로운 목소리 모델 생성")
    st.write("특정 음성 입력 → 모델로 음성 변조 기능 개발 필요")

def page_music_voice_separation():
    st.title("음원과 음성 분리후 음성변조 노래 생성")
    audio_file = st.file_uploader("음성, 음악 파일 업로드(mp3,wav,mid 등)", type=['mp3','wav','mid'])
    if audio_file:
        st.write("음원/음성 분리 및 변조된 음성 입힌 노래 생성 기능 개발 필요")

def page_image_ocr_translate():
    st.title("이미지 글자 인식 및 번역")
    image_file = st.file_uploader("이미지 업로드", type=['png','jpg','jpeg','bmp'])
    if image_file:
        st.write("OCR 및 다국어 번역 기능 개발 필요")

def page_text_image_generation():
    st.title("텍스트로 이미지 생성 및 이미지 변형")
    st.write("텍스트 입력 → 이미지 생성")
    st.write("이미지 업로드 → 텍스트에 따른 이미지 변형 기능 개발 필요")

def page_text_image_video_generation():
    st.title("텍스트 및 이미지 기반 영상 생성")
    st.write("텍스트, 이미지 입력 → 영상 생성 기능 개발 필요")

# 선택한 페이지에 따른 함수 호출
if page == "챗봇":
    page_chatbot()
elif page == "문서 요약 및 검색":
    page_document_summary_search()
elif page == "동영상 음성 분리":
    page_video_audio_extraction()
elif page == "목소리 모델 생성 및 변조":
    page_voice_modeling()
elif page == "음원 분리 및 음성 변조 노래 생성":
    page_music_voice_separation()
elif page == "이미지 내 텍스트 인식 및 번역":
    page_image_ocr_translate()
elif page == "텍스트→이미지 생성 및 이미지 변형":
    page_text_image_generation()
elif page == "텍스트·이미지 기반 영상 생성":
    page_text_image_video_generation()
