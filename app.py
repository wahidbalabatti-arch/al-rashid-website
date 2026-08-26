from flask import Flask, render_template_string, send_from_directory
import os

# ============================================================
# FLASK
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)


# ============================================================
# IMAGES
# ============================================================

@app.route("/logo")
def logo():
    return send_from_directory(BASE_DIR, "LOGO.jpeg")


@app.route("/cover")
def cover():
    return send_from_directory(BASE_DIR, "COVER_PAGE.png")


# ============================================================
# WEBSITE
# ============================================================

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<meta name="description"
      content="Al Rashid Perfume & Attar — Premium perfumes, attars and watches in Kolar, Karnataka.">

<title>Al Rashid | Luxury Perfume & Attar</title>


<!-- Google Fonts -->

<link rel="preconnect"
      href="https://fonts.googleapis.com">

<link rel="preconnect"
      href="https://fonts.gstatic.com"
      crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600;700&display=swap"
      rel="stylesheet">


<style>

/* ============================================================
   VARIABLES
   ============================================================ */

:root {

    --green: #03150d;
    --green2: #08251a;
    --green3: #0d3524;

    --gold: #d6ad52;
    --gold-light: #f0d58b;
    --gold-dark: #8c6927;

    --cream: #f8f1df;
    --white: #ffffff;
    --muted: #aaa99f;

}


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

    background: var(--green);

    color: var(--cream);

    font-family: "Montserrat", sans-serif;

    overflow-x: hidden;

}


/* ============================================================
   SCROLLBAR
   ============================================================ */

::-webkit-scrollbar {

    width: 8px;

}


::-webkit-scrollbar-track {

    background: #020c07;

}


::-webkit-scrollbar-thumb {

    background: var(--gold-dark);

    border-radius: 20px;

}


/* ============================================================
   NAVIGATION
   ============================================================ */

.navbar {

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;

    height: 82px;

    z-index: 9999;

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding: 10px 5%;

    background:
        rgba(2, 15, 9, .82);

    backdrop-filter: blur(18px);

    border-bottom:
        1px solid rgba(214,173,82,.22);

    transition: .4s;

}


.brand {

    display: flex;

    align-items: center;

    gap: 13px;

    text-decoration: none;

}


.brand img {

    width: 52px;

    height: 52px;

    object-fit: contain;

}


.brand-name {

    color: var(--gold-light);

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 28px;

    font-weight: 700;

}


.nav-links {

    display: flex;

    gap: 32px;

    list-style: none;

}


.nav-links a {

    color: #eee;

    text-decoration: none;

    font-size: 13px;

    font-weight: 500;

    letter-spacing: 1px;

    transition: .3s;

}


.nav-links a:hover {

    color: var(--gold-light);

}


.nav-whatsapp {

    padding: 12px 21px;

    border-radius: 30px;

    background:
        linear-gradient(
            135deg,
            var(--gold-light),
            var(--gold)
        );

    color: #06150d;

    font-size: 13px;

    font-weight: 700;

    text-decoration: none;

    transition: .3s;

}


.nav-whatsapp:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 30px
        rgba(214,173,82,.25);

}


/* ============================================================
   MOBILE MENU
   ============================================================ */

.menu-button {

    display: none;

    border: 1px solid var(--gold-dark);

    background: transparent;

    color: var(--gold-light);

    font-size: 22px;

    width: 43px;

    height: 43px;

    border-radius: 10px;

}


.mobile-menu {

    display: none;

    position: fixed;

    top: 82px;

    left: 0;

    width: 100%;

    z-index: 9998;

    background: rgba(3,21,13,.97);

    border-bottom:
        1px solid var(--gold-dark);

    padding: 20px;

}


.mobile-menu a {

    display: block;

    padding: 15px;

    text-align: center;

    color: white;

    text-decoration: none;

    border-bottom:
        1px solid rgba(214,173,82,.1);

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
        130px 20px 80px;

    background-color: var(--green);

    background-image:

        linear-gradient(
            rgba(1,12,7,.42),
            rgba(1,12,7,.86)
        ),

        url("/cover");

    background-size: cover;

    background-position: center;

    background-repeat: no-repeat;

    overflow: hidden;

}


