import requests
import streamlit as st
# from streamlit_lottie import st_lottie

st.set_page_config(page_title="Jerome Brown", page_icon=":rocket:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None 
    return r.json()


def local_css(file_name):
    with open(file_name) as f: 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        
local_css("style/style.css")

# lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_vbhx85ve.json")


with st.container():
    st.subheader("Hi, I am Jerome :wave:")
st.title("A innovator from the midwest :beers: ")
st.write("I am passionate about using technology to solve complex problems")


with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What I do")
            st.write("##")
            st.write(
    """
    Build things
    """         
            )
            
            

with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("Reading & Classes :book:")
            st.write("##")
            st.write(
    """
   https://ocw.mit.edu/courses/15-s08-fintech-shaping-the-financial-world-spring-2020/
    """         
            )
            
            
# with right_column:
#     st_lottie(lottie_coding, height=300, key="coding")
 with st.container():
    st.write("---")
        if st.button('Say hello'):
            st.write('Why hello there')
                else:
                 st.write('Goodbye')
    
    
    
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    
    contact_form = """
<form action="https://formsubmit.co/jbreview@outlook.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea> 
    <button type="submit">Send</button>
</form>
"""

    left_column, right_column = st.columns(2)
    
    with left_column:
        
        st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
        
