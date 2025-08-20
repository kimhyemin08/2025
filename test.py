import streamlit as st
import random

st.title("🏆 남자 캐릭터 성격 월드컵")

# 캐릭터 데이터 (이름, 성격 설명, 드라마, 명대사)
characters = {
    "백이진 (남주혁)": {
        "desc": "겉으로는 성실한 기자지만, 속으로는 누구보다 따뜻하게 챙겨주는 타입.",
        "drama": "스물다섯 스물하나",
        "quote": "오늘도 뉴스 읽어주러 왔습니다 📺"
    },
    "문지웅 (최현욱)": {
        "desc": "쾌활하고 유머러스해서 분위기를 이끄는 에너지메이커.",
        "drama": "스물다섯 스물하나",
        "quote": "야~ 우리 오늘도 재밌게 놀자!"
    },
    "배견우 (추영우)": {
        "desc": "겉으론 무심하고 퉁명스러워 보이지만 마음은 여린 츤데레.",
        "drama": "견우와 선녀",
        "quote": "괜히 다가오지 마… 하지만 넌 괜찮아."
    },
    "안수호 (최현욱)": {
        "desc": "조용하지만 친구를 위해서라면 누구보다 강해지는 든든한 보호자.",
        "drama": "약한 영웅 Class 1",
        "quote": "내 친구 건드리면 가만 안 둬."
    },
    "박후민 (려운)": {
        "desc": "리더십이 강하고 책임감 있는 든든한 오빠 타입.",
        "drama": "약한 영웅 Class 2",
        "quote": "대장은 내가 한다. 따라와 💪"
    },
    "서준태 (최민영)": {
        "desc": "겉으론 순해 보여도 속은 강단 있고 똑 부러지는 성격.",
        "drama": "약한 영웅 Class 2",
        "quote": "나? 겉으론 순해 보여도 만만하게 보면 안 돼."
    },
    "금성제 (이준영)": {
        "desc": "모든 게 귀찮은 듯하지만 가까워지면 의외로 다정한 타입.",
        "drama": "약한 영웅 Class 2",
        "quote": "흥, 다 귀찮네. 그래도 넌 맘에 들어."
    }
}

# 초기 세팅
if "rounds" not in st.session_state:
    st.session_state.rounds = list(characters.keys())
    random.shuffle(st.session_state.rounds)
    st.session_state.winners = []

# 라운드 진행
if len(st.session_state.rounds) >= 2:
    c1, c2 = st.session_state.rounds[:2]

    st.subheader("🔥 둘 중 어떤 성격이 더 끌리나요?")
    col1, col2 = st.columns(2)

    with col1:
        st.info(characters[c1]["desc"])
        if st.button("👉 이 성격 선택", key=c1):
            st.session_state.winners.append(c1)
            st.session_state.rounds = st.session_state.rounds[2:]

    with col2:
        st.info(characters[c2]["desc"])
        if st.button("👉 이 성격 선택", key=c2):
            st.session_state.winners.append(c2)
            st.session_state.rounds = st.session_state.rounds[2:]

# 라운드 종료 후 다음 라운드로
elif len(st.session_state.rounds) == 0 and len(st.session_state.winners) > 1:
    st.session_state.rounds = st.session_state.winners
    st.session_state.winners = []
    random.shuffle(st.session_state.rounds)
    st.success("👉 다음 라운드로 진출!")

# 최종 결과 공개
elif len(st.session_state.winners) == 1:
    winner = st.session_state.winners[0]
    info = characters[winner]
    st.balloons()
    st.header(f"💖 당신이 선택한 이상형 캐릭터는...")
    st.subheader(f"✨ {winner} ✨")
    st.write(f"📺 출연작: {info['drama']}")
    st.write(f"🗨️ 명대사: {info['quote']}")
    st.write(f"🔮 당신과의 싱크로율: {random.randint(70, 100)}%")

    if st.button("다시 하기"):
        st.session_state.rounds = list(characters.keys())
        random.shuffle(st.session_state.rounds)
        st.session_state.winners = []
