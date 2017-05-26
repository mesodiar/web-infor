#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import html

content = """
<body style="background-color:white;" padding-top: 51px;>
  <div style="background-image: url(../images/bread.jpg); min-height:400px; background-position:center">
    <ul>
      <li><a href="index.py" style="float: left">Home</a></li>
      <li><a href="reviews.py">Reviews</a></li>
      <li><a href="news.py">News</a></li>
      <li><a href="about.py">About</a></li>
    </ul>
    <h1 style="color:white">Content 2</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-9 article-left-aside">
        <h3>How to eat at NYC’s best restaurants for under $50</h3>
        <img src="../images/under50.jpg" class="displayed">
        <p>Are you a cash-strapped foodie who’s dying to eat at one of New York’s best restaurants? We got you covered—and for $50 or less. Even the most celebrated restaurants sometimes let you snag the best dishes at affordable prices if you know when to go. So whether you’re in the mood for amazing French restaurants, or fantastic Italian restaurants, plan ahead and take advantage of these lunch deals, bar menus and pre-theater specials.
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
           <a href="content_3.py">
            <img src="../images/blue.jpg" style="float: left;">
            <p>The best New York delis</p>
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