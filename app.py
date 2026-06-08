import streamlit as st
import pandas as pd
from styles import CSS
from utils import calculate_gematria, calculate_compatibility, generate_magic_square
import datetime

# --- Configuration ---
OWNER_NAME = "المعالج والباحث عمار المصري (طبيب الروح)"
WHATSAPP_NUMBER = "201093642315"
WHATSAPP_NUMBER2 = "201090329193"
TIKTOK_URL = "#"
YOUTUBE_URL = "https://www.youtube.com/@خواطرروحانية"
YOUTUBE_URL2 = "https://www.youtube.com/@ammarelmasre.313"
FACEBOOK_URL = "https://www.facebook.com/ammarelmasre2022"
OWNER_EMAIL = "your@email.com"

YOUTUBE_VIDEOS = [
    {"id": "L1va0lHlepo", "title": "خواطر روحانية — الفيديو المثبت"},
    {"id": "7WrdfWoKDEE", "title": "أحدث المحتوى"},
]

# Page Configuration
st.set_page_config(
    page_title=OWNER_NAME,
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply CSS
st.markdown(CSS, unsafe_allow_html=True)

# Initialize Session State for History
if 'history' not in st.session_state:
    st.session_state.history = []

def add_to_history(tool, input_data, result):
    entry = {
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tool": tool,
        "input": input_data,
        "result": result
    }
    st.session_state.history.append(entry)

# Sidebar Navigation
with st.sidebar:
    st.markdown(f"<h2 style='text-align: center; border: none;'>{OWNER_NAME}</h2>", unsafe_allow_html=True)
    page = st.radio("", ["الرئيسية", "مركز الأبحاث الروحانية", "الخدمات", "التواصل الاجتماعي", "اتصل بنا", "سجل العمليات"])
    
    st.markdown("---")
    st.markdown("### تواصل سريع")
    st.markdown(f"[واتساب 1](https://wa.me/{WHATSAPP_NUMBER}) | [واتساب 2](https://wa.me/{WHATSAPP_NUMBER2})")
    st.markdown(f"[فيسبوك]({FACEBOOK_URL}) | [يوتيوب 1]({YOUTUBE_URL})")

# --- Home Page ---
if page == "الرئيسية":
    st.markdown(f"<h1>{OWNER_NAME}</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("https://img.freepik.com/free-photo/mystical-background-with-burning-candles-and-old-books_23-2149301416.jpg", caption="طبيب الروح")
    
    with col2:
        st.markdown(f"""
        <div class='card arabic-text'>
            <h3>مرحباً بكم في عالم الأسرار</h3>
            <p>أنا <b>عمار المصري</b>، المعالج والباحث في العلوم الروحانية والحرف الملقب بـ <b>طبيب الروح</b>. أقدم لكم هذا الموقع ليكون جسراً بين العلم الروحاني القديم والتقنية الحديثة.</p>
            <p>هنا تجدون أدوات حساب الجمل، التوافق بين الأسماء، وتوليد الأوفاق العددية بدقة متناهية.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3>معرض الفيديوهات المختارة</h3>", unsafe_allow_html=True)
    v_col1, v_col2 = st.columns(2)
    with v_col1:
        st.video(f"https://www.youtube.com/watch?v={YOUTUBE_VIDEOS[0]['id']}")
        st.caption(YOUTUBE_VIDEOS[0]['title'])
    with v_col2:
        st.video(f"https://www.youtube.com/watch?v={YOUTUBE_VIDEOS[1]['id']}")
        st.caption(YOUTUBE_VIDEOS[1]['title'])

# --- Spiritual Research Hub ---
elif page == "مركز الأبحاث الروحانية":
    st.markdown("<h1>مركز الأبحاث الروحانية (الحاسبة)</h1>", unsafe_allow_html=True)
    
    tab_a, tab_b, tab_c = st.tabs(["حساب الجمل (Gematria)", "التوافق (Compatibility)", "مولد الأوفاق (Magic Square)"])
    
    with tab_a:
        st.markdown("<div class='arabic-text'><h3>حساب الجمل الكبير</h3></div>", unsafe_allow_html=True)
        text_input = st.text_input("أدخل الاسم أو النص:", key="gematria_input")
        if st.button("احسب القيمة"):
            if text_input:
                val, element = calculate_gematria(text_input)
                res_text = f"القيمة: {val} | الطبيع: {element}"
                st.markdown(f"<div class='result-box arabic-text'>{res_text}</div>", unsafe_allow_html=True)
                add_to_history("حساب الجمل", text_input, res_text)
            else:
                st.warning("يرجى إدخال نص")

    with tab_b:
        st.markdown("<div class='arabic-text'><h3>قياس التوافق بين شخصين</h3></div>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            name1 = st.text_input("اسم الطالب:")
        with col2:
            name2 = st.text_input("اسم المطلوب:")
            
        if st.button("كشف التوافق"):
            if name1 and name2:
                v1, v2, winner = calculate_compatibility(name1, name2)
                res_text = f"قيمة {name1}: {v1} | قيمة {name2}: {v2} | الغالب: {winner}"
                st.markdown(f"<div class='result-box arabic-text'>{res_text}</div>", unsafe_allow_html=True)
                add_to_history("التوافق", f"{name1} vs {name2}", res_text)
            else:
                st.warning("يرجى إدخال الاسمين")

    with tab_c:
        st.markdown("<div class='arabic-text'><h3>توليد الوفق المثلث (3x3)</h3></div>", unsafe_allow_html=True)
        num_input = st.number_input("أدخل العدد المراد تعميره (Input):", min_value=15, value=15)
        if st.button("توليد الوفق"):
            square = generate_magic_square(num_input)
            if square:
                df = pd.DataFrame(square)
                st.table(df)
                res_text = f"وفق للعدد {num_input}"
                st.markdown(f"<div class='result-box arabic-text'>{res_text}</div>", unsafe_allow_html=True)
                add_to_history("مولد الأوفاق", str(num_input), str(square))

# --- Services ---
elif page == "الخدمات":
    st.markdown("<h1>الخدمات والاستشارات</h1>", unsafe_allow_html=True)
    
    services = [
        {"name": "الاستشارة الروحانية", "desc": "تحليل شامل للحالة الروحانية وتقديم الحلول المناسبة.", "price": "تواصل لتحديد الموعد"},
        {"name": "تحليل السلوك والشخصية", "desc": "دراسة عميقة للشخصية بناءً على علم الحرف والأرقام.", "price": "تواصل لتحديد الموعد"}
    ]
    
    for s in services:
        st.markdown(f"""
        <div class='card arabic-text'>
            <h3>{s['name']}</h3>
            <p>{s['desc']}</p>
            <p><b>السعر:</b> {s['price']}</p>
        </div>
        """, unsafe_allow_html=True)
        msg = f"مرحباً طبيب الروح، أود الاستفسار عن خدمة: {s['name']}"
        whatsapp_link = f"https://wa.me/{WHATSAPP_NUMBER}?text={msg}"
        st.markdown(f"<a href='{whatsapp_link}' target='_blank'><button style='width:100%; padding:10px; background-color:#8B4513; color:#D4AF37; border:none; border-radius:5px; cursor:pointer;'>احجز الآن عبر واتساب</button></a>", unsafe_allow_html=True)

# --- Social Media ---
elif page == "التواصل الاجتماعي":
    st.markdown("<h1>تابعنا على منصات التواصل</h1>", unsafe_allow_html=True)
    
    socials = [
        {"name": "Facebook", "url": FACEBOOK_URL, "desc": "الصفحة الرسمية على فيسبوك"},
        {"name": "YouTube - خواطر روحانية", "url": YOUTUBE_URL, "desc": "القناة الأولى للدروس والخواطر"},
        {"name": "YouTube - عمار المصري", "url": YOUTUBE_URL2, "desc": "القناة الثانية للمحتوى الروحاني"},
        {"name": "TikTok", "url": TIKTOK_URL, "desc": "مقاطع قصيرة وفوائد سريعة"},
    ]
    
    for social in socials:
        st.markdown(f"""
        <div class='card' style='text-align:center;'>
            <h3>{social['name']}</h3>
            <p>{social['desc']}</p>
            <a href='{social['url']}' target='_blank'><button style='width:100%;'>انتقال للحساب</button></a>
        </div>
        """, unsafe_allow_html=True)

# --- Contact ---
elif page == "اتصل بنا":
    st.markdown("<h1>تواصل معنا</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        with st.form("contact_form"):
            name = st.text_input("الاسم الكامل")
            email = st.text_input("البريد الإلكتروني")
            message = st.text_area("رسالتك")
            submitted = st.form_submit_button("إرسال")
            if submitted:
                st.success("تم استلام رسالتك بنجاح، سنرد عليك قريباً.")
    with col2:
        st.markdown(f"""
        <div class='card arabic-text'>
            <h3>معلومات الاتصال المباشر</h3>
            <p><b>الرقم الأساسي:</b> {WHATSAPP_NUMBER}</p>
            <p><b>الرقم الثانوي:</b> {WHATSAPP_NUMBER2}</p>
            <p><b>البريد الإلكتروني:</b> {OWNER_EMAIL}</p>
            <p>نحن متواجدون للرد على استفساراتكم على مدار الساعة.</p>
        </div>
        """, unsafe_allow_html=True)

# --- History ---
elif page == "سجل العمليات":
    st.markdown("<h1>سجل الأبحاث</h1>", unsafe_allow_html=True)
    if st.session_state.history:
        for entry in reversed(st.session_state.history):
            st.markdown(f"""
            <div class='card arabic-text'>
                <small>{entry['time']}</small>
                <h4>{entry['tool']}</h4>
                <p><b>المدخلات:</b> {entry['input']}</p>
                <p><b>النتيجة:</b> {entry['result']}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.info("لا يوجد سجل عمليات حتى الآن.")

# Footer
st.markdown("---")
st.markdown(f"<p style='text-align: center;'>© 2026 {OWNER_NAME} - جميع الحقوق محفوظة</p>", unsafe_allow_html=True)
