from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =========================================================
# IMAGES
# =========================================================

@app.route("/logo")
def logo():
    return send_from_directory(BASE_DIR, "LOGO.jpeg")


@app.route("/cover")
def cover():
    return send_from_directory(BASE_DIR, "COVER_PAGE.png")


# =========================================================
# WEBSITE
# =========================================================

HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<meta name="description"
      content="Al Rashid - Premium Perfumes and Luxury Attars in Kolar">

<title>AL RASHID | Perfume & Attar</title>


<link rel="preconnect"
      href="https://fonts.googleapis.com">

<link rel="preconnect"
      href="https://fonts.gstatic.com"
      crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap"
      rel="stylesheet">


<style>

/* =========================================================
   BASIC
========================================================= */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {

    background: #050706;

    color: #f5f1e6;

    font-family: "Montserrat", sans-serif;

    overflow-x: hidden;
}


/* =========================================================
   NAVIGATION
========================================================= */

nav {

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;

    height: 78px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 0 6%;

    z-index: 1000;

    background: rgba(5, 7, 6, 0.88);

    backdrop-filter: blur(15px);

    border-bottom: 1px solid
                rgba(212, 175, 91, 0.15);
}


.logo-area {

    display: flex;

    align-items: center;

    gap: 12px;

    text-decoration: none;
}


.logo-area img {

    width: 45px;
    height: 45px;

    object-fit: contain;
}


.logo-name {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 27px;

    color: #d8b866;

    letter-spacing: 1px;
}


nav ul {

    display: flex;

    gap: 30px;

    list-style: none;
}


nav ul a {

    text-decoration: none;

    color: #d0d0ca;

    font-size: 10px;

    letter-spacing: 2px;

    transition: 0.3s;
}


nav ul a:hover {

    color: #d8b866;
}


.nav-button {

    text-decoration: none;

    padding: 11px 20px;

    border-radius: 30px;

    background: #d8b866;

    color: #07100b;

    font-size: 10px;

    font-weight: 600;

    letter-spacing: 1px;
}


/* =========================================================
   HERO
========================================================= */

.hero {

    height: 100vh;

    min-height: 650px;

    position: relative;

    display: flex;

    align-items: center;

    justify-content: center;

    text-align: center;

    background:

        linear-gradient(
            rgba(0, 0, 0, 0.35),
            rgba(0, 0, 0, 0.78)
        ),

        url("/cover");

    background-size: cover;

    background-position: center;
}


.hero-content {

    max-width: 800px;

    padding: 30px;
}


.hero-logo {

    width: 105px;

    height: 105px;

    object-fit: contain;

    margin-bottom: 25px;
}


.small-title {

    color: #d8b866;

    font-size: 10px;

    letter-spacing: 6px;

    margin-bottom: 15px;
}


.hero h1 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(70px, 12vw, 145px);

    font-weight: 500;

    line-height: 0.8;

    color: #e4c978;
}


.hero h2 {

    margin-top: 25px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(22px, 3vw, 34px);

    font-weight: 400;

    letter-spacing: 7px;
}


.hero p {

    max-width: 570px;

    margin: 25px auto 0;

    color: #d0d0ca;

    font-size: 13px;

    line-height: 1.9;
}


.buttons {

    display: flex;

    justify-content: center;

    gap: 12px;

    margin-top: 30px;

    flex-wrap: wrap;
}


.button {

    text-decoration: none;

    padding: 14px 27px;

    border-radius: 30px;

    font-size: 10px;

    letter-spacing: 1.5px;

    transition: 0.3s;
}


.button-gold {

    background: #d8b866;

    color: #07100b;
}


.button-outline {

    border: 1px solid #d8b866;

    color: #e4c978;
}


.button:hover {

    transform: translateY(-3px);
}


/* =========================================================
   SECTIONS
========================================================= */

section {

    padding: 100px 7%;
}


