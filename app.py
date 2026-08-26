from flask import Flask, render_template_string

app = Flask(__name__)

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
          content="Al Rashid, perfume, attar, perfumes in Kolar, premium perfume, watches, Kolar">

    <title>Al Rashid | Perfume & Attar</title>


    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }


        body {
            font-family: Georgia, "Times New Roman", serif;
            background: #03140d;
            color: #f5e7b2;
            overflow-x: hidden;
        }


        /* ================= NAVBAR ================= */

        nav {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 999;

            display: flex;
            justify-content: space-between;
            align-items: center;

            padding: 15px 6%;

            background: rgba(3, 20, 13, 0.92);
            backdrop-filter: blur(12px);

            border-bottom: 1px solid rgba(217,173,69,.4);
        }


        .nav-logo {
            display: flex;
            align-items: center;
            gap: 12px;

            font-size: 22px;
            font-weight: bold;
            color: #d9ad45;
        }


        .nav-logo img {
            width: 45px;
            height: 45px;
            object-fit: contain;
            border-radius: 50%;
        }


        nav ul {
            display: flex;
            gap: 28px;
            list-style: none;
        }


        nav a {
            text-decoration: none;
            color: #eee;
            transition: .3s;
        }


        nav a:hover {
            color: #d9ad45;
        }


        .nav-whatsapp {
            padding: 10px 18px;
            border-radius: 25px;
            background: #d9ad45;
            color: #061b12 !important;
            font-weight: bold;
        }


        /* ================= HERO ================= */

        .hero {

            min-height: 100vh;

            display: flex;
            align-items: center;
            justify-content: center;

            text-align: center;

            padding: 100px 20px 60px;

            background:
                linear-gradient(
                    rgba(2,16,10,.68),
                    rgba(2,16,10,.88)
                ),
                url("/static/COVER_PAGE.jpeg");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }


        .hero-content {
            max-width: 1000px;
        }


        .hero-logo {
            width: 130px;
            height: 130px;
            object-fit: contain;
            margin-bottom: 20px;

            filter:
                drop-shadow(0 0 20px rgba(217,173,69,.5));
        }


        .hero h1 {
            font-size: clamp(55px, 9vw, 110px);
            color: #e5bd5c;
            letter-spacing: 3px;

            text-shadow:
                0 5px 30px rgba(0,0,0,.8);
        }


        .hero h2 {
            font-size: clamp(20px, 3vw, 32px);
            letter-spacing: 8px;
            color: white;
            margin-top: 10px;
        }


        .hero p {
            margin: 30px auto;
            max-width: 700px;

            font-size: 21px;
            line-height: 1.7;
            color: #eee;
        }


        .gold-line {
            width: 180px;
            height: 2px;
            background: #d9ad45;
            margin: 25px auto;
        }


        .buttons {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
        }


        .button {
            display: inline-block;

            padding: 15px 30px;

            border-radius: 35px;

            text-decoration: none;

            font-weight: bold;

            transition: .3s;
        }


        .button-gold {
            background: #d9ad45;
            color: #061b12;
        }


        .button-outline {
            border: 1px solid #d9ad45;
            color: #d9ad45;
        }


        .button:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 30px rgba(217,173,69,.25);
        }


        /* ================= SECTIONS ================= */

        section {
            padding: 100px 6%;
        }


        .section-title {
            text-align: center;
            margin-bottom: 55px;
        }


        .section-title h2 {
            font-size: clamp(35px, 5vw, 55px);
            color: #e3bd61;
        }


        .section-title p {
            margin-top: 15px;
            color: #aaa;
            font-family: Arial, sans-serif;
        }


        /* ================= COLLECTION ================= */

        .cards {
            max-width: 1200px;
            margin: auto;

            display: grid;

            grid-template-columns:
                repeat(auto-fit, minmax(240px, 1fr));

            gap: 25px;
        }


        .card {
            padding: 40px 25px;

            text-align: center;

            background:
                linear-gradient(
                    145deg,
                    #0c2d1d,
                    #061b12
                );

            border: 1px solid #705621;

            border-radius: 18px;

            transition: .4s;
        }


        .card:hover {
            transform: translateY(-10px);

            border-color: #d9ad45;

            box-shadow:
                0 20px 50px rgba(0,0,0,.4);
        }


        .card-icon {
            font-size: 50px;
            margin-bottom: 20px;
        }


        .card h3 {
            color: #e3bd61;
            font-size: 26px;
            margin-bottom: 15px;
        }


        .card p {
            color: #ccc;
            line-height: 1.7;
            font-family: Arial, sans-serif;
        }


        /* ================= WHY US ================= */

        .features {
            max-width: 1100px;
            margin: auto;

            display: grid;

            grid-template-columns:
                repeat(auto-fit, minmax(200px, 1fr));

            gap: 20px;
        }


        .feature {
            text-align: center;
            padding: 30px 15px;
        }


        .feature-icon {
            font-size: 42px;
            margin-bottom: 15px;
        }


        .feature h3 {
            color: #d9ad45;
            margin-bottom: 10px;
        }


        .feature p {
            color: #aaa;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }


        /* ================= ABOUT ================= */

        .about {
            max-width: 1000px;
            margin: auto;

            text-align: center;

            background: #092219;

            border: 1px solid #604b21;

            border-radius: 25px;

            padding: 50px 30px;
        }


        .about p {
            color: #ddd;

            font-family: Arial, sans-serif;

            line-height: 1.9;

            font-size: 18px;
        }


        /* ================= LOCATION ================= */

        .location-box {
            max-width: 900px;
            margin: auto;

            text-align: center;

            padding: 50px 25px;

            border-radius: 25px;

            background:
                linear-gradient(
                    145deg,
                    #0b291c,
                    #061b12
                );

            border: 1px solid #705621;
        }


        .location-box h3 {
            color: #e3bd61;
            font-size: 30px;
            margin-bottom: 20px;
        }


        .location-box p {
            color: #ddd;
            font-family: Arial, sans-serif;
            line-height: 1.8;
        }


        /* ================= SOCIAL ================= */

        .social {
            text-align: center;
        }


        .instagram {
            color: #e3bd61;
            font-size: 26px;
            text-decoration: none;
        }


        .instagram:hover {
            text-decoration: underline;
        }


        /* ================= FOOTER ================= */

        footer {
            padding: 45px 20px;

            text-align: center;

            background: #020d08;

            border-top: 1px solid #604b21;

            color: #999;

            font-family: Arial, sans-serif;
        }


        footer strong {
            color: #d9ad45;
        }


        /* ================= MOBILE ================= */

        @media(max-width: 800px) {

            nav ul {
                display: none;
            }

            .hero {
                background-attachment: scroll;
            }

            .hero h1 {
                letter-spacing: 1px;
            }

            section {
                padding: 70px 5%;
            }

        }


    </style>

</head>


<body>


<!-- ================= NAVIGATION ================= -->

<nav>

    <div class="nav-logo">

        <img src="/static/LOGO.JPEG"
             alt="Al Rashid Logo">

        Al Rashid

    </div>


    <ul>

        <li>
            <a href="#home">Home</a>
        </li>

        <li>
            <a href="#collection">Collection</a>
        </li>

        <li>
            <a href="#about">About</a>
        </li>

        <li>
            <a href="#location">Location</a>
        </li>

        <li>
            <a href="#contact">Contact</a>
        </li>

    </ul>


    <a class="nav-whatsapp"
       href="https://wa.me/919620963982"
       target="_blank">

        WhatsApp

    </a>

</nav>



<!-- ================= HERO ================= -->

<header class="hero" id="home">

    <div class="hero-content">

        <img class="hero-logo"
             src="/static/LOGO.JPEG"
             alt="Al Rashid">

        <h1>Al Rashid</h1>

        <h2>PERFUME & ATTAR</h2>

        <div class="gold-line"></div>

        <p>
            Discover premium fragrances, elegant attars
            and stylish watches crafted for every occasion.
        </p>


        <div class="buttons">

            <a class="button button-gold"
               href="#collection">

                Explore Collection

            </a>


            <a class="button button-outline"
               href="https://wa.me/919620963982?text=Hello%20Al%20Rashid%2C%20I%20would%20like%20to%20know%20about%20your%20perfumes."

               target="_blank">

                Order on WhatsApp

            </a>

        </div>

    </div>

</header>



<!-- ================= COLLECTION ================= -->

<section id="collection">

    <div class="section-title">

        <h2>Our Collection</h2>

        <p>
            Find a fragrance that matches your personality.
        </p>

    </div>


    <div class="cards">


        <div class="card">

            <div class="card-icon">🌹</div>

            <h3>Premium Perfumes</h3>

            <p>
                Elegant and sophisticated fragrances
                for everyday wear and special occasions.
            </p>

        </div>


        <div class="card">

            <div class="card-icon">🪔</div>

            <h3>Attars</h3>

            <p>
                Traditional and modern attars with
                rich and distinctive fragrance profiles.
            </p>

        </div>


        <div class="card">

            <div class="card-icon">⌚</div>

            <h3>Watches</h3>

            <p>
                Stylish watches designed to complement
                your everyday appearance.
            </p>

        </div>


        <div class="card">

            <div class="card-icon">✨</div>

            <h3>New Arrivals</h3>

            <p>
                Discover our latest fragrances and
                new additions to the collection.
            </p>

        </div>


    </div>

</section>



<!-- ================= WHY US ================= -->

<section>

    <div class="section-title">

        <h2>Why Choose Al Rashid?</h2>

        <p>
            Quality, fragrance and service.
        </p>

    </div>


    <div class="features">


        <div class="feature">

            <div class="feature-icon">💎</div>

            <h3>Premium Quality</h3>

            <p>
                Carefully selected fragrances.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">⏳</div>

            <h3>Long Lasting</h3>

            <p>
                Fragrances made to stay with you.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">💰</div>

            <h3>Great Prices</h3>

            <p>
                Premium choices at attractive prices.
            </p>

        </div>


        <div class="feature">

            <div class="feature-icon">❤️</div>

            <h3>Customer First</h3>

            <p>
                Your satisfaction matters to us.
            </p>

        </div>


    </div>

</section>



<!-- ================= ABOUT ================= -->

<section id="about">

    <div class="section-title">

        <h2>About Al Rashid</h2>

    </div>


    <div class="about">

        <p>

            Welcome to <strong style="color:#d9ad45;">
            Al Rashid Perfume & Attar
            </strong>.

            We offer a collection of premium perfumes,
            traditional attars and stylish watches.

            Whether you are searching for a signature
            fragrance, a special gift or something for
            everyday use, our collection is designed to
            give you a memorable fragrance experience.

        </p>

    </div>

</section>



<!-- ================= LOCATION ================= -->

<section id="location">

    <div class="section-title">

        <h2>Visit Our Store</h2>

    </div>


    <div class="location-box">

        <h3>Al Rashid Perfume & Attar</h3>

        <p>

            📍 MG Road, Kolar, Karnataka

            <br>

            Next to Parvath Sports

            <br><br>

            📞 +91 96209 63982

        </p>


        <br>


        <div class="buttons">

            <a class="button button-gold"

               href="https://www.google.com/maps/search/?api=1&query=Al+Rashid+Perfume+Attar+MG+Road+Kolar"

               target="_blank">

                Open Google Maps

            </a>


            <a class="button button-outline"

               href="https://wa.me/919620963982"

               target="_blank">

                WhatsApp Us

            </a>

        </div>

    </div>

</section>



<!-- ================= INSTAGRAM ================= -->

<section id="contact">

    <div class="social">

        <div class="section-title">

            <h2>Follow Al Rashid</h2>

            <p>
                Follow us for new arrivals and updates.
            </p>

        </div>


        <a class="instagram"

           href="https://www.instagram.com/alrashid.luxury/"

           target="_blank">

            📸 @alrashid.luxury

        </a>

        <br><br>


        <a class="button button-gold"

           href="https://wa.me/919620963982"

           target="_blank">

            💬 Chat on WhatsApp

        </a>

    </div>

</section>



<!-- ================= FOOTER ================= -->

<footer>

    <strong>Al Rashid Perfume & Attar</strong>

    <br><br>

    Premium Perfumes • Attars • Watches

    <br><br>

    MG Road, Kolar, Karnataka

    <br><br>

    © 2026 Al Rashid. All Rights Reserved.

</footer>


</body>

</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(
        debug=False,
        use_reloader=False
    )