.hero::before {

    content: "";

    position: absolute;

    width: 600px;

    height: 600px;

    border-radius: 50%;

    background:
        rgba(214,173,82,.08);

    filter: blur(100px);

    top: 20%;

    left: 50%;

    transform:
        translate(-50%, -50%);

}


.hero-content {

    position: relative;

    z-index: 2;

    max-width: 1050px;

    animation:
        heroAppear 1.3s ease;

}


@keyframes heroAppear {

    from {

        opacity: 0;

        transform:
            translateY(30px);

    }

    to {

        opacity: 1;

        transform:
            translateY(0);

    }

}


.hero-logo {

    width: 145px;

    height: 145px;

    object-fit: contain;

    margin-bottom: 15px;

    filter:
        drop-shadow(
            0 0 30px
            rgba(214,173,82,.5)
        );

}


.small-label {

    font-size: 12px;

    letter-spacing: 6px;

    color: var(--gold-light);

    margin-bottom: 18px;

    text-transform: uppercase;

}


.hero-title {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(70px, 12vw, 150px);

    line-height: .8;

    font-weight: 600;

    color: var(--gold-light);

    letter-spacing: -3px;

    text-shadow:
        0 8px 40px
        rgba(0,0,0,.7);

}


.hero-subtitle {

    margin-top: 30px;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(23px, 4vw, 40px);

    letter-spacing: 10px;

    color: white;

}


.ornament {

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 15px;

    margin: 28px auto;

}


.ornament span {

    width: 80px;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            var(--gold)
        );

}


.ornament span:last-child {

    background:
        linear-gradient(
            90deg,
            var(--gold),
            transparent
        );

}


.ornament b {

    color: var(--gold);

    font-size: 15px;

}


.hero-text {

    max-width: 720px;

    margin: auto;

    color: #eee;

    font-size: 16px;

    line-height: 1.9;

}


.hero-buttons {

    display: flex;

    justify-content: center;

    flex-wrap: wrap;

    gap: 14px;

    margin-top: 32px;

}


.btn {

    padding: 15px 29px;

    border-radius: 50px;

    text-decoration: none;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: .5px;

    transition: .35s;

}


.btn-gold {

    color: #07150d;

    background:
        linear-gradient(
            135deg,
            var(--gold-light),
            var(--gold)
        );

}


.btn-outline {

    color: var(--gold-light);

    border:
        1px solid var(--gold);

    background:
        rgba(0,0,0,.15);

}


.btn:hover {

    transform:
        translateY(-5px);

    box-shadow:
        0 15px 35px
        rgba(0,0,0,.35);

}


/* ============================================================
   SECTION COMMON
   ============================================================ */

section {

    padding: 110px 6%;

    position: relative;

}


.section-heading {

    text-align: center;

    max-width: 750px;

    margin:
        0 auto 60px;

}


.section-label {

    color: var(--gold);

    font-size: 11px;

    letter-spacing: 5px;

    text-transform: uppercase;

    margin-bottom: 14px;

}


.section-heading h2 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(42px, 6vw, 65px);

    font-weight: 600;

    color: var(--gold-light);

}


.section-heading p {

    color: var(--muted);

    margin-top: 12px;

    line-height: 1.8;

    font-size: 14px;

}


/* ============================================================
   COLLECTION
   ============================================================ */

.collection {

    background:

        radial-gradient(
            circle at 20% 20%,
            rgba(214,173,82,.05),
            transparent 30%
        );

}


.product-grid {

    max-width: 1200px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(
            4,
            1fr
        );

    gap: 20px;

}


.product {

    min-height: 300px;

    position: relative;

    overflow: hidden;

    display: flex;

    flex-direction: column;

    justify-content: flex-end;

    padding: 28px;

    border:
        1px solid rgba(214,173,82,.25);

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            #103522,
            #061a10
        );

    transition: .45s;

}


.product::before {

    content: "";

    position: absolute;

    width: 180px;

    height: 180px;

    border-radius: 50%;

    background:
        rgba(214,173,82,.07);

    top: -60px;

    right: -60px;

    transition: .5s;

}


.product:hover {

    transform:
        translateY(-10px);

    border-color:
        var(--gold);

    box-shadow:
        0 25px 60px
        rgba(0,0,0,.4);

}


.product:hover::before {

    transform: scale(2);

}


.product-icon {

    font-size: 60px;

    margin-bottom: auto;

    position: relative;

}


