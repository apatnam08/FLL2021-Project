#!/usr/bin/python
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
#fn = int(form["post"].value)
fn = int(form['user'].value)
print("slider: ", fn)

htmlFile = open('client\\sliderWithPost.html', 'w')
   
htmlFile.write('''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.slidecontainer {
  width: 100%;
}

.slider {
  -webkit-appearance: none;
  width: 50%;
  height: 25px;
  background: #d3d3d3;
  outline: none;
  opacity: 0.7;
  -webkit-transition: .2s;
  transition: opacity .2s;
}

.slider:hover {
  opacity: 1;
}

.slider::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 25px;
  height: 25px;
  background: #4CAF50;
  cursor: pointer;
}

.slider::-moz-range-thumb {
  width: 25px;
  height: 25px;
  background: #4CAF50;
  cursor: pointer;
}
</style>
</head>
<body>

<h1>Custom Range Slider</h1>
<p>Drag the slider to display the current value.</p>

<div class="slidecontainer">
  <input type="range" min="1" max="100" value="50" class="slider" id="myRange">
  <p>Value: <span id="demo"></span></p>
</div>

<form name="input" action="../cgi-bin/gettingPostValue.py" method="post">
 <input type="text" name="user" id="mytext">
 <input type="submit" value="Submit">
</form>

<script>
var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value;

slider.oninput = function() {
  output.innerHTML = this.value;
document.getElementById("mytext").value = this.value;
}
</script><p>'''+str(fn)+'''</p>

</body>
</html>
''')
#<b><a href = "../cgi-bin/gettingPostValue.py?post=500">Apply</a></b><br/>
htmlFile.close()  

message = 'The points were given succesfully'
print("Content-Type: text/html\n")
print("<html>")
print("<body>")
print("<p>%s</p>"  % (message))
print("<h3>To go back to the page, <a href=\"..\\client\\sliderWithPost.html\">click here</a></h2>")
print("</body>")
print("</html>")