#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi, cgitb, pymysql
import os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()

form = cgi.FieldStorage()
ID = form.getvalue("id")
q = """Select * from useregister where id = "%s" """ % ID
cur.execute(q)
rec = cur.fetchall()

q1 = """Select * from shopregister where id = "%s" """ % ID
cur.execute(q1)
recc = cur.fetchall()

q3 = """Select * from addproduct where offer>0 """
cur.execute(q3)
offer = cur.fetchall()

print("""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DoEmart</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="home.css">
    <script src="home.js"></script>
</head>
<body>
    <header class="navbar navbar-expand-sm bg-dark navbar-dark">
        <div>
            <nav class="navbar navbar-inverse">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#mynav">
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                            <span class="icon-bar"></span>
                        </button>
                        <img src="assets/Do.png" alt="logo" class="navbar-brand">
                        <a href="home.py" class="navbar-brand">DoEmart</a>
                    </div>
                    <div class="collapse navbar-collapse" id="mynav">
                        <ul class="nav navbar-nav navbar-right">
                            <li class="active" ><a href="#"><span class="glyphicon glyphicon-gift"></span>Offers</a></li>
                            <li><a href="faqs.py"><span class="glyphicon glyphicon-question-sign"></span>FAQs</a></li>
                            <li><a href="#" id="login" data-toggle="dropdown" style="height: 45px;">Sign in <span class="caret"></span></a>
                                <ul class="dropdown-menu" id="loginmenu">
                                    <li><button type="button" class="btn btn-default" data-toggle="modal" data-target="#mymodal" style="width: 100%;">Admin</button></li>
                                    <li><button type="button" class="btn btn-default" data-toggle="modal" data-target="#shopmodal"  style="width: 100%;">Shopkeeper</button></li>
                                    <li><button type="button" class="btn btn-default" data-toggle="modal" data-target="#usermodal"  style="width: 100%;">User</button></li>
                                </ul>
                            </li>

                            <li><a href="#" id="signup" data-toggle="dropdown" style="height: 45px;">Sign up <span class="caret"></span></a>
                                <ul class="dropdown-menu">
                                    <li><button type="button" class="btn btn-default" data-toggle="modal" data-target="#shopmodal1"  style="width: 100%;">Shopkeeper</button></li>
                                    <li><button type="button" class="btn btn-default" data-toggle="modal" data-target="#usermodal1"  style="width: 100%;">User</button></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <!-- Admin login -->
            <div class="modal fade" id="mymodal"  role="dialog">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4  class="modal-title">Admin Login</h4>
                        </div>
                        <div class="modal-body">
                            <div class="col-md-2"></div>
                            <div class="col-md-8">
                                <form action="admindash.py" method="post" enctype="multipart/form-data" name="admin-login" onsubmit="return admin()">
                                    <div class="form-group">
                                        <input type="text" placeholder="Username" id="user" name="adminuser" class="form-control"><br>
                                        <input type="password" placeholder="Password" id="pass" name="adminpass" maxlength="8" class="form-control"><br><br>
                                        <center><input type="submit" id="sub" name="adminsub" value="Login" class="btn btn-danger" class="form-control"></center>
                                    </div>
                                </form>
                            </div>
                            <div class="col-md-2"></div>
                        </div>
                        <div class="modal-footer">
                        </div>
                    </div>
                </div>
            </div>
            <!-- --------- -->

            <!-- Shopkeeper login -->
            <div class="modal fade" id="shopmodal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">Shopkeeper Login</h4>
                        </div>
                        <div class="modal-body">
                            <div class="col-md-2"></div>
                            <div class="col-md-8">
                                <form method="post" enctype="multipart/form-data" name="shoplogin" onsubmit="return shopvalidate()">
                                    <label for=""  id="label"><span class="glyphicon glyphicon-envelope"></span> Email Id </label>
                                    <input type="email" id="email" name="slemail" class="form-control">
                                    <label for="" id="label"><span class="glyphicon glyphicon-lock"></span> Password </label>
                                    <input type="password" id="passw" name="slpass" maxlength="8" class="form-control">
                                    <a href="shopforgot.py">Forgot password? </a><br>
                                    <center><input type="submit" id="sub" name="shopsub" class="btn btn-danger"></center>
                                 </form>
                            </div>
                            <div class="col-md-2"></div>
                        </div>
                        <div class="modal-footer">
                            <div class="col-md-6"></div>
                            <div class="col-md-6">
                                New User?<a href="#"  data-toggle="modal" data-target="#shopmodal1">Create Account</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- ------------ -->

            <!-- User login -->
            <div class="modal fade" id="usermodal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">User Login</h4>
                        </div>
                        <div class="modal-body">
                                <form enctype="multipart/form-data" name="userlogin" onsubmit="return uservalidate()" method="post">
                                    <label for="" id="label"><span class="glyphicon glyphicon-envelope"></span> Email Id</label> 
                                   <input type="email" id="email" name="uemail" class="form-control">
                                   <label for="" id="label"><span class="glyphicon glyphicon-lock"></span> Password</label> 
                                    <input type="password" id="passw" name="upassw" maxlength="8" class="form-control">
                                    <a href="forget.py">Forgot password? </a><br>
                                    <center><input type="submit" id="sub" name="usersub" class="btn btn-danger"></center>
                                </form>
                                <div class="row mt-4">
                                    <div class="col-md-7"></div>
                                    <div class="col-md-5">
                                        New User?<a href="#" class="btn"  data-toggle="modal" data-target="#usermodal1">Create Account</a>
                                    </div>
                                </div>
                                
                            </div>
                        </div>
                        <div class="modal-footer">
                                
                        </div>
                    </div>
                </div>
            </div>
            <!-- ------------ -->

            <!-- shopkeeper signup -->
            <div class="modal fade" id="shopmodal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">Shopkeeper Sign up</h4>
                        </div>
                        <div class="modal-body">
                                <form  name="shopsignup" method="post" enctype="multipart/form-data" >
                                    <div class="form-group">
                                        <label for="" id="label">Shop Name <span class="glyphicon glyphicon-asterisk"></span></label>
                                        <input type="text" id="sname" name="sname" placeholder="Eg. Kanna Silks" class="form-control">
                                        <label for="" id="label">Owner Name <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="text" id="oname" name="oname"  placeholder="Eg. Sutha" class="form-control">

                                        <label for="gender" id="gender" name="gender">Gender  <span class="glyphicon glyphicon-asterisk"></span></label>
                                        <input type="radio" value="male" name="gender">
                                        <label for="label3" id="gender" name="gender">Male</label>
                                        <input type="radio" value="female" name="gender">
                                        <label for="label4" id="gender" name="gender">Female</label><br>

                                        <label for="" id="label" name="label">Owner's Age <span class="glyphicon glyphicon-asterisk"></span> </label>
                                        <input type="number" name="age" id="age" class="form-control">

                                        <label for="" id="label">Shop Established Since <span class="glyphicon glyphicon-asterisk"></span></label>
                                        <input type="date" name="year" id="year" class="form-control">

                                        <label for="" id="label">Email Id  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="email" name="email" id="email" class="form-control" placeholder="Eg. mailid@gmail.com">

                                        <label for="" id="label" name="label" >Mobile Number <span class="glyphicon glyphicon-asterisk"></span> </label>
                                        <input type="number" name="phno" id="phno" class="form-control" maxlength="10">

                                        <label for="" id="label">WhatsApp Number <span class="glyphicon glyphicon-asterisk"></span> </label>
                                        <input type="number" name="wappno" id="wappno" class="form-control" maxlength="10">

                                        <label for="" id="label">Shop Address  <span class="glyphicon glyphicon-asterisk"></span> </label> 
                                        <input type="text" id="door" name="door" class="form-control"  placeholder="Door no.">
                                        <input type="text" id="street" name="street" class="form-control" placeholder="Street Name">
                                        <input type="text" id="district" name="district" class="form-control" placeholder="District">
                                        <input type="number" id="pin" name="pin" placeholder="Pincode" class="form-control" maxlength="6">

                                        <label for="" id="label">City  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="text" id="city" name="city" class="form-control" placeholder="Eg. Tuticorin">

                                        <label for="" id="label"> State <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="text" id="state" name="state" class="form-control" placeholder="Eg. India">

                                        <label for="" id="label">Owner Photo  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="file" name="photo" id="photo" class="form-control">

                                        <label for="" id="label">Shop License <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="file" name="slicence" id="slicence" class="form-control">

                                        <label for="" id="label">Owner Address Proof  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="file" name="addproof" id="addproof" class="form-control">

                                        <label for="" id="label">Shop Image  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                        <input type="file" name="simage" id="simage" class="form-control"><br>

                                        <input type="submit" value="Sign up" id="sub" name="sub" class="btn btn-danger">
                                    </div>
                                </form>
                            </div>>
                        <div class="modal-footer">
                            Already Register?<a href="#"  data-toggle="modal" data-target="#shopmodal">Login</a>
                        </div>
                    </div>
                </div>
            </div>
            <!-- -------- -->

            <!-- User Signup -->

            <div class="modal fade" id="usermodal1" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4 class="modal-title">User Sign up</h4>
                        </div>
                        <div class="modal-body">
                                <form action="home.py" method="post" enctype="multipart/form-data" name="usersignup" onsubmit="usersign()">
                                    <label for="" id="label">First Name <span class="glyphicon glyphicon-asterisk"></span></label>
                                    <input type="text" id="fname" name="fname" placeholder="Eg. Sutha" class="form-control">

                                    <label for="" id="label">Last Name <span class="glyphicon glyphicon-asterisk"></span></label> 
                                    <input type="text" id="lname" name="lname" placeholder="Eg. Kailasam" class="form-control">

                                    <label for="gender" id="gender" name="ugender">Gender</label>
                                    <input type="radio" value="male" name="ugender">
                                    <label for="label3" id="gender" name="ugender">Male</label>
                                    <input type="radio" value="female" name="ugender">
                                    <label for="label4" id="gender" name="ugender">Female</label><br>

                                    <label for="" id="label" name="label" >Mobile Number <span class="glyphicon glyphicon-asterisk"></span> </label>
                                    <input type="number" name="uphno" id="uphno" maxlength="10" class="form-control">

                                    <label for="" id="label">WhatsApp Number <span class="glyphicon glyphicon-asterisk"></span> </label>
                                    <input type="number" name="uwappno" id="uwappno" maxlength="10"class="form-control">

                                    <label for="" id="label">Address  <span class="glyphicon glyphicon-asterisk"></span> </label> 
                                    <input type="text" id="door" name="udoor"  placeholder="Door no." class="form-control">
                                    <input type="text" id="street" name="ustreet" placeholder="Street Name" class="form-control">
                                    <input type="text" id="district" name="udistrict" placeholder="District" class="form-control">
                                    <input type="text" id="pin" name="upin" placeholder="Pincode" class="form-control">

                                    <label for="" id="label">City  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                    <input type="text" id="city" name="ucity" placeholder="Eg. Tuticorin" class="form-control">

                                    <label for="" id="label"> State  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                    <input type="text" id="state" name="ustate" placeholder="Eg. Tamil Nadu --090-" class="form-control">

                                    <label for="" id="label">Email Id  <span class="glyphicon glyphicon-asterisk"></span></label> 
                                    <input type="email" name="uemail" id="email" placeholder="Eg. mailid@gmail.com" class="form-control"> 

                                    <label for="" id="label">Aadhaar Card<span class="glyphicon glyphicon-asterisk"></span></label> 
                                    <input type="file" name="aadhar" id="aadhar" class="form-control"><br><br>

                                    <input type="submit" value="Sign up" name="usub" class="btn btn-danger">
                                </form>
                        </div>
                        <div class="modal-footer">
                            Already Register?<a href="#"  data-toggle="modal" data-target="#shopmodal">Login</a>
                        </div>
                    </div>
                </div>
            </div>


        </div>
    </header>

    <!-- content -->
    <div class="container-fluid">
        <div class="row ">
            <div class="header">
                <div class="header--wrapper">
                    <h3 class="text-capitalize">offer products </h3>
                </div>
            </div>
        </div><br><br>
        <div class="row dress-card-container">
  """)
