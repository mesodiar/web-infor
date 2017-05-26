#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import html

content = """
<body style="background-color:white;">
  <div style="background-image: url(../images/burger.jpg); min-height:400px; background-position:center">
    <ul>
      <li><a href="index.py" style="float: left">Home</a></li>
      <li><a href="reviews.py">Reviews</a></li>
      <li><a href="news.py">News</a></li>
      <li><a href="about.py">About</a></li>
    </ul>
    <h1 class="font-effect-anaglyph">News</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-4 article">
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

      <div class="col-4 article">
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

      <div class="col-4 article">
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