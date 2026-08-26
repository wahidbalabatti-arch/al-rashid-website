from flask import Flask, render_template_string, send_from_directory
import os

# ============================================================
# FLASK SETUP
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


# ============================================================
# IMAGE ROUTES
# Images are directly beside app.py
# ============================================================

@app.route("/logo")
def logo():
    return send_from_directory(BASE_DIR, "LOGO.jpeg")


@app.route("/cover")
def cover():
    return send_from_directory(BASE_DIR, "COVER_PAGE.png")


# ============================================================
# WEBSITE HTML & EMBEDDED CSS/JS
# ============================================================

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Al Rashid Perfume & Attar - Luxury artisanal fragrances, rare traditional attars, and premium timepieces in Kolar, Karnataka.">
<meta name="keywords" content="Al Rashid, Luxury Perfume, Oud, Perfume Kolar, Attar, Designer Watches Kolar">
<meta name="theme-color" content="#020d08">
<title>Al Rashid | Luxury Perfume & Attar</title>

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">

<style>
/* ============================================================
   VARIABLES & THEME CONFIGURATION
   ============================================================ */
:root {
    --bg-dark: #020d08;
    --bg-card: rgba(8, 28, 19, 0.65);
    --gold-primary: #e3bd61;
    --gold-gradient: linear-gradient(135deg, #fceeb5 0%, #d9ad45 50%, #9e751b 100%);
    --gold-glow: rgba(217, 173, 69, 0.35);
    --text-main: #f5f5f7;
    --text-sub: #b0c2b7;
    --glass-border: rgba(217, 173, 69, 0.22);
    --nav-height: 80px;
}

/* ============================================================
   RESET & BASE STYLES
   ============================================================ */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background: var(--bg-dark);
    color: var(--text-main);
    overflow-x: hidden;
    position: relative;
}

/* Ambient Background Lights */
body::before, body::after {
    content: "";
    position: fixed;
    border-radius: 50%;
    filter: blur(140px);
    z-index: -1;
    pointer-events: none;
}
body::before {
    top: -10%;
    left: -10%;
    width: 50vw;
    height: 50vw;
    background: rgba(217, 173, 69, 0.08);
}
body::after {
    bottom: 10%;
    right: -10%;
    width: 60vw;
    height: 60vw;
    background: rgba(4, 45, 29, 0.25);
}

/* Typographic Hierarchy */
h1, h2, h3, .brand-font {
    font-family: 'Cinzel', serif;
}

/* Custom Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-track {
    background: var(--bg-dark);
}
::-webkit-scrollbar-thumb {
    background: #0d3a26;
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: var(--gold-primary);
}

/* ============================================================
   NAVIGATION (GLASSMORPHISM)
   ============================================================ */
nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: var(--nav-height);
    z-index: 1000;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 6%;
    background: rgba(2, 13, 8, 0.75);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--glass-border);
    transition: all 0.4s ease;
}

.nav-logo {
    display: flex;
    align-items: center;
    gap: 14px;
    text-decoration: none;
}

.nav-logo img {
    width: 44px;
    height: 44px;
    object-fit: contain;
    border-radius: 50%;
    border: 1px solid var(--gold-primary);
    box-shadow: 0 0 12px var(--gold-glow);
}

.nav-logo span {
    font-size: 22px;
    font-weight: 700;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 2px;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 32px;
    list-style: none;
}

.nav-links a {
    color: var(--text-sub);
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    transition: all 0.3s ease;
    position: relative;
}

.nav-links a::after {
    content: '';
    position: absolute;
    bottom: -6px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gold-gradient);
    transition: width 0.3s ease;
}

.nav-links a:hover {
    color: var(--text-main);
}

.nav-links a:hover::after {
    width: 100%;
}

.whatsapp-nav {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 22px;
    border-radius: 50px;
    background: var(--gold-gradient);
    color: #020d08 !important;
    font-weight: 700;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
    text-decoration: none;
    box-shadow: 0 4px 20px var(--gold-glow);
    transition: all 0.3s ease;
}