for i in offer:
    fn = "product/" + i[7]
    offer = float(i[8])
    price = float(i[6])
    offerprice = price - offer
    id = i[9]
    q = """Select shopname from shopregister where id="%s" """ %id
    cur.execute(q)
    shopname = cur.fetchone()
    print("""
            <div class="col-md-3 text-center dress">
                <div class="dress-card">
                    <h4 class="dress-card-title text-capitalize bg-light">%s</h4>
                    <img class="dress-card-img-top img-fluid" src="%s" alt="%s" style="max-height: 200px;">
                    <h4 class="dress-card-title text-capitalize">%s</h4>
                    <p class="dress-card-para" >%s</p>
                    <p class="dress-card-para"><span class="dress-card-price">Rs.<strike>%s</strike> %s </span></p>
                    <button type="button" class="btn btn-danger" data-toggle="modal" data-target="#usermodal"  style="font-size: 20px;">Buy Now</button>
                </div>
            </div>
    """%(shopname[0],fn,i[2],i[2],i[3],i[6],offerprice))
print("""
                   
            </div> 
        </div><br><br> 

    <!-- Footer   -->
    <footer class="text-center">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <h5>About DoEmart</h5>
                    <p>Your go-to online shopping destination for a wide range of products. Discover the best deals and shop with confidence at DoEMart.</p>
                </div>
                <div class="col-md-3">
                    <h5>Quick Links</h5>
                    <ul class="list-unstyled">
                        <li><a href="./home.py" style="color: black;">Home</a></li>
                        <li><a href="#" style="color: black;">Shop</a></li>  
                        <li><a href="#" style="color: black;">Contact Us</a></li>
                        <li><a href="#" style="color: black;">Privacy Policy</a></li>
                        <li><a href="#" style="color: black;">Terms of Service</a></li>
                    </ul>
                </div>
                <div class="col-md-3">
                    <h5>Contact Information</h5>
                    <p>123 DoEMart Street, Tuticorin, TamilNadu</p>
                    <p>Email: doemart@gmail.com</p>
                     <p>Phone: +91 9876543210</p>
                </div>
                <div class="col-md-3">
                    <h5>Follow Us</h5>
                    <p>Stay connected with us on social media:</p>
                    <a href="#" class="fa fa-facebook"></a>
                    <a href="#" class="fa fa-twitter"></a>
                    <a href="#" class="fa fa-instagram"></a>
                    <a href="#" class="fa fa-pinterest"></a>
                </div>
            </div>
            <hr>
            <div class="row">
                <div class="col-md-12">
                    <p>&copy; 2024 DoEmart. All rights reserved.</p>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>
""")

