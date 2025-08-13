# app.py
# -------------------------------------------------------------
# 💖 MBTI 궁합 보기 (16개 타입 전 조합 지원)
# - 두 사람의 MBTI를 어떤 순서로 입력해도 동일한 결과
# - 16 x 16 = 256 모든 경우의 수 커버 (알고리즘으로 계산)
# - 점수(%) + 설명 + 타입 카드 + 상위 궁합 추천 리스트
# - Streamlit UI 구성
# -------------------------------------------------------------

import streamlit as st
import re
from typing import Tuple, List, Dict

st.set_page_config(page_title="MBTI 궁합 보기", page_icon="💖", layout="centered")
st.title("💖 MBTI 궁합 보기")
st.caption("16개 MBTI의 모든 조합을 알고리즘으로 계산하여 궁합 점수와 설명을 제공합니다.")

ALL_TYPES = [
    "INTJ","INTP","ENTJ","ENTP",
    "INFJ","INFP","ENFJ","ENFP",
    "ISTJ","ISFJ","ESTJ","ESFJ",
    "ISTP","ISFP","ESTP","ESFP",
]

# 간단 타입 설명 (필요에 따라 자유롭게 수정/보완)
TYPE_DESC: Dict[str, str] = {
    "INTJ": "전략가 · 비전을 현실로 설계하는 유형",
    "INTP": "논리학자 · 개념과 원리를 탐구하는 유형",
    "ENTJ": "통솔자 · 목표 달성에 체계적인 리더",
    "ENTP": "변론가 · 새로운 아이디어를 즐기는 유형",
    "INFJ": "옹호자 · 가치와 의미를 중시하는 통찰가",
    "INFP": "중재자 · 진정성과 조화를 추구",
    "ENFJ": "선도자 · 타인을 이끄는 따뜻한 리더",
    "ENFP": "활동가 · 열정과 영감을 전파하는 유형",
    "ISTJ": "현실주의자 · 책임감과 신뢰가 강함",
    "ISFJ": "수호자 · 헌신과 배려가 기본",
    "ESTJ": "경영자 · 실행력과 조직력 탁월",
    "ESFJ": "집정관 · 공동체 중심의 조화",
    "ISTP": "장인 · 문제 해결에 강한 실무형",
    "ISFP": "탐험가 · 따뜻하고 유연한 미감",
    "ESTP": "사업가 · 에너지와 즉흥적 실행",
    "ESFP": "연예인 · 즐거움과 활기를 선사",
}

LETTER_SETS = [
    set("EI"), set("SN"), set("TF"), set("JP")
]

MBTI_PATTERN = re.compile(r"^[EI][SN][TF][JP]$")

# -------------------------------------------------------------
# 유틸
# -------------------------------------------------------------

def normalize_mbti(s: str) -> str:
    s = (s or "").strip().upper()
    # 흔한 오타 보정 (소문자, 공백, 한글입력 혼용 대비)
    mapping = {
        "I": "I", "E": "E", "S": "S", "N": "N", "T": "T", "F": "F", "J": "J", "P": "P"
    }
    s = "".join(mapping.get(ch, ch) for ch in s)
    return s


def is_valid_mbti(s: str) -> bool:
    return bool(MBTI_PATTERN.match(s))


def opposite_letter(c: str) -> str:
    pairs = {"E":"I","I":"E","S":"N","N":"S","T":"F","F":"T","J":"P","P":"J"}
    return pairs[c]

# -------------------------------------------------------------
# 궁합 스코어 알고리즘 (대칭, 16x16 전 조합 커버)
# -------------------------------------------------------------
# 아이디어:
# - 기본점수 50
# - 서로 반대인 차원(E-I, S-N, T-F, J-P)일수록 보완이 잘 되므로 +12씩 가산
# - 동일 차원은 안정감 가산 +6
# - N&F 동시 보유(둘 다 N, 둘 다 F)면 공감/비전 보너스 +4
# - S&T 동시 보유(둘 다 S, 둘 다 T)면 실무/현실 보너스 +3
# - 둘 다 J 혹은 둘 다 P면 생활 리듬 보너스 +2
# - 캡: 95, 플로어: 5
# 설명은 각 차원 비교를 바탕으로 자연어로 생성


def compatibility_score(a: str, b: str) -> int:
    a, b = normalize_mbti(a), normalize_mbti(b)
    base = 50
    score = base

    # 차원별 비교
    for i in range(4):
        if a[i] == b[i]:
            score += 6
        else:
            # 반대면 보완 보너스
            score += 12

    # 테마 보너스
    if a[1] == b[1] == 'N' and a[2] == b[2] == 'F':
        score += 4
    if a[1] == b[1] == 'S' and a[2] == b[2] == 'T':
        score += 3
    if a[3] == b[3]:
        score += 2

    return int(max(5, min(95, score)))


