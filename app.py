import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image

st.set_page_config(page_title="Short Film", page_icon=":tada:", layout="wide")

def load_lottiefile(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

def local_css(f_name):
    try:
        with open(f_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"CSS file not found: {f_name}")

# Ensure the correct paths to your files
local_css("style\\style.css")
lottie_coding = load_lottiefile("folder\\ss.json")
img_contact_form = Image.open("image\\1.png")
img_lottie_animation = Image.open("image\\2.jpg")

# Use st.sidebar() for the right column
right_column = st.sidebar

with st.container():
    st.subheader("Hi, I am Siva :wave:")
    st.title("A shortfilm actor from Yanam")
    st.write("I am passionate about finding new and young talents to become film workers.")

with st.container():
    st.header('What I Do')
    st.write("##")
    st.write(
        """
        We are a four-member team consisting of Siva (main lead actor), Ravi (production), Durga (writer), and Avinash (DOP).
        We create short films that can be found on the AvinashDigitals YouTube channel. 
        Our team collectively directs the short films, including titles such as 'Maya Grandham' and 'Vunnadhi Okate Life,' both
        """
    )
    st.write("[Youtube channel >](https://www.youtube.com/watch?v=cuHzB5UB3fc)")

# Use right_column for the sidebar
with right_column:
    st_lottie(lottie_coding, height=300, key="acting")

with st.container():
    st.write("---")
    st.header("My projects")
    st.write("##")

    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_contact_form)

    with text_column:
        st.subheader("If you're interested in Film Editing")
        st.write(
            """
            Embark on an exciting journey in the world of editing with Avinash, one of our exceptional editors. Avinash is a dedicated professional, committed to providing comprehensive training and unwavering support to help you refine your editing skills. Under his expert guidance, you can anticipate receiving top-notch training and mentorship in the editing field, ensuring a robust foundation for your creative endeavors. Join us, and let Avinash empower you with the knowledge and tools to thrive in the realm of editing.
            """
        )
        st.markdown("[(Avinash's Editing) Watch video....>](https://www.youtube.com/shorts/yJzV3eQGQwM)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.write(
            """
            Discover the art of editing with Ravi (Sendhil), a stellar member of our editing team. Ravi is a passionate professional, devoted to offering extensive training and steadfast support to assist you in honing your editing skills. With his wealth of experience and insightful guidance, you can anticipate receiving unparalleled training and mentorship in the editing domain, laying the groundwork for a successful creative journey. Join us, and let Ravi empower you with the expertise and tools needed to excel in the dynamic world of editing.
            """
        )
        st.markdown("[(Ravi's editing) Watch video....>](https://www.youtube.com/shorts/WTNuGB_fp_c)")

with st.container():
    st.write("---")
    st.header("Contact")
    st.write("##")
    st.write("If you are interested in contacting me and showing your talents, contact our team on Instagram.")
    st.markdown("[Siva >](https://www.instagram.com/sivaramaraju__/?hl=en)")
    st.markdown("[Durga >](https://www.instagram.com/bannuroyals/?hl=en)")
    st.markdown("[Ravi >](https://www.instagram.com/royalsun1318/?hl=en)")
    st.markdown("[Avinash >](https://www.instagram.com/creator_avihero/?hl=en)")

with st.container():
    st.write("---")
    st.header("GET IN TOUCH WITH ME!")
    st.write("##")
contact_form = """
<form action="https://formsubmit.co/pakalapatisivaramaraju@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <input type="tel" name="phone" placeholder="Your phone number" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
 """
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
