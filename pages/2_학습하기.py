import streamlit as st

st.set_page_config(page_title="직육면체 학습하기", layout="centered")

st.title("✏️ 직육면체 겉넓이 연습장")

st.markdown(
    "직육면체의 가로(`가로`), 세로(`세로`), 높이(`높이`)를 입력하면 아래의 세 가지 방법으로 겉넓이를 계산하고 단계별로 확인할 수 있습니다."
)

st.write("---")

# 입력
st.subheader("길이 입력")
w = st.number_input("가로 (예: 6)", min_value=0.0, value=6.0, step=0.5, format="%.2f")
d = st.number_input("세로 (예: 4)", min_value=0.0, value=4.0, step=0.5, format="%.2f")
h = st.number_input("높이 (예: 3)", min_value=0.0, value=3.0, step=0.5, format="%.2f")

st.write("---")

# 직육면체 SVG 동적 생성
st.subheader("입력값에 맞는 직육면체")
scale = 20  # 1 단위당 20픽셀
depth_dx = d * scale * (40.0 / 120.0)  # 깊이 x 오프셋 (약 0.33배)
depth_dy = -d * scale * (30.0 / 100.0)  # 깊이 y 오프셋 (약 0.3배)

padding = 40
view_w = max(300, int(w * scale + depth_dx + padding * 2))
view_h = max(260, int(h * scale + abs(depth_dy) + padding * 2))

# 정면 기준점
fx = padding + 30
fy = padding + 20

# 정면 꼭짓점 (직사각형)
fx1, fy1 = fx, fy
fx2, fy2 = fx + w * scale, fy
fx3, fy3 = fx + w * scale, fy + h * scale
fx4, fy4 = fx, fy + h * scale

# 윗면 꼭짓점 (평행사변형)
tx1, ty1 = fx, fy
tx2, ty2 = fx + w * scale, fy
tx3, ty3 = fx + w * scale + depth_dx, fy + depth_dy
tx4, ty4 = fx + depth_dx, fy + depth_dy

# 우측면 꼭짓점 (평행사변형)
rx1, ry1 = fx + w * scale, fy
rx2, ry2 = fx + w * scale + depth_dx, fy + depth_dy
rx3, ry3 = fx + w * scale + depth_dx, fy + h * scale + depth_dy
rx4, ry4 = fx + w * scale, fy + h * scale

