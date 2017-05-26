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
    <h1 style="color:white">Review 3</h1>
  </div>
  <div class="container">
    <div class="row">
      <div class="col-9 article-left-aside">
        <h3>White Gold Butchers</h3>
        <img class="displayed" src="../images/butcher.jpg">
        <p>
          Full table service is relegated to dinner only, but waiters execute it with a casual indifference (on a recent night, one scatterbrained server forgot the table’s crispy, beef-fat–slathered potatoes not once, but twice) that distracts from standout dishes like a juicy rotisserie chicken for two ($48), painted with a salsa verde that throbs with anchovy and herbs, or a gorgeous bowl of bone broth ($11). Lustier than its paper-cup brethren, that silky, intensely beefy elixir is dressed with hunks of kabocha, Taleggio and a slick of pumpkin-seed oil.
        </p>
        <p>Better is lunchtime, which is more low-key: You order straight from the counter and have your meatball sandwich (the excellent, oozing rendition here sports tangy tomato sauce and soft pools of Spanish miticrema ($12)) delivered to a table or to one of the window stools. It’s then, with uptown folk yakking over steamy chicken-soup bowls ($8) and snappy house-made hot dogs piled with plucky kimchi ($7), that White Gold settles into itself and feels the most, well, Bloomfieldian. It may not serve a burger, but when you have a freshly butchered porchetta sandwich ($10) that melts immediately upon contact, who needs one?
           <br><br>
        </p>
        <p><b>White Gold Butchers<br> ✭✭✭✭ <br></b>
           375 Amsterdam Ave (212-362-8731, whitegoldbutchers.com). Average main course: $22.</p>
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
           <a href="content_5.py">
            <img src="../images/massoni.jpg" style="float: left;">
            <p>Massoni</p>
            <p>101 E 31st St, NYC</p>
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