.product-number {

    position: absolute;

    top: 20px;

    right: 22px;

    color:
        rgba(214,173,82,.45);

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 25px;

}


.product h3 {

    position: relative;

    color: var(--gold-light);

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 30px;

    margin-bottom: 8px;

}


.product p {

    position: relative;

    color: #aaa;

    font-size: 13px;

    line-height: 1.7;

}


/* ============================================================
   LUXURY STATISTICS
   ============================================================ */

.stats {

    background:
        #071d13;

    border-top:
        1px solid rgba(214,173,82,.15);

    border-bottom:
        1px solid rgba(214,173,82,.15);

}


.stat-grid {

    max-width: 1000px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

}


.stat {

    text-align: center;

    padding: 25px;

    border-right:
        1px solid rgba(214,173,82,.15);

}


.stat:last-child {

    border-right: none;

}


.stat-number {

    color: var(--gold-light);

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 45px;

}


.stat-text {

    color: #999;

    font-size: 11px;

    letter-spacing: 2px;

    text-transform: uppercase;

}


/* ============================================================
   EXPERIENCE
   ============================================================ */

.experience {

    background:
        linear-gradient(
            180deg,
            #03150d,
            #061c12
        );

}


.experience-box {

    max-width: 1100px;

    margin: auto;

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 60px;

    align-items: center;

}


.experience-image {

    min-height: 450px;

    border-radius: 25px;

    background:

        linear-gradient(
            rgba(0,0,0,.25),
            rgba(0,0,0,.55)
        ),

        url("/cover");

    background-size: cover;

    background-position: center;

    border:
        1px solid rgba(214,173,82,.35);

    box-shadow:
        0 30px 70px
        rgba(0,0,0,.35);

}


.experience-text h2 {

    font-family:
        "Cormorant Garamond",
        serif;

    color: var(--gold-light);

    font-size: 55px;

    line-height: 1;

    margin-bottom: 25px;

}


.experience-text p {

    color: #b7b7b2;

    font-size: 14px;

    line-height: 2;

    margin-bottom: 20px;

}


.signature {

    color: var(--gold);

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 30px;

    font-style: italic;

}


/* ============================================================
   WHY US
   ============================================================ */

.features {

    max-width: 1100px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 20px;

}


.feature {

    padding: 35px 22px;

    text-align: center;

    background:
        rgba(255,255,255,.025);

    border:
        1px solid rgba(214,173,82,.14);

    border-radius: 18px;

    transition: .35s;

}


.feature:hover {

    transform:
        translateY(-7px);

    border-color:
        rgba(214,173,82,.5);

}


.feature-icon {

    font-size: 35px;

    margin-bottom: 18px;

}


.feature h3 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 25px;

    color: var(--gold-light);

    margin-bottom: 10px;

}


.feature p {

    color: #999;

    font-size: 12px;

    line-height: 1.8;

}


/* ============================================================
   REVIEWS
   ============================================================ */

.reviews {

    background:
        #061b12;

}


.review-grid {

    max-width: 1100px;

    margin: auto;

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 20px;

}


.review {

    padding: 32px;

    background:
        rgba(255,255,255,.025);

    border:
        1px solid rgba(214,173,82,.17);

    border-radius: 18px;

}


.stars {

    color: var(--gold);

    letter-spacing: 3px;

    margin-bottom: 18px;

}


.review p {

    color: #c7c7c2;

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 21px;

    line-height: 1.5;

    font-style: italic;

}


.reviewer {

    color: var(--gold-light);

    margin-top: 22px;

    font-size: 12px;

}


/* ============================================================
   INSTAGRAM
   ============================================================ */

.instagram-section {

    text-align: center;

}


.instagram-handle {

    display: inline-block;

    margin-top: 10px;

    color: var(--gold-light);

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 34px;

    text-decoration: none;

    transition: .3s;

}


.instagram-handle:hover {

    color: white;

}


/* ============================================================
   LOCATION
   ============================================================ */

.location {

    background:
        linear-gradient(
            180deg,
            #03150d,
            #020d08
        );

}


.location-card {

    max-width: 1000px;

    margin: auto;

    padding: 55px;

    text-align: center;

    border:
        1px solid rgba(214,173,82,.3);

    border-radius: 25px;

    background:
        linear-gradient(
            145deg,
            #0d2f20,
            #06170e
        );

    box-shadow:
        0 25px 60px
        rgba(0,0,0,.25);

}


