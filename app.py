import streamlit as st
from datetime import datetime
import urllib.parse

# ── Page Config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="طبيب الروح | Tabib Al-Rouh",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Constants ─────────────────────────────────────────────────────────────────
WHATSAPP_NUMBER  = "201093642315"   # الرقم الأول
WHATSAPP_NUMBER2 = "201090329193"   # الرقم الثاني
TIKTOK_URL       = "#"             # سيُضاف الرابط لاحقاً
YOUTUBE_URL      = "https://www.youtube.com/@خواطرروحانية"
YOUTUBE_URL2     = "https://www.youtube.com/@ammarelmasre.313"
FACEBOOK_URL     = "https://www.facebook.com/ammarelmasre2022"
OWNER_NAME       = "طبيب الروح"
OWNER_EMAIL      = "your@email.com"

YOUTUBE_VIDEOS = [
    {"id": "L1va0lHlepo", "title": "خواطر روحانية — الفيديو المثبت"},
    {"id": "7WrdfWoKDEE", "title": "أحدث المحتوى"},
]

# ── Global CSS ────────────────────────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400&family=Cinzel+Decorative:wght@400;700&family=Lateef:wght@300;400;700&display=swap');

    :root {
        --parchment:  #FDF5E6;
        --parchment2: #F5E6CC;
        --gold:       #B8860B;
        --gold-light: #DAA520;
        --mahogany:   #8B4513;
        --mahogany-dark: #5C2E0A;
        --ink:        #2C1A0E;
        --smoke:      #6B4C2A;
        --shadow:     rgba(44,26,14,0.18);
    }

    /* ── Base ── */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--parchment) !important;
        font-family: 'Amiri', serif !important;
        color: var(--ink) !important;
    }
    [data-testid="stAppViewContainer"]::before {
        content: "";
        position: fixed; inset: 0; pointer-events: none; z-index: 0;
        background-image:
            radial-gradient(ellipse at 20% 10%, rgba(184,134,11,.08) 0%, transparent 55%),
            radial-gradient(ellipse at 80% 90%, rgba(139,69,19,.10) 0%, transparent 55%),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='400' height='400'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.65' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='400' height='400' filter='url(%23n)' opacity='.04'/%3E%3C/svg%3E");
    }
    [data-testid="stHeader"] { display: none; }
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stBottomBlockContainer"] { display: none; }
    footer { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar { width: 6px; }
    ::-webkit-scrollbar-track { background: var(--parchment2); }
    ::-webkit-scrollbar-thumb { background: var(--gold); border-radius: 3px; }

    /* ── Navbar ── */
    .navbar {
        display: flex; align-items: center; justify-content: space-between;
        padding: 14px 48px;
        background: linear-gradient(135deg, var(--mahogany-dark) 0%, var(--mahogany) 60%, var(--mahogany-dark) 100%);
        border-bottom: 2px solid var(--gold);
        box-shadow: 0 4px 24px var(--shadow);
        position: sticky; top: 0; z-index: 999;
        direction: rtl;
    }
    .navbar-logo {
        font-family: 'Cinzel Decorative', serif;
        font-size: 1.45rem; font-weight: 700;
        color: var(--gold-light);
        letter-spacing: 2px;
        text-shadow: 0 2px 8px rgba(0,0,0,.4);
    }
    .navbar-logo span { color: #fff; font-size: .85rem; display: block; font-family: 'Amiri', serif; font-weight:400; letter-spacing:1px; }
    .nav-links { display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }
    .nav-btn {
        background: transparent;
        border: 1px solid rgba(218,165,32,.4);
        color: var(--parchment);
        padding: 6px 18px; border-radius: 20px;
        font-family: 'Amiri', serif; font-size: 1rem;
        cursor: pointer; transition: all .25s;
        text-decoration: none; display: inline-block;
    }
    .nav-btn:hover, .nav-btn.active {
        background: var(--gold); color: var(--ink);
        border-color: var(--gold);
        box-shadow: 0 0 12px rgba(218,165,32,.5);
    }

    /* ── Hero ── */
    .hero {
        text-align: center; padding: 80px 24px 60px;
        background: linear-gradient(180deg, rgba(139,69,19,.06) 0%, transparent 100%);
        position: relative;
    }
    .hero-ornament { font-size: 2.2rem; color: var(--gold); opacity: .6; letter-spacing: 8px; }
    .hero-title {
        font-family: 'Cinzel Decorative', serif;
        font-size: clamp(2.2rem, 5vw, 3.8rem);
        color: var(--mahogany);
        text-shadow: 2px 2px 0 rgba(184,134,11,.2);
        margin: 12px 0 4px;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-family: 'Lateef', serif;
        font-size: clamp(1.3rem, 2.5vw, 1.9rem);
        color: var(--gold); letter-spacing: 4px; margin-bottom: 20px;
    }
    .hero-desc {
        max-width: 680px; margin: 0 auto 36px;
        font-size: 1.18rem; line-height: 1.9;
        color: var(--smoke); direction: rtl;
    }
    .hero-cta {
        display: inline-block;
        background: linear-gradient(135deg, var(--mahogany), var(--mahogany-dark));
        color: var(--gold-light) !important;
        padding: 14px 40px; border-radius: 30px;
        font-family: 'Amiri', serif; font-size: 1.2rem;
        text-decoration: none;
        border: 1px solid var(--gold);
        box-shadow: 0 4px 20px rgba(139,69,19,.35);
        transition: all .3s;
        cursor: pointer;
    }
    .hero-cta:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(139,69,19,.5);
        background: linear-gradient(135deg, var(--gold), var(--gold-light));
        color: var(--ink) !important;
    }

    /* ── Section Divider ── */
    .section-divider {
        display: flex; align-items: center;
        gap: 16px; margin: 0 auto 40px;
        max-width: 600px; padding: 0 24px;
    }
    .divider-line { flex: 1; height: 1px; background: linear-gradient(90deg, transparent, var(--gold), transparent); }
    .divider-gem { color: var(--gold); font-size: 1.3rem; }

    /* ── Section Title ── */
    .section-title {
        font-family: 'Cinzel Decorative', serif;
        font-size: clamp(1.4rem, 3vw, 2.2rem);
        color: var(--mahogany); text-align: center;
        margin-bottom: 6px;
    }
    .section-sub {
        font-family: 'Lateef', serif;
        font-size: 1.15rem; color: var(--gold);
        text-align: center; margin-bottom: 32px;
        letter-spacing: 3px;
    }

    /* ── Cards ── */
    .card {
        background: linear-gradient(145deg, #fffdf7, var(--parchment2));
        border: 1px solid rgba(184,134,11,.3);
        border-radius: 12px;
        padding: 28px 24px;
        box-shadow: 0 4px 20px var(--shadow);
        transition: transform .25s, box-shadow .25s;
        direction: rtl;
    }
    .card:hover { transform: translateY(-4px); box-shadow: 0 8px 32px var(--shadow); }
    .card-icon { font-size: 2.4rem; margin-bottom: 12px; }
    .card-title {
        font-family: 'Cinzel Decorative', serif;
        font-size: 1.1rem; color: var(--mahogany); margin-bottom: 10px;
    }
    .card-body { font-size: 1.05rem; line-height: 1.8; color: var(--smoke); }

    /* ── Result Box ── */
    .result-box {
        background: linear-gradient(135deg, var(--mahogany-dark), var(--mahogany));
        border: 1px solid var(--gold);
        border-radius: 12px; padding: 28px 24px;
        color: var(--parchment); text-align: center;
        margin-top: 24px; direction: rtl;
        box-shadow: 0 6px 24px rgba(92,46,10,.4);
    }
    .result-number {
        font-family: 'Cinzel Decorative', serif;
        font-size: 3.5rem; color: var(--gold-light);
        text-shadow: 0 0 20px rgba(218,165,32,.6);
    }
    .result-label { font-family: 'Lateef', serif; font-size: 1.3rem; color: var(--parchment2); letter-spacing: 2px; }
    .result-element { font-size: 1.6rem; margin-top: 8px; }

    /* ── Magic Square ── */
    .magic-table {
        margin: 0 auto;
        border-collapse: separate;
        border-spacing: 6px;
    }
    .magic-cell {
        width: 72px; height: 72px;
        background: linear-gradient(135deg, var(--mahogany-dark), var(--mahogany));
        color: var(--gold-light);
        font-family: 'Cinzel Decorative', serif;
        font-size: 1.5rem;
        text-align: center; vertical-align: middle;
        border: 1px solid var(--gold);
        border-radius: 8px;
        box-shadow: inset 0 2px 6px rgba(0,0,0,.3);
    }

    /* ── Service Cards ── */
    .service-card {
        background: linear-gradient(160deg, #fffdf5, var(--parchment2));
        border: 1px solid rgba(184,134,11,.4);
        border-top: 4px solid var(--gold);
        border-radius: 14px; padding: 32px 28px;
        text-align: center; direction: rtl;
        box-shadow: 0 6px 28px var(--shadow);
        transition: transform .3s, box-shadow .3s;
    }
    .service-card:hover { transform: translateY(-6px); box-shadow: 0 12px 40px var(--shadow); }
    .service-icon { font-size: 3rem; margin-bottom: 16px; }
    .service-title {
        font-family: 'Cinzel Decorative', serif;
        font-size: 1.15rem; color: var(--mahogany); margin-bottom: 12px;
    }
    .service-desc { font-size: 1.08rem; line-height: 1.8; color: var(--smoke); margin-bottom: 24px; }
    .wa-btn {
        display: inline-block;
        background: linear-gradient(135deg, #25D366, #128C7E);
        color: #fff !important; text-decoration: none;
        padding: 12px 32px; border-radius: 25px;
        font-family: 'Amiri', serif; font-size: 1.1rem;
        box-shadow: 0 4px 16px rgba(37,211,102,.35);
        transition: all .3s;
    }
    .wa-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(37,211,102,.5); }

    /* ── Bio ── */
    .bio-section {
        background: linear-gradient(135deg, var(--mahogany-dark), var(--mahogany));
        color: var(--parchment); padding: 60px 40px;
        direction: rtl; position: relative; overflow: hidden;
    }
    .bio-section::before {
        content: "🔮";
        position: absolute; right: -20px; top: 50%; transform: translateY(-50%);
        font-size: 12rem; opacity: .05;
    }
    .bio-title {
        font-family: 'Cinzel Decorative', serif;
        font-size: 1.8rem; color: var(--gold-light);
        margin-bottom: 20px;
    }
    .bio-text { font-size: 1.15rem; line-height: 2.1; max-width: 700px; }

    /* ── Contact Form ── */
    .contact-wrapper {
        background: linear-gradient(145deg, #fffdf7, var(--parchment2));
        border: 1px solid rgba(184,134,11,.35);
        border-radius: 16px; padding: 40px 36px;
        box-shadow: 0 6px 30px var(--shadow);
        direction: rtl;
        max-width: 580px; margin: 0 auto;
    }

    /* ── Social Icons ── */
    .social-row { display: flex; gap: 20px; justify-content: center; margin: 32px 0; }
    .social-icon {
        display: inline-flex; align-items: center; justify-content: center;
        width: 52px; height: 52px; border-radius: 50%;
        font-size: 1.4rem; text-decoration: none;
        border: 2px solid var(--gold);
        color: var(--mahogany);
        background: var(--parchment2);
        transition: all .3s;
        box-shadow: 0 3px 12px var(--shadow);
    }
    .social-icon:hover {
        background: var(--mahogany); color: var(--gold-light);
        transform: translateY(-4px) scale(1.08);
        box-shadow: 0 8px 24px rgba(139,69,19,.4);
    }

    /* ── History Log ── */
    .log-entry {
        background: var(--parchment2);
        border-right: 3px solid var(--gold);
        border-radius: 0 8px 8px 0;
        padding: 12px 16px; margin-bottom: 10px;
        font-size: .95rem; direction: rtl;
        color: var(--ink);
    }
    .log-time { font-size: .8rem; color: var(--smoke); }

    /* ── Streamlit overrides ── */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: #fffdf5 !important;
        border: 1px solid rgba(184,134,11,.4) !important;
        border-radius: 8px !important;
        font-family: 'Amiri', serif !important;
        font-size: 1.05rem !important;
        color: var(--ink) !important;
        direction: rtl;
    }
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: var(--gold) !important;
        box-shadow: 0 0 0 2px rgba(184,134,11,.2) !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, var(--mahogany), var(--mahogany-dark)) !important;
        color: var(--gold-light) !important;
        border: 1px solid var(--gold) !important;
        font-family: 'Amiri', serif !important;
        font-size: 1.1rem !important;
        padding: 10px 32px !important;
        border-radius: 25px !important;
        transition: all .25s !important;
        box-shadow: 0 4px 16px rgba(139,69,19,.3) !important;
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 24px rgba(139,69,19,.5) !important;
        background: linear-gradient(135deg, var(--gold), var(--gold-light)) !important;
        color: var(--ink) !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent !important;
        border-bottom: 1px solid rgba(184,134,11,.3) !important;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        color: var(--smoke) !important;
        font-family: 'Amiri', serif !important;
        font-size: 1.1rem !important;
        border-radius: 8px 8px 0 0 !important;
        border: none !important;
        padding: 10px 24px !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, var(--mahogany), var(--mahogany-dark)) !important;
        color: var(--gold-light) !important;
    }
    label[data-testid="stWidgetLabel"] {
        font-family: 'Amiri', serif !important;
        font-size: 1.05rem !important;
        color: var(--mahogany) !important;
        font-weight: 700 !important;
        direction: rtl;
    }
    .stAlert { border-radius: 10px !important; font-family: 'Amiri', serif !important; }
    div[data-testid="column"] { padding: 0 10px !important; }
    .stMarkdown p { direction: rtl; }

    /* ── Responsive ── */
    @media (max-width: 768px) {
        .navbar { padding: 12px 20px; flex-direction: column; gap: 12px; }
        .hero { padding: 50px 16px 40px; }
        .bio-section { padding: 40px 20px; }
        .contact-wrapper { padding: 28px 20px; }
    }
    </style>
    """, unsafe_allow_html=True)

# ── Helpers ───────────────────────────────────────────────────────────────────
GEMATRIA_MAP = {
    'أ': 1,  'ا': 1,  'ب': 2,  'ج': 3,  'د': 4,  'ه': 5,  'و': 6,
    'ز': 7,  'ح': 8,  'ط': 9,  'ي': 10, 'ى': 10, 'ك': 20, 'ل': 30,
    'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90, 'ق': 100,
    'ر': 200,'ش': 300,'ت': 400,'ث': 500,'خ': 600,'ذ': 700,'ض': 800,
    'ظ': 900,'غ': 1000,'ة': 5,  'ء': 1,  'ئ': 10, 'ؤ': 6,  'إ': 1,
    'آ': 1,
}
ELEMENTS = {0: ("🔥 النار", "fire"), 1: ("🌍 الأرض", "earth"), 2: ("💨 الهواء", "air"), 3: ("💧 الماء", "water")}
ELEMENT_COLORS = {"fire": "#c0392b", "earth": "#8B4513", "air": "#2980b9", "water": "#16a085"}

def calc_gematria(text: str) -> int:
    return sum(GEMATRIA_MAP.get(c, 0) for c in text)

def digit_sum(n: int) -> int:
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def get_element(value: int):
    r = value % 4
    return ELEMENTS[r]

def build_whatsapp_url(service: str, number: int = 1) -> str:
    msg = f"السلام عليكم، أريد الاستفسار عن خدمة: {service}"
    num = WHATSAPP_NUMBER if number == 1 else WHATSAPP_NUMBER2
    return f"https://wa.me/{num}?text={urllib.parse.quote(msg)}"

def magic_square_3x3(start: int):
    """Fill 3x3 magic square starting from 'start', increment by 1."""
    n = start
    sq = [[0]*3 for _ in range(3)]
    # Siamese method (de la Loubère)
    i, j = 0, 1  # start position: row 0, col 1
    for _ in range(9):
        sq[i][j] = n
        n += 1
        ni, nj = (i - 1) % 3, (j + 1) % 3
        if sq[ni][nj] != 0:
            ni, nj = (i + 1) % 3, j
        i, j = ni, nj
    return sq

def log_result(section: str, text: str):
    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.insert(0, {
        "section": section,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S")
    })
    if len(st.session_state.history) > 30:
        st.session_state.history = st.session_state.history[:30]

# ── Components ────────────────────────────────────────────────────────────────
def render_navbar(active="home"):
    pages = [
        ("home",     "🏠 الرئيسية"),
        ("research", "🔮 مركز البحث"),
        ("services", "✨ الخدمات"),
        ("contact",  "📬 تواصل معنا"),
    ]
    links_html = "".join(
        f'<a class="nav-btn {"active" if p[0]==active else ""}" '
        f'href="?page={p[0]}">{p[1]}</a>'
        for p in pages
    )
    st.markdown(f"""
    <nav class="navbar">
        <div class="navbar-logo">
            TABIB AL-ROUH
            <span>طبيب الروح ✦ علوم روحانية</span>
        </div>
        <div class="nav-links">{links_html}</div>
    </nav>
    """, unsafe_allow_html=True)

def render_footer():
    st.markdown(f"""
    <div style="background:var(--mahogany-dark);color:var(--parchment2);
                text-align:center;padding:36px 24px;direction:rtl;
                border-top:2px solid var(--gold);margin-top:60px;">
        <div class="social-row">
            <a class="social-icon" href="{TIKTOK_URL}" target="_blank" title="TikTok">𝕋</a>
            <a class="social-icon" href="{YOUTUBE_URL}" target="_blank" title="خواطر روحانية">▶</a>
            <a class="social-icon" href="{YOUTUBE_URL2}" target="_blank" title="القناة الثانية">▶</a>
            <a class="social-icon" href="{FACEBOOK_URL}" target="_blank" title="Facebook">f</a>
            <a class="social-icon" href="{build_whatsapp_url('استفسار عام', 1)}" target="_blank" title="واتساب 1">💬</a>
            <a class="social-icon" href="{build_whatsapp_url('استفسار عام', 2)}" target="_blank" title="واتساب 2">💬</a>
        </div>
        <p style="font-family:'Lateef',serif;font-size:1.1rem;color:var(--gold);letter-spacing:3px;margin:0;">
            ✦ طبيب الروح ✦ جميع الحقوق محفوظة {datetime.now().year} ✦
        </p>
    </div>
    """, unsafe_allow_html=True)

def section_header(title: str, sub: str = ""):
    st.markdown(f"""
    <div class="section-divider"><div class="divider-line"></div>
        <span class="divider-gem">◆</span><div class="divider-line"></div></div>
    <h2 class="section-title">{title}</h2>
    {"" if not sub else f'<p class="section-sub">{sub}</p>'}
    """, unsafe_allow_html=True)

# ── Pages ─────────────────────────────────────────────────────────────────────
def page_home():
    render_navbar("home")

    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-ornament">✦ ✦ ✦</div>
        <h1 class="hero-title">TABIB AL-ROUH</h1>
        <div class="hero-subtitle">طبيب الروح</div>
        <p class="hero-desc">
            مرحباً بكم في عالم العلوم الروحانية والحسابات الغيبية — حيث يلتقي العلم القديم
            بالحكمة الخالدة. استكشف أسرار الأسماء، وتوافق الأرواح، وأنوار المربعات السحرية.
        </p>
        <a class="hero-cta" href="?page=services">احجز استشارتك الآن ✦</a>
    </div>
    """, unsafe_allow_html=True)

    # Bio
    st.markdown("""
    <div class="bio-section">
        <div style="max-width:900px;margin:0 auto;display:flex;gap:40px;align-items:center;flex-wrap:wrap;">
            <div style="font-size:6rem;">🔮</div>
            <div>
                <h3 class="bio-title">من أنا؟</h3>
                <p class="bio-text">
                    أنا <strong style="color:var(--gold-light);">طبيب الروح</strong> — باحث في العلوم الروحانية والحسابات الجُمَّلية،
                    أمضيت سنوات في دراسة أسرار الحروف والأرقام وتأثيرها على الإنسان وحياته.
                    أقدم استشارات شخصية متخصصة في تحليل الشخصية، دراسة التوافق، وإعداد الأحجبة
                    والمربعات السحرية وفق الأسس العلمية الموروثة.
                    <br/><br/>
                    🔸 أكثر من [X] سنة خبرة &nbsp;|&nbsp; 🔸 آلاف الحالات المدروسة &nbsp;|&nbsp; 🔸 نتائج موثقة
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # YouTube Gallery
    st.markdown("<div style='padding:60px 40px 20px;'>", unsafe_allow_html=True)
    section_header("أحدث المحتوى", "✦ قناتي على يوتيوب ✦")

    cols = st.columns(len(YOUTUBE_VIDEOS))
    for col, vid in zip(cols, YOUTUBE_VIDEOS):
        with col:
            st.markdown(f"""
            <div class="card" style="padding:0;overflow:hidden;">
                <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;">
                    <iframe style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;"
                        src="https://www.youtube.com/embed/{vid['id']}"
                        title="{vid['title']}" allowfullscreen></iframe>
                </div>
                <p style="padding:12px;text-align:center;font-family:'Amiri',serif;
                          font-size:1rem;color:var(--mahogany);font-weight:700;direction:rtl;">
                    {vid['title']}
                </p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # CTA strip
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,var(--mahogany-dark),var(--mahogany));
                text-align:center;padding:50px 24px;margin-top:40px;direction:rtl;">
        <h3 style="font-family:'Cinzel Decorative',serif;color:var(--gold-light);
                   font-size:1.6rem;margin-bottom:16px;">هل تريد معرفة أسرار اسمك؟</h3>
        <p style="color:var(--parchment2);font-size:1.15rem;margin-bottom:28px;">
            احجز استشارة شخصية مع طبيب الروح الآن وابدأ رحلتك نحو المعرفة
        </p>
        <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
            <a class="hero-cta" href="{build_whatsapp_url('استشارة روحانية', 1)}" target="_blank">
                💬 واتساب 1
            </a>
            <a class="hero-cta" href="{build_whatsapp_url('استشارة روحانية', 2)}" target="_blank">
                💬 واتساب 2
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_footer()


