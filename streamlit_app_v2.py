import streamlit as st

st.title("python station")
st.header("streamlit tutorial")
st.subheader("complete streamlit tutorial")
st.text(''' hello python programers
welcome to python station 
hope you are liking it''')
st.write('this is bold writer function')
#image
from PIL import Image
img = Image.open('dashboard.jpeg')
st.image(img,caption="this is ashutosh")
st.success('winner')
st.error('kuch to galat hai')
st.warning('khabardar')
st.info("Note : yaad rakhna warna")
#sidebar

st.sidebar.header('About this development')

st.sidebar.text('''this is the sidebar
of the page
more information
just to see the working''')

#widgets

cb = st.checkbox('show the text')

if cb:
    st.write('thanks for checking the box')

rb = st.radio('what is your gender',('male','female','other'))

if rb == 'male':
    st.success('Go ahead')
elif rb =='female':
    st.warning('wait for clarificaation')
else:
    st.text('you are not allowed')


#selectbox
sb = st.selectbox('What you do for living',[' ','programmer','mechanic','doctor'])
st.write('you are a ',sb)

#multiselect
ms = st.multiselect('what countries do you like ',('india','china','russia','africa'))
st.write('you have made ',len(ms),ms)

#button
if st.button('About the page'):
    st.write('Hey there this page is to show streamlit capabilites')
    
#textinput  
gmail = st.text_input('Enter the gmail')
if '@gmail.com' in gmail:
    st.write('Confirm your gmail : ',gmail)
else:
    st.warning('pls enter correct email adress')

#textarea
st.text_area('Give your feedback ')