def compatibility_explainer(a: str, b: str) -> List[str]:
    a, b = normalize_mbti(a), normalize_mbti(b)
    notes = []

    # E/I
    if a[0] != b[0]:
        notes.append("에너지 방향(E/I)이 보완되어 서로의 페이스를 조절해 줍니다.")
    else:
        notes.append("비슷한 에너지 성향(E/I)으로 생활 리듬이 잘 맞습니다.")

    # S/N
    if a[1] != b[1]:
        notes.append("정보 처리(S/N)가 상호 보완되어 현실과 아이디어의 균형이 좋습니다.")
    else:
        if a[1] == 'N':
            notes.append("둘 다 N이라 비전/통찰 대화가 즐겁습니다.")
        else:
            notes.append("둘 다 S라 실용적이고 구체적 대화가 편합니다.")

    # T/F
    if a[2] != b[2]:
        notes.append("의사결정(T/F)이 보완되어 논리와 공감의 밸런스가 좋습니다.")
    else:
        if a[2] == 'F':
            notes.append("둘 다 F라 관계와 감정에 민감하며 배려가 잘 맞습니다.")
        else:
            notes.append("둘 다 T라 합리성과 효율을 중시하는 결이 같습니다.")

    # J/P
    if a[3] != b[3]:
        notes.append("생활 방식(J/P)이 달라 융통성과 계획성이 균형을 이룹니다.")
    else:
        if a[3] == 'J':
            notes.append("둘 다 J라 계획/마감 준수가 편안합니다.")
        else:
            notes.append("둘 다 P라 즉흥/유연성이 잘 맞습니다.")

    return notes


# 한 타입 기준 전체 매칭 순위표 반환

def ranked_matches_for(t: str) -> List[Tuple[str, int]]:
    out = []
    for other in ALL_TYPES:
        out.append((other, compatibility_score(t, other)))
    out.sort(key=lambda x: x[1], reverse=True)
    return out


# -------------------------------------------------------------
# UI
# -------------------------------------------------------------
with st.container():
    st.subheader("두 사람의 MBTI를 선택하세요")
    col1, col2 = st.columns(2)
    with col1:
        mbti_a = st.selectbox("첫 번째", ALL_TYPES, index=ALL_TYPES.index("INFP"))
    with col2:
        mbti_b = st.selectbox("두 번째", ALL_TYPES, index=ALL_TYPES.index("ENFJ"))

    # 자유 입력(오타도 수용) 옵션
    with st.expander("직접 입력(선택 박스와 무관, 오타 자동 보정)"):
        a_free = st.text_input("첫 번째 MBTI 직접 입력", value="")
        b_free = st.text_input("두 번째 MBTI 직접 입력", value="")
        if a_free:
            mbti_a = normalize_mbti(a_free)
        if b_free:
            mbti_b = normalize_mbti(b_free)

    # 유효성 체크 및 교차 순서 동일성 안내
    valid = is_valid_mbti(mbti_a) and is_valid_mbti(mbti_b)
    if not valid:
        st.error("MBTI는 E/I, S/N, T/F, J/P 각 1글자씩 총 4글자여야 합니다. 예: INFP, ESTJ")

    # 결과 카드
    if valid:
        score = compatibility_score(mbti_a, mbti_b)
        notes = compatibility_explainer(mbti_a, mbti_b)

        st.markdown("---")
        st.subheader("✨ 궁합 결과")
        st.markdown(f"**{mbti_a}** × **{mbti_b}** → **{score}%**")
        st.progress(score/100)
        for n in notes:
            st.write("• " + n)

        # 타입 카드
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"### 🧩 {mbti_a}")
            st.caption(TYPE_DESC.get(mbti_a, ""))
        with c2:
            st.markdown(f"### 🧩 {mbti_b}")
            st.caption(TYPE_DESC.get(mbti_b, ""))

        st.info("입력 순서는 결과에 영향을 주지 않습니다. (A×B = B×A)")

# 전체 조합 가이드
st.markdown("---")
st.subheader("📈 타입별 상위 궁합 추천")
sel = st.selectbox("기준 타입 선택", ALL_TYPES, index=ALL_TYPES.index("INFP"))
ranked = ranked_matches_for(sel)

# 상위 5 표시
st.write("상위 5 궁합")
for t, s in ranked[:5]:
    badge = "✅" if s >= 85 else ("👍" if s >= 75 else "👌")
    st.write(f"{badge} **{sel} × {t}** : {s}%")

with st.expander("전체 16개 타입과의 점수 보기"):
    for t, s in ranked:
        st.write(f"- {sel} × {t} : {s}%")

st.markdown("<small>※ 이 앱의 점수는 심리검사 대체가 아닌, 성향 보완/유사성에 기초한 휴리스틱입니다.</small>", unsafe_allow_html=True)
