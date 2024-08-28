#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
import smtplib
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
q = """Select * from useregister"""
cur.execute(q)
rec = cur.fetchall()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin-Dashboard</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.min.css">
    <!-- <link rel="stylesheet" href="home.css"> -->
    <script src="./home.js"></script>
</head>
<style>
        *{
        margin: 3;
        padding: 2;
        border: none;
        outline: none;
        box-sizing: border-box;
        font-family: 'Poppins',  sans-serif;
    }
    body{
        display: flex;
    }

    .sidebar{
        position: sticky;
        top: 0;
        left: 0;
        bottom: 0;
        width: 90px;
        height: 100vh;
        padding: 0 1.7rem;
        color: #fff;
        overflow: hidden;
        transition: all 0.5s linear;
        /* background-color: rgba(113, 99, 186, 255); */
        background-color: #003f5c;
    }

    .sidebar:hover{
        width: 300px;
        transition: 0.5s;
    }
    li{
        list-style: none;
    }

    .collapse span,.collapse i{
        display: inline;
    }
    .logo{
        height: 80px;
        padding: 15px;
    }

    .menu{
        height: 88% ;
        position: relative;
        list-style: none;
        padding: 0;
    }

    .menu li{
        padding: 1rem;
        margin: 8px 0;
        border-radius: Box;
        transition: all 0.5s ease-in-out;
    }

    .menu li:hover{
        background: #e0e0e058;
        border-radius: 50px;
    }

    .menu a{
        color: white;
        font-size: 14px;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }
    .menu .dash{
        font-size: 20px;
    }

    .menu a span{
        overflow: hidden;
    }

    .menu a i{
        font-size: 1.9rem;
    }

    .main--content{
        position: relative;
        background: #ebe9e9;
        width: 100%;
        padding: 1rem;
    }

    .header--wrapper img{
        width: 50px;
        height: 50px;
        cursor: pointer;
        border-radius: 50%;
    }
    .header--wrapper{
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        background: #FCF6F5;
        border-radius: 10px;
        padding: 10px 2rem;
        margin-bottom: 1rem;
    }
    .header--title{
        /* color:rgba(113, 99, 186, 255) ; */
        color: #003f5c;
    }

    .user--info{
        display: flex;
        align-items: center;
        gap: 1;
    }

    .main--title{
        color:#003f5c ;
    }

    .tabular--wrapper{
        background: #fff;
        margin-top: 1rem;
        border-radius: 10px;
        
    }

    .table-container{
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        overflow: auto;
    }
    table{
        width: 100%;
        border-collapse: collapse;
       
    }
    thead{
        background: #d6e8ee;
        color: #fff;
    }
    th{
        padding: 15px;
        text-align: center;
        color: rgba(0, 0, 0, 0.473);
    }
    tbody{
        background: #f2f2f2;
    }

    td{
        padding: 15px;
        font-size: 12px;
        color: #333;
        text-align: center;
    }

    tr:nth-child(even){
        background: #e0e0e058;
    }
    .table-container button{
        color: #fff ;
        cursor: pointer;
    }
