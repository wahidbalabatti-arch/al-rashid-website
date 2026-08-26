from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Al Rashid | Perfume & Attar</title>

    <style>
        body {
            margin: 0;
            font-family: Georgia, serif;
            background: #061b12;
            color: #f5e7b2;
            text-align: center;
        }

        header {
            min-height: 90vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(
                rgba(3,20,13,.85),
                rgba(3,20,13,.95)
            );
        }

        .logo {
            font-size: 70px;
            color: #d9ad45;
        }

        h1 {
            font-size: 80px;
            color: #e3bd61;
            margin: 10px;
        }

        .subtitle {
            font-size: 25px;
            letter-spacing: 5px;
            color: white;
        }

        .tagline {
            font-size: 22px;
            margin: 30px;
        }

        a.button {
            display: inline-block;
            padding: 15px 30px;
            margin: 10px;
            background: #d9ad45;
            color: #061b12;
            text-decoration: none;
            border-radius: 30px;
            font-weight: bold;
        }

        section {
            padding: 70px 20px;
        }

        h2 {
            color: #e3bd61;
            font-size: 40px;
        }

        .products {
            display: grid;
            grid-template-columns:
                repeat(auto-fit, minmax(220px, 1fr));
            gap: 25px;
            max-width: 1100px;
            margin: auto;
        }

        .card {
            background: #0b291c;
            border: 1px solid #8d6b27;
            border-radius: 15px;
            padding: 30px;
        }

        .card h3 {
            color: #e3bd61;
        }

        .card p {
            color: #ddd;
            line-height: 1.6;
        }

        footer {
            padding: 30px;
            border-top: 1px solid #604b21;
            color: #aaa;
        }

        .gold {
            color: #d9ad45;
        }

        @media(max-width:600px) {
            h1 {
                font-size: 50px;
            }

            .subtitle {
                font-size: 16px;
            }
        }
    </style>
</head>

<body>

<header>
    <div>

        <div class="logo">AR</div>

        <h1>Al Rashid</h1>

        <div class="subtitle">
            PERFUME & ATTAR
        </div>

        <p class="tagline">
            Premium Fragrances • Timeless Impression
        </p>

        <a class="button" href="#collection">
            Explore Collection
        </a>

        <a class="button"
           href="https://www.instagram.com/alrashid.luxury/"
           target="_blank">
            Instagram
        </a>

    </div>
</header>


<section id="collection">

    <h2>Our Collection</h2>

    <div class="products">

        <div class="card">
            <h3>🌹 Premium Perfumes</h3>
            <p>
                Elegant fragrances for everyday wear
                and special occasions.
            </p>
        </div>

        <div class="card">
            <h3>🪔 Attars</h3>
            <p>
                Traditional and modern attars with
                rich, long-lasting fragrances.
            </p>
        </div>

        <div class="card">
            <h3>⌚ Watches</h3>
            <p>
                Stylish watches for every occasion.
            </p>
        </div>

        <div class="card">
            <h3>✨ New Arrivals</h3>
            <p>
                Explore our latest fragrances and
                exclusive collections.
            </p>
        </div>

    </div>

</section>


<section>

    <h2>Why Al Rashid?</h2>

    <div class="products">

        <div class="card">
            <h3>Premium Quality</h3>
            <p>Carefully selected fragrances.</p>
        </div>

        <div class="card">
            <h3>Long Lasting</h3>
            <p>Fragrances that stay with you all day.</p>
        </div>

        <div class="card">
            <h3>Best Prices</h3>
            <p>Premium fragrances at affordable prices.</p>
        </div>

        <div class="card">
            <h3>Happy Customers</h3>
            <p>Your trust motivates us to do better.</p>
        </div>

    </div>

</section>


<section>

    <h2>Visit Our Store</h2>

    <p>
        <strong class="gold">
            Al Rashid Perfume & Attar
        </strong>
    </p>

    <p>
        MG Road, Kolar, Karnataka
        <br>
        Next to Parvath Sports
    </p>

    <br>

    <a class="button"
       href="https://www.google.com/maps/search/?api=1&query=Al+Rasheed+Perfume+Attar+Kolar"
       target="_blank">
        📍 Google Maps
    </a>

</section>


<section>

    <h2>Follow Us</h2>

    <p>
        Instagram:
        <a
           href="https://www.instagram.com/alrashid.luxury/"
           target="_blank"
           class="gold">
           @alrashid.luxury
        </a>
    </p>

</section>


<footer>

    © 2026
    <span class="gold">
        Al Rashid Perfume & Attar
    </span>

    <br><br>

    Premium Fragrances • Attars • Watches

</footer>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)