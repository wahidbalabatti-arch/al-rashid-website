from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================
# IMAGE ROUTES
# ============================================================

@app.route("/logo")
def logo():
    return send_from_directory(BASE_DIR, "LOGO.jpeg")


@app.route("/cover")
def cover():
    return send_from_directory(BASE_DIR, "COVER_PAGE.png")


# ============================================================
# LUXURY WEBSITE
# ============================================================

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<meta name="description"
content="Al Rashid — Premium Perfume, Attar & Luxury Collection in Kolar.">

<title>AL RASHID — Perfume & Attar</title>

<link rel="preconnect" href="https://fonts.googleapis.com">

<link rel="preconnect"
href="https://fonts.gstatic.com"
crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;600;700&family=DM+Sans:wght@300;400;500;600&display=swap"
rel="stylesheet">


<style>

/* =========================================================
   CORE
========================================================= */

:root{

    --black:#030504;
    --black2:#07100c;
    --emerald:#09251a;
    --emerald2:#103a28;

    --gold:#c9a24d;
    --gold2:#e7ca7b;
    --gold3:#8c6a2b;

    --white:#f8f5ed;
    --muted:#9d9c94;

}


*{
    margin:0;
    padding:0;
    box-sizing:border-box;
}


html{
    scroll-behavior:smooth;
}


body{

    background:var(--black);

    color:var(--white);

    font-family:"DM Sans",sans-serif;

    overflow-x:hidden;

}


/* =========================================================
   CURSOR GLOW
========================================================= */

.cursor-glow{

    position:fixed;

    width:300px;
    height:300px;

    border-radius:50%;

    background:
    radial-gradient(
        circle,
        rgba(201,162,77,.06),
        transparent 70%
    );

    pointer-events:none;

    transform:translate(-50%,-50%);

    z-index:0;

}


/* =========================================================
   NAVBAR
========================================================= */

.nav{

    position:fixed;

    top:0;
    left:0;

    width:100%;

    height:86px;

    display:flex;

    align-items:center;

    justify-content:space-between;

    padding:0 5%;

    z-index:9999;

    background:
    linear-gradient(
        rgba(3,5,4,.92),
        rgba(3,5,4,.60)
    );

    backdrop-filter:blur(20px);

    border-bottom:
    1px solid rgba(201,162,77,.16);

}


.brand{

    display:flex;

    align-items:center;

    gap:13px;

    text-decoration:none;

}


.brand img{

    width:48px;
    height:48px;

    object-fit:contain;

}


.brand-text{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:29px;

    color:var(--gold2);

    letter-spacing:1px;

}


.links{

    display:flex;

    gap:35px;

    list-style:none;

}


.links a{

    text-decoration:none;

    color:#ddd;

    font-size:11px;

    letter-spacing:2px;

    transition:.3s;

}


.links a:hover{

    color:var(--gold2);

}


.nav-button{

    text-decoration:none;

    color:#07100b;

    background:
    linear-gradient(
        135deg,
        var(--gold2),
        var(--gold)
    );

    padding:12px 22px;

    border-radius:40px;

    font-size:11px;

    font-weight:600;

    letter-spacing:1px;

    transition:.3s;

}


.nav-button:hover{

    transform:translateY(-2px);

    box-shadow:
    0 10px 30px
    rgba(201,162,77,.25);

}


.menu{

    display:none;

    background:none;

    border:1px solid var(--gold3);

    color:var(--gold2);

    width:43px;
    height:43px;

    border-radius:8px;

    font-size:20px;

}


/* =========================================================
   HERO
========================================================= */

.hero{

    height:100vh;

    min-height:720px;

    position:relative;

    display:flex;

    align-items:center;

    justify-content:center;

    text-align:center;

    overflow:hidden;

    background:

    linear-gradient(
        180deg,
        rgba(0,0,0,.15),
        rgba(0,0,0,.72)
    ),

    url("/cover");

    background-size:cover;

    background-position:center;

}


.hero::after{

    content:"";

    position:absolute;

    inset:0;

    background:
    radial-gradient(
        ellipse at center,
        transparent 20%,
        rgba(0,0,0,.7) 100%
    );

}


