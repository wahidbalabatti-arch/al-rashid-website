from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# ============================================================
# IMAGE ROUTES
# Images are directly inside the same folder as app.py
# ============================================================

@app.route("/logo")
def logo():
    return send_from_directory(".", "LOGO.JPEG")


@app.route("/cover")
def cover():
    return send_from_directory(".", "COVER PAGE.jpeg")


# ============================================================
# MAIN WEBSITE
# ============================================================

HTML = """
<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<meta name="description"
      content="Al Rashid Perfume & Attar - Premium perfumes, attars and watches in Kolar, Karnataka.">

<meta name="keywords"
      content="Al Rashid, Al Rashid Perfume, Attar, Perfume Kolar, Premium Perfume, Watches Kolar">

<title>Al Rashid | Perfume & Attar</title>


<style>

/* ============================================================
   BASIC
   ============================================================ */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
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

    height: 75px;

    z-index: 9999;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 10px 5%;

    background:
        rgba(3, 20, 13, 0.94);

    backdrop-filter: blur(15px);

    border-bottom:
        1px solid rgba(217, 173, 69, 0.4);

}


.nav-logo {

    display: flex;

    align-items: center;

    gap: 12px;

    color: #d9ad45;

    font-size: 23px;

    font-weight: bold;

}


.nav-logo img {

    width: 48px;

    height: 48px;

    object-fit: contain;

    border-radius: 50%;

}


nav ul {

    display: flex;

    gap: 30px;

    list-style: none;

}


nav ul li a {

    text-decoration: none;

    color: #eeeeee;

    font-family: Arial, sans-serif;

    font-size: 15px;

    transition: 0.3s;

}


nav ul li a:hover {

    color: #d9ad45;

}


.nav-whatsapp {

    padding: 11px 20px;

    border-radius: 30px;

    background: #d9ad45;

    color: #061b12 !important;

    font-family: Arial, sans-serif;

    font-weight: bold;

    text-decoration: none;

}


/* ============================================================
   HERO
   ============================================================ */

.hero {

    min-height: 100vh;

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    padding:
        120px 20px
        70px;

    position: relative;

    background:

        linear-gradient(
            rgba(2, 15, 9, 0.58),
            rgba(2, 15, 9, 0.90)
        ),

        url("/cover");

    background-size: cover;

    background-position: center;

    background-attachment: fixed;

}


.hero::after {

    content: "";

    position: absolute;

    inset: 0;

    background:
        radial-gradient(
            circle at center,
            transparent 15%,
            rgba(0,0,0,.35) 100%
        );

    pointer-events: none;

}


.hero-content {

    position: relative;

    z-index: 2;

    max-width: 1000px;

}


.hero-logo {

    width: 145px;

    height: 145px;

    object-fit: contain;

    margin-bottom: 20px;

    filter:
        drop-shadow(
            0 0 25px
            rgba(217,173,69,.6)
        );

}


.hero h1 {

    font-size:
        clamp(55px, 9vw, 110px);

    color: #e5bd5c;

    letter-spacing: 3px;

    text-shadow:
        0 5px 30px
        rgba(0,0,0,.9);

}


.hero h2 {

    font-size:
        clamp(18px, 3vw, 30px);

    letter-spacing: 8px;

    color: white;

    margin-top: 10px;

}


.gold-line {

    width: 180px;

    height: 2px;

    background: #d9ad45;

    margin: 28px auto;

}


.hero-description {

    max-width: 720px;

    margin: 0 auto 30px;

    color: #eeeeee;

    font-family: Arial, sans-serif;

    font-size: 19px;

    line-height: 1.8;

}


/* ============================================================
   BUTTONS
   ============================================================ */

.buttons {

    display: flex;

    justify-content: center;

    align-items: center;

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

    transition: .3s;

}


.button-gold {

    background: #d9ad45;

    color: #061b12;

}


.button-outline {

    border:
        1px solid #d9ad45;

    color: #d9ad45;

}


.button:hover {

    transform: translateY(-5px);

    box-shadow:
        0 12px 30px
        rgba(217,173,69,.25);

}


/* ============================================================
   GENERAL SECTIONS
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

    color: #999;

    font-family: Arial, sans-serif;

}


/* ============================================================
   COLLECTION CARDS
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

    transition: .4s;

}


.card:hover {

    transform: translateY(-10px);

    border-color: #d9ad45;

    box-shadow:
        0 20px 50px
        rgba(0,0,0,.45);

}


.card-icon {

    font-size: 52px;

    margin-bottom: 20px;

}


.card h3 {

    color: #e3bd61;

    font-size: 26px;

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

    color: #999;

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
   STORE / LOCATION
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
   SOCIAL
   ============================================================ */

.social {

    text-align: center;

}


.instagram {

    color: #e3bd61;

    font-size: 27px;

    text-decoration: none;

    transition: .3s;

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

    color: #888;

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

@media(max-width: 850px) {

    nav {

        height: auto;

        padding: 12px 5%;

    }


    nav ul {

        display: none;

    }


    .nav-logo {

        font-size: 19px;

    }


    .nav-whatsapp {

        padding: 9px 15px;

        font-size: 13px;

    }


    .hero {

        background-attachment: scroll;

    }


    .hero h2 {

        letter-spacing: 4px;

    }


    section {

        padding:
            75px 5%;

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


    <ul>

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
        class="nav-whatsapp"
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
            PERFUME & ATTAR
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



        <div class="card">

            <div class="card-icon">
                🪔
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
     WHY AL RASHID
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
                Al Rashid Perfume & Attar
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
            Al Rashid Perfume & Attar
        </h3>


        <p>

            📍

            MG Road,
            Kolar,
            Karnataka

            <br>

            Next to Parvath Sports

            <br><br>

            📞
            +91 96209 63982

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
        Al Rashid Perfume & Attar
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
# RUN WEBSITE
# ============================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )