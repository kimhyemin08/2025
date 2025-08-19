import streamlit as st
import random

st.title("🏆 남자 캐릭터 이상형 월드컵")

characters = {
    "백이진 (남주혁)": {"drama": "스물다섯 스물하나", "quote": "오늘도 뉴스 읽어주러 왔습니다 📺"},
    "문지웅 (최현욱)": {"drama": "스물다섯 스물하나", "quote": "야~ 우리 오늘도 재밌게 놀자!"},
    "배견우 (추영우)": {"drama": "견우와 선녀", "quote": "괜히 다가오지 마… 하지만 넌 괜찮아."},
    "안수호 (최현욱)": {"drama": "약한 영웅 Class 1", "quote": "내 친구 건드리면 가만 안 둬."},
    "박후민 (려운)": {"drama": "약한 영웅 Class 2", "quote": "대장은 내가 한다. 따라와 💪"},
    "서준태 (최민영)": {"drama": "약한 영웅 Class 2", "quote": "나? 겉으론 순해 보여도 만만하게 보면 안 돼."},
    "금성제 (이준영)": {"drama": "약한 영웅 Class 2", "quote": "흥, 다 귀찮네. 그래도 넌 맘에 들어."}
}

# 세션 상태 초기화
if "rounds" not in st.session_state:
    st.session_state.rounds = list(characters.keys())
    random.shuffle(st.session_state.rounds)
    st.session_state.winners = []

# 라운드 진행
if len(st.session_state.rounds) >= 2:
    c1, c2 = st.session_state.rounds[:2]

    st.write("🔥 대결! 둘 중 누가 더 마음에 드나요?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"{c1}"):
            st.session_state.winners.append(c1)
            st.session_state.rounds = st.session_state.rounds[2:]

    with col2:
        if st.button(f"{c2}"):
            st.session_state.winners.append(c2)
            st.session_state.rounds = st.session_state.rounds[2:]

# 라운드 종료 → 다음 라운드 셋업
elif len(st.session_state.rounds) == 0 and len(st.session_state.winners) > 1:
    st.session_state.rounds = st.session_state.winners
    st.session_state.winners = []
    random.shuffle(st.session_state.rounds)
    st.success("👉 다음 라운드로 진출합니다!")

# 최종 결과
elif len(st.session_state.winners) == 1:
    winner = st.session_state.winners[0]
    info = characters[winner]
    st.balloons()
    st.header(f"💖 최종 우승 캐릭터는: {winner}!")
    st.write(f"({info['drama']})")
    st.write(f"🗨️ {info['quote']}")
    st.write(f"✨ 당신과의 싱크로율: {random.randint(70, 100)}%")

    if st.button("다시 하기"):
        st.session_state.rounds = list(characters.keys())
        random.shuffle(st.session_state.rounds)
        st.session_state.winners = []