svg_str = (
    f"<div style='max-width: 420px; margin: 20px auto;'>"
    f"<svg viewBox='0 0 {view_w} {view_h}' width='100%' xmlns='http://www.w3.org/2000/svg'>"
    f"<defs> <style> .dash {{ stroke-dasharray:4 3; }} </style> </defs>"
    
    # 정면 (녹색)
    f"<polygon points='{fx1},{fy1} {fx2},{fy2} {fx3},{fy3} {fx4},{fy4}' "
    f"fill='rgba(199,240,182,0.98)' stroke='#2F6B2F' stroke-width='2'/>"
    
    # 윗면 (연두색)
    f"<polygon points='{tx1},{ty1} {tx2},{ty2} {tx3},{ty3} {tx4},{ty4}' "
    f"fill='rgba(223,247,216,0.98)' stroke='#2F6B2F' stroke-width='2'/>"
    
    # 우측면 (밝은 녹색)
    f"<polygon points='{rx1},{ry1} {rx2},{ry2} {rx3},{ry3} {rx4},{ry4}' "
    f"fill='rgba(182,235,160,0.98)' stroke='#2F6B2F' stroke-width='2'/>"
    
    # 보이는 실선 모서리
    f"<line x1='{fx1}' y1='{fy1}' x2='{fx2}' y2='{fy2}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{fx1}' y1='{fy1}' x2='{fx4}' y2='{fy4}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{fx2}' y1='{fy2}' x2='{fx3}' y2='{fy3}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{fx3}' y1='{fy3}' x2='{fx4}' y2='{fy4}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{fx2}' y1='{fy2}' x2='{rx2}' y2='{ry2}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{rx2}' y1='{ry2}' x2='{rx3}' y2='{ry3}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{rx3}' y1='{ry3}' x2='{rx4}' y2='{ry4}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{fx1}' y1='{fy1}' x2='{tx4}' y2='{ty4}' stroke='#2F6B2F' stroke-width='2'/>"
    f"<line x1='{fx2}' y1='{fy2}' x2='{tx3}' y2='{ty3}' stroke='#2F6B2F' stroke-width='2'/>"
    
    # 숨은 점선 모서리
    f"<line x1='{tx4}' y1='{ty4}' x2='{tx3}' y2='{ty3}' class='dash' stroke='#2F6B2F' stroke-width='1.2'/>"
    f"<line x1='{tx4}' y1='{ty4}' x2='{fx + depth_dx}' y2='{fy + h * scale + depth_dy}' class='dash' stroke='#2F6B2F' stroke-width='1.2'/>"
    f"<line x1='{fx + depth_dx}' y1='{fy + h * scale + depth_dy}' x2='{tx3}' y2='{fy + h * scale + depth_dy}' class='dash' stroke='#2F6B2F' stroke-width='1.2'/>"
    f"<line x1='{fx4}' y1='{fy4}' x2='{fx + depth_dx}' y2='{fy + h * scale + depth_dy}' class='dash' stroke='#2F6B2F' stroke-width='1.2'/>"
    f"<line x1='{fx3}' y1='{fy3}' x2='{tx3}' y2='{fy + h * scale + depth_dy}' class='dash' stroke='#2F6B2F' stroke-width='1.2'/>"
    
    # 길이 라벨
    f"<text x='{(fx1 + fx2) / 2}' y='{fy - 5}' text-anchor='middle' font-size='14' font-weight='bold' fill='#2F6B2F'>{w:.1f}</text>"
    f"<text x='{(tx1 + tx4) / 2 - 15}' y='{(ty1 + ty4) / 2 + 5}' text-anchor='middle' font-size='14' font-weight='bold' fill='#2F6B2F'>{d:.1f}</text>"
    f"<text x='{fx - 15}' y='{(fy1 + fy4) / 2 + 5}' text-anchor='middle' font-size='14' font-weight='bold' fill='#2F6B2F'>{h:.1f}</text>"
    f"</svg></div>"
)

st.markdown(svg_str, unsafe_allow_html=True)

st.write("---")

# 개별 면 넓이 계산
area_front = w * h
area_back = area_front
area_left = d * h
area_right = area_left
area_top = w * d
area_bottom = area_top

# 각 방법의 총합 미리 계산
method1_total = area_front + area_back + area_left + area_right + area_top + area_bottom
bottom_double = area_bottom * 2
sides_sum = area_front + area_back + area_left + area_right
method2_total = bottom_double + sides_sum
three_sides_sum = (w * d) + (d * h) + (w * h)
method3_total = three_sides_sum * 2

# 변수 포맷팅 (소수점 1자리 정리)
w_str, d_str, h_str = f"{w:.1f}", f"{d:.1f}", f"{h:.1f}"
f_str, b_str, l_str, r_str, t_str, bot_str = f"{area_front:.1f}", f"{area_back:.1f}", f"{area_left:.1f}", f"{area_right:.1f}", f"{area_top:.1f}", f"{area_bottom:.1f}"

# 1️⃣ 방법 1 실시간 풀이 텍스트
process_text_m1 = (
    f"💡 **실시간 풀이 과정 (여섯 면 각각 더하기):** \n"
    f"직육면체를 둘러싸고 있는 6개 면의 넓이를 하나씩 다 구하면 \n"
    f"• **앞면** (가로×높이) = {w_str} × {h_str} = **{f_str}** | **뒷면** (가로×높이) = {w_str} × {h_str} = **{b_str}** \n"
    f"• **왼쪽 면** (세로×높이) = {d_str} × {h_str} = **{l_str}** | **오른쪽 면** (세로×높이) = {d_str} × {h_str} = **{r_str}** \n"
    f"• **윗면** (가로×세로) = {w_str} × {d_str} = **{t_str}** | **밑면** (가로×세로) = {w_str} × {d_str} = **{bot_str}** 입니다. \n\n"
    f"따라서 여섯 면의 넓이를 모두 더하면  \n"
    f"**{f_str} + {b_str} + {l_str} + {r_str} + {t_str} + {bot_str} = {method1_total:.1f} ㎠** 입니다!"
)

