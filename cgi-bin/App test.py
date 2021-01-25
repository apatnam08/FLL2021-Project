#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fn = int(form['user'].value)

# below code is to regenerate html page for the updated private gallery

htmlFile = open('client\\App.html', 'w')
   
htmlFile.write('''<!DOCTYPE html>
<html>
<head>
  <title>WALL-Exercising | App</title>
<style>
/* The Modal (background) */
.modal {
  display: none; /* Hidden by default */
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  padding-top: 100px; /* Location of the box */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0,0.4); /* Black w/ opacity */
}

/* Modal Content */
.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

/* The Close Button */
.close {
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
div.header {
  position: -webkit-sticky;
  position: sticky;
  box-shadow: 0px 4px 5px gray;
  top: 0;
  padding: 25px;
  background-color: #f5f5f5;
  text-align: center;
  width: 100%;
}
body {
  font-family: "Lucida Sans Unicode", "Lucida Grande", sans-serif;
  background-color: white;
  text-align: center;
}

div.shadow {
  color: white;
  text-shadow: 1px 1px 2px black, 0 0 10px black, 0 0 5px black;
}

* {
  box-sizing: border-box;
}

/* Add padding to containers */
.container {
  padding: 15px;
  background-color: white;
}

input[type=text], input[type=password] {
  width: 50%;
  padding: 15px;
  margin: 10px 0 20px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #000080;
  color: white;
  box-shadow: 0px 7px 5px #000049;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 9%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}

/* Add a blue text color to links */
a {
  color: #E6B000;
}

/* Set a grey background color and center the text of the "sign in" section */
.footer {
  background-color: black;
  text-align: center;
  width: 100%;
}
</style>
</head>
<body>
<div class = "header">
	

''')
imgLine='<b>The WALL-Exercising | <a href="Sign In.html">Sign in</a> | <a href="Excercise app Gallary.html">Gallery</a> | <a href="Exercise app Inspiration.html">Inspiration</a> | <a href="Excercise app Research.html">Analytics</a> | <a href="App Image Verification.html">e-Verify</a> | <a href="Admin.html">Admin-Only</a> &nbsp; &nbsp; &nbsp; &nbsp; <button id="myBtn" class="registerbtn" >Thank you!</button> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 	<span style="background-color: #CBCBCB">' + str(fn) + ' points</span></b>' + '\n'
htmlFile.write(imgLine)
htmlFile.write('''
</div>
<br/>
<!-- The Modal -->
<div id="myModal" class="modal">

  <!-- Modal content -->
  <div class="modal-content">
    <span class="close">&times;</span>
    <p>Since you just got started with our app, we'll thank you and give you 1000 points!</p>
  </div>

</div>

<script>
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
</script>

<a href = "https://cdn.cdnparenting.com/articles/2018/06/467385302-H.jpg"><img src = "https://cdn.cdnparenting.com/articles/2018/06/467385302-H.jpg" height="200" width = "301" ALIGN="left"></a>
<img src = "https://www.cheatsheet.com/wp-content/uploads/2015/08/Happy-friends-running-in-the-park.jpg" height="200" width = "301" ALIGN="left">
<img src = "https://goalrilla.com/static/ef1f77d8f29dc8f0ee4351fb3ac96b4d/0e329/b5000w_goalrilla_gs72c_dscf7824.jpg" height="200" width = "300" ALIGN="left">
<img src = "https://www.baptistmilestone.com/hs-fs/hub/388982/file-1944606465-jpg/Blog_Images/kids_exercising.jpg?width=400&name=kids_exercising.jpg" height="200" width = "300" ALIGN="left">
<img src = "https://healthpoweredkids.org/wp-content/uploads/2015/08/IMG_3451-e1438879101858.jpg" height="200" width = "300" ALIGN="left">
<img src = "https://www.verywellfamily.com/thmb/HdUIFUInf0JmHUzKtezLyZ-sYFw=/500x350/filters:no_upscale():max_bytes(150000):strip_icc()/boys-playing-in-a-soccer-match-557921577-572104783df78c56409d29c4.jpg" height="200" width = "300" ALIGN="left">
<img src = "https://iyca.org/wp-content/uploads/2012/07/training-young-athletes-with-deadlifts.jpg" height="200" width = "300" ALIGN="right">
<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
<center>
<div class = "shadow">
    <h1>Experience the Power of Exercising!</h1>
	<br/><br/>
</div>
<img src = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/kid-exercises-1508981273.jpg" height="200" width = "300" ALIGN="left">
<img src = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/articles/2016/06/student-cycling-1499802293.jpg" height="200" width = "300" ALIGN="right">
<div>
	<h3><b>Ever wish you got more screen time on your favorite apps?</b></h3>
	<h3><b>Or wish you gained cool prizes?</b></h3>
	<h3><b>All while making your parents happy?</b></h3>
</div>
<br/><br/>
<img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIy7eE2h5kLK6OIAQ2_K8rkyTGtrlw20oP0w&usqp=CAU" height="200" width = "300" ALIGN="left">
<img src = "https://content.active.com/Assets/Active.com+Content+Site+Digital+Assets/Kids/Galleries/Outdoor+Exercise/Slide+6.jpg" height="200" width = "300" ALIGN="right">
<div class = "shadow">
	<br/>	
    <h2><b>Then WALL-Exercising is the thing for you!</b></h2>
</div>
<div>
	<h3><b>All YOU have to do is exercise!<b></h3>
	<h3><b>Exercise daily to complete goals....<b></h3>
</div>
<img src = "https://i.guim.co.uk/img/media/5994290cd2f3a9440bcffdf31f513ae258323c78/0_0_6000_3600/master/6000.jpg?width=445&quality=85&auto=format&fit=max&s=ea015bb6148b686a43d663f5b844957d" height="200" width = "300" ALIGN="left">
<img src = "https://cdn.psychologytoday.com/sites/default/files/styles/article-inline-half/public/field_blog_entry_images/no-attribution-CC0%20public%20domain-run-1321278_1920.jpg?itok=k9yEKjPY" height="200" width = "300" ALIGN="right">
<div>
	<h3><b>Complete goals to unlock XP....<b></h3>
	<h3><b>Turn in XP to gain prizes!<b></h3>
</div>
<div class = "shadow">
	<br/>	
    <h2><b>That's ALL!</b><h2>
	<br/><br/>
</div>
</center>
<div class = "container footer" style = "color:gray">
	  <h2><pre class="tab">The WALL-Exercising                 Sign up today!</pre></h2>
	  Call me at: <a href="tel:+15167896226">+1-516-789-6226</a>
</div>
''')
htmlFile.write("</body>\n")
htmlFile.write("</html>\n")
htmlFile.close()  

message = 'The points were given succesfully'
print("Content-Type: text/html\n")
print("<html>")
print("<body>")
print("<p>%s</p>"  % (message))
print("<h3>To go back to the Admin page, <a href=\"..\\client\\Admin.html\">click here</a></h2>")
print("</body>")
print("</html>")