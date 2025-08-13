import streamlit as st

# 예시 궁합 데이터 (점수 + 설명)
compatibility_data = {
    ("INTJ", "ENFP"): (95, "서로의 부족한 부분을 채워주는 최고의 조합입니다."),
    ("ENFP", "INTJ"): (95, "서로의 부족한 부분을 채워주는 최고의 조합입니다."),
    ("INFP", "ENFJ"): (90, "감성과 배려가 넘치는 따뜻한 관계입니다."),
    ("ENFJ", "INFP"): (90, "상대방의 마음을 잘 이해하고 배려합니다."),
    ("ISTJ", "ESFP"): (88, "현실 감각과 즐거움이 조화를 이룹니다."),
    ("ESFP", "ISTJ"): (88, "현실 감각과 즐거움이 조화를 이룹니다."),
    ("ISFJ", "ESTP"): (85, "서로의 다른 성향이 매력으로 작용합니다."),
    ("ESTP", "ISFJ"): (85, "서로의 다른 성향이 매력으로 작용합니다."),
}

# MBTI별 기본 이미지 URL (예시, 실제는 원하는 이미지 주소로 변경 가능)
mbti_images = {
    "INTJ": "https://i.imgur.com/4AiXzf8.jpeg",
    "ENFP": "https://i.imgur.com/PF8QXkN.jpeg",
    "INFP": "https://i.imgur.com/1bX5QhS.jpeg",
    "ENFJ": "https://i.imgur.com/ebHfuth.jpeg",
    "ISTJ": "https://i.imgur.com/kCSaQQG.jpeg",
    "ESFP": "https://i.imgur.com/cYhR7xY.jpeg",
    "ISFJ": "https://i.imgur.com/nI4QKpP.jpeg",
    "ESTP": "https://i.imgur.com/dVbNwYb.jpeg",
}

# 앱 제목
st.set_page_config(page_title="MBTI 궁합 보기", page_icon="💖")
st.title("💖 MBTI 궁합 보기")

st.markdown("두 사람의 MBTI를 입력하면 궁합 점수와 설명을 알려드립니다!")

# 두 사람 MBTI 입력
col1, col2 = st.columns(2)
with col1:
    mbti1 = st.text_input("첫 번째 사람 MBTI").upper()
with col2:
    mbti2 = st.text_input("두 번째 사람 MBTI").upper()

# 버튼 클릭 시 결과
if st.button("궁합 보기"):
    if mbti1 in mbti_images and mbti2 in mbti_images:
        # 궁합 데이터 검색
        score, description = compatibility_data.get((mbti1, mbti2), (70, "보통의 궁합입니다. 서로를 이해하려는 노력이 필요합니다."))

        # 결과 표시
        st.subheader(f"✨ 궁합 점수: {score}%")
        st.write(description)

        # 이미지 카드 표시
        c1, c2 = st.columns(2)
        with c1:
            st.image(mbti_images[mbti1], caption=f"{mbti1}", use_column_width=True)
        with c2:
            st.image(mbti_images[mbti2], caption=f"{mbti2}", use_column_width=True)

    else:
        st.error("올바른 MBTI를 입력해주세요. (예: INFP, ENFP)")
