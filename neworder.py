#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql,os
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
q = """SELECT orders.id,useregister.firstname,useregister.lastname,useregister.address ,useregister.phno,orders.proname,orders.quan,orders.size,orders.rate,orders.card,orders.cardno,orders.exdate,orders.status,orders.shopid FROM orders INNER JOIN useregister ON orders.userid = useregister.id where orders.shopid="%s" """%ID
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
    th{
        text-align: center;
        background: #FCF6F5;
    }
    #addproduct table th {
        text-align: left;
        border: hidden;
        background: white;
    }
    #addproduct table td{
        border: hidden;
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
                            <a href="./addproduct.py?id=%s" ><i class="fas fa-cart-plus"></i>  
                                <span>New</span></a>
                        </li>
                        <li>
                            <a href="./exproduct.py?id=%s">
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
                            <a href="./neworder.py?id=%s">
                                <i class="fas fa-cart-plus"></i>  
                                <span>New</span>
                            </a>
                        </li>
                        <li>
                            <a href="./exorders.py?id=%s">
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
                            <a href="./newoffer.py?id=%s">
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
                    <a href="home.py" class="logout" >
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
    """ % (ID))
print("""
        <div class="main--container">
            <div class="main--title">
                <div class="col-md-10">
                    <h3>New Orders</h3>
                </div>
            </div>
            
            <div class="table--wrapper">
                <div class="table--container">
                    <div class="col-md-12">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th>Order Id</th>
                                    <th>Name</th>
                                    <th>Address</th>
                                    <th>Phone number</th>
                                    <th>Product name</th>
                                    <th>Quantity</th>
                                    <th>Size</th>
                                    <th>Price</th>
                                    <th>Payment Method</th>
                                    <th>Card Number</th>
                                    <th>Expiry Date</th>
                                    <th colspan=2>Action</th>
                                </tr>
                            </thead>
""")
for i in rec:
    if i[12] != "Confirm" and i[12] != "Cancel":
        print("""
         
                               <tbody>
                                <tr>
                                <form method="post">
                                    <td>%s</td>
                                    <td>%s %s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <td>%s</td>
                                    <input type="hidden" name="orderid" value="%s">
                                    <td><input type="submit" name="confirm" class="btn btn-success" value="Confirm"></td>
                                    <td><input type="submit" name="delete" class="btn btn-danger" value="Cancel"></td>
                                </form>
    """ % (i[0],i[1],i[2],i[3], i[4], i[5], i[6],i[7],i[8],i[9],i[10],i[11],i[0]))

print("""
                                
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    
</body>
</html>
""")

confirm = form.getvalue("confirm")
delete = form.getvalue("delete")
orderid = form.getvalue("orderid")

if orderid != None:
    if confirm != None:
        q = """Update orders set status = "%s" where id="%s" """ % (confirm, orderid)
        cur.execute(q)
        con.commit()
        print("""
        <script>
            alert("Order has confirmed");
        </script>
        """)

    if delete != None:
        q = """Update orders set status = "%s" where id="%s" """ %(delete,orderid)
        cur.execute(q)
        con.commit()
        print("""
            <script>
                alert("Request denied");
            </script>
            """)