.hero-content{

    position:relative;

    z-index:2;

    max-width:1000px;

    padding:20px;

    animation:
    entrance 1.4s ease;

}


@keyframes entrance{

    from{
        opacity:0;
        transform:translateY(35px);
    }

    to{
        opacity:1;
        transform:translateY(0);
    }

}


.hero-logo{

    width:135px;
    height:135px;

    object-fit:contain;

    margin-bottom:25px;

    filter:
    drop-shadow(
        0 0 30px
        rgba(201,162,77,.45)
    );

}


.eyebrow{

    color:var(--gold2);

    font-size:10px;

    letter-spacing:7px;

    margin-bottom:20px;

}


.hero h1{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:
    clamp(80px,13vw,175px);

    font-weight:500;

    line-height:.75;

    letter-spacing:-4px;

    color:#f0d995;

    text-shadow:
    0 15px 50px
    rgba(0,0,0,.8);

}


.hero h2{

    margin-top:35px;

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:
    clamp(20px,3vw,34px);

    font-weight:400;

    letter-spacing:12px;

    color:white;

}


.hero-line{

    width:160px;

    height:1px;

    background:
    linear-gradient(
        90deg,
        transparent,
        var(--gold),
        transparent
    );

    margin:30px auto;

}


.hero p{

    max-width:650px;

    margin:auto;

    color:#ddd;

    font-size:14px;

    line-height:2;

}


.hero-buttons{

    display:flex;

    justify-content:center;

    gap:14px;

    flex-wrap:wrap;

    margin-top:32px;

}


.btn{

    display:inline-flex;

    align-items:center;

    justify-content:center;

    padding:15px 28px;

    min-width:185px;

    border-radius:50px;

    text-decoration:none;

    font-size:11px;

    font-weight:600;

    letter-spacing:1.5px;

    transition:.35s;

}


.gold-btn{

    color:#07100b;

    background:
    linear-gradient(
        135deg,
        #f0d995,
        #c9a24d
    );

}


.outline-btn{

    color:var(--gold2);

    border:
    1px solid var(--gold);

    background:
    rgba(0,0,0,.2);

}


.btn:hover{

    transform:translateY(-5px);

    box-shadow:
    0 15px 35px
    rgba(0,0,0,.4);

}


/* =========================================================
   SCROLL INDICATOR
========================================================= */

.scroll{

    position:absolute;

    bottom:30px;

    left:50%;

    transform:translateX(-50%);

    z-index:3;

    color:#aaa;

    font-size:9px;

    letter-spacing:4px;

}


.scroll::after{

    content:"";

    display:block;

    width:1px;

    height:45px;

    margin:12px auto 0;

    background:
    linear-gradient(
        var(--gold),
        transparent
    );

}


/* =========================================================
   GENERAL SECTIONS
========================================================= */

section{

    padding:120px 6%;

    position:relative;

}


.section-top{

    max-width:750px;

    margin:
    0 auto 65px;

    text-align:center;

}


.label{

    color:var(--gold);

    font-size:9px;

    letter-spacing:5px;

    text-transform:uppercase;

    margin-bottom:17px;

}


.section-top h2{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:
    clamp(45px,6vw,72px);

    font-weight:500;

    color:var(--gold2);

    line-height:.95;

}


.section-top p{

    color:var(--muted);

    font-size:13px;

    line-height:1.9;

    margin-top:18px;

}


/* =========================================================
   COLLECTION
========================================================= */

.collection{

    background:

    radial-gradient(
        circle at 10% 20%,
        rgba(201,162,77,.045),
        transparent 30%
    ),

    var(--black);

}


.collection-grid{

    max-width:1200px;

    margin:auto;

    display:grid;

    grid-template-columns:
    repeat(4,1fr);

    gap:18px;

}


.collection-card{

    min-height:390px;

    position:relative;

    overflow:hidden;

    padding:30px;

    display:flex;

    flex-direction:column;

    justify-content:flex-end;

    background:
    linear-gradient(
        150deg,
        #123b29,
        #06140d
    );

    border:
    1px solid rgba(201,162,77,.18);

    transition:.5s;

}


