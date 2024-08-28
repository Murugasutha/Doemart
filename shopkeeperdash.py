#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()

form = cgi.FieldStorage()
ID = form.getvalue("id")
q = """Select * from shopregister where id="%s" """%ID
cur.execute(q)
rec= cur.fetchall()

q1 = """Select count(id) from addproduct where shopid="%s" """%ID
cur.execute(q1)
totalproduct = cur.fetchone()

q2 = """Select count(id) from orders where status="Received" and shopid="%s" """ %ID
cur.execute(q2)
soldproduct = cur.fetchone()

q3 = """Select sum(rate) from orders where status="Received" and shopid="%s" """ %ID
cur.execute(q3)
amount = cur.fetchone()

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

    .card--container{
        background: #fff;
        padding: 2rem;
        border-radius: 10px;
        justify-content: space-evenly;
    }

    .card--wrapper{
        display: flex;
        flex-wrap: wrap;
        gap: 1rem;
    }

    .main--title{
        color: #003f5c;
        padding-bottom: 10px;
        font-size: 17px;
        font-weight: 500;
    }

    .product--card{
        background: rgb(229,223,223);
        border-radius: 10px;
        padding: 1.2rem;
        width: 290px;
        height: 150px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        transition: all 0.5s ease-in-out;
    }

    .product--card:hover{
        transform: translateY(-5px);
    }

    .card--header{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .count{
        display: flex;
        flex-direction: column;
    }

    .title{
        font-size: 13px;
        font-weight: 200;
    }

    .count-value{
        font-size: 30px;
        background-color: #ebe9e9;
        
    }

    .icon{
        color: #fff;
        padding: 1.2rem;
        height: 50px;
        width: 50px;
        text-align: center;
        border-radius: 50%;
        font-size: 2.3rem;
        background: red;
    }

    .dark-green{
        background-color: darkgreen;
    }

    .dark-purple{
        background-color: purple;
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
                <li class="active">
                    <a href="shopkeeperdash.py?id=%s">
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
for i in rec:
    fn = "dbmedia/" + i[16]
    name= i[1]
    print("""
    <div class="main--content">
        <div class="header--wrapper">
            <div class="header--title">
                <span>Dashboard</span>
                <h2 class="text-capitalize">Welcome %s</h2>
            </div>
            <div class="user--info">
                <a href="shopprofile.py?id=%s"><img src="%s" alt="admin"></a>
            </div>
        </div>
        """%(name,ID,fn))
print("""
        <div class="card--container">
            <h3 class="main--title">Today's data</h3>
            <div class="card--wrapper">
                <div class="product--card">
                    <div class="card--header">
                        <div class="count">
                            <span class="title">TOTAL PRODUCT</span>
                        </div>
                        <i class="fas fa-tags icon"></i>
                    </div>
                    <span class="count-value">%s</span>
                </div>

                <div class="product--card">
                    <div class="card--header">
                        <div class="count">
                            <span class="title">NO. OF PRODUCT SOLD</span>
                        </div>
                        <i class="fas fa-coins icon dark-green"></i>
                    </div>
                    <span class="count-value">%s</span>
                </div>

                <div class="product--card">
                    <div class="card--header">
                        <div class="count">
                            <span class="title">TRANSACTIONS</span>
                        </div>
                        <i class="fas fa-comment-dollar icon dark-purple"></i>
                    </div>
                    <span class="count-value"><I class="fas fa-rupee-sign"></I> %s</span>
                </div>
                """ %(totalproduct[0],soldproduct[0],amount[0]))
print("""
            </div>
        </div>
    </div>

    
</body>
</html>
""")