.section-title {

    text-align: center;

    max-width: 700px;

    margin: 0 auto 55px;
}


.section-title span {

    color: #d8b866;

    font-size: 9px;

    letter-spacing: 4px;
}


.section-title h2 {

    margin-top: 12px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(45px, 6vw, 65px);

    font-weight: 500;

    color: #e4c978;
}


.section-title p {

    margin-top: 15px;

    color: #888d87;

    font-size: 12px;

    line-height: 1.8;
}


/* =========================================================
   COLLECTION
========================================================= */

.collection {

    background: #07100c;
}


.collection-grid {

    max-width: 1100px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 20px;
}


.collection-card {

    min-height: 330px;

    padding: 35px;

    display: flex;

    flex-direction: column;

    justify-content: flex-end;

    position: relative;

    overflow: hidden;

    border: 1px solid
            rgba(216, 184, 102, 0.18);

    background:
        linear-gradient(
            145deg,
            #123424,
            #07110c
        );

    transition: 0.4s;
}


.collection-card:hover {

    transform: translateY(-8px);

    border-color: #d8b866;
}


.card-number {

    position: absolute;

    top: 22px;
    right: 25px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 30px;

    color:
        rgba(216, 184, 102, 0.3);
}


.card-icon {

    font-size: 42px;

    margin-bottom: auto;
}


.collection-card h3 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 32px;

    font-weight: 500;

    color: #e4c978;
}


.collection-card p {

    margin-top: 8px;

    color: #929791;

    font-size: 11px;

    line-height: 1.8;
}


/* =========================================================
   ABOUT
========================================================= */

.about {

    background: #050706;
}


.about-container {

    max-width: 1050px;

    margin: auto;

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 60px;

    align-items: center;
}


.about-image {

    height: 520px;

    background:

        linear-gradient(
            rgba(0,0,0,0.1),
            rgba(0,0,0,0.4)
        ),

        url("/cover");

    background-size: cover;

    background-position: center;

    border: 1px solid
            rgba(216, 184, 102, 0.25);
}


.about-text span {

    color: #d8b866;

    font-size: 9px;

    letter-spacing: 4px;
}


.about-text h2 {

    margin-top: 15px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 60px;

    line-height: 0.9;

    color: #e4c978;

    font-weight: 500;
}


.about-text p {

    margin-top: 20px;

    color: #999d98;

    font-size: 12px;

    line-height: 2;
}


/* =========================================================
   FEATURED
========================================================= */

.featured {

    background: #07100c;
}


.featured-box {

    max-width: 900px;

    margin: auto;

    padding: 55px 30px;

    text-align: center;

    border: 1px solid
            rgba(216, 184, 102, 0.25);

    background:
        linear-gradient(
            145deg,
            #102b1d,
            #06100b
        );
}


.featured-box h3 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 43px;

    color: #e4c978;
}


.featured-box p {

    max-width: 600px;

    margin: 15px auto 25px;

    color: #999d98;

    font-size: 12px;

    line-height: 1.8;
}


/* =========================================================
   CONTACT
========================================================= */

.contact {

    background: #050706;

    text-align: center;
}


.contact-box {

    max-width: 800px;

    margin: auto;

    padding: 60px 25px;

    border: 1px solid
            rgba(216, 184, 102, 0.2);
}


.contact-box h2 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 55px;

    color: #e4c978;
}


.contact-box p {

    margin: 18px 0 25px;

    color: #929791;

    font-size: 12px;

    line-height: 2;
}


.phone {

    color: #d8b866;

    font-size: 17px;

    text-decoration: none;
}


/* =========================================================
   FOOTER
========================================================= */

footer {

    padding: 60px 20px 30px;

    text-align: center;

    background: #020302;

    border-top: 1px solid
                rgba(216, 184, 102, 0.15);
}


.footer-logo {

    width: 60px;

    height: 60px;

    object-fit: contain;
}


