[README.md](https://github.com/user-attachments/files/28693858/README.md)
# طبيب الروح | Tabib Al-Rouh — Platform

## 🚀 الإعداد السريع

### 1. تعديل المعلومات الشخصية
افتح ملف `app.py` وعدّل هذه الثوابت في الأعلى:

```python
WHATSAPP_NUMBER = "201XXXXXXXXX"   # رقمك الدولي بدون +
TIKTOK_URL      = "https://tiktok.com/@your_handle"
YOUTUBE_URL     = "https://youtube.com/@your_channel"
INSTAGRAM_URL   = "https://instagram.com/your_handle"
OWNER_EMAIL     = "your@email.com"
```

### 2. إضافة فيديوهات يوتيوب
عدّل قائمة `YOUTUBE_VIDEOS`:
```python
YOUTUBE_VIDEOS = [
    {"id": "VIDEO_ID_HERE", "title": "عنوان الفيديو"},
    ...
]
```
الـ VIDEO_ID هو الجزء بعد `v=` في رابط اليوتيوب.

---

## ☁️ النشر على Streamlit Cloud (مجاناً)

1. ارفع المجلد على GitHub كـ repository جديد
2. اذهب إلى [share.streamlit.io](https://share.streamlit.io)
3. سجّل الدخول بحسابك على GitHub
4. اضغط "New app" واختر الـ repo
5. الملف الرئيسي: `app.py`
6. اضغط Deploy ✅

---

## 🧮 آلية الحسابات

### الجُمَّل الكبير
يعتمد على جدول أبجد هوّز الكلاسيكي (قيم 1–1000).

### العناصر (modulo 4)
- الباقي 0 → النار 🔥
- الباقي 1 → الأرض 🌍
- الباقي 2 → الهواء 💨
- الباقي 3 → الماء 💧

### المربع السحري 3×3
- رقم البداية = (الرقم المُدخل − 8) ÷ 3
- يُملأ بطريقة Siamese (de la Loubère) مع زيادة 1 في كل خطوة
- المجموع السحري يساوي مجموع كل صف وعمود وقطر

---

## 📂 هيكل الملفات

```
tabib_alrouh/
├── app.py              # التطبيق الرئيسي
├── requirements.txt    # المكتبات المطلوبة
├── .streamlit/
│   └── config.toml     # إعدادات المظهر
└── README.md           # هذا الملف
```