.collection-card::before{

    content:"";

    position:absolute;

    width:250px;
    height:250px;

    border-radius:50%;

    top:-100px;
    right:-100px;

    background:
    radial-gradient(
        circle,
        rgba(201,162,77,.14),
        transparent 70%
    );

    transition:.6s;

}


.collection-card:hover{

    transform:
    translateY(-12px);

    border-color:
    rgba(201,162,77,.65);

    box-shadow:
    0 30px 70px
    rgba(0,0,0,.5);

}


.collection-card:hover::before{

    transform:scale(1.5);

}


.card-number{

    position:absolute;

    top:22px;
    right:25px;

    font-family:
    "Cormorant Garamond",
    serif;

    color:
    rgba(231,202,123,.35);

    font-size:30px;

}


.card-icon{

    font-size:55px;

    margin-bottom:auto;

}


.collection-card h3{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:32px;

    font-weight:500;

    color:var(--gold2);

    position:relative;

}


.collection-card p{

    color:#9d9d96;

    font-size:12px;

    line-height:1.8;

    margin-top:9px;

    position:relative;

}


/* =========================================================
   DIVIDER
========================================================= */

.divider{

    width:100%;

    height:1px;

    background:
    linear-gradient(
        90deg,
        transparent,
        rgba(201,162,77,.3),
        transparent
    );

}


/* =========================================================
   BRAND STORY
========================================================= */

.story{

    background:
    linear-gradient(
        180deg,
        #06150e,
        #030805
    );

}


.story-grid{

    max-width:1150px;

    margin:auto;

    display:grid;

    grid-template-columns:
    1fr 1fr;

    gap:70px;

    align-items:center;

}


.story-image{

    height:600px;

    background:

    linear-gradient(
        rgba(0,0,0,.15),
        rgba(0,0,0,.55)
    ),

    url("/cover");

    background-size:cover;

    background-position:center;

    border:
    1px solid rgba(201,162,77,.3);

    position:relative;

}


.story-image::after{

    content:"";

    position:absolute;

    inset:18px;

    border:
    1px solid
    rgba(231,202,123,.3);

}


.story-text h2{

    font-family:
    "Cormorant Garamond",
    serif;

    color:var(--gold2);

    font-size:
    clamp(50px,6vw,76px);

    font-weight:500;

    line-height:.9;

}


.story-text p{

    color:#aaa;

    font-size:13px;

    line-height:2;

    margin-top:25px;

}


.signature{

    margin-top:35px;

    font-family:
    "Cormorant Garamond",
    serif;

    font-style:italic;

    font-size:32px;

    color:var(--gold);

}


/* =========================================================
   EXPERIENCE
========================================================= */

.experience{

    background:#030705;

}


.experience-grid{

    max-width:1050px;

    margin:auto;

    display:grid;

    grid-template-columns:
    repeat(4,1fr);

    border:
    1px solid rgba(201,162,77,.15);

}


.experience-card{

    padding:45px 25px;

    text-align:center;

    border-right:
    1px solid rgba(201,162,77,.15);

}


.experience-card:last-child{

    border-right:none;

}


.experience-icon{

    font-size:30px;

    margin-bottom:20px;

}


.experience-card h3{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:27px;

    color:var(--gold2);

}


.experience-card p{

    color:#777;

    font-size:11px;

    line-height:1.8;

    margin-top:10px;

}


/* =========================================================
   QUOTE
========================================================= */

.quote{

    padding:
    150px 20px;

    text-align:center;

    background:

    linear-gradient(
        rgba(2,5,3,.7),
        rgba(2,5,3,.85)
    ),

    url("/cover");

    background-size:cover;

    background-position:center;

}


.quote-mark{

    color:var(--gold);

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:80px;

    line-height:.5;

}


.quote h2{

    max-width:900px;

    margin:30px auto;

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:
    clamp(40px,6vw,70px);

    font-weight:400;

    color:#f1e7ca;

    line-height:1.05;

}


/* =========================================================
   REVIEWS
========================================================= */

