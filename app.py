import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="webfish", page_icon="🐠", layout="wide")

# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()

import streamlit as st

def display_lottie(url, height=300):
    st.markdown(
        f"""
        <iframe src="{url}" width="100%" height="{height}" frameborder="0" allowfullscreen></iframe>
        """,
        unsafe_allow_html=True
    )


#Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
# --- Load Assets ---
# Tampilkan Lottie di Streamlit
# display_lottie("https://lottie.host/embed/f7982d10-b7fd-4d7e-9f58-3af9a2cd64ad/vb4bVHUw5K.lottie")
img_contact_from = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# --- Header Section ---
with st.container():
    st.subheader("Hi, I am Fishbot 🐠")
    st.title("Fishbot, Asisten Pintar untuk Pertumbuhan Ikan")
    st.write("Kami berkomitmen untuk membantu pembudidaya ikan dengan solusi cerdas berbasis AI, memberikan prediksi dan panduan optimal untuk perkembangan ikan air tawar.")
    st.write("[Learn More >](https://efishery.com/)")

# --- What I Do ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: 
        st.header("What I do")
        st.write("##")
        st.write(
            """
             Di channel YouTube kami, Kamu bisa belajar tentang:

            * Membantu pembudidaya ikan memanfaatkan teknologi AI dalam kegiatan sehari-hari.
            Mengatasi tantangan perhitungan rumit dan pengelolaan data pertumbuhan ikan dengan solusi praktis.
            * Belajar menganalisis data dan prediksi pertumbuhan ikan secara akurat untuk hasil yang lebih optimal.
            * Menemukan cara terbaik untuk mengelola perkembangan ikan air tawar dengan efisien dan inovatif.
            * Jika ini menarik bagi Anda, jangan lupa untuk subscribe dan aktifkan notifikasi agar tidak ketinggalan konten terbaru
            """
        )
        st.write("[Youtube Chanel >](http://www.youtube.com/@eFisheryID)")
    with right_column:
    #    st_lottie(lottie_fish, height=300, key="coding") 
    # Tampilkan Lottie di Streamlit
            display_lottie("https://lottie.host/embed/569a15e5-8448-435b-b3b0-46e703bb14af/0QyEuyzLAE.lottie")

       


# --- Projects ---
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write('##')
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column: 
        st.subheader("Fishbot Sahabat Cerdas untuk Budidaya Ikan")
        st.write(
            """
            Punya kendala dengan pertumbuhan ikan air tawar? Tenang, Fishbot hadir untuk membantu!
            Dengan fitur prediksi pintar, panduan praktis, dan teknologi yang mudah digunakan, Fishbot siap jadi solusi andalan Anda.
            Ingin tahu bagaimana Fishbot bisa membuat budidaya ikan jadi lebih mudah dan efisien? Yuk, cari tahu lebih lanjut!
            """
        )
        st.markdown("[watch video...](https://youtu.be/TXSOitGoINE)")
    with st.container():
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_contact_from)
        with text_column:
            st.subheader("Hubungi Fishbot Mudah dan Cepat")
            st.write(
               """
                "Punya pertanyaan seputar perkembangan ikan? Kirim pesan ke Fishbot, dan dapatkan solusi cepat untuk budidaya ikan Anda!".
                """ 
            )
            st.markdown("[Watch Video...](https://youtube.be/FOULV9Xij_8)")


# --- Contact ---
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

 # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/deanramadhan037165@gmail.com" method="POST">
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

# --- Fitur Chatbot ---
# Menambahkan custom CSS untuk membuat tombol tetap di posisi kanan bawah
st.markdown("""
    <style>
    .fixed-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #f9f9f9;
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        z-index: 1000;
    }
    .fixed-button img {
        width: 24px;
        height: 24px;
        vertical-align: middle;
    }
    .fixed-button a {
        text-decoration: none;
        color: navy;
        font-weight: bold;
        margin-left: 4px;
        font-size: 14px;
    }
    </style>

    <div class="fixed-button">
        <a href="https://fishbot-app.streamlit.app/" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/128/6667/6667572.png" alt="fishbot">
            fishbot
        </a>
    </div>
""", unsafe_allow_html=True)
