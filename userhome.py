#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
q = """Select* from useregister where id="%s" """ %(ID)
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
     <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/owl.carousel.min.js" integrity="sha512-bPs7Ae6pVvhOSiIcyUClR7/q2OAsRiovw4vAkX+zJbw3ShAeeqezq50RIIcIURq7Oa20rW2n2q+fyXBNcU9lrw==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.min.css">
    <link rel="stylesheet" href="userhome.css"> 
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="./home.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.carousel.min.css" integrity="sha512-tS3S5qG0BlhnQROyJXvNjeEM4UpMXHrQfTGmbQ1gKmelCxlSEBUaxhRBj/EFTzpbP4RVSrpEikbmdJobCvhE3g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/OwlCarousel2/2.3.4/assets/owl.theme.default.min.css" integrity="sha512-sMXtMNL1zRzolHYKEujM2AqCLUR9F2C4/05cdbxjjLSRvMQIciEPCQZo++nk7go3BtSuK9kfa/s+a4f4i5pLkw==" crossorigin="anonymous" referrerpolicy="no-referrer" />

</head>
<style>
    .offcanvas{
        max-width: 270px;
        width:100%;
        background-color: rgb(41, 37, 37);;
        color: #fff;
    }
    .offcanvas-body{
        /* position: sticky;
        top: 5px;
        bottom: 0;
        width: 200px;
        height: 100vh; */
        /* padding: 0 1.7rem; */
        color: #fff;
        overflow-y: auto;
        scrollbar-color: grey rgb(41, 37, 37);
        transition: all 0.5s linear;
        /* background-color: rgba(113, 99, 186, 255); */
        background-color: rgb(41, 37, 37);
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


    /* .menu li:hover{
        background: #e0e0e058;
        border-radius: 50px;
    } */
    .menu a{
        color: white;
        font-size: 14px;
        text-decoration: none;
        display: flex;
        align-items: center;
        gap: 1.5rem;
    }

    .menu a span{
        overflow: hidden;
    }

    .menu a i{
        font-size: 1.5rem;
    }
    .navbar{
        position: relative;
    }
    .nav-item {
        position: absolute;
        right: 70px;
        top: 4px;

    }
    .nav-link a{
        color: #fff;
    }

    .nav-link:hover{
        color: #fff;
    }

    /* .main--content{
        position: relative;
        width: 100%;
        display: flex;
    } */
    
    .cinner{
        height: 450px;
   }
   .cimg{
        height: 100%;
        object-fit:cover;
        filter: brightness(0.5);
   }
   /* .card--container{
        display: flex;
        flex-wrap: wrap;
   } */

   .card--container .row a{
        text-decoration: none;
        color: black;
    }
    .owl--container{
        background-color: #e0e0e058;
        height: 260px;
        border-radius: 25px;
        padding: 1rem;
    }

    footer {
        background-color: black;
        padding: 20px;
        color: white;
    }
    footer a{
        text-decoration: none;
    }

    footer .container .a{
        color: white;
    }
    .fb,.tw,.in,.pt{
        color: black;
        background: white;
        padding: 5px;
        font-size: 25px;
        border-radius: 50px;
    }
    .fa:hover{
        opacity: 0.7;
        text-decoration: none;
    }

</style>
""")
print("""
<body>
   
    <!-- Offcanvas Sidebar -->
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
                                        <a href="./homeappliance.py?id=%s" class="fs-5" >Home Appliances
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
                                Offers </i></a>
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
  """ %(ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID,ID))
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
        <div class="main--content"> 
            <div class="row">
                <div class="col-md-12">
                    <div id="demo1" class="carousel slide" data-bs-ride="carousel">
        
                        <!-- Indicators/dots -->
                        <div class="carousel-indicators">
                        <button type="button" data-bs-target="#demo1" data-bs-slide-to="0" class="active"></button>
                        <button type="button" data-bs-target="#demo1" data-bs-slide-to="1"></button>
                        <button type="button" data-bs-target="#demo1" data-bs-slide-to="2"></button>
                        <button type="button" data-bs-target="#demo1" data-bs-slide-to="3"></button>
                        <button type="button" data-bs-target="#demo1" data-bs-slide-to="4"></button>
                        <button type="button" data-bs-target="#demo1" data-bs-slide-to="5"></button>
                            
                        </div>
                    
                        <!-- The slideshow/carousel -->
                        <div class="carousel-inner cinner">
                        <div class="carousel-item active">
                            <img src="./assets/enthusiastic-woman-long-dress-posing-one-leg-cloakroom.jpg" alt="Los Angeles" class="d-block w-100 cimg">
                            <div class="carousel-caption top-0 mt-4 ">
                                <h5  class="mt-5 display-1 fw-bolder text-capitalize">Tops & Tees</h5>
                                <p class="fs-3 text-uppercase">Under <i class="fas fa-rupee-sign"></i>499</p>
                                <button type="button" class="btn btn-dark px-4 py-2 fs-5 mt-2">View Collections</button>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="./assets/boyred.jpg" alt="Chicago" class="d-block w-100 cimg">
                            <div class="carousel-caption top-0 mt-4 ">
                                <h5  class="mt-5 display-1 fw-bolder text-capitalize">Western Wears</h5>
                                <p class="fs-3 text-uppercase">Min 50% offer</p>
                                <button type="button" class="btn btn-dark px-4 py-2 fs-5 mt-2">Shop Now</button>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="./assets/makeupcover.jpg" alt="New York" class="d-block w-100 cimg" >
                            <div class="carousel-caption top-0 mt-4 ">
                                <h5  class="mt-5 display-1 fw-bolder text-capitalize">New Launch</h5>
                                <p class="fs-3 text-uppercase">Flat 20% offer</p>
                                <button type="button" class="btn btn-dark px-4 py-2 fs-5 mt-2">View Collections</button>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="./assets/redelectronic.jpg" alt="New York" class="d-block w-100 cimg" >
                            <div class="carousel-caption top-0 mt-4 ">
                                <h5  class="mt-5 display-1 fw-bolder text-capitalize">Smart Electronics</h5>
                                <p class="fs-3 text-uppercase">30%-60% offer</p>
                                <button type="button" class="btn btn-dark px-4 py-2 fs-5 mt-2">View Collections</button>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="./assets/redshoes.jpg" alt="New York" class="d-block w-100 cimg" >
                            <div class="carousel-caption top-0 mt-4">
                                <h5  class="mt-5 display-1 fw-bolder text-capitalize">Active Wear</h5>
                                <p class="fs-3 text-uppercase">40%-70% offer</p>
                                <button type="button" class="btn btn-dark px-4 py-2 fs-5 mt-2">View Collections</button>
                            </div>
                        </div>
                        <div class="carousel-item">
                            <img src="./assets/supermarket-banner-with-food (1).jpg" alt="New York" class="d-block w-100 cimg" >
                            <div class="carousel-caption top-0 mt-4 ">
                                <h5  class="mt-5 display-1 fw-bolder text-capitalize">Starting <i class="fas fa-rupee-sign"></i>149</h5>
                                <p class="fs-3 text-uppercase">Daily needs</p>
                                <button type="button" class="btn btn-dark px-4 py-2 fs-5 mt-2">View Collections</button>
                            </div>
                        </div>
                        </div>
                    
                        <!-- Left and right controls/icons -->
                        <button class="carousel-control-prev" type="button" data-bs-target="#demo1" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon"></span>
                        </button>
                        <button class="carousel-control-next" type="button" data-bs-target="#demo1" data-bs-slide="next">
                        <span class="carousel-control-next-icon"></span>
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </div><br><br>
""")
print("""
    <div class="container-fluid">
        <div class="card--container">
            <div class="row">
                <div class="col-md-2">
                    <a href="./homeappliance.py?id=%s">
                        <center><img src="./assets/homecat.jpg" alt="Home Appliances" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Home Appliances</h5>
                        
                    </a>
                </div>
                <div class="col-md-2">
                    <a href="./fashion.py?id=%s">
                        <center><img src="./assets/womencat.avif" alt="Fashion" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Fashion</h5>
                    </a>
                </div>
                <div class="col-md-2">
                    <a href="./makeup.py?id=%s">
                        <center><img src="./assets/makeupcat.avif" alt="makeup" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Makeup Products</h5>
                    </a>
                </div>
                <div class="col-md-2">
                    <a href="/accessories.py?id=%s">
                        <center><img src="./assets/acesscat.jpg" alt="accessories" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Accessories</h5>
                    </a>
                </div>
                <div class="col-md-2">
                    <a href="./grocery.py?id=%s">
                        <center><img src="./assets/groerycat.jpg" alt="groceries" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Groceries</h5>
                    </a>
                </div>
                <div class="col-md-2">
                    <a href="./footwear.py?id=%s">
                        <center><img src="./assets/footwearwhite.jpg" alt="footwear" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Footwear</h5>
                    </a>
                </div>
            </div><br>
            <div class="row">
                <div class="col-md-3"></div>
                <div class="col-md-2">
                    <a href="./electronics.py?id=%s">
                        <center><img src="./assets/eleccat.jpg" alt="electronics" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Electronics</h5>
                    </a>
                </div>
                <div class="col-md-2">
                    <a href="./stationary.py?id=%s">
                        <center><img src="./assets/stationarycat.jpg" alt="stationary" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center">Stationary</h5>
                    </a>
                </div>
                <div class="col-md-2">
                    <a href="./gifts.py?id=%s">
                        <center><img src="./assets/toyscat.avif" alt="gifts&toys" class="rounded-circle " width="150px" height="150px"></center>
                        <h5 class="text-center ">Gifts & Toys</h5>
                    </a>
                </div>
            </div>
        </div>
    </div><br><br>

"""%(ID,ID,ID,ID,ID,ID,ID,ID,ID))
import owl
print(owl)
print("""
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