.reviews{

    background:#07160f;

}


.review-grid{

    max-width:1100px;

    margin:auto;

    display:grid;

    grid-template-columns:
    repeat(3,1fr);

    gap:18px;

}


.review{

    padding:38px;

    border:
    1px solid rgba(201,162,77,.15);

    background:
    rgba(255,255,255,.015);

}


.stars{

    color:var(--gold);

    letter-spacing:3px;

    font-size:12px;

}


.review p{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:22px;

    line-height:1.45;

    font-style:italic;

    color:#d5d3ca;

    margin-top:20px;

}


.reviewer{

    margin-top:25px;

    font-size:10px;

    letter-spacing:2px;

    color:var(--gold);

}


/* =========================================================
   INSTAGRAM
========================================================= */

.instagram{

    text-align:center;

    background:#030604;

}


.instagram-name{

    display:block;

    margin-top:25px;

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:42px;

    color:var(--gold2);

    text-decoration:none;

    transition:.3s;

}


.instagram-name:hover{

    color:white;

}


/* =========================================================
   LOCATION
========================================================= */

.location{

    background:
    linear-gradient(
        180deg,
        #07170f,
        #020403
    );

}


.location-card{

    max-width:1000px;

    margin:auto;

    text-align:center;

    padding:65px 25px;

    border:
    1px solid rgba(201,162,77,.3);

    background:
    linear-gradient(
        145deg,
        #0d3020,
        #06130c
    );

}


.location-card h3{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:45px;

    color:var(--gold2);

}


.location-card p{

    color:#aaa;

    font-size:13px;

    line-height:2;

    margin:20px 0 30px;

}


/* =========================================================
   CTA
========================================================= */

.cta{

    text-align:center;

    padding:150px 20px;

    background:

    linear-gradient(
        rgba(1,5,3,.65),
        rgba(1,5,3,.9)
    ),

    url("/cover");

    background-size:cover;

    background-position:center;

}


.cta h2{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:
    clamp(55px,8vw,100px);

    color:var(--gold2);

    font-weight:500;

    line-height:.9;

}


/* =========================================================
   FOOTER
========================================================= */

footer{

    background:#010201;

    padding:70px 20px 30px;

    text-align:center;

    border-top:
    1px solid rgba(201,162,77,.15);

}


.footer-logo{

    width:65px;
    height:65px;

    object-fit:contain;

}


.footer-brand{

    font-family:
    "Cormorant Garamond",
    serif;

    font-size:32px;

    color:var(--gold2);

    margin-top:10px;

}


.footer-sub{

    color:#555;

    font-size:9px;

    letter-spacing:4px;

    margin-top:5px;

}


.footer-links{

    margin:30px 0;

}


.footer-links a{

    color:#777;

    text-decoration:none;

    margin:0 10px;

    font-size:10px;

}


.footer-links a:hover{

    color:var(--gold);

}


.copy{

    color:#444;

    font-size:9px;

    line-height:2;

}


/* =========================================================
   WHATSAPP
========================================================= */

.whatsapp{

    position:fixed;

    right:23px;
    bottom:23px;

    width:60px;
    height:60px;

    display:flex;

    align-items:center;
    justify-content:center;

    border-radius:50%;

    background:#25d366;

    color:white;

    text-decoration:none;

    font-size:27px;

    z-index:9990;

    box-shadow:
    0 10px 30px
    rgba(0,0,0,.5);

    transition:.3s;

}


.whatsapp:hover{

    transform:scale(1.12);

}


/* =========================================================
   REVEAL
========================================================= */

.reveal{

    opacity:0;

    transform:translateY(35px);

    transition:
    opacity .9s ease,
    transform .9s ease;

}


.reveal.active{

    opacity:1;

    transform:translateY(0);

}


/* =========================================================
   MOBILE
========================================================= */

