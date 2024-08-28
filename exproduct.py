#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
q = """Select * from addproduct where shopid="%s" """%ID
cur.execute(q)
rec = cur.fetchall()

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shopkeeper-Dashboard</title>
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
        overflow-y: auto;
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
    .main--title button{
        display: flex;
        margin-top: 20px;
    }
    .plus{
        font-size: 14px;
        font-weight: 500;
    }
    th,td{
        text-align: center;
    }
    .table--wrapper th{
        padding: 15px;
        text-align: center;
        background: #d6e8ee;
        color: rgba(0, 0, 0, 0.473);
    }
    .table--wrapper tbody{
        background: #f2f2f2;
    }

    .table--wrapper td{
        padding: 15px;
        font-size: 12px;
        color: #333;
        text-align: center;
    }

    .table--wrapper tr:nth-child(even){
        background: #e0e0e058;
    }

</style>
<body>
    <div class="sidebar">
        <div class="logo">
""")
print("""
            <ul class="menu">
                <li>
                    <a href="#" class="dash">
                        <!-- <i class="fa fa-poll"></i> -->
                        <img src="./assets/reddlogo.webp" alt="logo" width="35px" height="35px">
                        <span>DoEmart</span>
                    </a>
                </li>
                <li>
                    <a href="./shopkeeperdash.py?id=%s">
                        <i class="fa fa-home"></i>
                        <span>Home</span>
                    </a>
                </li>
                <li>
                    <a href="#" data-toggle="collapse" data-target="#promenu">
                        <i class="fa fa-tags"></i>
                        <span>Product <span class="caret"></span></span>
                    </a>
                    <ul id="promenu" class="collapse">
                        <li>
                            <a href="addproduct.py?id=%s" ><i class="fas fa-cart-plus"></i>  
                                <span>New</span></a>
                        </li>
                        <li>
                            <a href="exproduct.py?id=%s">
                                <i class="fas fa-cart-arrow-down"></i>  
                            <span>Existing</span>
                            </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#" data-toggle="collapse" data-target="#ordermenu">
                        <i class="fas fa-shopping-cart"></i>
                        <span>Orders <span class="caret"></span></span>
                    </a>
                    <ul id="ordermenu" class="collapse">
                        <li>
                            <a href="neworder.py?id=%s">
                                <i class="fas fa-cart-plus"></i>  
                                <span>New</span>
                            </a>
                        </li>
                        <li>
                            <a href="exorders.py?id=%s">
                                <i class="fas fa-cart-arrow-down"></i>  
                                <span>Existing</span>
                            </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#" data-toggle="collapse" data-target="#offermenu">
                        <i class="fas fa-gift"></i>
                        <span>Offers <span class="caret"></span></span>
                    </a>
                    <ul id="offermenu" class="collapse">
                        <li>
                            <a href="newoffer.py?id=%s">
                                <i class="fas fa-cart-plus"></i>  
                                <span>New</span>
                            </a>
                        </li>
                        <li>
                            <a href="exoffer.py?id=%s">
                                <i class="fas fa-cart-arrow-down"></i>  
                                <span>Existing</span>
                            </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="#" data-toggle="collapse" data-target="#transmenu">
                        <i class="fas fa-dollar-sign"></i>
                        <span>Transaction <span class="caret"></span></span>
                    </a>
                    <ul id="transmenu" class="collapse">
                        <li>
                            <a href="">
                                <i class="fas fa-cart-plus"></i>  
                                <span>New</span>
                            </a>
                        </li>
                        <li>
                            <a href="">
                                <i class="fas fa-cart-arrow-down"></i>  
                                <span>Existing</span>
                            </a>
                        </li>
                    </ul>
                </li>
                <li>
                    <a href="./home.py" class="logout" >
                        <i class="fas fa-sign-out-alt"></i>
                        <span>Log out</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
"""%(ID,ID,ID,ID,ID,ID,ID))
print("""
    <div class="main--content">
        <div class="header--wrapper">
            <div class="header--title">
                <span>Dashboard</span>
                <h2>Welcome Shopkeeper</h2>
            </div>
            <div class="user--info">
                <a href="shopprofile.py?id=%s"><img src="./assets/adminbluelogo.webp" alt="admin"></a>
            </div>
        </div>
