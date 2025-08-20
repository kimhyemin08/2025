import streamlit as st
import random

st.title("🔮 꿈 진로 심리테스트")
st.write("당신의 성격으로 알아보는 미래의 진로 타입!")

# 질문/선택지 데이터
questions = [
    {
        "q": "학교에서 자유시간이 생겼을 때 나는?",
        "options": {
            "a": ("친구들이랑 모여 수다 떨기", "idol"),
            "b": ("혼자 유튜브/넷플릭스 보기", "creator"),
            "c": ("운동장에서 뛰어놀기", "athlete"),
            "d": ("친구 과제 도와주기", "mentor")
        }
    },
    {
        "q": "친구들이 나한테 자주 하는 말은?",
        "options": {
            "a": ("너 텐션 미쳤다ㅋㅋ", "idol"),
            "b": ("넌 진짜 꾸준하다", "creator"),
            "c": ("넌 아이디어가 많아", "creator"),
            "d": ("넌 다 계획이 있구나", "mentor")
        }
    },
    {
        "q": "꿈에서 자주 꾸는 모습은?",
        "options": {
            "a": ("무대 위에서 박수받는 나", "idol"),
            "b": ("여행 다니며 사진 찍는 나", "creator"),
            "c": ("경기장에서 우승컵 드는 나", "athlete"),
            "d": ("강의실에서 발표하는 나", "mentor")
        }
    }
]

results = {
    "idol": {
        "title": "🎤 아이돌 / 인플루언서 타입",
        "desc": "사람들 앞에 서는 걸 좋아하는 에너자이저! 주목받을 때 제일 행복한 스타일 ✨"
    },
    "creator": {
        "title": "📸 크리에이터 / 작가 타입",
        "desc": "혼자만의 세계에서 몰입할 때 가장 빛나는 타입. 남들이 못 보는 디테일을 잘 본다 👀"
    },
    "athlete": {
        "title": "⚽ 운동선수 타입",
        "desc": "에너지 폭발! 몸으로 부딪히는 걸 즐기는 액션파. 노력으로 결과를 만들어내는 사람 💪"
    },
    "mentor": {
        "title": "📚 교사 / 멘토 타입",
        "desc": "계획적이고 책임감 있는 리더. 다른 사람의 성장을 함께 기뻐할 줄 아는 스타일 🌱"
    }
}

# 상태 저장
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = []

# 질문 진행
if st.session_state.step < len(questions):
    q = questions[st.session_state.step]
    st.subheader(q["q"])
    for key, (text, category) in q["options"].items():
        if st.button(text, key=f"{st.session_state.step}_{key}"):
            st.session_state.answers.append(category)
            st.session_state.step += 1
            st.rerun()   # ✅ 수정: experimental_rerun → rerun

# 결과 계산
else:
    st.balloons()
    final = max(set(st.session_state.answers), key=st.session_state.answers.count)
    st.header("✨ 결과 발표 ✨")
    st.subheader(results[final]["title"])
    st.write(results[final]["desc"])
    st.write(f"🔮 싱크로율: {random.randint(70,100)}%")

    if st.button("🔁 다시 하기"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.rerun()
