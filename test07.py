#!C:\Users\tanumond\AppData\Local\Programs\Python\Python310\python.exe

# Import modules for CGI handling 
import cgi, cgitb 
import mysql.connector
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "testdatabase"
)
# Get data from fields
product = form.getvalue('product')
build  = form.getvalue('build')
#dropdown = form.getvalue('dropdown')

cursor = mydb.cursor()
cursor.execute("SELECT * FROM `testtable` WHERE product = %s and build = %s;", (product, build))

result = cursor.fetchall()
print ("Content-type:text/html\r\n\r\n")

print('<html>')
print('<head>')
print('<title>Restore dependent packages</title>')
print("""<style>
         
    h3 {color:#E31616;font-size:17pt}
    center {color:black;font-family:'Times New Roman', Times, serif;font-size:12pt}
    h4 {color:black;font-size:17pt;}
    td {color:black;font-family:'Times New Roman', Times, serif;font-size:13pt; font-weight: bold}
    p {color:#1793D1;font-family:'Times New Roman', Times, serif;font-size:14pt}
    select {color:black;font-family:'Times New Roman', Times, serif;font-size:13pt}  
        </style>""")

print('<script src="https://code.jquery.com/jquery-3.4.1.min.js"></script>')      
print('<script src="js/checkAll.min.js"></script>')  
      
print('</head>')
print('<body>')



print('<center><h4>Please provide the following details</h4>')
        
print('<form name = "input" action = "test7.py" method = "get">')
print('<input name="request" type="hidden">')   
print('<table width="90%" border="1">')

print('<tr>')
print('<td width="60%">Product Name? (example: guiFramework, provide pkgget_name for best results)</td>')
if ("product" not in form ):
    print('<td><input type="text" name="product" required></td>')
else:    
    print('<td><input type="text" name="product" value="%s" required></td>'%(product))
print('</tr>')

print('<tr>')
print('<td>  Build_context.ini content</td>')
if ("build" not in form ):
    print('<td><textarea name = "build" cols = "109" rows = "19"></textarea></td>')
    
else:    
    print('<td><textarea name = "build" cols = "109" rows = "19">%s</textarea></td>' %(build)) 
print('</tr>')
print('</table><br>')

print('<center><input type="submit" name="Search"></center>')
print('</form>')
print('</center>')
print('</body>')
print('</html>')



def show():
    print ("<html>")
    print ("<head>")
    print ("<title>Name</title>")
   
    print('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>')      


    print("""<script type="text/javascript">  
            function selects(){  
                var ele=document.getElementsByName('chk');  
                for(var i=0; i<ele.length; i++){  
                    if(ele[i].type=='checkbox')  
                        ele[i].checked=true;  
                }  
            }  
            function deSelect(){  
                var ele=document.getElementsByName('chk');  
                for(var i=0; i<ele.length; i++){  
                    if(ele[i].type=='checkbox')  
                        ele[i].checked=false;  
                      
                }  
            }             
        </script>""")

    print ("""<style type="text/css">
    h3 {color:#E31616;font-size:16pt}
    center {color:black;font-family:'Times New Roman', Times, serif;font-size:12pt}
    h4 {color:black;font-size:17pt;padding-top:20px}
    td {color:black;font-family:'Times New Roman', Times, serif;font-size:12pt}
    p {color:#1793D1;font-family:'Times New Roman', Times, serif;font-size:14pt}
    
    
    </style>""")


    print ("</head>")
    print ("<body>")


    print('<center>')
    print ('<h3>Missing Anchor List </h3>\n')
    #print('<h5>%s</h5>',(result[0][1]))
    print ('<table width=90%% align=center border=1><tr align=center><th>Sl. No.</th><th>pkgget name</th><th>version</th><th>S3 location</th><th>US location</th><th><input type = "checkbox" class="checkAll" id="chkall" name = "chk" value = "on" /></th></tr>')
    print ('<tbody>')
    for i in result:
        """
        sl = i[0]
        pkgget = i[3]
        version = i[4]
        s3 = i[5]
        us = i[6]
        """
        #print ('<tr align=center><td>'+sl+'</td><td>'+pkgget+'</td><td>'+version+'</td><td>'+s3+'</td><td>'+us+'</td><td><input type = "checkbox" name = "chk" class="chck" value = "on" /> </td></tr>')
        print ('<tr align=center><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><input type = "checkbox" name = "chk" class="chck" value = "on" /> </td></tr>' %(result.index(i)+1,i[3],i[4],i[5],i[6]))
    print ('</tbody>')
    print('</table>')
    print('</center>')
    print('<br>')
    cursor.close()
    mydb.close()
    print("""<center>
    <input type="button" onclick='selects()' value="Select All"/>  
        <input type="button" onclick='deSelect()' value="Deselect All"/>
        <input type="button" value="Restore"/> 
         </center>""")
    
    print("""<script type="text/javascript">
                $(document).ready(function(){
                $('#chkall').click(function(){
                $(".chck").prop('checked', $ (this).prop('checked'));
                });
                });
            </script>""")

    print ("</body>")
    print ("</html>")

if ("product" not in form and "build" not in form):
    print(" ")
else:    
    show()