.whatsapp-nav:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 25px rgba(217,173,69,.5);
}

.mobile-toggle {
    display: none;
    background: none;
    border: none;
    color: var(--gold-primary);
    font-size: 26px;
    cursor: pointer;
}

/* ============================================================
   HERO SECTION
   ============================================================ */
.hero {
    min-height: 100vh;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: calc(var(--nav-height) + 40px) 20px 80px;
    background-color: var(--bg-dark);
    background-image:
        radial-gradient(circle at center, rgba(3, 20, 13, 0.4) 0%, rgba(2, 13, 8, 0.95) 100%),
        url("/cover");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 900px;
    animation: fadeIn 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}

.hero-badge {
    display: inline-block;
    padding: 6px 18px;
    border-radius: 30px;
    background: rgba(217, 173, 69, 0.1);
    border: 1px solid rgba(217, 173, 69, 0.3);
    color: var(--gold-primary);
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 25px;
}

.hero-logo {
    width: 130px;
    height: 130px;
    object-fit: contain;
    margin-bottom: 25px;
    border-radius: 50%;
    padding: 8px;
    background: rgba(2, 13, 8, 0.5);
    border: 1px solid var(--glass-border);
    box-shadow: 0 0 40px var(--gold-glow);
    animation: float 6s ease-in-out infinite;
}

.hero h1 {
    font-size: clamp(48px, 8vw, 95px);
    font-weight: 700;
    line-height: 1.05;
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 3px;
    text-shadow: 0 10px 30px rgba(0,0,0,0.5);
}

.hero h2 {
    margin-top: 15px;
    font-size: clamp(14px, 2.5vw, 22px);
    letter-spacing: 10px;
    color: var(--text-sub);
    font-weight: 400;
}

.gold-line {
    width: 120px;
    height: 1px;
    background: var(--gold-gradient);
    margin: 30px auto;
    position: relative;
}
.gold-line::after {
    content: "◆";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: var(--gold-primary);
    font-size: 10px;
    background: var(--bg-dark);
    padding: 0 8px;
}

.hero-description {
    max-width: 680px;
    margin: 0 auto 40px;
    color: var(--text-sub);
    font-size: 17px;
    line-height: 1.8;
    font-weight: 300;
}

/* Buttons */
.buttons {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
}

.button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    padding: 16px 36px;
    border-radius: 50px;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    cursor: pointer;
}

.button-gold {
    background: var(--gold-gradient);
    color: #020d08;
    box-shadow: 0 10px 30px var(--gold-glow);
}

.button-gold:hover {
    transform: translateY(-4px);
    box-shadow: 0 15px 35px rgba(217,173,69,0.5);
}

.button-outline {
    border: 1px solid var(--glass-border);
    color: var(--text-main);
    background: rgba(8, 28, 19, 0.4);
    backdrop-filter: blur(10px);
}

.button-outline:hover {
    border-color: var(--gold-primary);
    color: var(--gold-primary);
    transform: translateY(-4px);
    background: rgba(217, 173, 69, 0.05);
}

/* ============================================================
   SECTIONS GENERAL
   ============================================================ */
section {
    padding: 120px 6%;
    position: relative;
}

.section-title {
    text-align: center;
    margin-bottom: 70px;
}

.section-title .subtitle {
    color: var(--gold-primary);
    font-size: 12px;
    letter-spacing: 4px;
    text-transform: uppercase;
    display: block;
    margin-bottom: 10px;
}

.section-title h2 {
    font-size: clamp(32px, 4vw, 52px);
    background: var(--gold-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 1px;
}

/* ============================================================
   COLLECTION SECTION
   ============================================================ */
.cards {
    max-width: 1200px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 30px;
}

.card {
    padding: 45px 30px;
    text-align: center;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 24px;
    backdrop-filter: blur(15px);
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    position: relative;
    overflow: hidden;
}

.card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: radial-gradient(circle at top right, rgba(217,173,69,0.12), transparent 60%);
    opacity: 0;
    transition: opacity 0.4s ease;
}

