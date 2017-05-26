#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cgi
import html

content = """
<body style="background-color:black;" padding-top: 51px;>
  <div style="background-image: url(../images/desks.jpg); min-height:400px; background-position:center">
    <ul>
      <li><a href="index.py" style="float: left">Home</a></li>
      <li><a href="reviews.py">Reviews</a></li>
      <li><a href="news.py">News</a></li>
      <li><a href="about.py">About</a></li>
    </ul>
    <h1 class="font-effect-anaglyph">About</h1>
  </div>
  <div class="container">
   <div class="row">
      <div class="col-9 article-left-aside">
        <h3>Mils ( Mesodiar )</h3>
        <img src="../images/profile.png" style="width:35%"class="displayed">
        <div class="col-3"></div>
          <p style="text-align:left; padding: 0px 0px 0px 30px">My name is Mils. I’m a new intern from KMITL in IT engineering. My hobbies are watching movies and running. I’m interest in photography and traveling. I’m a kind of easy-going person and enjoy outdoor activities. My favourite artists are Kodaline and Ed sheeran. I don’t watch TV much but spending time with youtube instead. Please feel free to talk with me :)
          </p>
      </div>
      <div class="col-3">
        <div class="article-right-aside">
          <a href="https://mesodiar.wordpress.com/" ><p>Blog</p></a>
          <a href="https://twitter.com/mesodiar"><p>Twitter</p></a>
          <a href="https://instagram.com/mesodiar/"><p>Instagram</p></a>
          <p><button class="userButton" onclick="helloStranger()">Hello</button></p>
          <p id="demo"></p>
        </div>
      </div>
    </div>
    <div class="bodyimage"></div>
  </div>
  <footer>
    <a href="https://www.facebook.com/"><i class="fa fa-facebook-official" style="font-size:36px;color:white"></i></a>
    <a href="https://www.pinterest.com/"><i class="fa fa-pinterest-p" style="font-size:36px;color:white"></i></a>
    <a href="https://twitter.com/"><i class="fa fa-twitter" style="font-size:36px;color:white"></i></a>
    <a href="https://www.flickr.com/"><i class="fa fa-flickr" style="font-size:36px;color:white"></i></a>
    <a href="https://www.linkedin.com"><i class="fa fa-linkedin" style="font-size:36px;color:white"></i></a>
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