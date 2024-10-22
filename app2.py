import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.write('st.write')

# 样式1——Markdown格式输出
st.write('helllo, *world!* : sunglasses:')  # 接受markdown格式用write输出
# st.markdown('helllo, *world!* :sunglasses:')

# 样式2——数值类型特殊格式
st.write(1234)

# 样式3——python数据框dataframe显示为表格
df = pd.DataFrame({
    'firts column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

# 样式4——支持分段输出
st.write('Below is a DataFrame:', df, 'Above is a dataframe')

# 样式5——图形输出
df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c']
)
st.write(c)