# 2️⃣ 방법 2 실시간 풀이 텍스트
process_text_m2 = (
    f"💡 **실시간 풀이 과정 (밑면×2 + 옆면합):** \n"
    f"위·아래에 있는 2개의 밑면과 옆을 둘러싼 4개의 옆면으로 나누어 구하면 \n"
    f"• **밑면 1개의 넓이** = {w_str} × {d_str} = {t_str} 이므로, **밑면 2개의 넓이**는 {t_str} × 2 = **{bottom_double:.1f}** 입니다. \n"
    f"• **옆면 4개의 넓이 합** = 앞면({f_str}) + 뒷면({b_str}) + 왼쪽({l_str}) + 오른쪽({r_str}) = **{sides_sum:.1f}** 입니다. \n\n"
    f"따라서 (밑면 2개 넓이)와 (옆면 전체 넓이)를 더하면  \n"
    f"**{bottom_double:.1f} + {sides_sum:.1f} = {method2_total:.1f} ㎠** 입니다!"
)

# 3️⃣ 방법 3 실시간 풀이 텍스트
process_text_m3 = (
    f"💡 **실시간 풀이 과정 (합동인 세 면의 합 × 2):** \n"
    f"마주 보는 세 쌍의 면이 합동이라는 성질을 이용해 세 면의 넓이를 먼저 구하면 \n"
    f"• **가로 × 세로 (밑면)** = {w_str} × {d_str} = **{t_str}** \n"
    f"• **세로 × 높이 (옆면)** = {d_str} × {h_str} = **{l_str}** \n"
    f"• **가로 × 높이 (앞면)** = {w_str} × {h_str} = **{f_str}** 입니다. \n\n"
    f"따라서 세 면의 넓이 합인 **({t_str} + {l_str} + {f_str}) = {three_sides_sum:.1f}** 이고, "
    f"여기에 똑같은 면이 2개씩 있으므로 **2배**를 하면 총 겉넓이는 **{method3_total:.1f} ㎠** 입니다!"
)

# UI: 방법 선택 혹은 모두 보기
st.subheader("계산 방법 선택")
choice = st.radio("방법을 선택하세요:", ("모두 보기", "방법 1: 여섯 면 더하기", "방법 2: (밑면×2)+옆면합", "방법 3: (가로×세로 + 세로×높이 + 가로×높이) × 2"))

if choice == "모두 보기":
    st.subheader("방법 1 — 여섯 면의 넓이를 각각 더하기")
    st.info(process_text_m1)  # 수식 나열 레이블 삭제 후 친절한 설명만 표시

    st.subheader("방법 2 — (밑면의 넓이 × 2) + (옆면의 넓이의 합)")
    st.info(process_text_m2)

    st.subheader("방법 3 — (가로×세로 + 세로×높이 + 가로×높이) × 2")
    st.info(process_text_m3)

    st.write("---")
    if abs(method1_total - method2_total) < 1e-6 and abs(method1_total - method3_total) < 1e-6:
        st.success(f"최종 계산 결과: **{method1_total:.1f} ㎠** (세 방법의 결과가 모두 일치합니다 ✅)")
    else:
        st.warning("세 방법의 결과가 일치하지 않습니다 — 입력값을 다시 확인하세요.")

elif choice == "방법 1: 여섯 면 더하기":
    st.subheader("방법 1 — 여섯 면의 넓이를 각각 더하기")
    st.success(process_text_m1)

elif choice == "방법 2: (밑면×2)+옆면합":
    st.subheader("방법 2 — (밑면의 넓이 × 2) + (옆면의 넓이의 합)")
    st.success(process_text_m2)

else:
    st.subheader("방법 3 — (가로×세로 + 세로×높이 + 가로×높이) × 2")
    st.success(process_text_m3)

st.write("---")
st.write("참고: 단위는 입력과 동일합니다. 예: cm로 입력하면 결과는 cm² 입니다.")