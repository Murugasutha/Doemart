#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql,os
cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
form = cgi.FieldStorage()
ID = form.getvalue("id")
proimage = form.getvalue("proimage")
q = """Select * from shopregister where id='%s' """ %ID
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
    
    .img--container{
        background-color: white;
        border-radius: 25px;
        height: 350px;
        
    }
    .img--container button{
        width: 150px;
    }

    .form--container{
        background-color: white;
        border-radius: 25px;
        height: 400px;
    }

    .form--container table{
       border-radius: 25px;
    }
    .form--container table th{
        border: hidden;
    }

    .form--container table td{
        border: hidden;
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
                    <a href="home.py" class="logout" >
                        <i class="fas fa-sign-out-alt"></i>
                        <span>Log out</span>
                    </a>
                </li>
            </ul>
        </div>
    </div>
"""%(ID,ID,ID,ID,ID,ID,ID,))
for i in rec:
    name= i[1]
    print("""
    <div class="main--content">
        <div class="header--wrapper">
            <div class="header--title">
                <span>Dashboard</span>
                <h2>Welcome %s</h2>
            </div>
        </div>
    """%(name))
for i in rec:
    print("""
        <div class="tabular--wrapper">
            <h3 class="main--title">
                Profile
            </h3>
               <div class="row text-center">
                    <div class="col-md-2"></div>
                    <div class="col-md-3 mt-4" >
                        <div class="img--container">
                            <form method="post" enctype="multipart/form-data">
                                <input type="text" name="fname" value='%s' readonly class="text-capitalize form-control text-center mt-4"><br><br>
                            </form>
                                <img src='./dbmedia/%s' name="profile" alt="profile" class="rounded-circle" style="max-height: 200px;" style="border-radius:50px;">
                        </div>
                    </div>
                    <div class="col-md-5 mt-4">
                        <div class="form--container">
                            <form  method="post" enctype="multipart/form-data">
                                <table class="table add">
                                    <tr>
                                        <th>Shop Name </th>
                                        <td><input type="text" name="efname" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Owner Name</th>
                                        <td><input type="text" name="elname" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Address</th>
                                        <td><textarea class="form-control" name="eadd"  id="eadd" cols="30" rows="5">%s</textarea></td>
                                    </tr>
                                    <tr>
                                        <th>Mobile Number</th>
                                        <td>
                                        <input type="number" name="ephno" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Update profile</th>
                                        <td><input type="file" name="propic"  class="form-control"><br></td>
                                    </tr>
                                </table>
                                <center><input type="submit" name="update" value="Update" class="btn btn-md btn-primary"></center>
                            </form>
        """%(i[1],i[16],i[1],i[2],i[10],i[8]))
print("""
                        </div>
                    </div>
                </div>
            </div>
         </div>
    </body>
</html>
""")

update = form.getvalue("update")


if update != None:
    if len(form)!=0:
        fname = form.getvalue("efname")
        lname = form.getvalue("elname")
        address = form.getvalue("eadd")
        phno = form.getvalue("ephno")
        profile = form['propic']
        if profile.filename:
            fn = os.path.basename(profile.filename)
            open("dbmedia/" + fn, "wb").write(profile.file.read())
            q = """Update shopregister set shopname='%s', ownername='%s', address='%s',shopimg='%s', phno='%s' where id='%s' """ %(fname,lname,address,fn,phno,ID)
            cur.execute(q)
            con.commit()
            print("""
                <script>
                    alert("Updated Successfully!!");
                </script>    
            """)