.footer-name {

    margin-top: 8px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 32px;

    color: #d8b866;
}


.social {

    margin: 22px 0;
}


.social a {

    color: #999d98;

    text-decoration: none;

    font-size: 11px;

    transition: 0.3s;
}


.social a:hover {

    color: #d8b866;
}


.copyright {

    color: #555a55;

    font-size: 9px;

    line-height: 1.8;
}


/* =========================================================
   WHATSAPP
========================================================= */

.whatsapp {

    position: fixed;

    right: 22px;

    bottom: 22px;

    width: 57px;

    height: 57px;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    background: #25D366;

    color: white;

    text-decoration: none;

    font-size: 25px;

    z-index: 999;

    box-shadow:
        0 8px 25px
        rgba(0,0,0,0.4);

}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 800px) {

    nav ul,
    .nav-button {
        display: none;
    }

    .hero h1 {
        font-size: 72px;
    }

    .collection-grid {
        grid-template-columns: 1fr;
    }

    .about-container {
        grid-template-columns: 1fr;
    }

    .about-image {
        height: 380px;
    }

}


@media (max-width: 500px) {

    section {
        padding: 75px 5%;
    }

    .hero {
        min-height: 650px;
    }

    .hero-logo {
        width: 85px;
        height: 85px;
    }

    .hero h1 {
        font-size: 62px;
    }

    .hero h2 {
        font-size: 18px;
        letter-spacing: 4px;
    }

    .about-text h2 {
        font-size: 48px;
    }

    .contact-box h2 {
        font-size: 43px;
    }

    .button {
        width: 100%;
        max-width: 300px;
    }

}

</style>

</head>


<body>


<!-- =========================================================
     NAV
========================================================= -->

<nav>

    <a href="#home" class="logo-area">

        <img src="/logo"
             alt="Al Rashid Logo">

        <span class="logo-name">
            Al Rashid
        </span>

    </a>


    <ul>

        <li>
            <a href="#home">
                HOME
            </a>
        </li>

        <li>
            <a href="#collection">
                COLLECTION
            </a>
        </li>

        <li>
            <a href="#about">
                ABOUT
            </a>
        </li>

        <li>
            <a href="#contact">
                CONTACT
            </a>
        </li>

    </ul>


    <a
        href="https://wa.me/919620963982"
        target="_blank"
        class="nav-button">

        WHATSAPP

    </a>

</nav>



<!-- =========================================================
     HERO
========================================================= -->

<header class="hero" id="home">

    <div class="hero-content">


        <img
            src="/logo"
            alt="Al Rashid"
            class="hero-logo">


        <div class="small-title">
            LUXURY FRAGRANCE
        </div>


        <h1>
            AL RASHID
        </h1>


        <h2>
            PERFUME & ATTAR
        </h2>


        <p>

            Discover premium fragrances
            and timeless attars created
            for your signature presence.

        </p>


        <div class="buttons">

            <a
                href="#collection"
                class="button button-gold">

                EXPLORE COLLECTION

            </a>


            <a
                href="https://wa.me/919620963982"
                target="_blank"
                class="button button-outline">

                CONTACT US

            </a>

        </div>


    </div>

</header>



<!-- =========================================================
     COLLECTION
========================================================= -->

<section
    class="collection"
    id="collection">


    <div class="section-title">

        <span>
            OUR COLLECTION
        </span>

        <h2>
            Find Your Fragrance
        </h2>

        <p>
            Carefully selected fragrances
            for every personality and occasion.
        </p>

    </div>


    <div class="collection-grid">


        <div class="collection-card">

            <div class="card-number">
                01
            </div>

            <div class="card-icon">
                🌹
            </div>

            <h3>
                Premium Perfumes
            </h3>

            <p>
                Elegant fragrances with
                distinctive character and
                lasting impressions.
            </p>

        </div>


        <div class="collection-card">

            <div class="card-number">
                02
            </div>

            <div class="card-icon">
                🪔
            </div>

            <h3>
                Luxury Attars
            </h3>

            <p>
                Traditional and rich fragrances
                with depth and character.
            </p>

        </div>


        <div class="collection-card">

            <div class="card-number">
                03
            </div>

            <div class="card-icon">
                ✨
            </div>

            <h3>
                Premium Collection
            </h3>

            <p>
                Explore our carefully selected
                premium fragrance range.
            </p>

        </div>


    </div>


