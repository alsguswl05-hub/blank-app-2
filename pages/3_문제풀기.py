import random
import streamlit as st

st.set_page_config(page_title="직육면체 겉넓이 퀴즈", layout="centered")

st.title("✏️ 도전! 직육면체 겉넓이 박사 퀴즈")
st.markdown("배운 내용을 바탕으로 스스로 문제를 풀어보세요. 계산기를 쓰지 않고 직접 풀면 실력이 더 늘어날 거예요!")
st.write("---")

# 1. 세션 상태(session_state) 초기화
if "quiz_w" not in st.session_state:
    st.session_state.quiz_w = float(random.randint(3, 10))
    st.session_state.quiz_d = float(random.randint(3, 10))
    st.session_state.quiz_h = float(random.randint(3, 10))
    st.session_state.checked = False  # 정답 확인 버튼을 눌렀는지 여부

# 현재 출제된 문제의 가로, 세로, 높이 가져오기
qw = st.session_state.quiz_w
qd = st.session_state.quiz_d
qh = st.session_state.quiz_h

# 정답 계산해두기 (채점용 내부 변수)
correct_answer = ((qw * qd) + (qd * qh) + (qw * qh)) * 2

# 2. 문제 출제 화면
st.subheader("📝 오늘의 문제")
st.info(f"**가로 {qw:.0f}cm, 세로 {qd:.0f}cm, 높이 {qh:.0f}cm**인 직육면체가 있습니다. 이 직육면체의 겉넓이는 얼마일까요?")

# 3. 정답 입력창 및 버튼
user_answer = st.number_input(
    "정답을 입력하세요 (단위: ㎠)", 
    min_value=0.0, 
    value=0.0, 
    step=None, 
    format="%.0f"
)

col1, col2 = st.columns(2)

with col1:
    if st.button("정답 확인하기", use_container_width=True):
        st.session_state.checked = True

with col2:
    if st.button("🔄 다음 문제 풀기", use_container_width=True):
        st.session_state.quiz_w = float(random.randint(3, 10))
        st.session_state.quiz_d = float(random.randint(3, 10))
        st.session_state.quiz_h = float(random.randint(3, 10))
        st.session_state.checked = False
        st.container().empty()
        st.rerun()

st.write("---")

# 4. 채점 및 오답노트 피드백 영역
if st.session_state.checked:
    if round(user_answer, 1) == round(correct_answer, 1):
        st.success(f"🎉 정답입니다! 대단해요! (정답: {correct_answer:.0f}㎠)")
        st.balloons()
    else:
        # ❌ 정답 숫자 노출을 모두 제거했습니다.
        st.error(f"❌ 아쉽지만 틀렸습니다. 어디서 계산이 틀렸는지 다시 한번 차근차근 풀어볼까요?")
        
        # 안내 가이드에 쓰일 변수 바인딩
        qw_str, qd_str, qh_str = f"{qw:.0f}", f"{qd:.0f}", f"{qh:.0f}"
        
        st.markdown("### 📖 친절한 오답 힌트")
        st.warning(
            f"**정답을 보기 전에 스스로 정답을 찾아내면 수학 실력이 쏙쏙 자라나요!**\n\n"
            f"가장 실수를 줄일 수 있는 **'합동인 세 면의 넓이 합 × 2'** 공식을 생각하며 다시 계산해 봐요. \n\n"
            f"1. **밑면의 넓이 구하기**: 가로({qw_str}) × 세로({qd_str})를 계산해 보세요.\n"
            f"2. **옆면1의 넓이 구하기**: 세로({qd_str}) × 높이({qh_str})를 계산해 보세요.\n"
            f"3. **옆면2의 넓이 구하기**: 가로({qw_str}) × 높이({qh_str})를 계산해 보세요.\n\n"
            f"위에서 구한 **세 면의 넓이를 모두 더한 뒤, 마지막에 꼭 2배**를 해주어야 해요. \n"
            f"식의 순서나 더하기, 곱하기 계산에서 실수가 없었는지 다시 확인하고 입력창에 새 정답을 적어보세요! 💪"
        )