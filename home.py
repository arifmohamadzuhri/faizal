import streamlit as st

st.set_page_config(
    page_title="Portfolio | arief mohamad",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SUGENG RAWUH DI PORTFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("About Me")
   st.image("me.jpg", width= 390)

with col2:
   st.header("Data Diri")
   st.subheader("NAMA : MOHAMAD ARIEF FAKHRUDIN Z")
   st.caption("NIM : 0402201102")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 20 Mei 1997 
            - Alamat               : Pengaradan Tanjung Brebes
            - Hobi                 : Ibadah, Sholawatan & Playing Soccer
            - Cita-cita            : sukses dunia akhirat
            - Status               : Punya Nida
            """
        )
   col1, col2, col3, col4, = st.columns(4)
with col1:
   
    st.image("yt.png", width= 50)
    st.link_button("Youtube Chanel", "https://l.instagram.com/?u=https%3A%2F%2Fyoutube.com%2F%40miftahuljannah-hz4bq%3Fsi%3DcEEoMZHnvU__KAJU&e=AT0XewW7_qHmMXPBeOVV0Szc150BexD8EL08l6Zbz8ORqh3h0wLNIth3LsNX7S1CN-di0YJTYmeuOAFEsbDwk3SoMNyxnrZ8P1qE9Xbk5M0dTMFpxxEVxylDWk-Bg8v6Of5ex8Q")
with col2:
   
    st.image("fb.png", width= 50)
    st.link_button("Facebook", "https://l.instagram.com/?u=https%3A%2F%2Fwww.facebook.com%2Farif.elbarca.9%3Fmibextid%3DZbWKwL&e=AT0XewW7_qHmMXPBeOVV0Szc150BexD8EL08l6Zbz8ORqh3h0wLNIth3LsNX7S1CN-di0YJTYmeuOAFEsbDwk3SoMNyxnrZ8P1qE9Xbk5M0dTMFpxxEVxylDWk-Bg8v6Of5ex8Q")
with col3:
    
    st.image("ig.png", width= 50)
    st.link_button("Instagram", "https://instagram.com/arif_alakbar.id?igshid=NzZlODBkYWE4Ng%3D%3D")
with col4:
    
    st.image("tiktok.png", width= 50)
    st.link_button("TikTok", "https://l.instagram.com/?u=https%3A%2F%2Fwww.tiktok.com%2F%40arifalakbar.id%3F_t%3D8hWVXmaAYK2%26_r%3D1&e=AT0XewW7_qHmMXPBeOVV0Szc150BexD8EL08l6Zbz8ORqh3h0wLNIth3LsNX7S1CN-di0YJTYmeuOAFEsbDwk3SoMNyxnrZ8P1qE9Xbk5M0dTMFpxxEVxylDWk-Bg8v6Of5ex8Q ")


st.header("*Call Me If You Want*")

st.link_button("Go to contact", "http://localhost:8501/contact")
