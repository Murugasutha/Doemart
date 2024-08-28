#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
q1 = """Select * from useregister where id="%s" """%(ID)
cur.execute(q1)
recc = cur.fetchall()

q = """Select* from addproduct where category = "homeapliances" """
cur.execute(q)
rec = cur.fetchall()

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
    <script src="./home.js"></script>
</head>
<body>
    <div class="offcanvas offcanvas-start" id="demo">
        <div class="offcanvas-header">
            <h1 class="offcanvas-title">Menu</h1>
            <button type="button" class="btn-close text-reset bg-light" data-bs-dismiss="offcanvas"></button>
        </div>
        <div class="offcanvas-body">
            <div class="sidebar">
                <div class="logo">
                    <ul class="menu">
                        <li class="active">
                            <a href="./userhome.py?id=%s" class="fs-5">
                                Home
                            </a>
                        </li>
                        <li>
                            <a href="" class="fs-5"  data-bs-toggle="collapse" data-bs-target="#promenu">
                                Category <i class="fa fa-caret-down"></i>
                            </a>
                            <div id="promenu" class="collapse">
                                <ul >
                                    <li>
                                        <a href="./homeappliances.py?id=%s" class="fs-5" >Home Appliances
                                            </a>
                                    </li>
                                    <li>
                                        <a class="fs-5" href="./fashion.py?id=%s">  
                                        Clothing
                                        </a>
                                    </li>
                                    <li>
                                        <a href="./footwear.py?id=%s" class="fs-5">  
                                        Footwear
                                        </a>
                                    </li>
                                    <li>
                                        <a href="./electronics.py?id=%s" class="fs-5">  
                                        Electronics
                                        </a>
                                    </li>
                                    <li>
                                        <a href="./makeup.py?id=%s" class="fs-5">  
                                        Makeup Products
                                        </a>
                                    </li>
                                    <li>
                                        <a href="./gifts.py?id=%s"class="fs-5">  
                                        Gifts and Toys
                                        </a>
                                    </li>
                                    <li>
                                        <a href="./accessories.py?id=%s" class="fs-5">  
                                        Accessories
                                        </a>
                                    </li>
                                    <li>
                                        <a href="./stationary.py?id=%s" class="fs-5">  
                                        Stationary
                                        </a>
                                    </li>
                                    <li>
                                        <a href="./grocery.py?id=%s" class="fs-5">  
                                        Groceries
                                        </a>
                                    </li>
                                </ul>
                            </div>

                        </li>
                        <li>
                            <a href="useroffer.py?id=%s" class="fs-5">
                                Offers</a>
                        </li>
                        <li>
                            <a href="#" class="fs-5" data-bs-toggle="collapse" data-bs-target="#ordermenu">
                                Orders <i class="fa fa-caret-down"></i>
                            </a>
                            <div id="ordermenu" class="collapse">
                                <ul >
                                    <li>
                                        <a href="userorder.py?id=%s" class="fs-5">
                                            New
                                        </a>
                                    </li>
                                    <li>
                                        <a href="exuserorder.py?id=%s" class="fs-5">
                                            Existing
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

        </div>
    </div>
""" % (ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID, ID))
print("""
  <header>
    <nav class="navbar navbar-expand-sm  bg-dark navbar-dark mynav">
        <div class="container-fluid">
            <button class="btn navbar-brand" type="button" data-bs-toggle="offcanvas" data-bs-target="#demo">
                <i class="fas fa-bars"></i>
              </button>
          <a class="navbar-brand justify-content-center" href="./userhome.py?id=%s">DoEmart</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynav">
            <a class="nav-link" href="#"><img src="./assets/adminimg.jfif" alt="" width="30px" class="rounded-circle"></a>
          </button>
          <div class="collapse navbar-collapse" id="mynav">
                <ul class="nav">
                    <li class="nav-item">
                    <div class="dropdown">
"""%(ID))
print("""
                        <a class="nav-link" href="#" class="dropdown-toggle" data-bs-toggle="dropdown" style="color: white;"><img src="assets/userdefault" alt="" width="30px" class="rounded-circle">  Profile</a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item text-center" href="profile.py?id=%s">Edit Profile</a></li>
                            <li><a class="dropdown-divider" href="#"><hr></hr></a></li>
                            <li><a class="dropdown-item text-center" href="home.py">Log Out</a></li>
                        </ul>
                    </div>
                    </li>
                </ul>
          </div>
        </div>
      </nav>
  </header>
""" %(ID))
print("""
  <div class="container-fluid">
        <div class="row ">
            <div class="header">
                <div class="header--wrapper">
                    <h3 class="text-capitalize">result for Fashion: </h3>
                </div>
            </div>
        </div><br><br>
        <div class="row dress-card-container">
  """)
for i in rec:
    fn = "product/" + i[7]
    print("""
            <div class="col-md-3 text-center dress">
                <div class="dress-card">
                    <img class="dress-card-img-top img-fluid" src="%s" alt="%s" style="max-height: 200px;">
                    <h4 class="dress-card-title text-capitalize">%s</h4>
                    <p class="dress-card-para" >%s</p>
                    <p class="dress-card-para"><span class="dress-card-price">Rs.%s &ensp;</span></p>
                    <a href="buynow.py?id=%s" target="_blank"><button type="button" class="btn btn-dark" style="font-size: 20px;">Buy Now</button></a>
                </div>
            </div>
    """ % (fn, i[2], i[2], i[3], i[6], i[0]))
print("""

            </div> 
        </div><br><br> 
    <!-- Footer   -->
    <footer class="text-center">
        <div class="container">
            <div class="row">
                <div class="col-md-3">
                    <h5>About DoEmart</h5>
                    <p>Your online shopping destination for a wide range of products. Discover the best deals and shop with confidence at DoEmart.</p>
                </div>
                <div class="col-md-3">
                    <h5>Quick Links</h5>
                    <ul class="list-unstyled a">
                        <li><a href="./home.py" style="color: white;">Home</a></li>
                        <li><a href="#" style="color: white;">Shop</a></li>  
                        <li><a href="#" style="color: white;">Contact Us</a></li>
                        <li><a href="#" style="color: white;">Privacy Policy</a></li>
                        <li><a href="#" style="color: white;">Terms of Service</a></li>
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
                    <a href="#" class="fa fa-facebook fb"></a>
                    <a href="#" class="fa fa-twitter tw"></a>
                    <a href="#" class="fa fa-instagram in"></a>
                    <a href="#" class="fa fa-pinterest pt"></a>
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