import streamlit as st
import pandas as pd

# 데이터 불러오기
df = pd.read_csv("celeb_data.csv")

st.title("이상형 연예인 추천기")

# 사용자 입력
st.subheader("당신의 이상형 특징을 선택하세요")
features = st.multiselect(
    "특징 선택",
    options=["하얀피부", "긴머리", "단발머리", "쌍꺼풀", "무쌍", "긴얼굴", "둥근얼굴"]
)

# 추천 로직
if st.button("추천받기"):
    if features:
        # 특징이 포함된 연예인 필터링
        filtered = df[df["특징태그"].apply(lambda x: all(f in x for f in features))]
        
        if len(filtered) > 0:
            for _, row in filtered.iterrows():
                st.image(row["이미지URL"], caption=row["이름"])
        else:
            st.warning("해당 특징의 연예인을 찾지 못했습니다.")
    else:
        st.warning("특징을 하나 이상 선택해주세요.")
