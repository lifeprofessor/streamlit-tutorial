import streamlit as st
import time

st.write('### :orange[progress]')

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.005)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")

st.code('''
import time

progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.005)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")
        ''')

st.write('### :orange[spinner]')

with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Done!')

st.code('''
import time
with st.spinner('Wait for it...'):
    time.sleep(2)
st.success('Done!')
        ''')

st.write('### :orange[status]')

with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button('Rerun2')

st.code('''
with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)

st.button('Rerun2')
        ''')

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.button('Rerun3')

st.code('''
with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.button('Rerun3')
        ''')

st.write('### :orange[toast]')

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

st.code('''
if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')
        ''')

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()

st.code('''
def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()
        ''')

st.write('### :orange[error/warning/info/success/exception]')

st.error('This is an error', icon="🚨")
st.code('''
        st.error('This is an error', icon="🚨")
        ''')
st.warning('This is a warning', icon="⚠️")
st.code('''
        st.warning('This is a warning', icon="⚠️")
        ''')

st.info('This is a purely informational message', icon="ℹ️")
st.code('''
        st.info('This is a purely informational message', icon="ℹ️")
        ''')

st.success('This is a success message!', icon="✅")
st.code('''
        st.success('This is a success message!', icon="✅")
        ''')

e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
st.code('''
e = RuntimeError('This is an exception of type RuntimeError')
st.exception(e)
        ''')