.location-card h3 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 40px;

    color: var(--gold-light);

}


.location-card p {

    color: #bbb;

    font-size: 14px;

    line-height: 2;

    margin:
        20px 0 28px;

}


/* ============================================================
   CTA
   ============================================================ */

.cta {

    padding: 120px 20px;

    text-align: center;

    background:

        linear-gradient(
            rgba(2,15,9,.72),
            rgba(2,15,9,.9)
        ),

        url("/cover");

    background-size: cover;

    background-position: center;

}


.cta h2 {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size:
        clamp(45px, 7vw, 75px);

    color: var(--gold-light);

}


.cta p {

    max-width: 650px;

    margin: 20px auto;

    color: #ddd;

    line-height: 1.8;

}


/* ============================================================
   FOOTER
   ============================================================ */

footer {

    padding: 65px 20px 30px;

    text-align: center;

    background: #010a06;

    border-top:
        1px solid rgba(214,173,82,.2);

}


.footer-logo {

    width: 70px;

    height: 70px;

    object-fit: contain;

    margin-bottom: 10px;

}


.footer-name {

    font-family:
        "Cormorant Garamond",
        serif;

    font-size: 30px;

    color: var(--gold-light);

}


.footer-links {

    margin:
        25px 0;

}


.footer-links a {

    margin:
        0 10px;

    color: #999;

    text-decoration: none;

    font-size: 12px;

}


.footer-links a:hover {

    color: var(--gold);

}


.copyright {

    color: #555;

    font-size: 11px;

}


/* ============================================================
   FLOATING WHATSAPP
   ============================================================ */

.whatsapp-float {

    position: fixed;

    right: 22px;

    bottom: 22px;

    width: 62px;

    height: 62px;

    z-index: 9990;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;

    background: #25D366;

    color: white;

    text-decoration: none;

    font-size: 28px;

    box-shadow:
        0 10px 30px
        rgba(0,0,0,.4);

    transition: .3s;

}


.whatsapp-float:hover {

    transform:
        scale(1.1);

}


/* ============================================================
   REVEAL ANIMATION
   ============================================================ */

.reveal {

    opacity: 0;

    transform:
        translateY(30px);

    transition:
        opacity .8s ease,
        transform .8s ease;

}


.reveal.active {

    opacity: 1;

    transform:
        translateY(0);

}


/* ============================================================
   TABLET
   ============================================================ */

@media(max-width: 1000px) {

    .product-grid {

        grid-template-columns:
            repeat(2, 1fr);

    }


    .features {

        grid-template-columns:
            repeat(2, 1fr);

    }


    .stat-grid {

        grid-template-columns:
            repeat(2, 1fr);

    }


    .stat {

        border-bottom:
            1px solid rgba(214,173,82,.15);

    }


    .review-grid {

        grid-template-columns:
            1fr;

    }

}


/* ============================================================
   MOBILE
   ============================================================ */

@media(max-width: 760px) {

    .navbar {

        height: 70px;

    }


    .nav-links {

        display: none;

    }


    .nav-whatsapp {

        display: none;

    }


    .menu-button {

        display: block;

    }


    .mobile-menu.show {

        display: block;

    }


    .brand-name {

        font-size: 23px;

    }


    .hero {

        min-height: 100svh;

        padding-top: 110px;

        background-position:
            center center;

    }


    .hero-logo {

        width: 110px;

        height: 110px;

    }


    .hero-title {

        font-size: 72px;

        letter-spacing: -2px;

    }


    .hero-subtitle {

        font-size: 19px;

        letter-spacing: 5px;

    }


    .hero-text {

        font-size: 14px;

    }


    section {

        padding:
            80px 5%;

    }


    .product-grid {

        grid-template-columns:
            1fr;

    }


    .features {

        grid-template-columns:
            1fr;

    }


    .stat-grid {

        grid-template-columns:
            1fr 1fr;

    }


    .stat {

        border-right:
            1px solid rgba(214,173,82,.15);

    }


    .experience-box {

        grid-template-columns:
            1fr;

    }


    .experience-image {

        min-height: 350px;

    }


    .experience-text h2 {

        font-size: 45px;

    }


    .location-card {

        padding: 35px 20px;

    }


    .location-card h3 {

        font-size: 32px;

    }


    .cta {

        padding:
            90px 20px;

    }

}