@media(max-width:900px){

    .links,
    .nav-button{

        display:none;

    }


    .menu{

        display:block;

    }


    .collection-grid{

        grid-template-columns:
        repeat(2,1fr);

    }


    .story-grid{

        grid-template-columns:1fr;

    }


    .story-image{

        height:450px;

    }


    .experience-grid{

        grid-template-columns:
        repeat(2,1fr);

    }


    .experience-card:nth-child(2){

        border-right:none;

    }


    .experience-card:nth-child(1),
    .experience-card:nth-child(2){

        border-bottom:
        1px solid rgba(201,162,77,.15);

    }


    .review-grid{

        grid-template-columns:1fr;

    }

}


@media(max-width:600px){

    .nav{

        height:72px;

    }


    .brand-text{

        font-size:24px;

    }


    .hero{

        min-height:700px;

    }


    .hero-logo{

        width:105px;
        height:105px;

    }


    .hero h1{

        font-size:70px;

        letter-spacing:-2px;

    }


    .hero h2{

        font-size:17px;

        letter-spacing:6px;

    }


    .hero p{

        font-size:13px;

    }


    section{

        padding:85px 5%;

    }


    .collection-grid{

        grid-template-columns:1fr;

    }


    .collection-card{

        min-height:320px;

    }


    .story-image{

        height:360px;

    }


    .experience-grid{

        grid-template-columns:1fr;

    }


    .experience-card{

        border-right:none;

        border-bottom:
        1px solid rgba(201,162,77,.15);

    }


    .experience-card:last-child{

        border-bottom:none;

    }


    .location-card h3{

        font-size:34px;

    }


    .instagram-name{

        font-size:32px;

    }


    .btn{

        width:100%;

        max-width:310px;

    }

}

</style>

</head>


<body>


<div class="cursor-glow"
id="glow">
</div>


<!-- =========================================================
     NAVIGATION
========================================================= -->

<nav class="nav">

    <a href="#home"
    class="brand">

        <img src="/logo"
        alt="Al Rashid">

        <span class="brand-text">
            Al Rashid
        </span>

    </a>


    <ul class="links">

        <li>
            <a href="#home">HOME</a>
        </li>

        <li>
            <a href="#collection">COLLECTION</a>
        </li>

        <li>
            <a href="#story">OUR STORY</a>
        </li>

        <li>
            <a href="#reviews">REVIEWS</a>
        </li>

        <li>
            <a href="#location">VISIT</a>
        </li>

    </ul>


    <a
    href="https://wa.me/919620963982"
    target="_blank"
    class="nav-button">

        WHATSAPP

    </a>


    <button
    class="menu"
    onclick="openMenu()">

        ☰

    </button>

</nav>



<!-- =========================================================
     HERO
========================================================= -->

<header
class="hero"
id="home">


<div class="hero-content">


    <img
    src="/logo"
    class="hero-logo"
    alt="Al Rashid Logo">


    <div class="eyebrow">
        LUXURY FRAGRANCE HOUSE
    </div>


    <h1>
        Al Rashid
    </h1>


    <h2>
        PERFUME &amp; ATTAR
    </h2>


    <div class="hero-line">
    </div>


    <p>

        A world of refined fragrance,
        timeless attars and sophisticated
        style — created for those who
        leave an impression.

    </p>


    <div class="hero-buttons">


        <a
        href="#collection"
        class="btn gold-btn">

            DISCOVER COLLECTION

        </a>


        <a
        href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20explore%20your%20collection."
        target="_blank"
        class="btn outline-btn">

            CONTACT US

        </a>


    </div>


</div>


<div class="scroll">
    SCROLL
</div>


</header>



<div class="divider">
</div>



<!-- =========================================================
     COLLECTION
========================================================= -->

<section
class="collection"
id="collection">


<div class="section-top reveal">

    <div class="label">
        THE COLLECTION
    </div>

    <h2>
        Fragrance With Character
    </h2>

    <p>
        Discover carefully selected
        fragrances and timeless pieces
        designed to complement your
        personality.
    </p>

</div>


