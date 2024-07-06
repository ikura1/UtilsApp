import re

import qrcode
import streamlit as st


def create_qr_code_image(text: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    return qr.make_image(fill_color="black", back_color="white")


st.set_page_config(page_title="Url2QRCode", page_icon="🌍")
st.markdown("# Url2QRCode")

st.write(
    """
Urlを入力すると、QRコードを生成します。
"""
)

text = st.text_input("Enter text to convert to QR code", "https://google.com")
if not re.match(r"https?://.+", text):
    st.error("Please enter a valid URL starting with http:// or https://")
else:
    image = create_qr_code_image(text)
    image_path = "qr_code.png"

    image.save(image_path)

    st.image(image_path, caption="QR code", use_column_width=True)
