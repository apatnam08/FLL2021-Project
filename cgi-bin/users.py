#!/usr/bin/python

# Import modules for CGI handling
import cgi, cgitb
import csv

cgitb.enable()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('fname')
last_name  = form.getvalue('lname')
email = form.getvalue('email')
password = form.getvalue('psw')
age = form.getvalue('amount')
heart_rate = form.getvalue('amounts')
height = form.getvalue('inches')
weight = form.getvalue('pounds')
sight = form.getvalue('sight')

if form.getvalue('gender'):
   gender = form.getvalue('gender')
else:
   gender = "Not set"

if form.getvalue('state'):
   state = form.getvalue('state')
else:
   state = "Not entered"
   
if form.getvalue('disability'):
   disability = form.getvalue('disability')
else:
   disability = "Not set"
# store user details in a file
file = open('users.csv', 'a')
record=first_name+','+last_name+','+email+','+password+','+gender+','+age+' years old'+','+heart_rate+' bpm'+','+height+' inches'+','+weight+' pounds'+','+'20/'+sight+','+'state: '+state+','+'Disability? '+disability+'\n'
file.write(record)
file.close()

file = open('users.csv' , 'r')
reader = csv.reader(file)
user_dict = {}
for column in reader:
    user_dict[column[2]] = {'fname':column[0], 'lname':column[1], 'password':column[3]}



print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>WALL-Exercising | Welcome</title>")
print("</head>")
print("<body>")
print("<center>")
print("<br/>")
print("<h1>Welcome %s %s</h1>" % (first_name, last_name))
'''
for w in user_dict:
    if user_dict[w[0]] == email:
         print ("<h2>Username used<h2>")
'''
print("<h4>%s</h>" % (user_dict))
print("<h2>To got to the app, <a href=\"..\\client\\App.html\">click here</a></h2>")
#print("<h3>To go to the app <p href = "App.html"> click here</p><h3>")
#print("<input id="signup_btn" type="submit" value="Start Excercising Now!" ></input>")
print("</center>")
'''
w_weightage = 0.3
h_weightage = 0.3
b_weightage = 0.2
e_weightage = 0.2

#Elementary schoolers
if age >= "6" and age <= "10":
    we = weight
    he = height
    be = heart_rate
    ee = sight

    #weight
    we_min = 45
    we_max = 70
    normal_we = (we - we_min) / (we_max - we_min)
    we_rounded = round(normal_we * w_weightage, 2)
    #print (normal_we)
    #print ("Rounded w/ weightage: ", we_rounded)

    #height
    he_min = 45
    he_max = 54
    normal_he = (he - he_min) / (he_max - he_min)
    he_rounded = round(normal_he * h_weightage, 2)
    #print (normal_he)
    #print ("Rounded w/ weightage: ", he_rounded)

    #heart rate
    be_min = 60
    be_max = 120
    normal_be = (be - be_min) / (be_max - be_min)
    be_rounded = round(normal_be * b_weightage, 2)
    #print (normal_be)
    #print ("Rounded w/ weightage: ", be_rounded)

    #eyesight 
    ee_min = 10
    ee_max = 30
    normal_ee = (ee - ee_min) / (ee_max - ee_min)
    ee_rounded = round(normal_ee * e_weightage, 2)
    #print (normal_ee)
    #print ("Rounded w/ weightage: ", ee_rounded)
    
    e_score = we_rounded + he_rounded + be_rounded + ee_rounded
    print("<h2>Your score is: %s </h2>" % ((e_score / 0.5)*100) )
    
#Middle schoolers
elif age >= "11" and age <= "14":
    wm = weight
    hm = height
    bm = heart_rate
    em = sight
    
    #weight
    wm_min = 78
    wm_max = 112
    normal_wm = (wm - wm_min) / (wm_max - wm_min)
    wm_rounded = round(normal_wm * w_weightage, 2)
    #print (normal_wm)
    #print ("Rounded w/ weightage: ", wm_rounded)

    #height
    hm_min = 56
    hm_max = 64
    normal_hm = (hm - hm_min) / (hm_max - hm_min)
    hm_rounded = round(normal_hm * h_weightage, 2)
    #print (normal_hm)
    #print ("Rounded w/ weightage: ", hm_rounded)
    
    #heart rate
    bm_min = 50
    bm_max = 105
    normal_bm = (bm - bm_min) / (bm_max - bm_min)
    bm_rounded = round(normal_bm * b_weightage, 2)
    #print (normal_bm)
    #print ("Rounded w/ weightage: ", bm_rounded)

    #eyesight 
    em_min = 10
    em_max = 30
    normal_em = (em - em_min) / (em_max - em_min)
    em_rounded = round(normal_em * e_weightage, 2)
    #print (normal_em)
    #print ("Rounded w/ weightage: ", em_rounded)
    
    m_score = wm_rounded + hm_rounded + bm_rounded + em_rounded
    print("<h2>Your score is: %s </h2>" % ((m_score / 0.5)*100) )
else:
    print("<h2>Invalid</h2>")

'''
print("</body>")
print("</html>")
