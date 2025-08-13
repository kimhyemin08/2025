import streamlit as st

# MBTI 궁합 데이터 (예시)
compatibility = {
    "INTJ": ("ENFP", "서로의 부족한 부분을 채워주는 최고의 조합입니다."),
    "INTP": ("ENTJ", "논리와 실행력이 완벽히 결합된 관계입니다."),
    "ENTJ": ("INTP", "서로의 장단점을 잘 이해하는 파트너입니다."),
    "ENTP": ("INFJ", "새로운 아이디어와 깊은 공감이 어우러집니다."),
    "INFJ": ("ENTP", "서로에게 영감을 주고받는 관계입니다."),
    "INFP": ("ENFJ", "감성과 배려가 넘치는 따뜻한 관계입니다."),
    "ENFJ": ("INFP", "상대방의 마음을 잘 이해하고 배려합니다."),
    "ENFP": ("INTJ", "새로운 모험과 안정감을 동시에 줍니다."),
    "ISTJ": ("ESFP", "현실 감각과 즐거움이 조화를 이룹니다."),
    "ISFJ": ("ESTP", "서로의 다른 성향이 매력으로 작용합니다."),
    "ESTJ": ("ISTP", "실행력과 분석력이 결합된 관계입니다."),
    "ESFJ": ("ISFP", "서로의 장점을 살려주는 관계입니다."),
    "ISTP": ("ESTJ", "효율과 실행을 동시에 만족시키는 관계입니다."),
    "ISFP": ("ESFJ", "서로에게 편안함과 안정감을 줍니다."),
    "ESTP": ("ISFJ", "활발함과 배려가 어우러지는 관계입니다."),
    "ESFP": ("ISTJ", "즐거움과 안정감을 동시에 제공합니다."),
}

# Streamlit 앱
st.title("💖 MBTI 궁합 보기")

user_mbti = st.text_input("당신의 MBTI를 입력하세요 (예: INFP)").upper()

if st.button("궁합 보기"):
    if user_mbti in compatibility:
        match_mbti, description = compatibility[user_mbti]
        st.success(f"당신과 잘 맞는 MBTI: **{match_mbti}**")
        st.write(description)
    else:
        st.error("올바른 MBTI를 입력해주세요. (예: INFP)")