/* ============================================================
   VERY SMALL
   ============================================================ */

@media(max-width: 420px) {

    .hero-title {

        font-size: 60px;

    }


    .hero-subtitle {

        font-size: 16px;

        letter-spacing: 4px;

    }


    .stat-grid {

        grid-template-columns:
            1fr;

    }


    .stat {

        border-right: none;

    }


    .btn {

        width: 100%;

        max-width: 310px;

    }

}

</style>

</head>


<body>


<!-- ============================================================
     NAVIGATION
     ============================================================ -->

<nav class="navbar">


    <a
        href="#home"
        class="brand">

        <img
            src="/logo"
            alt="Al Rashid Logo">

        <span class="brand-name">
            Al Rashid
        </span>

    </a>


    <ul class="nav-links">

        <li>
            <a href="#home">HOME</a>
        </li>

        <li>
            <a href="#collection">COLLECTION</a>
        </li>

        <li>
            <a href="#experience">ABOUT</a>
        </li>

        <li>
            <a href="#reviews">REVIEWS</a>
        </li>

        <li>
            <a href="#location">LOCATION</a>
        </li>

    </ul>


    <a
        href="https://wa.me/919620963982"
        target="_blank"
        class="nav-whatsapp">

        WhatsApp

    </a>


    <button
        class="menu-button"
        onclick="toggleMenu()">

        ☰

    </button>

</nav>


<!-- MOBILE MENU -->

<div
    class="mobile-menu"
    id="mobileMenu">

    <a href="#home"
       onclick="toggleMenu()">
       Home
    </a>

    <a href="#collection"
       onclick="toggleMenu()">
       Collection
    </a>

    <a href="#experience"
       onclick="toggleMenu()">
       About
    </a>

    <a href="#reviews"
       onclick="toggleMenu()">
       Reviews
    </a>

    <a href="#location"
       onclick="toggleMenu()">
       Location
    </a>

</div>



<!-- ============================================================
     HERO
     ============================================================ -->

<header
    class="hero"
    id="home">


    <div class="hero-content">


        <img
            src="/logo"
            class="hero-logo"
            alt="Al Rashid">


        <div class="small-label">
            ESTABLISHED WITH PASSION
        </div>


        <h1 class="hero-title">
            Al Rashid
        </h1>


        <div class="hero-subtitle">
            PERFUME &amp; ATTAR
        </div>


        <div class="ornament">

            <span></span>

            <b>✦</b>

            <span></span>

        </div>


        <p class="hero-text">

            Discover an elegant world of
            premium fragrances, timeless
            attars and refined style.

            <br>

            Find the fragrance that becomes
            part of your identity.

        </p>


        <div class="hero-buttons">


            <a
                href="#collection"
                class="btn btn-gold">

                EXPLORE COLLECTION

            </a>


            <a
                href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20know%20about%20your%20fragrances."
                target="_blank"
                class="btn btn-outline">

                💬 ORDER ON WHATSAPP

            </a>


        </div>


    </div>

</header>



<!-- ============================================================
     COLLECTION
     ============================================================ -->

<section
    class="collection"
    id="collection">


    <div class="section-heading reveal">

        <div class="section-label">
            THE COLLECTION
        </div>

        <h2>
            Crafted For Your Presence
        </h2>

        <p>
            Explore our carefully selected
            collection of fragrances and
            accessories.
        </p>

    </div>


    <div class="product-grid">


        <div class="product reveal">

            <div class="product-number">
                01
            </div>

            <div class="product-icon">
                🌹
            </div>

            <h3>
                Premium Perfumes
            </h3>

            <p>
                Sophisticated fragrances
                created for memorable
                occasions.
            </p>

        </div>


        <div class="product reveal">

            <div class="product-number">
                02
            </div>

            <div class="product-icon">
                🪔
            </div>

            <h3>
                Luxury Attars
            </h3>

            <p>
                Rich traditional scents
                with a modern character.
            </p>

        </div>


        <div class="product reveal">

            <div class="product-number">
                03
            </div>

            <div class="product-icon">
                ⌚
            </div>

            <h3>
                Premium Watches
            </h3>

            <p>
                Elegant timepieces that
                complete your style.
            </p>

        </div>


        <div class="product reveal">

            <div class="product-number">
                04
            </div>

            <div class="product-icon">
                ✨
            </div>

            <h3>
                New Arrivals
            </h3>

            <p>
                Discover our latest
                fragrances and products.
            </p>

        </div>


    </div>

