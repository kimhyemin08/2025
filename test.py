import streamlit as st

characters = {
    "나희도 (김태리)": {
        "desc": "밝고 열정적이며, 절대 포기하지 않는 긍정적인 성격.",
        "drama": "스물다섯 스물하나",
        "img": "url_to_nahee_do_image"
    },
    "백이진 (남주혁)": {
        "desc": "따뜻하고 책임감 넘치며, 성실한 노력파.",
        "drama": "스물다섯 스물하나",
        "img": "url_to_baek_i_jin_image"
    },
    "배견우 (추영우)": {
        "desc": "차가운 듯 하지만 내면은 따뜻한, 스스로를 지키려는 소년.",
        "drama": "견우와 선녀",
        "img": "url_to_gyunwoo_image"
    },
    "박성아 (조이현)": {
        "desc": "직진적이고 용감한, 첫사랑을 위해 무엇이든 하는 소녀.",
        "drama": "견우와 선녀",
        "img": "url_to_sung_a_image"
    },
    "표지호 (차강윤)": {
        "desc": "순정적이고 조력자 타입, 묵묵한 감정 표현.",
        "drama": "견우와 선녀",
        "img": "url_to_jiho_image"
    },
    "연시은 (박지훈)": {
        "desc": "침착하고 분석적인 이성파.",
        "drama": "약한 영웅 Class 1",
        "img": "url_to_yunsieun_image"
    },
    "수호 (최현욱)": {
        "desc": "충성스럽고 따뜻한 친구.",
        "drama": "약한 영웅 Class 1",
        "img": "url_to_suho_image"
    },
    "범석 (홍경민)": {
        "desc": "솔직하고 감정 표현이 풍부한 성격.",
        "drama": "약한 영웅 Class 1",
        "img": "url_to_beomseok_image"
    }
}

st.title("🌟 내가 가장 좋아할 캐릭터는?")

options = [info["desc"] for info in characters.values()]
choice = st.radio("마음에 드는 성격을 골라보세요:", options)

if choice:
    for name, info in characters.items():
        if info["desc"] == choice:
            st.subheader("💖 당신이 좋아할 캐릭터는:")
            st.write(f"**{name}** — {info['drama']}")
            st.write(info["desc"])
            st.image(info["img"], caption=f"{name} ({info['drama']})")