ssubmit = form.getvalue("sub")
usubmit = form.getvalue("usub")
suser = form.getvalue("shopemail")
spass = form.getvalue("shoppassw")
slogin = form.getvalue("shopsub")
ulogin = form.getvalue("usersub")
semail = form.getvalue("email")
uemail = form.getvalue("uemail")

if ssubmit != None:
    if len(form) != 0:
        shopname = form.getvalue("sname")
        ownername = form.getvalue("oname")
        gender = form.getvalue("gender")
        ownerage = form.getvalue("age")
        shopyear = form.getvalue("year")
        semail = form.getvalue("email")
        sphno = form.getvalue("phno")
        swappno = form.getvalue("wappno")
        saddress = f"{form.getvalue('door')}, {form.getvalue('street')}, {form.getvalue('district')}, {form.getvalue('pin')}"
        scity = form.getvalue("city")
        sstate = form.getvalue("state")
        ownerphoto = form['photo']
        shoplicense = form['slicence']
        owneradd = form['addproof']
        shopimg = form['simage']

        if ownerphoto.filename and shoplicense.filename and owneradd.filename and shopimg.filename:
            fnowner = os.path.basename(ownerphoto.filename)
            open("dbmedia/" + fnowner, "wb").write(ownerphoto.file.read())
            fnshoplicense = os.path.basename(shoplicense.filename)
            open("dbmedia/" + fnshoplicense, "wb").write(shoplicense.file.read())
            fnowneradd = os.path.basename(owneradd.filename)
            open("dbmedia/" + fnowneradd, "wb").write(owneradd.file.read())
            fnshopimg = os.path.basename(shopimg.filename)
            open("dbmedia/" + fnshopimg, "wb").write(shopimg.file.read())
            q = """INSERT INTO `shopregister`( shopname, ownername, gender, age, shopyear, email, phno, wappno, address, city, state, ownerimg, license, addproof,shopimg) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            shopname, ownername, gender, ownerage, shopyear, semail, sphno, swappno, saddress, scity, sstate, fnowner,
            fnshoplicense, fnowneradd, fnshopimg)
            cur.execute(q)
            con.commit()
            print("""
                    <script>
                        alert("Registered successfully!! Once your profile been approved, you will receive your password.Check your email!. ")
                    </script>
            """)

if usubmit != None:
    if len(form) != 0:
        fname = form.getvalue("fname")
        lname = form.getvalue("lname")
        ugender = form.getvalue("ugender")
        uphno = form.getvalue("uphno")
        uwappno = form.getvalue("uwappno")
        uaddress = f"{form.getvalue('udoor')}, {form.getvalue('ustreet')}, {form.getvalue('udistrict')}, {form.getvalue('upin')}"
        ucity = form.getvalue("ucity")
        ustate = form.getvalue("ustate")
        uemail = form.getvalue("uemail")
        aadhar = form["aadhar"]
        if aadhar.filename:
            fnaadhar = os.path.basename(aadhar.filename)
            open("dbmedia/" + fnaadhar, "wb").write(aadhar.file.read())
            q1 = """INSERT INTO useregister(firstname, lastname, gender, phno, wapp, address, city, state, email,  aadhar) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (
            fname, lname, ugender, uphno, uwappno, uaddress, ucity, ustate, uemail, fnaadhar)
            cur.execute(q1)
            con.commit()
            print("""
                    <script>
                        alert("Registered successfully")
                    </script>
            """)

if slogin != None:
    slemail = form.getvalue("slemail")
    slpass = form.getvalue("slpass")
    q = """select id from shopregister where email = '%s' and password = '%s'""" % (slemail, slpass)
    cur.execute(q)
    recc = cur.fetchone()
    print("""
                    <script>
                        alert("Login successfully");
                        location.href="shopkeeperdash.py?id=%s";
                    </script>
                """ % (recc[0]))

if ulogin != None:
    uemail = form.getvalue("uemail")
    lpass = form.getvalue("upassw")
    q = """select id from useregister where  email = '%s' and password = '%s' """ % (uemail, lpass)
    cur.execute(q)
    rec = cur.fetchone()
    print("""
         <script>
            alert("Login successfully");
              location.href="userhome.py?id=%s";
         </script>
    """ % (rec[0]))