</section>



<!-- ============================================================
     STATS
     ============================================================ -->

<section class="stats">


    <div class="stat-grid">


        <div class="stat reveal">

            <div class="stat-number">
                ✦
            </div>

            <div class="stat-text">
                Premium
            </div>

        </div>


        <div class="stat reveal">

            <div class="stat-number">
                100%
            </div>

            <div class="stat-text">
                Passion
            </div>

        </div>


        <div class="stat reveal">

            <div class="stat-number">
                ♥
            </div>

            <div class="stat-text">
                Customer First
            </div>

        </div>


        <div class="stat reveal">

            <div class="stat-number">
                KLR
            </div>

            <div class="stat-text">
                Kolar
            </div>

        </div>


    </div>

</section>



<!-- ============================================================
     EXPERIENCE
     ============================================================ -->

<section
    class="experience"
    id="experience">


    <div class="experience-box">


        <div
            class="experience-image reveal">
        </div>


        <div class="experience-text reveal">


            <div class="section-label">
                OUR STORY
            </div>


            <h2>
                A Fragrance
                <br>
                Worth Remembering
            </h2>


            <p>

                At

                <strong style="color:#d6ad52;">
                    Al Rashid
                </strong>,

                fragrance is more than
                a scent. It is a way of
                expressing personality,
                confidence and memories.

            </p>


            <p>

                We bring together premium
                perfumes, traditional attars
                and stylish watches for
                people who appreciate
                quality and elegance.

            </p>


            <div class="signature">
                Al Rashid
            </div>


        </div>


    </div>

</section>



<!-- ============================================================
     WHY US
     ============================================================ -->

<section>


    <div class="section-heading reveal">

        <div class="section-label">
            THE AL RASHID EXPERIENCE
        </div>

        <h2>
            Why Choose Us?
        </h2>

    </div>


    <div class="features">


        <div class="feature reveal">

            <div class="feature-icon">
                💎
            </div>

            <h3>
                Premium Quality
            </h3>

            <p>
                Carefully selected
                fragrances and products.
            </p>

        </div>


        <div class="feature reveal">

            <div class="feature-icon">
                🌿
            </div>

            <h3>
                Rich Fragrance
            </h3>

            <p>
                Beautiful scent profiles
                for every personality.
            </p>

        </div>


        <div class="feature reveal">

            <div class="feature-icon">
                ✨
            </div>

            <h3>
                Elegant Style
            </h3>

            <p>
                Products chosen to
                complement your style.
            </p>

        </div>


        <div class="feature reveal">

            <div class="feature-icon">
                ❤️
            </div>

            <h3>
                Personal Service
            </h3>

            <p>
                We care about every
                customer's experience.
            </p>

        </div>


    </div>

</section>



<!-- ============================================================
     REVIEWS
     ============================================================ -->

<section
    class="reviews"
    id="reviews">


    <div class="section-heading reveal">

        <div class="section-label">
            CUSTOMER LOVE
        </div>

        <h2>
            What Customers Say
        </h2>

        <p>
            Your experience means everything
            to us.
        </p>

    </div>


    <div class="review-grid">


        <div class="review reveal">

            <div class="stars">
                ★★★★★
            </div>

            <p>
                "Beautiful fragrance and
                excellent quality. The scent
                feels premium and elegant."
            </p>

            <div class="reviewer">
                — Customer
            </div>

        </div>


        <div class="review reveal">

            <div class="stars">
                ★★★★★
            </div>

            <p>
                "Loved the perfume collection.
                Very good options and
                friendly service."
            </p>

            <div class="reviewer">
                — Customer
            </div>

        </div>


        <div class="review reveal">

            <div class="stars">
                ★★★★★
            </div>

            <p>
                "The fragrance quality is
                really impressive. Definitely
                worth visiting."
            </p>

            <div class="reviewer">
                — Customer
            </div>

        </div>


    </div>

</section>



<!-- ============================================================
     INSTAGRAM
     ============================================================ -->

