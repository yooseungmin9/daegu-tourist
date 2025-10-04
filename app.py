import streamlit as st
import folium
from streamlit_folium import st_folium
from mountains import apsan, biseulsan, palgongsan

language_dict = {
    '팔공산': palgongsan,
    '앞산': apsan,
    '비슬산': biseulsan
}

st.title("대구의 주요 관광 정보")

# 사이드바에서 산 선택
selected_mountain = st.sidebar.selectbox("산을 선택하세요", list(language_dict.keys()))
mountain = language_dict[selected_mountain]

st.header(mountain["name"])
st.subheader(f"한자명: {mountain['hanja']}")
st.write(f"위치: {mountain['locate']}")

# 이미지 슬라이드용 세션 상태 초기화
if "image_idx" not in st.session_state:
    st.session_state.image_idx = 0

# 산이 바뀌면 이미지 인덱스 초기화
if "previous_mountain" not in st.session_state:
    st.session_state.previous_mountain = selected_mountain
elif st.session_state.previous_mountain != selected_mountain:
    st.session_state.image_idx = 0
    st.session_state.previous_mountain = selected_mountain

# 이전/다음 버튼과 현재 이미지 정보
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("◀ 이전"):
        if st.session_state.image_idx > 0:
            st.session_state.image_idx -= 1

with col3:
    if st.button("다음 ▶"):
        if st.session_state.image_idx < len(mountain["images"]) - 1:
            st.session_state.image_idx += 1

# 현재 슬라이드 이미지 표시
current_image = mountain["images"][st.session_state.image_idx]
st.image(current_image,
         caption=f"{mountain['name']} - 사진 {st.session_state.image_idx + 1} / {len(mountain['images'])}",
         use_container_width=True)

# 슬라이드 인디케이터 (점으로 현재 위치 표시)
indicator_cols = st.columns(len(mountain["images"]))
for i in range(len(mountain["images"])):
    with indicator_cols[i]:
        if i == st.session_state.image_idx:
            st.markdown("**●**", unsafe_allow_html=True)  # 현재 이미지
        else:
            st.markdown("○", unsafe_allow_html=True)      # 다른 이미지

# folium 지도 생성 및 출력
m = folium.Map(location=[mountain["latitude"], mountain["longitude"]], zoom_start=13)
folium.Marker([mountain["latitude"], mountain["longitude"]], tooltip=mountain["name"]).add_to(m)
st_folium(m, width=700, height=450)

# 관련 역사
st.subheader("관련 역사")
st.write(mountain["history"])

# 근처 맛집 리스트 출력
st.subheader("근처 맛집")
for restaurant in mountain["restaurants"]:
    st.write(f"- {restaurant}")