</section>



<!-- =========================================================
     ABOUT
========================================================= -->

<section
    class="about"
    id="about">


    <div class="about-container">


        <div class="about-image">
        </div>


        <div class="about-text">

            <span>
                ABOUT AL RASHID
            </span>

            <h2>
                Fragrance
                With Identity
            </h2>

            <p>

                Al Rashid is a fragrance
                destination in Kolar offering
                premium perfumes and
                traditional attars.

            </p>


            <p>

                We believe the right fragrance
                becomes part of your identity —
                something people remember
                even after you leave.

            </p>


            <p>

                <strong style="color:#d8b866;">
                    Faizan Sheikh
                </strong>
                is the shop owner and is
                committed to providing
                customers with a personal
                and enjoyable fragrance
                experience.

            </p>

        </div>


    </div>


</section>



<!-- =========================================================
     FEATURED
========================================================= -->

<section class="featured">


    <div class="section-title">

        <span>
            FEATURED
        </span>

        <h2>
            Premium Fragrance
        </h2>

    </div>


    <div class="featured-box">


        <h3>
            Your Signature Scent
        </h3>


        <p>

            Looking for something fresh,
            elegant, powerful or traditional?

            Visit Al Rashid and discover
            a fragrance that feels like you.

        </p>


        <a
            href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20want%20to%20know%20about%20your%20premium%20perfumes."
            target="_blank"
            class="button button-gold">

            ASK ABOUT PERFUMES

        </a>


    </div>


</section>



<!-- =========================================================
     CONTACT
========================================================= -->

<section
    class="contact"
    id="contact">


    <div class="section-title">

        <span>
            VISIT US
        </span>

        <h2>
            Come & Discover
        </h2>

    </div>


    <div class="contact-box">


        <h2>
            Al Rashid
        </h2>


        <p>

            Premium Perfumes & Attars

            <br>

            MG Road, Kolar, Karnataka

            <br>

            Next to Parvath Sports

        </p>


        <a
            href="tel:+919620963982"
            class="phone">

            +91 96209 63982

        </a>


        <div class="buttons">


            <a
                href="https://www.google.com/maps/search/?api=1&query=Al+Rashid+Perfume+Attar+MG+Road+Kolar"
                target="_blank"
                class="button button-gold">

                GOOGLE MAPS

            </a>


            <a
                href="https://wa.me/919620963982"
                target="_blank"
                class="button button-outline">

                WHATSAPP

            </a>


        </div>


    </div>


</section>



<!-- =========================================================
     FOOTER
========================================================= -->

<footer>


    <img
        src="/logo"
        alt="Al Rashid"
        class="footer-logo">


    <div class="footer-name">
        AL RASHID
    </div>


    <div class="social">

        <a
            href="https://www.instagram.com/alrashid.luxury/"
            target="_blank">

            Instagram
            ·
            @alrashid.luxury

        </a>

    </div>


    <div class="copyright">

        © 2026 Al Rashid Perfume & Attar

        <br>

        Kolar, Karnataka
        ·
        +91 96209 63982

    </div>


</footer>



<!-- =========================================================
     WHATSAPP
========================================================= -->

<a
    href="https://wa.me/919620963982"
    target="_blank"
    class="whatsapp">

    ☎

</a>


</body>

</html>
"""


# =========================================================
# HOME ROUTE
# =========================================================

@app.route("/")
def home():

    return render_template_string(HTML)


# =========================================================
# RUN
# =========================================================

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