<section
    class="instagram-section">


    <div class="section-heading reveal">

        <div class="section-label">
            FOLLOW OUR JOURNEY
        </div>

        <h2>
            Discover More
        </h2>

        <p>
            Follow us for new arrivals,
            fragrances and updates.
        </p>


        <a
            href="https://www.instagram.com/alrashid.luxury/"
            target="_blank"
            class="instagram-handle">

            @alrashid.luxury

        </a>

    </div>


    <a
        href="https://www.instagram.com/alrashid.luxury/"
        target="_blank"
        class="btn btn-outline">

        FOLLOW ON INSTAGRAM

    </a>

</section>



<!-- ============================================================
     LOCATION
     ============================================================ -->

<section
    class="location"
    id="location">


    <div class="section-heading reveal">

        <div class="section-label">
            FIND US
        </div>

        <h2>
            Visit Our Store
        </h2>

    </div>


    <div class="location-card reveal">


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


        <div class="hero-buttons">


            <a
                href="https://www.google.com/maps/search/?api=1&query=Al+Rashid+Perfume+Attar+MG+Road+Kolar"
                target="_blank"
                class="btn btn-gold">

                📍 OPEN GOOGLE MAPS

            </a>


            <a
                href="https://wa.me/919620963982"
                target="_blank"
                class="btn btn-outline">

                💬 WHATSAPP US

            </a>


        </div>


    </div>

</section>



<!-- ============================================================
     CTA
     ============================================================ -->

<section class="cta">


    <div class="reveal">


        <div class="section-label">
            YOUR SIGNATURE AWAITS
        </div>


        <h2>
            Find Your Signature Scent
        </h2>


        <p>
            Let your fragrance become
            part of the impression
            you leave behind.
        </p>


        <div class="hero-buttons">


            <a
                href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20want%20to%20explore%20your%20premium%20perfumes."
                target="_blank"
                class="btn btn-gold">

                💬 TALK TO US

            </a>


            <a
                href="#collection"
                class="btn btn-outline">

                EXPLORE COLLECTION

            </a>


        </div>


    </div>

</section>



<!-- ============================================================
     FOOTER
     ============================================================ -->

<footer>


    <img
        src="/logo"
        class="footer-logo"
        alt="Al Rashid Logo">


    <div class="footer-name">
        Al Rashid
    </div>


    <div
        style="
        color:#777;
        margin-top:5px;
        font-family:Georgia,serif;
        ">

        PERFUME &amp; ATTAR

    </div>


    <div class="footer-links">

        <a href="#home">
            Home
        </a>

        <a href="#collection">
            Collection
        </a>

        <a href="#experience">
            About
        </a>

        <a href="#reviews">
            Reviews
        </a>

        <a href="#location">
            Location
        </a>

    </div>


    <div class="copyright">

        © 2026 Al Rashid Perfume &amp; Attar.
        All Rights Reserved.

        <br>

        MG Road, Kolar, Karnataka
        •
        +91 96209 63982

    </div>


</footer>



<!-- ============================================================
     FLOATING WHATSAPP
     ============================================================ -->

<a
    href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20know%20about%20your%20products."
    target="_blank"
    class="whatsapp-float"
    aria-label="WhatsApp">

    ☎

</a>



<!-- ============================================================
     JAVASCRIPT
     ============================================================ -->

<script>


function toggleMenu() {

    const menu =
        document.getElementById("mobileMenu");

    menu.classList.toggle("show");

}


/* ============================================================
   SCROLL REVEAL
   ============================================================ */

const observer =
    new IntersectionObserver(

        (entries) => {

            entries.forEach(
                (entry) => {

                    if (entry.isIntersecting) {

                        entry.target
                            .classList
                            .add("active");

                    }

                }
            );

        },

        {
            threshold: 0.12
        }

    );


document
    .querySelectorAll(".reveal")
    .forEach(
        (element) => {

            observer.observe(element);

        }
    );


/* ============================================================
   CLOSE MOBILE MENU
   ============================================================ */

document
    .querySelectorAll(".mobile-menu a")
    .forEach(
        (link) => {

            link.addEventListener(
                "click",
                () => {

                    document
                        .getElementById("mobileMenu")
                        .classList
                        .remove("show");

                }
            );

        }
    );


</script>


</body>

</html>
"""


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template_string(HTML)


# ============================================================
# SERVER
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