<div class="collection-grid">


    <div class="collection-card reveal">

        <div class="card-number">
            I
        </div>

        <div class="card-icon">
            🌹
        </div>

        <h3>
            Premium Perfumes
        </h3>

        <p>
            Elegant fragrance compositions
            for everyday confidence and
            unforgettable occasions.
        </p>

    </div>


    <div class="collection-card reveal">

        <div class="card-number">
            II
        </div>

        <div class="card-icon">
            🪔
        </div>

        <h3>
            Luxury Attars
        </h3>

        <p>
            Rich traditional fragrance
            with depth, warmth and
            distinctive character.
        </p>

    </div>


    <div class="collection-card reveal">

        <div class="card-number">
            III
        </div>

        <div class="card-icon">
            ⌚
        </div>

        <h3>
            Watches
        </h3>

        <p>
            Refined accessories designed
            to complete your personal style.
        </p>

    </div>


    <div class="collection-card reveal">

        <div class="card-number">
            IV
        </div>

        <div class="card-icon">
            ✦
        </div>

        <h3>
            New Arrivals
        </h3>

        <p>
            Explore the latest additions
            to our collection.
        </p>

    </div>


</div>


</section>



<!-- =========================================================
     STORY
========================================================= -->

<section
class="story"
id="story">


<div class="story-grid">


    <div class="story-image reveal">
    </div>


    <div class="story-text reveal">


        <div class="label">
            THE AL RASHID STORY
        </div>


        <h2>
            More Than
            <br>
            A Fragrance
        </h2>


        <p>

            Fragrance is personal.

            It becomes part of your
            presence, your memories
            and the impression you
            leave behind.

        </p>


        <p>

            At <strong style="color:#e7ca7b;">
            Al Rashid
            </strong>,
            we bring together premium
            perfumes, traditional attars
            and elegant accessories for
            those who appreciate
            individuality and style.

        </p>


        <div class="signature">
            Al Rashid
        </div>


    </div>


</div>


</section>



<!-- =========================================================
     EXPERIENCE
========================================================= -->

<section
class="experience">


<div class="section-top reveal">

    <div class="label">
        THE EXPERIENCE
    </div>

    <h2>
        Why Al Rashid?
    </h2>

</div>


<div class="experience-grid">


    <div class="experience-card reveal">

        <div class="experience-icon">
            ◆
        </div>

        <h3>
            Premium
        </h3>

        <p>
            Carefully selected products
            with a focus on quality.
        </p>

    </div>


    <div class="experience-card reveal">

        <div class="experience-icon">
            ✦
        </div>

        <h3>
            Distinctive
        </h3>

        <p>
            Fragrances with personality
            and character.
        </p>

    </div>


    <div class="experience-card reveal">

        <div class="experience-icon">
            ♢
        </div>

        <h3>
            Elegant
        </h3>

        <p>
            Timeless style for every
            occasion.
        </p>

    </div>


    <div class="experience-card reveal">

        <div class="experience-icon">
            ♡
        </div>

        <h3>
            Personal
        </h3>

        <p>
            A customer experience
            that truly matters.
        </p>

    </div>


</div>


</section>



<!-- =========================================================
     QUOTE
========================================================= -->

<section class="quote">


<div class="reveal">

    <div class="quote-mark">
        “
    </div>

    <h2>
        Your fragrance introduces you
        before you even say a word.
    </h2>

    <div class="quote-mark">
        ”
    </div>

</div>


</section>



<!-- =========================================================
     REVIEWS
========================================================= -->

<section
class="reviews"
id="reviews">


<div class="section-top reveal">

    <div class="label">
        CUSTOMER EXPERIENCE
    </div>

    <h2>
        Loved By Customers
    </h2>

    <p>
        A fragrance should be remembered.
    </p>

</div>


<div class="review-grid">


    <div class="review reveal">

        <div class="stars">
            ★★★★★
        </div>

        <p>
            “Beautiful fragrance and
            excellent quality. The scent
            feels premium and elegant.”
        </p>

        <div class="reviewer">
            CUSTOMER
        </div>

    </div>


    <div class="review reveal">

        <div class="stars">
            ★★★★★
        </div>

        <p>
            “Loved the perfume collection.
            Very good options and
            friendly service.”
        </p>

        <div class="reviewer">
            CUSTOMER
        </div>

    </div>


    <div class="review reveal">

        <div class="stars">
            ★★★★★
        </div>

        <p>
            “The fragrance quality is
            impressive. Definitely worth
            visiting.”
        </p>

        <div class="reviewer">
            CUSTOMER
        </div>

    </div>