.card:hover {
    transform: translateY(-10px);
    border-color: var(--gold-primary);
    box-shadow: 0 20px 40px rgba(0,0,0,0.6), 0 0 30px var(--gold-glow);
}

.card:hover::before {
    opacity: 1;
}

.card-icon {
    font-size: 48px;
    margin-bottom: 25px;
    display: inline-block;
    filter: drop-shadow(0 4px 10px rgba(0,0,0,0.3));
    transition: transform 0.4s ease;
}

.card:hover .card-icon {
    transform: scale(1.15) rotate(5deg);
}

.card h3 {
    color: var(--gold-primary);
    font-size: 24px;
    margin-bottom: 15px;
    letter-spacing: 1px;
}

.card p {
    color: var(--text-sub);
    font-size: 15px;
    line-height: 1.7;
    font-weight: 300;
}

/* ============================================================
   WHY US SECTION
   ============================================================ */
.features {
    max-width: 1200px;
    margin: auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 25px;
}

.feature {
    text-align: center;
    padding: 35px 25px;
    background: rgba(2, 18, 11, 0.4);
    border: 1px solid rgba(217, 173, 69, 0.1);
    border-radius: 20px;
    transition: all 0.3s ease;
}

.feature:hover {
    border-color: rgba(217, 173, 69, 0.3);
    background: rgba(8, 28, 19, 0.5);
}

.feature-icon {
    font-size: 40px;
    margin-bottom: 20px;
}

.feature h3 {
    color: var(--text-main);
    font-size: 18px;
    margin-bottom: 10px;
    font-family: 'Plus Jakarta Sans', sans-serif;
    font-weight: 600;
}

.feature p {
    color: var(--text-sub);
    font-size: 14px;
    line-height: 1.6;
}

/* ============================================================
   ABOUT & LOCATION (GLASS PANELS)
   ============================================================ */
.glass-panel {
    max-width: 950px;
    margin: auto;
    padding: 60px 40px;
    text-align: center;
    background: var(--bg-card);
    border: 1px solid var(--glass-border);
    border-radius: 30px;
    backdrop-filter: blur(20px);
    box-shadow: 0 20px 50px rgba(0,0,0,0.5);
}

.about-box p {
    color: var(--text-sub);
    font-size: 18px;
    line-height: 2;
    font-weight: 300;
}

.location-box h3 {
    color: var(--gold-primary);
    font-size: 32px;
    margin-bottom: 20px;
}

.location-details {
    color: var(--text-sub);
    font-size: 18px;
    line-height: 1.9;
    margin-bottom: 35px;
}

.location-details strong {
    color: var(--text-main);
}

/* ============================================================
   SOCIAL SECTION
   ============================================================ */
.social-card {
    max-width: 700px;
    margin: 0 auto;
    text-align: center;
    padding: 50px 30px;
    background: linear-gradient(135deg, rgba(217,173,69,0.05), rgba(4,45,29,0.3));
    border: 1px solid var(--glass-border);
    border-radius: 30px;
}

.instagram-btn {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    color: var(--gold-primary);
    font-size: 22px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    margin-bottom: 25px;
}

.instagram-btn:hover {
    color: #ffffff;
    transform: scale(1.05);
}

/* ============================================================
   FOOTER
   ============================================================ */
footer {
    padding: 60px 20px;
    text-align: center;
    background: #010805;
    border-top: 1px solid rgba(217, 173, 69, 0.15);
    color: #66786e;
    font-size: 14px;
    line-height: 1.8;
}

footer strong {
    color: var(--gold-primary);
    font-size: 20px;
    font-family: 'Cinzel', serif;
    display: block;
    margin-bottom: 10px;
}

/* ============================================================
   ANIMATIONS
   ============================================================ */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

/* ============================================================
   RESPONSIVE DESIGN
   ============================================================ */