def page_research():
    render_navbar("research")
    st.markdown("<div style='padding:50px 32px 20px;'>", unsafe_allow_html=True)
    section_header("مركز البحث الروحاني", "✦ الحاسبة العلمية ✦")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🔢 الجُمَّل الكبير",
        "⚖️ التوافق",
        "🟫 المربع السحري",
        "📜 سجل النتائج",
    ])

    # ── Tab A: Gematria ──
    with tab1:
        st.markdown("<div style='direction:rtl;padding:20px 0;'>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="margin-bottom:24px;">
            <div class="card-icon">🔢</div>
            <div class="card-title">حاسبة الجُمَّل الكبير</div>
            <div class="card-body">
                أدخل نصاً أو اسماً لحساب قيمته الجُمَّلية الكبرى واستخراج عنصره الطبيعي.
            </div>
        </div>
        """, unsafe_allow_html=True)

        name_input = st.text_input("أدخل النص أو الاسم:", key="gem_input", placeholder="مثال: محمد")
        if st.button("احسب الجُمَّل ✦", key="gem_btn"):
            if name_input.strip():
                val = calc_gematria(name_input.strip())
                elem_label, elem_key = get_element(val)
                color = ELEMENT_COLORS[elem_key]
                log_result("الجُمَّل", f"{name_input} → {val} | العنصر: {elem_label}")
                st.markdown(f"""
                <div class="result-box">
                    <div class="result-label">القيمة الجُمَّلية لـ «{name_input}»</div>
                    <div class="result-number">{val:,}</div>
                    <div class="result-element" style="color:{color};font-size:1.8rem;margin-top:12px;">
                        عنصره: {elem_label}
                    </div>
                    <div style="font-size:.95rem;color:var(--parchment2);margin-top:12px;opacity:.8;">
                        الباقي من القسمة على 4 = {val % 4}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                # Breakdown table
                breakdown = [(c, GEMATRIA_MAP.get(c, 0)) for c in name_input if GEMATRIA_MAP.get(c, 0) > 0]
                if breakdown:
                    st.markdown("<br/><strong style='direction:rtl;color:var(--mahogany);font-family:Amiri,serif;'>تفصيل الحروف:</strong>", unsafe_allow_html=True)
                    cells = "".join(
                        f"<td style='padding:8px 14px;border:1px solid rgba(184,134,11,.3);text-align:center;"
                        f"font-family:Amiri,serif;background:var(--parchment2);'>{c}<br/>"
                        f"<strong style='color:var(--mahogany);'>{v}</strong></td>"
                        for c, v in breakdown
                    )
                    st.markdown(f"""
                    <div style='overflow-x:auto;direction:rtl;margin-top:8px;'>
                        <table style='border-collapse:collapse;margin:0 auto;'><tr>{cells}</tr></table>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("يرجى إدخال نص للحساب.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Tab B: Compatibility ──
    with tab2:
        st.markdown("<div style='direction:rtl;padding:20px 0;'>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="margin-bottom:24px;">
            <div class="card-icon">⚖️</div>
            <div class="card-title">حاسبة التوافق</div>
            <div class="card-body">
                قارن بين اسمين لمعرفة أيهما أقوى تأثيراً وأعلى قيمةً روحانية.
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            name_a = st.text_input("الاسم الأول (الطالب):", key="compat_a", placeholder="مثال: أحمد")
        with c2:
            name_b = st.text_input("الاسم الثاني (الهدف):", key="compat_b", placeholder="مثال: سارة")

        if st.button("قارن الآن ✦", key="compat_btn"):
            if name_a.strip() and name_b.strip():
                val_a = calc_gematria(name_a.strip())
                val_b = calc_gematria(name_b.strip())
                elem_a = get_element(val_a)
                elem_b = get_element(val_b)

                if val_a > val_b:
                    winner, loser, wv, lv = name_a, name_b, val_a, val_b
                elif val_b > val_a:
                    winner, loser, wv, lv = name_b, name_a, val_b, val_a
                else:
                    winner = loser = "تعادل تام"
                    wv = lv = val_a

                log_result("التوافق", f"{name_a}({val_a}) vs {name_b}({val_b}) → الفائز: {winner}")

                st.markdown(f"""
                <div style="display:flex;gap:16px;justify-content:center;flex-wrap:wrap;margin-top:20px;">
                    <div class="result-box" style="flex:1;min-width:200px;">
                        <div class="result-label">{name_a}</div>
                        <div class="result-number" style="font-size:2.5rem;">{val_a:,}</div>
                        <div class="result-element">{elem_a[0]}</div>
                    </div>
                    <div style="display:flex;align-items:center;font-size:2rem;color:var(--gold);">⚡</div>
                    <div class="result-box" style="flex:1;min-width:200px;">
                        <div class="result-label">{name_b}</div>
                        <div class="result-number" style="font-size:2.5rem;">{val_b:,}</div>
                        <div class="result-element">{elem_b[0]}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if winner != "تعادل تام":
                    diff = abs(wv - lv)
                    pct = round((wv / (wv + lv)) * 100) if (wv + lv) > 0 else 50
                    st.markdown(f"""
                    <div style="background:linear-gradient(135deg,#5C2E0A,var(--mahogany));
                                border:2px solid var(--gold);border-radius:14px;
                                padding:28px;text-align:center;color:var(--parchment);
                                direction:rtl;margin-top:20px;">
                        <div style="font-size:2.5rem;">🏆</div>
                        <div style="font-family:'Cinzel Decorative',serif;
                                    color:var(--gold-light);font-size:1.5rem;margin:8px 0;">
                            الفائز: «{winner}»
                        </div>
                        <div style="font-size:1.05rem;color:var(--parchment2);">
                            بفارق {diff:,} نقطة &nbsp;|&nbsp; قوة {pct}%
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="background:linear-gradient(135deg,#5C2E0A,var(--mahogany));
                                border:2px solid var(--gold);border-radius:14px;
                                padding:28px;text-align:center;color:var(--parchment);
                                direction:rtl;margin-top:20px;">
                        <div style="font-size:2rem;color:var(--gold-light);">⚖️ تعادل تام — القوتان متساويتان</div>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.warning("يرجى إدخال الاسمين معاً.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Tab C: Magic Square ──
    with tab3:
        st.markdown("<div style='direction:rtl;padding:20px 0;'>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="margin-bottom:24px;">
            <div class="card-icon">🟫</div>
            <div class="card-title">مولّد المربع السحري 3×3</div>
            <div class="card-body">
                أدخل رقماً لاستخراج المربع السحري. رقم البداية = (الرقم − 8) ÷ 3.
            </div>
        </div>
        """, unsafe_allow_html=True)

        num_input = st.text_input("أدخل الرقم المطلوب:", key="sq_input", placeholder="مثال: 11 أو 20")
        if st.button("ولِّد المربع ✦", key="sq_btn"):
            try:
                raw = int(num_input.strip())
                if (raw - 8) % 3 != 0:
                    st.error("⚠️ الرقم المُدخل يجب أن يكون من الشكل (3k + 8) مثل: 11، 14، 17، 20 ...")
                else:
                    start = (raw - 8) // 3
                    sq = magic_square_3x3(start)
                    row_sums = [sum(r) for r in sq]
                    col_sums = [sum(sq[r][c] for r in range(3)) for c in range(3)]
                    magic_sum = row_sums[0]
                    log_result("المربع السحري", f"رقم {raw} → بداية {start} | المجموع السحري {magic_sum}")

                    cells_html = ""
                    for row in sq:
                        cells_html += "<tr>"
                        for v in row:
                            cells_html += f'<td class="magic-cell">{v}</td>'
                        cells_html += "</tr>"

                    st.markdown(f"""
                    <div style="text-align:center;margin-top:20px;">
                        <div style="font-family:'Amiri',serif;font-size:1.1rem;
                                    color:var(--smoke);margin-bottom:16px;direction:rtl;">
                            رقم البداية: <strong style="color:var(--mahogany);">{start}</strong>
                            &nbsp;|&nbsp; الرقم المُدخل: <strong style="color:var(--mahogany);">{raw}</strong>
                        </div>
                        <table class="magic-table">{cells_html}</table>
                        <div style="margin-top:20px;background:var(--mahogany-dark);
                                    color:var(--gold-light);padding:14px 24px;
                                    border-radius:10px;display:inline-block;
                                    font-family:'Cinzel Decorative',serif;font-size:1.15rem;
                                    border:1px solid var(--gold);">
                            ✦ المجموع السحري = {magic_sum} ✦
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Verification
                    diag1 = sq[0][0] + sq[1][1] + sq[2][2]
                    diag2 = sq[0][2] + sq[1][1] + sq[2][0]
                    ok = all(s == magic_sum for s in row_sums + col_sums + [diag1, diag2])
                    st.markdown(f"""
                    <div style="text-align:center;margin-top:14px;
                                color:{'#27ae60' if ok else '#e74c3c'};
                                font-family:'Amiri',serif;font-size:1.05rem;">
                        {'✅ المربع صحيح — كل الصفوف والأعمدة والأقطار تساوي ' + str(magic_sum)
                         if ok else '⚠️ تحقق من الحساب'}
                    </div>
                    """, unsafe_allow_html=True)
            except ValueError:
                st.error("يرجى إدخال رقم صحيح.")
        st.markdown("</div>", unsafe_allow_html=True)

    # ── Tab D: History ──
    with tab4:
        st.markdown("<div style='direction:rtl;padding:20px 0;'>", unsafe_allow_html=True)
        section_header("سجل النتائج", "✦ آخر 30 عملية حسابية ✦")

        if "history" not in st.session_state or not st.session_state.history:
            st.info("لا توجد نتائج مسجلة بعد. استخدم الحاسبة أولاً.")
        else:
            if st.button("مسح السجل 🗑️", key="clear_log"):
                st.session_state.history = []
                st.rerun()
            st.markdown("<br/>", unsafe_allow_html=True)
            for entry in st.session_state.history:
                st.markdown(f"""
                <div class="log-entry">
                    <span style="color:var(--gold);font-weight:700;">[{entry['section']}]</span>
                    &nbsp;{entry['text']}
                    <span class="log-time"> — {entry['time']}</span>
                </div>
                """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    render_footer()


def page_services():
    render_navbar("services")
    st.markdown("<div style='padding:60px 32px;'>", unsafe_allow_html=True)
    section_header("خدماتي", "✦ استثمر في روحك ✦")

    services = [
        {
            "icon": "🔮",
            "title": "الاستشارة الروحانية",
            "desc": "جلسة شخصية متخصصة لتحليل اسمك وتاريخ ميلادك واستخراج الطاقة الروحانية المحيطة بك، مع توجيهات عملية لتحسين مسار حياتك.",
            "price": "تواصل لمعرفة السعر",
            "msg": "استشارة روحانية شخصية",
            "features": ["تحليل الاسم الكامل", "قراءة عنصر الشخصية", "توجيهات روحانية مخصصة"],
        },
        {
            "icon": "🧠",
            "title": "تحليل الشخصية",
            "desc": "دراسة معمّقة لشخصيتك من خلال حسابات الجُمَّل الكبير، واستخراج صفاتك الجوهرية، ونقاط القوة والضعف، وتحديد أفضل القرارات لك.",
            "price": "تواصل لمعرفة السعر",
            "msg": "تحليل الشخصية بالجُمَّل الكبير",
            "features": ["تقرير مكتوب شامل", "تحليل الاسم والكنية", "خريطة الشخصية الكاملة"],
        },
        {
            "icon": "💑",
            "title": "دراسة التوافق",
            "desc": "هل أنت متوافق مع شريكك أو شريكتك؟ احصل على إجابة علمية دقيقة من خلال مقارنة الأسماء وحسابات التوافق الروحاني.",
            "price": "تواصل لمعرفة السعر",
            "msg": "دراسة التوافق بين شخصين",
            "features": ["تقييم درجة التوافق", "تحليل عناصر الطرفين", "توصيات للتحسين"],
        },
        {
            "icon": "🟫",
            "title": "المربعات السحرية",
            "desc": "إعداد مربعات سحرية مخصصة بناءً على اسمك ورقمك الجُمَّلي، مكتوبة بالطريقة التقليدية الصحيحة وفق الأسس العلمية الموروثة.",
            "price": "تواصل لمعرفة السعر",
            "msg": "طلب مربع سحري مخصص",
            "features": ["مربع 3×3 مخصص", "شرح تفصيلي", "استخدامات وتوجيهات"],
        },
    ]

    cols = st.columns(2)
    for i, svc in enumerate(services):
        with cols[i % 2]:
            feats_html = "".join(f"<li style='margin:4px 0;'>✦ {f}</li>" for f in svc["features"])
            wa_url  = build_whatsapp_url(svc["msg"], 1)
            wa_url2 = build_whatsapp_url(svc["msg"], 2)
            st.markdown(f"""
            <div class="service-card" style="margin-bottom:24px;">
                <div class="service-icon">{svc['icon']}</div>
                <div class="service-title">{svc['title']}</div>
                <div class="service-desc">{svc['desc']}</div>
                <ul style="text-align:right;list-style:none;padding:0;
                           color:var(--smoke);font-size:1rem;margin-bottom:20px;">
                    {feats_html}
                </ul>
                <div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">
                    <a class="wa-btn" href="{wa_url}" target="_blank">💬 واتساب 1</a>
                    <a class="wa-btn" href="{wa_url2}" target="_blank">💬 واتساب 2</a>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Guarantee strip
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,var(--mahogany-dark),var(--mahogany));
                padding:50px 40px;text-align:center;direction:rtl;
                border-radius:16px;margin-top:40px;
                border:1px solid var(--gold);">
        <h3 style="font-family:'Cinzel Decorative',serif;color:var(--gold-light);font-size:1.5rem;margin-bottom:16px;">
            لماذا طبيب الروح؟
        </h3>
        <div style="display:flex;gap:32px;justify-content:center;flex-wrap:wrap;margin-top:24px;">
            {"".join(f'''<div style="color:var(--parchment);text-align:center;">
                <div style="font-size:2.2rem;margin-bottom:8px;">{ic}</div>
                <div style="font-family:'Amiri',serif;font-size:1rem;">{txt}</div>
            </div>''' for ic, txt in [
                ("⏱️","رد خلال 24 ساعة"),("🔒","خصوصية تامة"),
                ("📋","تقارير مكتوبة"),("🌟","سنوات من الخبرة"),
            ])}
        </div>
        <div style="margin-top:32px;display:flex;gap:16px;justify-content:center;flex-wrap:wrap;">
            <a class="hero-cta" href="{build_whatsapp_url('استفسار عام', 1)}" target="_blank">
                💬 واتساب 1
            </a>
            <a class="hero-cta" href="{build_whatsapp_url('استفسار عام', 2)}" target="_blank">
                💬 واتساب 2
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    render_footer()


def page_contact():
    render_navbar("contact")
    st.markdown("<div style='padding:60px 32px;'>", unsafe_allow_html=True)
    section_header("تواصل معنا", "✦ نحن هنا لأجلك ✦")

    c1, c2 = st.columns([3, 2], gap="large")

    with c1:
        st.markdown('<div class="contact-wrapper">', unsafe_allow_html=True)
        st.markdown("""
        <h3 style="font-family:'Cinzel Decorative',serif;color:var(--mahogany);
                   font-size:1.2rem;margin-bottom:20px;direction:rtl;">
            📬 أرسل رسالتك
        </h3>
        """, unsafe_allow_html=True)

        name  = st.text_input("الاسم الكامل:", key="c_name",  placeholder="اسمك الكريم")
        email = st.text_input("البريد الإلكتروني:", key="c_email", placeholder="example@mail.com")
        msg   = st.text_area("رسالتك:", key="c_msg", placeholder="اكتب استفسارك هنا...", height=140)

        if st.button("إرسال الرسالة ✦", key="send_btn"):
            if name.strip() and email.strip() and msg.strip():
                st.success("✅ تم إرسال رسالتك بنجاح! سنتواصل معك قريباً.")
                # Mailto link as fallback
                mailto = f"mailto:{OWNER_EMAIL}?subject=رسالة من {urllib.parse.quote(name)}&body={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{mailto}" style="font-family:Amiri,serif;color:var(--mahogany);">📧 افتح في بريدك الإلكتروني</a>', unsafe_allow_html=True)
            else:
                st.warning("يرجى ملء جميع الحقول.")

        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        wa_url  = build_whatsapp_url("استفسار عام", 1)
        wa_url2 = build_whatsapp_url("استفسار عام", 2)
        st.markdown(f"""
        <div style="direction:rtl;padding:0 8px;">
            <div class="card" style="margin-bottom:20px;">
                <div class="card-icon">💬</div>
                <div class="card-title">واتساب — رقم 1</div>
                <div class="card-body">+201093642315</div>
                <div style="margin-top:16px;">
                    <a class="wa-btn" href="{wa_url}" target="_blank">ابدأ المحادثة</a>
                </div>
            </div>
            <div class="card" style="margin-bottom:20px;">
                <div class="card-icon">💬</div>
                <div class="card-title">واتساب — رقم 2</div>
                <div class="card-body">+201090329193</div>
                <div style="margin-top:16px;">
                    <a class="wa-btn" href="{wa_url2}" target="_blank">ابدأ المحادثة</a>
                </div>
            </div>
            <div class="card" style="margin-bottom:20px;">
                <div class="card-icon">📱</div>
                <div class="card-title">منصاتي</div>
                <div class="card-body">تابعني على وسائل التواصل الاجتماعي</div>
                <div class="social-row" style="margin:16px 0 0;flex-wrap:wrap;">
                    <a class="social-icon" href="{TIKTOK_URL}" target="_blank" title="TikTok">𝕋</a>
                    <a class="social-icon" href="{YOUTUBE_URL}" target="_blank" title="خواطر روحانية">▶</a>
                    <a class="social-icon" href="{YOUTUBE_URL2}" target="_blank" title="القناة الثانية">▶</a>
                    <a class="social-icon" href="{FACEBOOK_URL}" target="_blank" title="Facebook">f</a>
                </div>
            </div>
            <div class="card">
                <div class="card-icon">⏰</div>
                <div class="card-title">أوقات الرد</div>
                <div class="card-body">
                    الأحد – الخميس<br/>9 صباحاً – 10 مساءً
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    render_footer()


# ── Router ────────────────────────────────────────────────────────────────────
def main():
    inject_css()

    params = st.query_params
    page = params.get("page", "home")

    if page == "research":
        page_research()
    elif page == "services":
        page_services()
    elif page == "contact":
        page_contact()
    else:
        page_home()


if __name__ == "__main__":
    main()