</div>


</section>



<!-- =========================================================
     INSTAGRAM
========================================================= -->

<section class="instagram">


<div class="section-top reveal">

    <div class="label">
        FOLLOW THE JOURNEY
    </div>

    <h2>
        Al Rashid Online
    </h2>

    <p>
        Discover new fragrances,
        arrivals and updates.
    </p>


    <a
    href="https://www.instagram.com/alrashid.luxury/"
    target="_blank"
    class="instagram-name">

        @alrashid.luxury

    </a>

</div>


<a
href="https://www.instagram.com/alrashid.luxury/"
target="_blank"
class="btn outline-btn">

    FOLLOW INSTAGRAM

</a>


</section>



<!-- =========================================================
     LOCATION
========================================================= -->

<section
class="location"
id="location">


<div class="section-top reveal">

    <div class="label">
        VISIT US
    </div>

    <h2>
        Find Al Rashid
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
        class="btn gold-btn">

            OPEN GOOGLE MAPS

        </a>


        <a
        href="https://wa.me/919620963982"
        target="_blank"
        class="btn outline-btn">

            WHATSAPP

        </a>


    </div>


</div>


</section>



<!-- =========================================================
     FINAL CTA
========================================================= -->

<section class="cta">


<div class="reveal">


    <div class="label">
        YOUR SIGNATURE AWAITS
    </div>


    <h2>
        Find Your
        <br>
        Signature Scent
    </h2>


    <div class="hero-buttons">


        <a
        href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20know%20about%20your%20perfumes."
        target="_blank"
        class="btn gold-btn">

            CHAT ON WHATSAPP

        </a>


        <a
        href="#collection"
        class="btn outline-btn">

            EXPLORE COLLECTION

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
class="footer-logo"
alt="Al Rashid Logo">


<div class="footer-brand">
    Al Rashid
</div>


<div class="footer-sub">
    PERFUME &amp; ATTAR
</div>


<div class="footer-links">

    <a href="#home">
        HOME
    </a>

    <a href="#collection">
        COLLECTION
    </a>

    <a href="#story">
        OUR STORY
    </a>

    <a href="#reviews">
        REVIEWS
    </a>

    <a href="#location">
        VISIT
    </a>

</div>


<div class="copy">

    © 2026 Al Rashid Perfume &amp; Attar.
    All Rights Reserved.

    <br>

    MG Road, Kolar, Karnataka
    •
    +91 96209 63982

</div>


</footer>



<!-- =========================================================
     WHATSAPP
========================================================= -->

<a
href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20know%20about%20your%20collection."
target="_blank"
class="whatsapp">

    ☎

</a>



<script>

/* =========================================================
   SCROLL REVEAL
========================================================= */

const observer =
new IntersectionObserver(

    entries => {

        entries.forEach(
            entry => {

                if(entry.isIntersecting){

                    entry.target
                    .classList
                    .add("active");

                }

            }
        );

    },

    {
        threshold:.12
    }

);


document
.querySelectorAll(".reveal")
.forEach(el => {

    observer.observe(el);

});



/* =========================================================
   CURSOR GOLD GLOW
========================================================= */

const glow =
document.getElementById("glow");


document.addEventListener(
    "mousemove",
    e => {

        glow.style.left =
        e.clientX + "px";

        glow.style.top =
        e.clientY + "px";

    }
);



/* =========================================================
   MOBILE MENU
========================================================= */

function openMenu(){

    const nav =
    document.querySelector(".links");

    if(
        nav.style.display === "flex"
    ){

        nav.style.display = "";

    }else{

        nav.style.display = "flex";

        nav.style.position = "fixed";

        nav.style.top = "72px";

        nav.style.left = "0";

        nav.style.width = "100%";

        nav.style.flexDirection = "column";

        nav.style.padding = "25px";

        nav.style.background =
        "rgba(3,5,4,.98)";

        nav.style.textAlign = "center";

    }

}

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