@media (max-width: 900px) {
    .nav-links {
        position: fixed;
        top: var(--nav-height);
        left: -100%;
        width: 100%;
        height: calc(100vh - var(--nav-height));
        background: rgba(2, 13, 8, 0.98);
        flex-direction: column;
        justify-content: center;
        gap: 40px;
        transition: left 0.4s ease;
        backdrop-filter: blur(25px);
    }

    .nav-links.active {
        left: 0;
    }

    .mobile-toggle {
        display: block;
    }

    section {
        padding: 80px 5%;
    }
}

@media (max-width: 480px) {
    .hero {
        background-attachment: scroll;
    }
    
    .glass-panel {
        padding: 40px 20px;
    }

    .button {
        width: 100%;
    }
}
</style>
</head>

<body>

<!-- ============================================================
     NAVIGATION
     ============================================================ -->
<nav>
    <a href="#home" class="nav-logo">
        <img src="/logo" alt="Al Rashid Logo">
        <span>AL RASHID</span>
    </a>

    <button class="mobile-toggle" id="menuToggle" aria-label="Toggle Navigation">☰</button>

    <ul class="nav-links" id="navLinks">
        <li><a href="#home">Home</a></li>
        <li><a href="#collection">Collection</a></li>
        <li><a href="#why">Why Us</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#location">Store</a></li>
    </ul>

    <a class="whatsapp-nav" href="https://wa.me/919620963982" target="_blank">
        💬 Connect
    </a>
</nav>

<!-- ============================================================
     HERO SECTION
     ============================================================ -->
<header class="hero" id="home">
    <div class="hero-content">
        <span class="hero-badge">Luxury Fragrances & Timepieces</span>
        
        <div>
            <img class="hero-logo" src="/logo" alt="Al Rashid Emblem">
        </div>

        <h1>AL RASHID</h1>
        <h2>PERFUME &amp; ATTAR</h2>

        <div class="gold-line"></div>

        <p class="hero-description">
            Step into a world of sensory distinction. Discover curated luxury perfumes, authentic pure attars, and elegant timepieces crafted for sophistication.
        </p>

        <div class="buttons">
            <a class="button button-gold" href="#collection">
                Explore Collection
            </a>
            <a class="button button-outline" href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20inquire%20about%20your%20luxury%20collection." target="_blank">
                💬 Order via WhatsApp
            </a>
        </div>
    </div>
</header>

<!-- ============================================================
     COLLECTION
     ============================================================ -->
<section id="collection">
    <div class="section-title">
        <span class="subtitle">Curated Offerings</span>
        <h2>The Signature Collection</h2>
    </div>

    <div class="cards">
        <div class="card">
            <div class="card-icon">🌹</div>
            <h3>Luxury Perfumes</h3>
            <p>Opulent and long-lasting fine spray fragrances blended for signature presence and daily sophistication.</p>
        </div>

        <div class="card">
            <div class="card-icon">🪔</div>
            <h3>Pure Attars</h3>
            <p>Non-alcoholic, traditional oil-based concentrates extracted from natural notes, rare spices, and rich woods.</p>
        </div>

        <div class="card">
            <div class="card-icon">⌚</div>
            <h3>Luxury Watches</h3>
            <p>Meticulously designed timepieces that blend timeless aesthetics with modern durability.</p>
        </div>

        <div class="card">
            <div class="card-icon">✨</div>
            <h3>Exotic Editions</h3>
            <p>Exclusive seasonal releases, concentrated oudh extracts, and limited-edition gift boxes.</p>
        </div>
    </div>
</section>

<!-- ============================================================
     WHY US
     ============================================================ -->
<section id="why">
    <div class="section-title">
        <span class="subtitle">Excellence Guaranteed</span>
        <h2>Why Choose Al Rashid</h2>
    </div>

    <div class="features">
        <div class="feature">
            <div class="feature-icon">💎</div>
            <h3>Artisanal Quality</h3>
            <p>Carefully sourced ingredients yielding true-to-character depth.</p>
        </div>

        <div class="feature">
            <div class="feature-icon">⏳</div>
            <h3>Long Lasting Sillage</h3>
            <p>Formulations specifically designed to linger throughout the day.</p>
        </div>

        <div class="feature">
            <div class="feature-icon">👑</div>
            <h3>Fair Luxury</h3>
            <p>Uncompromising premium scents offered at accessible pricing.</p>
        </div>

        <div class="feature">
            <div class="feature-icon">🤝</div>
            <h3>Personalized Advice</h3>
            <p>Tailored scent matching to complement your unique personality.</p>
        </div>
    </div>