"""%(ID))
print("""
        <div class="main--container">
            <div class="main--title">
                    <h3>Product Details</h3>
            </div>

            <div class="table--wrapper">
                <div class="table--container">
                    <div class="col-md-12">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Product Id</th>
                                    <th>Product Name</th>
                                    <th>Description</th>
                                    <th>Category</th>
                                    <th>Quantity</th>
                                    <th>Price</th>
                                    <th>Product Image</th>
                                    <th>Edit/Remove</th>
                                </tr>
                            </thead>
""")

for i in rec:
    fn = "product/" + i[7]
    print("""
                                <tbody>
                                    <tr>
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
                                        <div class="btn-grp">
                                            <input type="hidden" name="id" value="%s">
                                            <button type="button" name="edit" class="btn btn-primary" data-toggle="modal" data-target="#edits-%s"><i class="far fa-edit"></i></button>
                                            <button name="delete" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>
                                            <button name="update"><i class="fas fa-update"></i></button>
                                        </div>
""" %(i[1],i[2],i[3],i[4],i[5],i[6],i[0],i[0],fn,i[0],i[0]))
    print("""
                <!-- Add product -->
                <div class="modal fade" id="edits-%s"  role="dialog">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-header">
                                <button type="button" class="close" data-dismiss="modal">&times;</button>
                                <h4  class="modal-title">Edit Product</h4>
                            </div>

                            <div class="modal-body">
                                <form method="post" enctype="multipart/form-data">
                                    <table class="table add">
                                        <tr>
                                            <th>Product Id</th>
                                            <td><input type="number" value="%s" name="proid" class="form-control"></td>
                                        </tr>
                                        <tr>
                                            <th>Product Name</th>
                                            <td><input type="text" name="proname" value='%s' class="form-control"></td>
                                        </tr>
                                        <tr>
                                            <th>Description</th>
                                            <td><textarea name="des"  cols="30" rows="5" class="form-control" >%s</textarea></td>
                                        </tr>
                                        <tr>
                                        <th>Category</th>
                                        <td><select name="category" id="category" class="form-control">
                                            <option value="%s" selected disabled>%s</option>
                                            <option value="homeaapliances">Home Appliances</option>
                                            <option value="Clothing">Clothing</option>
                                            <option value="Groceries">Groceries</option>
                                            <option value="Footwear">Footwear</option>
                                            <option value="Accessories">Accessories</option>
                                            <option value="Stationary">Stationary</option>
                                            <option value="gifts">Gifts & Toys</option>
                                            <option value="Makeup products">Makeup products</option>
                                            <option value="Electronics">Electronics</option>
                                            <option value="others">Others</option>
                                        </select></td>
                                    </tr>
                                        <tr>
                                            <th>Quantity</th>
                                            <td><input type="number" value="%s" name="quantity" class="form-control"></td>
                                        </tr>
                                        <tr>
                                            <th>Price</th>
                                            <td><input type="number" value="%s" name="price" class="form-control"></td>
                                        </tr>
                                        <tr>
                                            <th>Product image</th>
                                            <td><input type="file" name="proimg" class="form-control btn btn-default"></td>
                                        </tr>
                                    </table>
                                    <input type="hidden" name="idd" value="%s">
                                    <center><input type="submit" name="update" class="btn btn-md btn-primary"></center>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                                      </form>
                                        </td>
                                    </tr>
        """ % (i[0], i[1], i[2], i[3], i[4],i[4],i[5],i[6],i[0]))
print("""
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    
</body>
</html>
""")
import os

idd = form.getvalue("idd")
delete = form.getvalue("delete")
update = form.getvalue("update")

if update != None:
    proid = form.getvalue("proid")
    proname = form.getvalue("proname")
    des = form.getvalue("des")
    category = form.getvalue("category")
    quantity = form.getvalue("quantity")
    price = form.getvalue("price")
    proimg = form['proimg']
    if proimg.filename:
        fn = os.path.basename(proimg.filename)
        open("dbmedia/" + fn, "wb").write(proimg.file.read())
        q = """Update addproduct set productid="%s", productname="%s", description="%s", category="%s", quantity="%s", price="%s", productimg="%s" where id= "%s" """ % (proid,proname,des,category,quantity,price,fn,idd)
        try:
            cur.execute(q)
            con.commit()
            print("""
                        <script>
                            alert("Updated successfully");
                        </script>
                    """)
        except Exception as e:
            print(f"Error updating database: {str(e)}")

if delete != None:
    q = """Delete from addproduct where id = "%s" """ %(idd)
    cur.execute(q)
    con.commit()
    print("""
    <script>
        alert("Deleted successfully");
    </script>
    """)