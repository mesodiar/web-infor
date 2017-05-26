#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import html

content = """
<body style="background-color:white;" padding-top: 51px;>
  <div style="background-image: url(../images/nuts.jpg); min-height:400px; background-position:center">
    <ul>
      <li><a href="index.py" style="float: left">Home</a></li>
      <li><a href="reviews.py">Reviews</a></li>
      <li><a href="news.py">News</a></li>
      <li><a href="about.py">About</a></li>
    </ul>
    <h1 style="color:white">Content 3</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-9 article-left-aside">
        <h3>The best New York delis</h3>
        <img src="../images/blue.jpg" class="displayed">
        <p>
            There are few things more synonymous with the city than the New York deli, and Gotham is rife with top-notch takes on the classic form. Whether you’re got a hankering for heaping pastrami sandwiches, want to compare and contrast the best bagels in NYC, or are looking for the best kosher restaurants to take your observing pal to, there’s a New York deli for you. Take a bite out of our roundup of NYC’s best delicatessens.
        </p>
        <p>Narrowing down the 100 best restaurants in New York City is no easy feat, given the sheer number of top-rate eateries NYC has to offer, from long-time favorites to the buzzy upstarts joining the fray week in and week out. But we put in the grunt work, detailing the city’s best Italian restaurants, best sushi, best Mexican spots and more. Here’s the best of the best: The 100 best restaurants that Time Out New York’s food editor—and New York itself—can’t live without.
        </p>
         <h3 style="color:#2e70db;"> Do you like this content? &nbsp
          <i onclick="thumbUpanddown(this)" class="thumb fa fa-thumbs-up" style="font-size:40px"></i>
        </h3>
      </div>
      <div class="col-3">
        <div class="article-right-aside">
            <a href="content_1.py">
            <img src="../images/hamburger.jpg" style="float: left;">
            <p>The best restaurants near the High Line</p>
            </a>
        </div>
        <div class="article-right-aside">
            <a href="content_2.py">
                <img src="../images/under50.jpg" style="float: left;">
                <p>How to eat at NYC’s best restaurants for under $50</p>
            </a>
        </div>
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