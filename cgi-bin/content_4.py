#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import html

content = """
<body style="background-color:white;" padding-top: 51px;>
  <div style="background-image: url(../images/wine.jpg); min-height:400px; background-position:center">
    <ul>
      <li><a href="index.py" style="float: left">Home</a></li>
      <li><a href="reviews.py">Reviews</a></li>
      <li><a href="news.py">News</a></li>
      <li><a href="about.py">About</a></li>
    </ul>
    <h1 style="color:white">Review 1</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-9 article-left-aside">
        <h3>Union Square Cafe</h3>
        <img class="displayed" src="../images/union-1.jpg">
        <p>Reboots are risky business—for every The Force Awakens, there’s a The Phantom Menace. Remakers have the punishing task of satisfying two audiences simultaneously: the established fan base, those who experienced the original run, and the new demographic, the young’uns looking for fresh twists among the familiar beats.
        </p>
        <p>Luckily, the force is strong with the new incarnation of Union Square Cafe, the beloved flagship of the formidable Danny Meyer empire that stood on East 16th Street since 1985, long before a Shake Shack patty ever sizzled on a griddle top. A rent spike at the original location prompted a move three blocks north to a 10,000-square-foot two-story space that’s nearly double the size of the bygone room; where the old boasted cramped low ceilings and a head-scratching multilevel layout, the new is a light and lofty setting designed by architect David Rockwell.
          <br><br>
        </p>
        <p><b>Union Square Cafe <br> ✭✭✭✭ <br></b>
           101 E 19th St (212-243-4020, unionsquarecafe.com). Average main course: $37.</p>
        <h3 style="color:#2e70db;"> Do you like this content? &nbsp
          <i onclick="thumbUpanddown(this)" class="thumb fa fa-thumbs-up" style="font-size:40px"></i>
        </h3>
      </div>
      <div class="col-3">
        <div class="article-right-aside">
          <a href="content_5.py">
            <img src="../images/massoni.jpg" style="float: left;">
            <p>Massoni</p>
            <p>101 E 31st St, NYC</p>
          </a>
        </div>
         <div class="article-right-aside">
           <a href="content_6.py">
            <img src="../images/butcher.jpg" style="float: left;">
            <p>White Gold Butchers</p>
            <p>375 Amsterdam Ave</p>
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