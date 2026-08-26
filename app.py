from flask import Flask, render_template_string, send_from_directory, request
import os

# ============================================================
# FLASK SETUP
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


# ============================================================
# WEBSITE URL
# Automatically detects Render / deployed domain
# ============================================================

def get_site_url():
    return request.url_root.rstrip("/")


# ============================================================
# IMAGE ROUTES
# Images are directly beside app.py
# ============================================================

@app.route("/logo")
def logo():
    return send_from_directory(
        BASE_DIR,
        "LOGO.jpeg",
        mimetype="image/jpeg"
    )


@app.route("/cover")
def cover():
    return send_from_directory(
        BASE_DIR,
        "COVER_PAGE.png",
        mimetype="image/png"
    )


# ============================================================
# WEBSITE HTML
# ============================================================

HTML = r"""
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">


<!-- ============================================================
     SEO
     ============================================================ -->

<meta name="description"
      content="Al Rashid Perfume & Attar — Premium perfumes, luxury attars and stylish watches in Kolar, Karnataka. Discover your signature fragrance.">

<meta name="keywords"
      content="Al Rashid, Al Rashid Perfume, Al Rashid Attar, Perfume Kolar, Attar Kolar, Premium Perfume Kolar, Luxury Attar Kolar, Watches Kolar">

<meta name="author"
      content="Al Rashid Perfume & Attar">

<meta name="theme-color"
      content="#03140d">


<!-- ============================================================
     OPEN GRAPH
     WhatsApp / Facebook / Social Preview
     ============================================================ -->

<meta property="og:type"
      content="website">

<meta property="og:title"
      content="Al Rashid | Perfume & Attar">

<meta property="og:description"
      content="Discover premium perfumes, luxury attars and stylish watches at Al Rashid, Kolar.">

<meta property="og:image"
      content="{{ site_url }}/logo">

<meta property="og:image:alt"
      content="Al Rashid Perfume & Attar">

<meta property="og:url"
      content="{{ site_url }}/">

<meta property="og:site_name"
      content="Al Rashid">


<!-- ============================================================
     TWITTER / X
     ============================================================ -->

<meta name="twitter:card"
      content="summary_large_image">

<meta name="twitter:title"
      content="Al Rashid | Perfume & Attar">

<meta name="twitter:description"
      content="Premium perfumes, luxury attars and stylish watches in Kolar.">

<meta name="twitter:image"
      content="{{ site_url }}/logo">


<title>
Al Rashid | Perfume & Attar
</title>


<style>

/* ============================================================
   RESET
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

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    background: #03140d;

    color: #f5e7b2;

    overflow-x: hidden;

}


/* ============================================================
   NAVIGATION
   ============================================================ */

nav {

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;

    height: 76px;

    z-index: 1000;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 10px 5%;

    background:
        rgba(2, 18, 11, 0.96);

    backdrop-filter: blur(15px);

    border-bottom:
        1px solid rgba(217, 173, 69, 0.35);

}


.nav-logo {

    display: flex;

    align-items: center;

    gap: 12px;

    color: #d9ad45;

    font-size: 24px;

    font-weight: bold;

}


.nav-logo img {

    width: 48px;

    height: 48px;

    object-fit: contain;

    border-radius: 50%;

}


.nav-links {

    display: flex;

    align-items: center;

    gap: 30px;

    list-style: none;

}


.nav-links a {

    color: #ffffff;

    text-decoration: none;

    font-family: Arial, sans-serif;

    font-size: 15px;

    transition: 0.3s;

}


.nav-links a:hover {

    color: #d9ad45;

}


.whatsapp-nav {

    display: inline-block;

    padding: 12px 22px;

    border-radius: 30px;

    background: #d9ad45;

    color: #071b11 !important;

    font-family: Arial, sans-serif;

    font-weight: bold;

    text-decoration: none;

    transition: 0.3s;

}


.whatsapp-nav:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 25px rgba(217,173,69,.3);

}


/* ============================================================
   HERO
   ============================================================ */

.hero {

    min-height: 100vh;

    position: relative;

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    padding:
        120px 20px 80px;

    background-color: #03140d;

    background-image:

        linear-gradient(
            rgba(2, 16, 10, 0.60),
            rgba(2, 16, 10, 0.88)
        ),

        url("/cover");

    background-size: cover;

    background-position: center;

    background-repeat: no-repeat;

}


.hero::before {

    content: "";

    position: absolute;

    inset: 0;

    background:
        radial-gradient(
            circle at center,
            rgba(217,173,69,.08),
            transparent 55%
        );

    pointer-events: none;

}


.hero-content {

    position: relative;

    z-index: 2;

    max-width: 1000px;

    width: 100%;

}


.hero-logo {

    width: 145px;

    height: 145px;

    object-fit: contain;

    margin-bottom: 15px;

    filter:
        drop-shadow(
            0 0 25px
            rgba(217,173,69,.65)
        );

}


.hero h1 {

    font-size:
        clamp(55px, 9vw, 110px);

    line-height: 1;

    color: #e8bd59;

    letter-spacing: 2px;

    text-shadow:
        0 5px 30px rgba(0,0,0,.8);

}


.hero h2 {

    margin-top: 20px;

    font-size:
        clamp(18px, 3vw, 30px);

    letter-spacing: 8px;

    color: #ffffff;

}


.gold-line {

    width: 180px;

    height: 2px;

    background: #d9ad45;

    margin: 30px auto;

}


.hero-description {

    max-width: 760px;

    margin:
        0 auto 32px;

    color: #eeeeee;

    font-family: Arial, sans-serif;

    font-size: 18px;

    line-height: 1.8;

}


/* ============================================================
   BUTTONS
   ============================================================ */

.buttons {

    display: flex;

    align-items: center;

    justify-content: center;

    flex-wrap: wrap;

    gap: 15px;

}


.button {

    display: inline-block;

    padding: 15px 30px;

    border-radius: 40px;

    text-decoration: none;

    font-family: Arial, sans-serif;

    font-weight: bold;

    transition: 0.3s;

    cursor: pointer;

    border: none;

}


.button-gold {

    background: #d9ad45;

    color: #061b12;

}


.button-outline {

    border:
        1px solid #d9ad45;

    color: #d9ad45;

    background:
        rgba(0,0,0,.12);

}


.button:hover {

    transform: translateY(-4px);

    box-shadow:
        0 12px 30px
        rgba(217,173,69,.25);

}


/* ============================================================
   SECTION
   ============================================================ */

section {

    padding: 100px 6%;

}


.section-title {

    text-align: center;

    margin-bottom: 55px;

}


.section-title h2 {

    color: #e3bd61;

    font-size:
        clamp(35px, 5vw, 55px);

}


.section-title p {

    margin-top: 15px;

    color: #999999;

    font-family: Arial, sans-serif;

}


/* ============================================================
   COLLECTION
   ============================================================ */

.cards {

    max-width: 1200px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(240px, 1fr)
        );

    gap: 25px;

}


.card {

    padding: 42px 25px;

    text-align: center;

    background:
        linear-gradient(
            145deg,
            #0d301f,
            #061b12
        );

    border:
        1px solid #705621;

    border-radius: 20px;

    transition: 0.4s;

}


.card:hover {

    transform: translateY(-10px);

    border-color: #d9ad45;

    box-shadow:
        0 20px 50px
        rgba(0,0,0,.45);

}


.card-icon {

    font-size: 50px;

    margin-bottom: 20px;

}


.card h3 {

    color: #e3bd61;

    font-size: 25px;

    margin-bottom: 15px;

}


.card p {

    color: #cccccc;

    font-family: Arial, sans-serif;

    line-height: 1.7;

}


/* ============================================================
   WHY US
   ============================================================ */

.features {

    max-width: 1150px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(
            auto-fit,
            minmax(200px, 1fr)
        );

    gap: 20px;

}


.feature {

    text-align: center;

    padding: 30px 15px;

}


.feature-icon {

    font-size: 45px;

    margin-bottom: 15px;

}


.feature h3 {

    color: #d9ad45;

    margin-bottom: 10px;

}


.feature p {

    color: #999999;

    font-family: Arial, sans-serif;

    line-height: 1.6;

}


/* ============================================================
   ABOUT
   ============================================================ */

.about-box {

    max-width: 1000px;

    margin: auto;

    padding: 55px 35px;

    text-align: center;

    background: #092219;

    border:
        1px solid #604b21;

    border-radius: 25px;

}


.about-box p {

    color: #dddddd;

    font-family: Arial, sans-serif;

    font-size: 18px;

    line-height: 1.9;

}


.gold {

    color: #d9ad45;

}


/* ============================================================
   LOCATION
   ============================================================ */

.location-box {

    max-width: 900px;

    margin: auto;

    padding: 55px 25px;

    text-align: center;

    background:
        linear-gradient(
            145deg,
            #0b291c,
            #061b12
        );

    border:
        1px solid #705621;

    border-radius: 25px;

}


.location-box h3 {

    color: #e3bd61;

    font-size: 31px;

    margin-bottom: 20px;

}


.location-box p {

    color: #dddddd;

    font-family: Arial, sans-serif;

    line-height: 1.9;

    font-size: 17px;

}


/* ============================================================
   SHARE WEBSITE
   ============================================================ */

.share-section {

    position: relative;

    overflow: hidden;

}


.share-box {

    max-width: 900px;

    margin: auto;

    padding: 60px 30px;

    text-align: center;

    background:
        linear-gradient(
            145deg,
            #0d301f,
            #061b12
        );

    border:
        1px solid #80642b;

    border-radius: 28px;

    box-shadow:
        0 25px 70px rgba(0,0,0,.35);

}


.share-logo {

    width: 90px;

    height: 90px;

    object-fit: contain;

    border-radius: 50%;

    margin-bottom: 20px;

    filter:
        drop-shadow(
            0 0 20px
            rgba(217,173,69,.5)
        );

}


.share-box h2 {

    color: #e8bd59;

    font-size:
        clamp(32px, 5vw, 50px);

    margin-bottom: 15px;

}


.share-box p {

    max-width: 650px;

    margin: 0 auto 25px;

    color: #cccccc;

    font-family: Arial, sans-serif;

    font-size: 17px;

    line-height: 1.7;

}


.share-link {

    display: inline-block;

    max-width: 90%;

    overflow: hidden;

    text-overflow: ellipsis;

    white-space: nowrap;

    padding: 13px 20px;

    margin-bottom: 28px;

    border-radius: 30px;

    border:
        1px solid rgba(217,173,69,.45);

    color: #d9ad45;

    background:
        rgba(0,0,0,.18);

    font-family: Arial, sans-serif;

}


.share-buttons {

    display: flex;

    justify-content: center;

    align-items: center;

    flex-wrap: wrap;

    gap: 12px;

}


.share-btn {

    padding: 13px 22px;

    border-radius: 30px;

    border: 1px solid #d9ad45;

    background: transparent;

    color: #e8bd59;

    font-family: Arial, sans-serif;

    font-weight: bold;

    text-decoration: none;

    cursor: pointer;

    transition: .3s;

}


.share-btn:hover {

    background: #d9ad45;

    color: #061b12;

    transform: translateY(-3px);

}


.share-btn.primary {

    background: #d9ad45;

    color: #061b12;

}


/* ============================================================
   SHARE MESSAGE
   ============================================================ */

#share-status {

    margin-top: 18px;

    color: #d9ad45;

    font-family: Arial, sans-serif;

    font-size: 14px;

    min-height: 20px;

}


/* ============================================================
   INSTAGRAM
   ============================================================ */

.social {

    text-align: center;

}


.instagram {

    color: #e3bd61;

    font-size: 27px;

    text-decoration: none;

    transition: 0.3s;

}


.instagram:hover {

    color: white;

}


/* ============================================================
   FOOTER
   ============================================================ */

footer {

    padding: 50px 20px;

    text-align: center;

    background: #020d08;

    border-top:
        1px solid #604b21;

    color: #888888;

    font-family: Arial, sans-serif;

    line-height: 1.8;

}


footer strong {

    color: #d9ad45;

    font-size: 20px;

}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 850px) {

    nav {

        height: auto;

        min-height: 70px;

        padding: 10px 4%;

    }


    .nav-links {

        display: none;

    }


    .nav-logo {

        font-size: 19px;

    }


    .nav-logo img {

        width: 42px;

        height: 42px;

    }


    .whatsapp-nav {

        padding: 9px 15px;

        font-size: 13px;

    }


    .hero {

        padding-top: 110px;

        background-position: center;

    }


    .hero-logo {

        width: 110px;

        height: 110px;

    }


    .hero h2 {

        letter-spacing: 4px;

    }


    .hero-description {

        font-size: 16px;

    }


    section {

        padding:
            75px 5%;

    }

}


/* ============================================================
   SMALL MOBILE
   ============================================================ */

@media (max-width: 480px) {

    .hero h1 {

        font-size: 55px;

    }


    .hero h2 {

        font-size: 17px;

        letter-spacing: 3px;

    }


    .button {

        width: 100%;

        max-width: 300px;

    }


    .share-btn {

        width: 100%;

        max-width: 300px;

    }


    .share-link {

        max-width: 100%;

        font-size: 13px;

    }

}

</style>

</head>


<body>


<!-- ============================================================
     NAVIGATION
     ============================================================ -->

<nav>

    <div class="nav-logo">

        <img
            src="/logo"
            alt="Al Rashid Logo">

        <span>
            Al Rashid
        </span>

    </div>


    <ul class="nav-links">

        <li>
            <a href="#home">
                Home
            </a>
        </li>

        <li>
            <a href="#collection">
                Collection
            </a>
        </li>

        <li>
            <a href="#why">
                Why Us
            </a>
        </li>

        <li>
            <a href="#about">
                About
            </a>
        </li>

        <li>
            <a href="#location">
                Location
            </a>
        </li>

    </ul>


    <a
        class="whatsapp-nav"
        href="https://wa.me/919620963982"
        target="_blank">

        WhatsApp

    </a>

</nav>


<!-- ============================================================
     HERO
     ============================================================ -->

<header
    class="hero"
    id="home">


    <div class="hero-content">


        <img
            class="hero-logo"
            src="/logo"
            alt="Al Rashid Perfume & Attar">


        <h1>
            Al Rashid
        </h1>


        <h2>
            PERFUME &amp; ATTAR
        </h2>


        <div class="gold-line"></div>


        <p class="hero-description">

            Discover premium fragrances,
            traditional attars and stylish watches
            designed to make every moment memorable.

        </p>


        <div class="buttons">


            <a
                class="button button-gold"
                href="#collection">

                Explore Collection

            </a>


            <a
                class="button button-outline"

                href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20know%20about%20your%20perfumes."

                target="_blank">

                💬 Order on WhatsApp

            </a>


        </div>


    </div>

</header>


<!-- ============================================================
     COLLECTION
     ============================================================ -->

<section id="collection">


    <div class="section-title">

        <h2>
            Our Collection
        </h2>

        <p>
            Discover something made for you.
        </p>

    </div>


    <div class="cards">


        <!-- PREMIUM PERFUMES -->

        <div class="card">

            <div class="card-icon">
                🌹
            </div>

            <h3>
                Premium Perfumes
            </h3>

            <p>
                Elegant and sophisticated
                fragrances for everyday wear
                and special occasions.
            </p>

        </div>


        <!-- ATTARS -->

        <div class="card">

            <div class="card-icon">
                🧴
            </div>

            <h3>
                Attars
            </h3>

            <p>
                Traditional and modern attars
                with rich and distinctive
                fragrance profiles.
            </p>

        </div>


        <!-- WATCHES -->

        <div class="card">

            <div class="card-icon">
                ⌚
            </div>

            <h3>
                Watches
            </h3>

            <p>
                Stylish watches designed to
                complement your personality
                and everyday style.
            </p>

        </div>


        <!-- NEW ARRIVALS -->

        <div class="card">

            <div class="card-icon">
                ✨
            </div>

            <h3>
                New Arrivals
            </h3>

            <p>
                Explore our latest fragrances,
                collections and new additions.
            </p>

        </div>


    </div>

</section>


<!-- ============================================================
     WHY US
     ============================================================ -->

<section id="why">


    <div class="section-title">

        <h2>
            Why Choose Al Rashid?
        </h2>

        <p>
            Quality • Fragrance • Service
        </p>

    </div>


    <div class="features">


        <div class="feature">

            <div class="feature-icon">
                💎
            </div>

            <h3>
                Premium Quality
            </h3>

            <p>
                Carefully selected fragrances
                and products.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">
                ⏳
            </div>

            <h3>
                Long Lasting
            </h3>

            <p>
                Fragrances made to stay
                with you.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">
                💰
            </div>

            <h3>
                Great Prices
            </h3>

            <p>
                Premium choices at
                attractive prices.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">
                ❤️
            </div>

            <h3>
                Customer First
            </h3>

            <p>
                Your satisfaction is
                important to us.
            </p>

        </div>


    </div>

</section>


<!-- ============================================================
     ABOUT
     ============================================================ -->

<section id="about">


    <div class="section-title">

        <h2>
            About Al Rashid
        </h2>

    </div>


    <div class="about-box">


        <p>

            Welcome to

            <strong class="gold">
                Al Rashid Perfume &amp; Attar
            </strong>.

            <br><br>

            We offer a collection of
            premium perfumes, traditional
            attars and stylish watches.

            <br><br>

            Whether you are looking for
            a signature fragrance,
            a special gift or something
            for everyday use, discover
            fragrances that suit your
            personality and style.

        </p>


    </div>

</section>


<!-- ============================================================
     LOCATION
     ============================================================ -->

<section id="location">


    <div class="section-title">

        <h2>
            Visit Our Store
        </h2>

    </div>


    <div class="location-box">


        <h3>
            Al Rashid Perfume &amp; Attar
        </h3>


        <p>

            📍 MG Road,
            Kolar, Karnataka

            <br>

            Next to Parvath Sports

            <br><br>

            📞 +91 96209 63982

        </p>


        <br>


        <div class="buttons">


            <a
                class="button button-gold"

                href="https://www.google.com/maps/search/?api=1&query=Al+Rashid+Perfume+Attar+MG+Road+Kolar"

                target="_blank">

                📍 Open Google Maps

            </a>


            <a
                class="button button-outline"

                href="https://wa.me/919620963982"

                target="_blank">

                💬 WhatsApp Us

            </a>


        </div>


    </div>

</section>


<!-- ============================================================
     SHARE WEBSITE
     ============================================================ -->

<section
    class="share-section"
    id="share">


    <div class="section-title">

        <h2>
            Share Al Rashid
        </h2>

        <p>
            Share our website with your friends and family.
        </p>

    </div>


    <div class="share-box">


        <img
            class="share-logo"
            src="/logo"
            alt="Al Rashid Logo">


        <h2>
            Know Someone Who Loves Fragrance?
        </h2>


        <p>

            Share Al Rashid Perfume &amp; Attar
            with your friends and help them
            discover premium perfumes,
            luxury attars and stylish watches
            in Kolar.

        </p>


        <div class="share-link">

            {{ site_url }}

        </div>


        <div class="share-buttons">


            <!-- WhatsApp -->

            <a
                class="share-btn primary"
                href="https://wa.me/?text={{ share_message }}"
                target="_blank">

                💬 Share on WhatsApp

            </a>


            <!-- Facebook -->

            <a
                class="share-btn"
                href="https://www.facebook.com/sharer/sharer.php?u={{ site_url | urlencode }}"
                target="_blank">

                Facebook

            </a>


            <!-- X / Twitter -->

            <a
                class="share-btn"
                href="https://twitter.com/intent/tweet?text={{ share_text | urlencode }}&url={{ site_url | urlencode }}"
                target="_blank">

                𝕏 Share

            </a>


            <!-- Native mobile share -->

            <button
                class="share-btn"
                onclick="nativeShare()">

                📤 Share

            </button>


            <!-- Copy link -->

            <button
                class="share-btn"
                onclick="copyWebsite()">

                🔗 Copy Link

            </button>


        </div>


        <div id="share-status"></div>


    </div>

</section>


<!-- ============================================================
     INSTAGRAM
     ============================================================ -->

<section>


    <div class="social">


        <div class="section-title">

            <h2>
                Follow Us
            </h2>

            <p>
                New arrivals, fragrances and updates.
            </p>

        </div>


        <a
            class="instagram"

            href="https://www.instagram.com/alrashid.luxury/"

            target="_blank">

            📸 @alrashid.luxury

        </a>


        <br><br><br>


        <a
            class="button button-gold"

            href="https://wa.me/919620963982"

            target="_blank">

            💬 Chat on WhatsApp

        </a>


    </div>

</section>


<!-- ============================================================
     FOOTER
     ============================================================ -->

<footer>


    <strong>
        Al Rashid Perfume &amp; Attar
    </strong>


    <br>


    Premium Perfumes
    •
    Attars
    •
    Watches


    <br>


    MG Road,
    Kolar,
    Karnataka


    <br>


    +91 96209 63982


    <br><br>


    © 2026
    Al Rashid.
    All Rights Reserved.


</footer>


<!-- ============================================================
     SHARE JAVASCRIPT
     ============================================================ -->

<script>

const websiteURL = {{ site_url | tojson }};

const shareText =
    "Discover Al Rashid Perfume & Attar — premium perfumes, luxury attars and stylish watches in Kolar.";


/* ============================================================
   NATIVE SHARE
   ============================================================ */

async function nativeShare() {

    if (navigator.share) {

        try {

            await navigator.share({

                title: "Al Rashid | Perfume & Attar",

                text: shareText,

                url: websiteURL

            });

        }

        catch (error) {

            console.log("Share cancelled.");

        }

    }

    else {

        copyWebsite();

    }

}


/* ============================================================
   COPY WEBSITE LINK
   ============================================================ */

async function copyWebsite() {

    try {

        await navigator.clipboard.writeText(websiteURL);

        document.getElementById("share-status").innerText =
            "✓ Website link copied successfully!";

        setTimeout(function() {

            document.getElementById("share-status").innerText = "";

        }, 3000);

    }

    catch (error) {

        document.getElementById("share-status").innerText =
            "Please copy the website address manually.";

    }

}

</script>


</body>

</html>
"""


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():

    site_url = get_site_url()

    share_message = (
        "Discover Al Rashid Perfume & Attar — "
        "premium perfumes, luxury attars and stylish watches "
        "in Kolar. Visit: " + site_url
    )

    share_text = (
        "Discover Al Rashid Perfume & Attar"
    )

    return render_template_string(
        HTML,
        site_url=site_url,
        share_message=share_message,
        share_text=share_text
    )


# ============================================================
# LOCAL / RENDER SERVER
# ============================================================

if __name__ == "__main__":

    port = int(
        os.environ.get(
            "PORT",
            5000
        )
    )

    app.run(

        host="0.0.0.0",

        port=port,

        debug=False,

        use_reloader=False

    )