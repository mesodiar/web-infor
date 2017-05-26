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
    <h1 style="color:white">Review 2</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-9 article-left-aside">
        <h3>Massoni</h3>
        <img class="displayed" src="../images/massoni.jpg">
        <p>Dale Talde serves tartare cannoli and Detroit pizza at his "Italianish" newcomer Massoni
        </p>
        <p>“Italianish.” It’s a word thrown around with great frequency at Massoni, the graffiti-tagged new arrival at the Arlo NoMad hotel from celebrity chef Dale Talde and his Three Kings Restaurant Group. Servers are quick to drop it during their tableside selling of gimmicky starters like small arancini balls built with biryani ($12)—the cardamom-and-curry zing is too subdued in the rice, but a side of yogurt-addled tomato sauce adds some necessary zing—and pistachio-crusted cannoli tubes piped with beef tartare ($16).
            <br><br>
        </p>
        <p><b>Massoni <br> ✭✭✭ <br></b>
          11 E 31st St (212-951-1141, massoninyc.com). Average pizza: $17.
        </p>
         <h3 style="color:#2e70db;"> Do you like this content? &nbsp
          <i onclick="thumbUpanddown(this)" class="thumb fa fa-thumbs-up" style="font-size:40px"></i>
        </h3>
      </div>
      <div class="col-3">
        <div class="article-right-aside">
          <a href="content_4.py">
            <img src="../images/union-1.jpg" style="float: left;">
            <p>Union Square Cafe</p>
            <p>101 E 19th St, NYC</p>
          </a>
        </div>
         <div class="article-right-aside">
           <a href="content_6.py">
            <img src="../images/butcher.jpg" style="float: left;">
            <p>White Gold Butchers</p>
            <p>375 Amsterdam Ave</p
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