#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import html

content = """<body style="background-color:white;" padding-top: 51px;>

<div style="background-image: url(../images/pizza.jpg); min-height:400px; background-position:center">
<ul>
<li><a href="index.py" style="float: left">Home</a></li>
<li><a href="reviews.py">Reviews</a></li>
<li><a href="news.py">News</a></li>
<li><a href="about.py">About</a></li>
</ul>
<h1 class="font-effect-anaglyph">FOODSTRAY</h1>
<h2 style="color:white">For every restaurant you love</h2>
</div>
<div class="container">
<div class="row">
<p><button class="button" style="vertical-align:middle" onclick="newSubscribe()"><span>Subscribe </span></button></p>
<p id="demo"></p>
</div>
<div class="row">
<div class="col-4 article" onmouseover="style.color='#e24a0d'" onmouseout="style.color='black'">
    <a href="content_4.py">
    <h3>Union Square Cafe</h3>
    <img src="../images/union-1.jpg">
    <p>One of New Yorks most cherished restaurants, makes its comeback</p>
    <p>
        Reboots are risky businessfor every The Force Awakens theres a The Phantom Menace. Remakers have the punishing task of satisfying two audiences simultaneously
    </p>
    </a>
</div>

<div class="col-4 article" onmouseover="style.color='#e24a0d'" onmouseout="style.color='black'">
    <a href="content_5.py">
    <h3>Massoni</h3>
    <img src="../images/massoni.jpg">
    <p>
        Dale Talde serves tartare cannoli and Detroit pizza at his "Italianish" newcomer Massoni
    </p>
    <p>
        “Italianish.” It’s a word thrown around with great frequency at Massoni, the graffiti-tagged new arrival at the Arlo NoMad hotel from celebrity chef Dale Talde and his Three Kings Restaurant Group.
    </p>
    </a>
</div>

<div class="col-4 article" onmouseover="style.color='#e24a0d'" onmouseout="style.color='black'">
    <a href="content_6.py">
    <h3>White Gold Butchers</h3>
    <img src="../images/butcher.jpg">
    <p>
        There’s no burger. At first, it seems sacrilege, given the ownership of the place. But then you take a big, sloppy bite of the kitchen’s chopped cheese sandwich—that meaty cross between a beef burger and a Philly cheesesteak, regularly found on bodega flattops in Harlem and the Bronx—and you realize, Oh yes, this is indeed an April Bloomfield restaurant.
    </p>
    </a>
</div>
</div>
<div class="row">
<p class="subheader">
    "The murals in restaurants are on par <br>with the food in museums."</p>
<p class="subheader" style="color:#B2BABB">- Peter De Vries</p>
<div class="parallax"></div>
<p class="subheader2">
    Your ultimate guide to restaurants </p>
    <div class="slideshow-container">
    <div class="mySlides fade">
        <div class="numbertext">1 / 3</div>
        <img src="../images/butcher.jpg" style="width:100%">
    </div>

    <div class="mySlides fade">
        <div class="numbertext">2 / 3</div>
        <img src="../images/under50.jpg" style="width:100%">
    </div>

    <div class="mySlides fade">
        <div class="numbertext">3 / 3</div>
        <img src="../images/union-1.jpg" style="width:100%">
    </div>

    <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
    <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<p class="subheader2" onmouseover="style.color='#0ce2c2'" onmouseout="style.color='#B2BABB'">The best restaurants and eateries in the city,<br>
    from casual to fine dining
</p>
</div>
<div class="row">
<div class="col-4 article" onmouseover="style.color='#e24a0d'" onmouseout="style.color='black'">
    <a href="content_1.py">
    <h3>The best restaurants near the High Line</h3>
    <img src="../images/hamburger.jpg">
    <p>It’s inevitable you’re going to walk through Chelsea’s elevated
        green space at some point during spring in New York, so sustain
        your meandering, 20-block trek along the tracks with a pit stop at one
        of the best restaurants near the High Line.
    </p>
    </a>
</div>

<div class="col-4 article" onmouseover="style.color='#e24a0d'" onmouseout="style.color='black'">
    <a href="content_2.py">
    <h3>How to eat at NYC’s best restaurants for under $50</h3>
    <img src="../images/under50.jpg">
    <p>Are you a cash-strapped foodie who’s dying to eat at one
        of New York’s best restaurants? We got you covered—and for $50
        or less. Even the most celebrated restaurants sometimes let you
        snag the best dishes at affordable prices if you know when to go.
    </p>
    </a>
</div>

<div class="col-4 article" onmouseover="style.color='#e24a0d'" onmouseout="style.color='black'">
    <a href="content_3.py">
    <h3>The best New York delis</h3>
    <img src="../images/blue.jpg">
    <p>There are few things more synonymous with the city
        than the New York deli, and Gotham is rife with top-notch
        takes on the classic form. Whether you’re got a hankering
        for heaping pastrami sandwiches, want to compare and contrast
        the best bagels in NYC, or are looking for the best kosher
        restaurants .</p>
    </a>
</div>
</div>
</div>
<footer>
<a href="#"><i class="fa fa-facebook-official" style="font-size:36px;color:white"></i></a>
<a href="#"><i class="fa fa-pinterest-p" style="font-size:36px;color:white"></i></a>
<a href="#"><i class="fa fa-twitter" style="font-size:36px;color:white"></i></a>
<a href="#"><i class="fa fa-flickr" style="font-size:36px;color:white"></i></a>
<a href="#"><i class="fa fa-linkedin" style="font-size:36px;color:white"></i></a>
</footer>
<script src="../myscripts.js"></script>
</body>
"""
print("""Content-type:text/html\n\n
        <!DOCTYPE html>
        <html lang="en">
            <head>
                <meta chardet="utf-8"/>
                <link rel="stylesheet" type = "text/css" href = "../myStyle.css" />
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <link rel="stylesheet" type="text/css" href="http://fonts.googleapis.com/css?family=Merriweather:bold,bolditalic,blackitalic|Roboto+Slab|Dancing+Script|Rancho&effect=anaglyph|shadow-multiple">
                <title> My server-side template </title>
            </head>
            """)

print(content)