#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import html

content = """
<body style="background-color:white;">
  <div style="background-image: url(../images/reviews.jpg); min-height:400px; background-position:center">
    <ul>
      <li><a href="index.py" style="float: left">Home</a></li>
      <li><a href="reviews.py">Reviews</a></li>
      <li><a href="news.py">News</a></li>
      <li><a href="about.py">About</a></li>
    </ul>
    <h1 class="font-effect-anaglyph">Reviews</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-4 article">
        <a href="content_4.py">
          <h3>Union Square Cafe</h3>
          <img src="../images/union-1.jpg">
          <p>One of New York’s most cherished restaurants, makes its comeback</p>
          <p>
            Reboots are risky business—for every The Force Awakens, there’s a The Phantom Menace. Remakers have the punishing task of satisfying two audiences simultaneously
          </p>
        </a>
      </div>

      <div class="col-4 article">
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

      <div class="col-4 article">
        <a href="content_6.py">
          <h3>White Gold Butchers</h3>
          <img src="../images/butcher.jpg">
          <p>
            There’s no burger. At first, it seems sacrilege, given the ownership of the place. But then you take a big, sloppy bite of the kitchen’s chopped cheese sandwich—that meaty cross between a beef burger and a Philly cheesesteak, regularly found on bodega flattops in Harlem and the Bronx—and you realize, Oh yes, this is indeed an April Bloomfield restaurant.
          </p>
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