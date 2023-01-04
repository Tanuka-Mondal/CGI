#!C:\Users\tanumond\AppData\Local\Programs\Python\Python310\python.exe

# Import modules for CGI handling 
import cgi, cgitb 

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')



print ("Content-type:text/html\r\n\r\n")

print ("<html>")
print ("<head>")
print ("<title>Restore dependent packages</title>")
print ("""<style>
            
    center {color:black;font-family:Tahoma;font-size:10pt}
    h4 {color:black;font-size:17pt;}
    
        </style>""")
      
print ("</head>")
print ("<body>")
print ("<center>")
print ("<h4>Please provide the following details</h4>")
print ("</center>")
print ('<form name = "input" action = "test4.py" method = "get">')
print ('First Name: <input type = "text" name = "first_name">  <br />')
            
print ('Last Name: <input type = "text" name = "last_name" />')
print ('<input type = "submit" value = "Submit" />')
print ('</form>')
print ('</body>')
print ('</html>')


def show(first_name, last_name):
    print ("<html>")
    print ("<head>")
    print ("<title>Name</title>")
    print ("</head>")
    print ("<body>")
    print ("<h2>Hello %s %s</h2>" % (first_name, last_name))
    print ("</body>")
    print ("</html>")
 

if ("first_name" not in form ):
    print(" ")
else:    
    show(first_name, last_name)