</section>

<!-- ============================================================
     ABOUT
     ============================================================ -->
<section id="about">
    <div class="section-title">
        <span class="subtitle">Our Legacy</span>
        <h2>About Al Rashid</h2>
    </div>

    <div class="glass-panel about-box">
        <p>
            Welcome to <strong style="color: var(--gold-primary); font-family: 'Cinzel', serif;">Al Rashid Perfume &amp; Attar</strong>. 
            <br><br>
            Rooted in the rich heritage of oriental perfumery, we bring you an unmatched assortment of signature perfumes, authentic concentrated attars, and exquisite watches. 
            <br><br>
            Whether you are seeking an enduring everyday scent, an imposing luxury gift, or a statement piece to define your look, our boutique delivers fragrances crafted to make every moment memorable.
        </p>
    </div>
</section>

<!-- ============================================================
     LOCATION & STORE
     ============================================================ -->
<section id="location">
    <div class="section-title">
        <span class="subtitle">Visit Boutique</span>
        <h2>Experience In Person</h2>
    </div>

    <div class="glass-panel location-box">
        <h3>Al Rashid Perfume &amp; Attar</h3>
        
        <div class="location-details">
            📍 MG Road, Kolar, Karnataka<br>
            <span style="color: var(--gold-primary); font-size: 15px;">(Next to Parvath Sports)</span>
            <br><br>
            📞 <strong>+91 96209 63982</strong>
        </div>

        <div class="buttons">
            <a class="button button-gold" href="https://www.google.com/maps/search/?api=1&query=Al+Rashid+Perfume+Attar+MG+Road+Kolar" target="_blank">
                📍 Open Google Maps
            </a>
            <a class="button button-outline" href="https://wa.me/919620963982" target="_blank">
                💬 Direct WhatsApp
            </a>
        </div>
    </div>
</section>

<!-- ============================================================
     SOCIAL
     ============================================================ -->
<section>
    <div class="social-card">
        <div class="section-title" style="margin-bottom: 30px;">
            <span class="subtitle">Stay Connected</span>
            <h2>Follow Our Journey</h2>
        </div>

        <a class="instagram-btn" href="https://www.instagram.com/alrashid.luxury/" target="_blank">
            📸 @alrashid.luxury
        </a>

        <div>
            <a class="button button-gold" href="https://wa.me/919620963982" target="_blank">
                💬 Chat with Us
            </a>
        </div>
    </div>
</section>

<!-- ============================================================
     FOOTER
     ============================================================ -->
<footer>
    <strong>AL RASHID</strong>
    <p>Luxury Perfumes • Concentrated Attars • Fine Watches</p>
    <p style="margin-top: 6px;">MG Road, Kolar, Karnataka | +91 96209 63982</p>
    <br>
    <p>© 2026 Al Rashid Luxury. All Rights Reserved.</p>
</footer>

<!-- JavaScript for Mobile Menu & Interactivity -->
<script>
    const toggle = document.getElementById('menuToggle');
    const links = document.getElementById('navLinks');

    toggle.addEventListener('click', () => {
        links.classList.toggle('active');
        toggle.textContent = links.classList.contains('active') ? '✕' : '☰';
    });

    // Close menu when clicking links on mobile
    document.querySelectorAll('.nav-links a').forEach(link => {
        link.addEventListener('click', () => {
            links.classList.remove('active');
            toggle.textContent = '☰';
        });
    });
</script>

</body>
</html>
"""


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template_string(HTML)


# ============================================================
# LOCAL / RENDER SERVER
# ============================================================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False,
        use_reloader=False
    )