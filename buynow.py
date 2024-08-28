#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
USERID = form.getvalue("userid")
SID = form.getvalue("shopid")
q1 = """Select* from useregister where id="%s" """%(USERID)
cur.execute(q1)
recc = cur.fetchall()
q = """Select* from addproduct where id="%s" """%(ID)
cur.execute(q)
rec = cur.fetchall()
q2 = """Select * from shopregister where id="%s" """%SID
cur.execute(q2)
shop = cur.fetchall()

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
<style>
    .text--container{
        color: gray;
    }
    .color{
        background-color: #fffefede;
        /* border: solid black 6px; */
        border-radius: 25px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
    }
    .text{
        color: black;
    }
    .info--container a{
        text-decoration: none;
    }
    .fs{
        font-size: 12px;
    }
</style>

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
                            <a href="#" class="fs-5">
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
    """%(USERID,USERID,USERID,USERID,USERID,USERID,USERID,USERID,USERID,USERID,USERID,USERID))
print("""
  <header>
    <nav class="navbar navbar-expand-sm  bg-dark navbar-dark mynav">
        <div class="container-fluid">
            <button class="btn navbar-brand" type="button" data-bs-toggle="offcanvas" data-bs-target="#demo">
                <i class="fas fa-bars"></i>
              </button>
          <a class="navbar-brand justify-content-center" href="./userhome.py?userid=%s">DoEmart</a>
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
""" %(USERID))
for i in shop:
    fn = "dbmedia/" + i[16]
    print("""
        <div class="container mt-2">
        <div class="row  text-capitalize color">
                <div class="col-lg-3"></div>
                <div class="col-lg-2">
                    <div class="image--container mt-3">
                        <img src="%s" alt="shopimg" class="img-fluid " style="max-width: 120px;">
                    </div>
                </div>
                <div class="col-lg-6">
                    <div class="text--container mt-2">
                        <h4 class="text-capitalize" style="color: rgb(99, 92, 92);">%s</h4>
                        <p class="mt-2 fs"><i class="fa fa-address-card" aria-hidden="true"></i> %s</p>
                        <p class="fs"><i class="fa fa-phone" aria-hidden="true"></i> %s</p>
                        <p class="fs"><i class="fa fa-calendar" aria-hidden="true"></i> Established since:  %s</p>
                    </div>
                </div>
            </div> 
      </div>
    """ %(fn,i[1],i[10],i[8],i[5]))
for i in rec:
    fn = "product/"+i[7]
    price = i[6]
    print("""
        <div class="container-fluid mt-3">
            <div class="row bg-light text-center">
                <div class="col-md-5">
                    <img class="dress-card-img-top img-fluid" style=" max-height: 400px;" src="%s" alt="img">
                </div>
                <div class="col-md-7 text-capitalize text-center" style="margin-top:25px;padding-left: 60px;">
                    <h4 class="dress-card-title mt-5">%s</h4>
                    <p class="dress-card-para">%s</p>
                    <form method="post" enctype="multipart/form-data" name="order" id="login">
                            <div class="form-group mt-4">
                                <p class="dress-card-para"><span class="dress-card-price">Rs %s</span></p>
                            </div>
                            <div class="form-group">
                                <input type="button" class="btn btn-success" data-bs-toggle="modal" data-bs-target="#myModal-%s" name="placeorder" value="Place Order">
                            </div>
                        </form>
        """%(fn,i[2],i[3],i[6],i[0]))
    print("""
                    <!-- place order -->
                    <div class="modal" id="myModal-%s">
                        <div class="modal-dialog">
                          <div class="modal-content">
                      
                            <!-- Modal Header -->
                            <div class="modal-header">
                              <h4 class="modal-title">Place Order</h4>
                              <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                            </div>
                      
                            <!-- Modal body -->
                            <div class="modal-body">
                                <form action="" method="post" enctype="multipart/form-data">
                                    <table class="table add">
                                        <tr>
                                            <th>Product Id</th>
                                            <td><input type="text" name="proid" value ="%s" class="form-control" readonly></td>
                                        </tr>
                                        <input type="hidden" name="proimg" value="%s" >
                                        <tr>
                                            <th>Product Name</th>
                                            <td><input type="text" name="proname" value ="%s" class="form-control" readonly></td>
                                        </tr>
                                        <tr>
                                            <th>Size</th>
                                            <td><select name="size"  class="form-control">
                                                <option value="select" selected disabled>Select</option>
                                                <option value="s">S</option>
                                                <option value="m">M</option>
                                                <option value="l">L</option>
                                                <option value="xl">XL</option>
                                                <option value="xxl">XXL</option>
                                                <option value="xxxl">XXXL</option>
                                             </select></td>
                                        </tr>
                                        <tr>
                                            <th>Quantity</th>
                                            <td><select name="quantity" id="quantity%s" onchange="update%s()" class="form-control">
                                                    <option value="select" selected disabled>select</option>
                                                    <option value="1">1</option>
                                                    <option value="2">2</option>
                                                    <option value="3">3</option>
                                                    <option value="4">4</option>
                                                </select>
                                            </td>
                                        </tr>
                                        <tr>
                                            <th>Price</th>
                                            <td><input type="number" id="price%s" name="price" value="%s"  class="form-control" readonly></td>
                                        </tr>
                                        <tr>
                                            <th>Total Price</th>
                                            <td><input type="text" id="totalPrice%s" name="totalprice" class="form-control" readonly></td>
                                        </tr>
                                        <tr>
                                            <th>Payment method</th>
                                            <td><input type="radio" name="pay" id="radio1" class="form-check-input" value="credit or debit card"  checked>Credit or Debit card<label class="form-check-label" for="radio1"></label></td>
                                        </tr>
                                        <tr>
                                            <th>Enter card number</th>
                                            <td><input type="number" name="card" class="form-control"></td>
                                        </tr>
                                        <tr>
                                            <th>Expiry Date</th>
                                            <td><input type="date" name="edate" class="form-control"></td>
                                            
                                        </tr>
                                    </table>
                                    <center><input type="submit" name="order1" value="Place Order" class="btn btn-md btn-primary"></center>
                                </form>
                            </div>
                      
                          </div>
                        </div>
                    </div>
                <script>
                        function update%s() {
                            var quantity = document.getElementById('quantity%s').value;
                            var price = document.getElementById('price%s').value;
                            var totalPricee = quantity*price;
                            
                             document.getElementById('totalPrice%s').value = totalPricee;
                        }
                </script>
             """ %(i[0],i[1],fn,i[2],i[0],i[0],i[0],i[6],i[0],i[0],i[0],i[0],i[0]))
print("""
                   </div>
                </div>""")
for i in shop:
    print("""
            <div class="row mt-4">
                <div class="col-lg-1"></div>
                <div class="col-md-6 bg-light">
                    <h5 class="text-capitalize">Buisness Details:</h5>
                    <p>%s</p>
                </div>
                <div class="col-md-1"></div>
                <div class="col-md-2 text-center  ">
                    <div class="info--container bg-light">
                        <h5 class="text--container text text-capitalize"><i class="fa fa-user"></i> contact person</h5>
                        <a href="#" class="card text-capitalize" data-bs-toggle="collapse" data-bs-target="#info"><h6> %s <i class="fa fa-caret-down"></i></h5></a>
                        <div class="collapse" id="info">
                            <div class="card card-body">
                                <p class="f"><i class="fa fa-envelope" aria-hidden="true"></i> <span style="font-size:13px;">%s</span></p>
                                <p><i class="fa fa-phone" aria-hidden="true"></i> <span>%s</span></p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div><br><br>
    """ %(i[18],i[2],i[6],i[8]))
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
import os
order1 = form.getvalue("order1")
order2 = form.getvalue("order2")


if order1 != None:
    if len(form) != 0:
        proname = form.getvalue("proname")
        proid = form.getvalue("proid")
        quan = form.getvalue("quantity")
        size = form.getvalue("size")
        prize = form.getvalue("totalprice")
        card = form.getvalue("pay")
        cardno = form.getvalue("card")
        exdate = form.getvalue("edate")
        proimg = form['proimg']
        if proimg.filename:
            fn = os.path.basename(proimg.filename)
            open("product/"+fn,"wb").write(proimg.file.read())
            q = """INSERT INTO orders(proid, proname, quan, size, rate, card, cardno, exdate,userid,shopid,proimg) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(proid,proname,quan,size,prize,card,cardno,exdate,USERID,SID,fn)
            cur.execute(q)
            con.commit()
            print("""
                <script>
                    alert("Your order placed");
                </script>
            """)

if order2 != None:
    if len(form) != 0:
        proname = form.getvalue("proname")
        proid = form.getvalue("proid")
        quan = form.getvalue("quantity")
        size = form.getvalue("size")
        prize = form.getvalue("totalprice")
        card = form.getvalue("pay")
        cardno = form.getvalue("card")
        exdate = form.getvalue("edate")
        proimg = form['proimg']
        if proimg.filename:
            fn = os.path.basename(proimg.filename)
            open("product/"+fn,"wb").write(proimg.file.read())
            q = """INSERT INTO orders(proid, proname, quan, size, rate, card, cardno, exdate,userid,shopid,proimg) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(proid,proname,quan,size,prize,card,cardno,exdate,USERID,SID,fn)
            cur.execute(q)
            con.commit()
            print("""
                <script>
                    alert("Your order placed");
                </script>
            """)