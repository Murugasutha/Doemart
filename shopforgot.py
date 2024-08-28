#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import smtplib

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
q = """select * from shopregister"""
cur.execute(q)
rec = cur.fetchall()
for i in rec:
    print("""
       <form>
            <input type="hidden" value="%s" name="uname">
            <input type="hidden" value="%s" name="password">
        </form> 
       """ % (i[2], i[7]))

print("""
            <!DOCTYPE html>
            <html lang="en">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
                <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> -->
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.min.css">
                <link rel="stylesheet" href="userhome.css">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        margin: 0;
                        margin-left: 25%;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 600px;
                        width: 50%;
                        background: crimson;
                    }

                    h2 {
                        color: #ccc;
                    }

                    .login-container {
                        background-color: #f5f2f2;
                        padding: 80px;
                        border-radius: 8px;
                        box-shadow: 5px 7px 6px rgba(19, 8, 8, 1);
                    }

                    .form-group {
                        margin-bottom: 15px;
                    }

                    .form-group label {
                        display: block;
                        font-weight: bold;
                    }

                    .form-group input {
                        width: 100%;
                        padding: 8px;
                        border: 1px solid #ccc;
                        border-radius: 4px;
                    }

                    .form-group button {
                        width: 100%;
                        padding: 8px;
                        background-color: #38d63e;
                        color: white;
                        border: none;
                        border-radius: 4px;
                        cursor: pointer;
                    }

                    .form-group a {
                        display: block;
                        text-align: center;
                        text-decoration: none;
                        color: #333;
                        margin-top: 10px;
                    }

                    
                    #hover1:hover {
                        background-color: #FCF6F5;
                    }
                </style>

            </head>

            <body>
                <div class="container">

                    <div class="login-container">
                        <h3>Forget Password </h3><br><br>
                        <form action="" method="post" enctype="multipart/form-data">
                            <div class="form-group">

                                <label for="username" clas>Email Id:</label>
                                <input type="email" name="userid" placeholder="Enter your mail" id="hover1"
                                    class="form-control" required><br><br>

                                <input type="submit" class="btn btn-dark"  name="submit" value="submit" class="form-control"> 
                                <a href="home.py" class="btn btn-danger " style="text decoration: none; color: white;">Back to Home Page</a>
                            </div>
                        </form>
                    </div>
                </div>
            </body>
            </html>
                """)


def is_uemail_exists(email):
    count = "SELECT COUNT(*) FROM useregister WHERE email='%s'" % email
    cur.execute(count)
    result = cur.fetchone()
    return result[0] == 0


form = cgi.FieldStorage()
email = form.getvalue("userid")
submit = form.getvalue("submit")
username = form.getvalue("uname")
if submit != None:
    if is_uemail_exists(email):
        print("""
                           <script>
                               alert("Email does not exists Resgister your account");
                           </script>
                       """)

    else:
        q = """Select password from shopregister where email="%s" """ % (email)
        cur.execute(q)
        passw = cur.fetchone()
        formadd = "murugasutha18@gmail.com"
        password = "btcr euiw gplh ddrj"
        toadd = email
        subject = "Welcome To DoEmart"
        body = "Hi! This is your Password:{}".format(passw[0])
        mes = "subject:{}\n\n{}".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(formadd, password)
        server.sendmail(formadd, toadd, mes)
        server.quit()
        print("""
            <script>
                alert("Email Sent");
            </script>""")