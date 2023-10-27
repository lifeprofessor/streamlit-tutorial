import streamlit as st

st.write('### :orange[Markdown]')
check1 = st.checkbox('Show Markdown Examples', value=False)
if check1:
    
    st.markdown("*Streamlit* is **really** ***cool***.")

    st.code(f"""
    st.markdown("*Streamlit* is **really** ***cool***.")
            """)

    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')

    st.code(f"""
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors].''')
            """)

    st.markdown("Here is a bouquet &mdash;\
                :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")
    st.code(f"""
    st.markdown("Here is a bouquet &mdash;\:tulip::cherry_blossom::rose::hibiscus:
            :sunflower::blossom:")
            """)


    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)

    st.code(f"""
    multi = '''If you end a line with two spaces,
    a soft return is used for the next line.

    Two (or more) newline characters in a row will result in a hard return.
    '''
    st.markdown(multi)
            """)

    md = st.text_area('Type in your markdown string (without outer quotes)',
                    "Happy Streamlit-ing! :balloon:")

    st.code(f"""
    md = st.text_area('Type in your markdown string (without outer quotes)',
                    "Happy Streamlit-ing! :balloon:")
            """)

    st.code(f"""
    import streamlit as st

    st.markdown('''{md}''')
    """)


    st.markdown(md)
    st.code(f"""
    st.markdown(md)
            """)

st.markdown('---')

st.write('### :orange[Title]')
check2 = st.checkbox('Show Title Examples', value=True)
if check2:
    st.title('This is a title')
    st.code(f'''
    st.title('This is a title')
            ''')

    st.title('_Streamlit_ is :blue[cool] :sunglasses:')
    st.code(f'''
    st.title('_Streamlit_ is :blue[cool] :sunglasses:')

            ''')
st.markdown('---')

st.write('### :orange[Header]')
check3 = st.checkbox('Show Header Examples', value=True)
if check3:
    st.header('This is a header with a divider', divider='rainbow')
    st.code('''
    st.header('This is a header with a divider', divider='rainbow')
            ''')

    st.header('_Streamlit_ is :blue[cool] :sunglasses:')
    st.code('''
    st.header('_Streamlit_ is :blue[cool] :sunglasses:')
            ''')

st.markdown('---')

st.write('### :orange[Sub Header]')
check4 = st.checkbox('Show Sub Header Examples', value=True)
if check4:
    st.subheader('This is a subheader with a divider', divider='rainbow')
    st.code('''
    st.subheader('This is a subheader with a divider', divider='rainbow')
            ''')

    st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
    st.code('''
    st.header('_Streamlit_ is :blue[cool] :sunglasses:')
            ''')

st.markdown('---')

st.write('### :orange[Caption]')
check5 = st.checkbox('Show Caption Examples', value=True)
if check5:
    st.caption('This is a string that explains something above.')
    st.code('''
    st.caption('This is a string that explains something above.')
            ''')

    st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
    st.code('''
    st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
            ''')
    
st.markdown('---')

st.write('### :orange[Code]')
check6 = st.checkbox('Show Code Examples', value=True)
if check6:
    code = '''def hello():
    print("Hello, Streamlit!")'''
    st.code(code, language='python')
    st.code(f'''
    code = \'\'\'def hello():
    print("Hello, Streamlit!")\'\'\'
    st.code(code, language='python')
            ''')
    
st.markdown('---')
st.write('### :orange[Text]')
check7 = st.checkbox('Show Text Examples', value=True)
if check7:
    st.text('This is some text.')
    st.code('''
    st.text('This is some text.')
            ''')
    
st.markdown('---')
st.write('### :orange[Latex]')
check8 = st.checkbox('Show Latex Examples', value=True)
if check8:
    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
    st.code('''
    st.latex(r\'\'\'
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    \'\'\')
            ''')

st.markdown('---')
st.write('### :orange[Divider]')
check9 = st.checkbox('Show Divider Examples', value=True)
if check9:
    st.divider()
    st.write("This is some text.")
    st.slider("This is a slider", 0, 100, (25, 75))
    st.divider()  # 👈 Draws a horizontal rule
    st.write("This text is between the horizontal rules.")

    st.code('''
    st.divider()
    st.write("This is some text.")
    st.slider("This is a slider", 0, 100, (25, 75))
    st.divider()  # 👈 Draws a horizontal rule
    st.write("This text is between the horizontal rules.")
            ''')
    


