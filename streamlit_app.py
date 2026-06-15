import streamlit as st

st.set_page_config(page_title="직육면체 겉넓이 학습 공간", page_icon="🧮", layout="centered")

st.title("🧮 직육면체 겉넓이 학습 공간")
st.markdown(
    "이 공간은 직육면체의 겉넓이를 쉽게 배우고 이해하는 학습 공간입니다. "
    "예를 들어, 친구에게 선물할 상자를 예쁜 포장지로 감싸려 할 때 포장지가 얼마나 필요한지 계산하는 상황을 떠올려보세요."
)

# 🎁 마주보는 면이 평행한 직육면체 + 띠 삭제 + 윗면 중앙 노란 리본 손그림 SVG
st.markdown(
    "<div style='max-width: 450px; margin: 20px auto; text-align: center;'>"
    "<svg viewBox='0 0 400 350' width='100%' xmlns='http://www.w3.org/2000/svg'>"
    
    ""
    "<defs>"
    "  <filter id='crayon-texture' x='-10%' y='-10%' width='120%' height='120%'>"
    "    <feTurbulence type='fractalNoise' baseFrequency='0.04' numOctaves='3' result='noise' />"
    "    <feDisplacementMap in='SourceGraphic' in2='noise' scale='3.5' xChannelSelector='R' yChannelSelector='G' />"
    "  </filter>"
    "</defs>"
    
    ""
    "<g filter='url(#crayon-texture)'>"
    
    "  "
    "  "
    "  "
    "  <polygon points='240,95 340,150 150,195 50,140' fill='#B9E5FF' stroke='#8DCEF7' stroke-width='6' stroke-linejoin='round'/>"
    "  "
    "  "
    "  <polygon points='50,140 150,195 150,315 50,260' fill='#74C2F7' stroke='#4BA9E8' stroke-width='6' stroke-linejoin='round'/>"
    "  "
    "  "
    "  <polygon points='150,195 340,150 340,270 150,315' fill='#9AD8FF' stroke='#6CBBEF' stroke-width='6' stroke-linejoin='round'/>"
    
    "  "
    "  "
    "  "
    "  <path d='M195,145 C165,105 150,155 195,145' fill='none' stroke='#FFF37A' stroke-width='10' stroke-linecap='round' stroke-linejoin='round'/>"
    "  <path d='M195,145 C165,105 150,155 195,145' fill='none' stroke='#FFD54F' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'/>"
    "  "
    "  "
    "  <path d='M195,145 C235,110 245,160 195,145' fill='none' stroke='#FFF37A' stroke-width='10' stroke-linecap='round' stroke-linejoin='round'/>"
    "  <path d='M195,145 C235,110 245,160 195,145' fill='none' stroke='#FFD54F' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'/>"
    "  "
    "  "
    "  <path d='M195,145 C200,165 205,185 205,195' fill='none' stroke='#FFF37A' stroke-width='9' stroke-linecap='round'/>"
    "  <path d='M195,145 C200,165 205,185 205,195' fill='none' stroke='#FFD54F' stroke-width='4' stroke-linecap='round'/>"
    "  "
    "  "
    "  <path d='M195,145 C180,155 165,165 155,170' fill='none' stroke='#FFF37A' stroke-width='9' stroke-linecap='round'/>"
    "  <path d='M195,145 C180,155 165,165 155,170' fill='none' stroke='#FFD54F' stroke-width='4' stroke-linecap='round'/>"
    
    "</g>"
    "</svg></div>", 
    unsafe_allow_html=True
)

st.write("### 학습 목표")
st.write(
    "- 직육면체의 겉넓이를 계산하는 방법을 이해하기\n"
    "- 각 변의 길이를 이용해 겉넓이를 구하는 공식을 익히기\n"
)

st.write("---")