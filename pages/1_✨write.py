import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write('### 안녕하세요. 저는 인생교수입니다. :smile:')
st.write('##### * 누군가의 인생길에 빛이 되고 싶다. ')

df = pd.DataFrame({
    '학년': [1, 2, 3, 4, 5, 6],
    '학생수': [20, 22, 23, 25, 24, 23],
})

st.write('* 초등학교 1~6학년 반별 평균 학생수')
st.write(df)

st.code('''
df = pd.DataFrame({
    '학년': [1, 2, 3, 4, 5, 6],
    '학생수': [20, 22, 23, 25, 24, 23],
})

st.write('* 초등학교 1~6학년 반별 평균 학생수')
st.write(df)
        ''')

st.write('1 + 1 = ', 1+1)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

st.code('''
st.write('1 + 1 = ', 1+1)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
        ''')

df2 = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['x', 'y', 'size'])
st.write(df2)

st.code('''
df2 = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['x', 'y', 'size'])
st.write(df2)
        ''')

chart = alt.Chart(df2).mark_circle().encode(
    x='x', y='y', size='size', color='size', tooltip=['x', 'y', 'size'])

'차트(100개의 랜덤한 수를 산점도로 출력)'
st.write(chart)

st.code('''
chart = alt.Chart(df2).mark_circle().encode(
    x='x', y='y', size='size', color='size', tooltip=['x', 'y', 'size'])

'차트(100개의 랜덤한 수를 산점도로 출력)'
st.write(chart)
        ''')
