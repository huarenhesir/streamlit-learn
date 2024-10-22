import streamlit as st
from datetime import time, datetime

st.header('st.slider 滑块学习')

# 样式1——普通滑块
st.subheader('普通滑块')  # 次级标题

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, "years old")

# 样式2——范围滑块
st.subheader('范围滑块')

values = st.slider(
     'select a range of values',
     0.0, 100.0, (25.0, 75.0))  # 小数点和小数点后的0不可省略
st.write('values: ', values)

# 样式3——时间范围滑块
st.subheader('时间范围滑块')

appointment = st.slider(
     "schedule your appointment:",
     value=(time(11, 30), time(12, 45))
)
st.write("you're scheduled for: ", appointment)

# 样式4——日期时间滑块：
st.subheader("时间滑块")

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="YY/MM/DD - hh:mm"
)
st.write("Start time: ", start_time)