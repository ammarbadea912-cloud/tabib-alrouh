CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:ital,wght@0,400;0,700;1,400;1,700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background-color: #FDF5E6;
        color: #4B2E1E;
        font-family: 'Amiri', serif;
    }

    .stApp {
        background-image: url('https://www.transparenttextures.com/patterns/parchment.png');
    }

    h1, h2, h3 {
        color: #8B4513;
        font-family: 'Amiri', serif;
        text-align: center;
        border-bottom: 2px solid #D4AF37;
        padding-bottom: 10px;
    }

    .stButton>button {
        background-color: #8B4513;
        color: #D4AF37;
        border: 2px solid #D4AF37;
        border-radius: 5px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }

    .stButton>button:hover {
        background-color: #D4AF37;
        color: #8B4513;
        border: 2px solid #8B4513;
    }

    .sidebar .sidebar-content {
        background-color: #F5DEB3;
    }

    .card {
        background-color: rgba(255, 255, 255, 0.5);
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #D4AF37;
        margin-bottom: 20px;
    }
    
    .result-box {
        background-color: #FFF8DC;
        border-left: 5px solid #8B4513;
        padding: 15px;
        margin-top: 10px;
        font-size: 1.2rem;
    }
    
    [data-testid="stSidebar"] {
        background-color: #F5DEB3;
    }
    
    .arabic-text {
        direction: rtl;
        text-align: right;
    }
</style>
"""
