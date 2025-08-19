import streamlit as st

st.title("🌟 당신이 좋아할 남자 캐릭터는?")

characters = {
    "백이진 (남주혁)": {
        "desc": "책임감 있고 따뜻한 현실파 신사.",
        "drama": "스물다섯 스물하나"
    },
    "문지웅 (최현욱)": {
        "desc": "밝고 유쾌한 분위기 메이커 친구.",
        "drama": "스물다섯 스물하나"
    },
    "배견우 (추영우)": {
        "desc": "차갑지만 내면은 따뜻한 경계심 많은 소년.",
        "drama": "견우와 선녀"
    },
    "안수호 (최현욱)": {
        "desc": "친구에게 헌신적인 보호자 타입.",
        "drama": "약한 영웅 Class 1"
    },
    "박후민 (려운)": {
        "desc": "호쾌하고 대장다운 힘 캐, 친구들을 포용하는 타입.",
        "drama": "약한 영웅 Class 2"
    },
    "서준태 (최민영)": {
        "desc": "언뜻 순해 보이지만 속은 깊고 복잡한 인물.",
        "drama": "약한 영웅 Class 2"
    },
    "금성제 (이준영)": {
        "desc": "자유롭고 냉소적이며 예측 불가능한 인물.",
        "drama": "약한 영웅 Class 2"
    }
}

options = [info["desc"] for info in characters.values()]
choice = st.radio("가장 끌리는 성격을 선택하세요:", options)

if choice:
    for name, info in characters.items():
        if info["desc"] == choice:
            st.subheader("💖 당신이 좋아할 남자 캐릭터는:")
            st.write(f"**{name} — {info['drama']}**")
            st.write(info["desc"])