</style>
<body>
    <div class="sidebar">
        <div class="logo">
            <ul class="menu">
                <li >
                    <a href="#" class="dash">
                        <!-- <i class="fa fa-poll"></i> -->
                        <img src="assets/reddlogo.webp" alt="logo" width="35px" height="35px">
                        <span>DoEmart</span>
                    </a>
                </li>
                <li>
                    <a href="admindash.py">
                        <i class="fa fa-home"></i>
                        <span>Home</span>
                    </a>
                </li>
                <li>
                    <a href="#" data-toggle="collapse" data-target="#shopmenu">
                        <i class="fa fa-user-tag"></i>
                        <span>Shopkeeper <span class="caret"></span></span>
                    </a>
                    <ul id="shopmenu" class="collapse">
                        <li>
                            <a href="newshop.py" ><i class="fas fa-user-plus"></i>  
                                <span>New</span></a>
                        </li>
                        <li>
                            <a href="shopex.py">
                                <i class="fas fa-user"></i>  
                            <span>Existing</span>
                            </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#" data-toggle="collapse" data-target="#usermenu" class="active">
                        <i class="fas fa-user-friends"></i>
                        <span>User <span class="caret"></span></span>
                    </a>
                    <ul id="usermenu" class="collapse">
                        <li><a href="newuser.py">
                            <i class="fas fa-user-plus"></i>  
                            <span>New</span>
                        </a>
                        </li>
                        <li><a href="userex.py">
                            <i class="fas fa-user"></i>  
                            <span>Existing</span>
                        </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="home.py" class="logout" >
                        <i class="fas fa-sign-out-alt"></i>
                        <span>Log out</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>

    <div class="main--content">
        <div class="header--wrapper">
            <div class="header--title">
                <span>Primary</span>
                <h2>Dashboard</h2>
            </div>
            <div class="user--info">
                <img src="assets/adminbluelogo.webp" alt="admin">
            </div>
        </div>
        
        <div class="tabular--wrapper">
            <h3 class="main--title">
                User Request
            </h3>
            <div class="table-container">
                <table class="table">
                    <thead>
                        <tr>
                            <th>First Name</th>
                            <th>Second Name</th>
                            <th>Gender</th>
                            <th>Address</th>
                            <th>State</th>
                            <th>Mobile number</th>
                            <th>Whatsapp number</th>
                            <th>Email Id</th>
                            <th>Address Proof</th>
                            <th>Request</th>
                        </tr>""")
for i in rec:
    fn = "dbmedia/"+i[11]
    if i[12] != 'approve' and i[12] != 'discard':
        print("""  
                        <tbody>
                            <tr>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>%s</td>
                                <td>
                                        <a href=""  data-toggle="modal" data-target="#aadhar-%s"><span class="glyphicon glyphicon-picture"><span></a>
                                        <!-- Modal -->
                                        <div class="modal fade" id="aadhar-%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                                            <div class="modal-dialog" role="document">
                                                <div class="modal-content">
                                                    <div class="modal-header">
                                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                            <span aria-hidden="true">&times;</span>
                                                        </button>
                                                        <h4 class="modal-title" id="myModalLabel">Image Viewer</h4>
                                                    </div>
                                                    <div class="modal-body text-center">
                                                        <img src="%s" alt="Image Viewer" class="img-responsive">
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                </td>
                                <td>
                                <form method="post" enctype="multipart/form-data">
                                        <input type="hidden" name="id" value="%s">
                                        <input type="hidden" name="aemail" value="%s">
                                        <input type="hidden" name="aname" value="%s">
                                        <button type="submit" name="approve" value="approve" class="btn btn-success">Approve</button>
                                    </form>
                                    <form method="post" enctype="multipart/form-data">
                                        <button type="submit" name="discard" value="discard" class="btn btn-danger">Discard</button>
                                    </form>
                                </td>
                            </tr>
                        
""" %(i[1],i[2],i[3],i[6],i[8],i[4],i[5],i[9],i[0],i[0],fn,i[0],i[9],i[1]))
print("""
                        </tbody>
                    </thead>
                </table>
            </div>
        </div>
    </div>

    
</body>
</html>""")

form = cgi.FieldStorage()
id = form.getvalue("id")
uemail = form.getvalue("aemail")
username = form.getvalue("aname")
approve = form.getvalue("approve")
discard = form.getvalue("discard")

if id != None:
    if approve != None:
        q1 = """Select max(id) from useregister"""
        cur.execute(q1)
        rec = cur.fetchone()
        if rec[0] != None:
            n = rec[0]
        else:
            n = 0
        z = ""
        if n <= 9:
            z = "000"
        elif n == 10 or n <= 99:
            z = "00"
        elif n > 99 or n <= 999:
            z = "0"
        uniquepass = "ude" + z + "U" + str(n + 1)
        q2 = """Update useregister set password="%s" where id="%s" """ % (uniquepass, id)
        cur.execute(q2)
        fromadd = "murugasutha18@gmail.com"
        password = "btcr euiw gplh ddrj"
        toadd = uemail
        subject = "Welcome to DoEmart!!!"
        body = "Hi! {} Use this Password: {} to login to your account\n Happy Shopping!!".format(username, uniquepass)
        msg = "subject: {}\n\n{}".format(subject, body)
        server = smtplib.SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(fromadd, password)
        server.sendmail(fromadd, toadd, msg)
        server.quit()
        q = """Update useregister set status = "%s" where id="%s" """ %(approve,id)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Approved Successfully");
        </script>
        """)

    if discard != None:
        q = """Update useregister set status = "%s" where id="%s" """ %(discard,id)
        cur.execute(q)
        con.commit()
        print("""
        <script>
        alert("Request denied");
        </script>
        """)
