#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")

import cgi,cgitb,pymysql
con = pymysql.connect(host="localhost", user="root", password="", database="doemart")
cur = con.cursor()
q = """Select* from shopregister where status = "approve" """
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
    .menu .dash{
        font-size: 20px;
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
                        <img src="./assets/reddlogo.webp" alt="logo" width="35px" height="35px">
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
                    <a href="#" data-toggle="collapse" data-target="#shopmenu" class="active">
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
                    <a href="#" data-toggle="collapse" data-target="#usermenu">
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
                <img src="./assets/adminbluelogo.webp" alt="admin">
            </div>
        </div>
        
        <div class="tabular--wrapper">
            <h3 class="main--title">
                Shop details
            </h3>
            <div class="table-container table-responsive">
                <table class="table">
                    <thead>
                        <tr>
                            <th>Shop Name</th>
                            <th>Owner Name</th>
                            <th>Gender</th>
                            <th>Address</th>
                            <th>Established since</th>
                            <th>Mobile number</th>
                            <th>Email Id</th>
                            <th>Password</th>
                            <th>Owner photo</th>
                            <th>Shop License</th>
                            <th>Address Proof</th>
                            <th>Shop Image</th>
                            <th>Edit/Remove</th>
                        </tr>
                    </thead>
""")
for i in rec:
    fn1 = "dbmedia/"+i[13]
    fn2 = "dbmedia/"+i[15]
    fn3 = "dbmedia/"+i[15]
    fn4 = "dbmedia/"+i[16]
    print("""
                        <tbody>
                         <form method="post" enctype="multipart/form-data">
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
                                        <a href=""  data-toggle="modal" data-target="#owner-%s"><span class="glyphicon glyphicon-picture"><span></a>                                    
                                        <!-- Modal -->
                                        <div class="modal fade" id="owner-%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
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
                                    <td><a href=""  data-toggle="modal" data-target="#license-%s"><span class="glyphicon glyphicon-picture"><span></a>
                                    
                                        <!-- Modal -->
                                        <div class="modal fade" id="license-%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
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
                                    <td><a href=""  data-toggle="modal" data-target="#address-%s"><span class="glyphicon glyphicon-picture"><span></a>
                                    
                                        <!-- Modal -->
                                        <div class="modal fade" id="address-%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
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
                                                    <div class="modal-footer">
                                                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                    <td>
                                        <a href=""  data-toggle="modal" data-target="#shopimg-%s"><span class="glyphicon glyphicon-picture"><span></a>
                                        <!-- Modal -->
                                        <div class="modal fade" id="shopimg-%s" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
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
                                        <div class="btn-grp">
                                            <input type="hidden" name="id" value="%s">
                                            <button type="button" name="edit" class="btn btn-primary" data-toggle="modal" data-target="#edits-%s"><i class="far fa-edit"></i></button>                                            
                                            <button name="delete" class="btn btn-danger"><i class="far fa-trash-alt"></i></button>
                                            <button name="update"><i class="fas fa-update"></i></button>
                                        </div>
                                    
    """ %(i[1],i[2],i[3],i[10],i[5],i[8],i[6],i[7],i[0],i[0],fn1,i[0],i[0],fn2,i[0],i[0],fn3,i[0],i[0],fn4,i[0],i[0]))
    print("""
            <!-- Add product -->
            <div class="modal fade" id="edits-%s"  role="dialog">
                <div class="modal-dialog">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal">&times;</button>
                            <h4  class="modal-title">Edit</h4>
                        </div>
                       
                        <div class="modal-body">
                            <form method="post" enctype="multipart/form-data">
                                <table class="table add">
                                    <tr>
                                        <th>Shop Name</th>
                                        <td><input type="text" name="fname" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Owner Name</th>
                                        <td><input type="text" name="lname" value='%s' class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Address</th>
                                        <td><textarea name="address"  cols="30" rows="5" class="form-control" >%s</textarea></td>
                                    </tr>
                                    <tr>
                                        <th>Phone number</th>
                                        <td><input type="number" value="%s" name="phno" class="form-control"></td>
                                    </tr>
                                    <tr>
                                        <th>Owner image</th>
                                        <td><input type="file" name="ownerimg" class="form-control btn btn-default"></td>
                                    </tr>
                                    <tr>
                                        <th>Shop License</th>
                                        <td><input type="file" name="license" class="form-control btn btn-default"></td>
                                    </tr>
                                    <tr>
                                        <th>Address Proof</th>
                                        <td><input type="file" name="addimg" class="form-control btn btn-default"></td>
                                    </tr>
                                    <tr>
                                        <th>Shop Image</th>
                                        <td><input type="file" name="shopimg" class="form-control btn btn-default"></td>
                                    </tr>
                                </table>
                                <center><input type="submit" name="update" value="Update" class="btn btn-md btn-primary"></center>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
                                  </form>
                                    </td>
                                </tr>
    """ %(i[0],i[1],i[2],i[10],i[8]))
print("""
                    </tbody>
                </table>
            </div>
        </div>
  

    
</body>
</html>
""")
import os
form = cgi.FieldStorage()
id = form.getvalue("id")
delete = form.getvalue("delete")
update = form.getvalue("update")
if update != None:
        fname = form.getvalue("fname")
        lname = form.getvalue("lname")
        address = form.getvalue("address")
        phno = form.getvalue("phno")
        ownimg =form['ownerimg']
        shopimg =form['shopimg']
        license =form['license']
        addimg = form['addimg']
        if addimg.filename and ownimg.filename and shopimg.filename and license.filename:
            fn1 = os.path.basename(addimg.filename)
            open("dbmedia/"+fn1,"wb").write(addimg.file.read())
            fn2 = os.path.basename(ownimg.filename)
            open("dbmedia/"+fn2,"wb").write(ownimg.file.read())
            fn3 = os.path.basename(shopimg.filename)
            open("dbmedia/"+fn3,"wb").write(shopimg.file.read())
            fn4 = os.path.basename(license.filename)
            open("dbmedia/"+fn4,"wb").write(license.file.read())
            q = """Update shopregister set shopname="%s", ownername="%s", address="%s", phno="%s", ownerimg="%s", shopimg="%s", license="%s", addproof="%s" where id=%s """ %(fname,lname,address,phno,fn2,fn3,fn4,fn1,id)
            cur.execute(q)
            con.commit()
            print("""
                <script>
                    alert("Updated successfully");
                </script>
            """)

if delete != None:
    q = """Delete from shopregister where id = "%s" """ %(id)
    cur.execute(q)
    con.commit()
    print("""
        <script>
        alert("Deleted successfully");
        </script>
    """)
