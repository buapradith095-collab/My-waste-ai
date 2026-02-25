import streamlit as st
import google-generativeai as genai
from PIL import Image

# ใส่ API Key ที่ได้จาก Google AI Studio ตรงนี้
API_KEY = "ใส่_API_KEY_ของคุณที่นี่"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI แยกขยะ", page_icon="♻️")
st.title("♻️ ระบบแยกขยะอัจฉริยะ")

uploaded_file = st.file_uploader("ถ่ายรูปหรือเลือกรูปขยะ...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='รูปขยะของคุณ', use_container_width=True)
    
    if st.button('วิเคราะห์เลย!'):
        with st.spinner('AI กำลังคิด...'):
            prompt = "บอกประเภทขยะในรูปนี้ และต้องทิ้งลงถังสีอะไร (เขียว, เหลือง, น้ำเงิน, แดง) พร้อมเหตุผล"
            response = model.generate_content([prompt, image])
            st.success("คำแนะนำจาก AI:")
            st.write(response.text)
