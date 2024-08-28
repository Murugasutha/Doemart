function admin(){
    user = document.forms["admin-login"]["user"].value
    pass = document.forms["admin-login"]["pass"].value

    if(user == " "){
            user.focus();
            alert("Username is empty");
            return false;
        }
        else if(pass == " "){
            pass.focus();
            alert("Password is empty");
            return false;
        }
        else if(user == "admin" && pass == "@dmin123"){
            alert("Login success");
            return true;
        }
        else{
            alert("Username or password is incorrect!!");
            return false;
        }
}

function shopvalidate(){
    email = document.forms["shoplogin"]["shopemail"];
    password = document.forms["shoplogin"]["shoppassw"];

    if(email.value == " "){
        username.focus();
        alert("Username is empty");
        return false;
    }
    else if(password.value == " "){
        password.focus();
        alert("Password is empty");
        return false;
    }
    else if(email.value == "sutha@gmail.com" && password.value == "12345678"){
        alert("Login success");
        return true;
    }
    else{
        alert("Email or Password is incorrect!!");
        return false;
    }
}

function uservalidate(){
    email = document.forms["userlogin"]["useremail"];
    password = document.forms["userlogin"]["userpassw"];

    if(email.value == " "){
        username.focus();
        alert("Username is empty");
        return false;
    }
    else if(password.value == " "){
        password.focus();
        alert("Password is empty");
        return false;
    }
    else{
        alert("Email or Password is incorrect!!");
        return false;
    }
}

function forgot(){
        username = document.forms["ret"]["user"];
        password = document.forms["ret"]["pswd"];
        cpassword = document.forms["ret"]["cpswd"]

        if(username.value == ""){
            username.focus();
            alert("Username is empty");
            return false;
        }
        else if(password.value == ""){
            password.focus();
            alert("Password is empty");
            return false;
        }
        else if(cpassword.value == ""){
            cpassword.focus();
            alert("Confirm Password is empty");
            return false;
        }
        else if(password.value == cpassword.value){
            alert("Password reset Successfully ");
            return true;
        }
        else{
        alert("Password and confirm password are not same");
        password.focus();
        return false;
        }
    }

    function validation() {
        var sname = document.forms["shopsignup"]["sname"].value;
        var oname = document.forms["shopsignup"]["oname"].value;
        var gender = document.querySelector('input[name="gender"]:checked');
        var age = document.forms["shopsignup"]["age"].value;
        var year = document.forms["shopsignup"]["year"].value;
        var phno = document.forms["shopsignup"]["phno"].value;
        var wappno = document.forms["shopsignup"]["wappno"].value;
        var door = document.forms["shopsignup"]["door"].value;
        var street = document.forms["shopsignup"]["street"].value;
        var district = document.forms["shopsignup"]["district"].value;
        var pin = document.forms["shopsignup"]["pin"].value;
        var city = document.forms["shopsignup"]["city"].value;
        var state = document.forms["shopsignup"]["state"].value;
        var country = document.forms["shopsignup"]["country"].value;
        var email = document.forms["shopsignup"]["email"].value;

        if (sname == "" || oname == "" || !gender || age == "" || year == "" || phno == "" || wappno == "" ||
            door == "" || street == "" || district == "" || pin == "" || city == "" || state == "" || country == "" || email == "") {
            alert("Please fill in all required fields.");
            return false;
        }
        else{
            alert("Registration Successfull")
            return true;
        }

    }
    function usersign() {
        var fname = document.forms["usersignup"]["fname"].value;
        var lname = document.forms["usersignup"]["lname"].value;
        var gender = document.querySelector('input[name="ugender"]:checked');
        var phno = document.forms["usersignup"]["uphno"].value;
        var wappno = document.forms["usersignup"]["uwappno"].value;
        var door = document.forms["usersignup"]["udoor"].value;
        var street = document.forms["usersignup"]["ustreet"].value;
        var district = document.forms["usersignup"]["udistrict"].value;
        var pin = document.forms["usersignup"]["upin"].value;
        var city = document.forms["usersignup"]["ucity"].value;
        var state = document.forms["usersignup"]["ustate"].value;
        var email = document.forms["usersignup"]["uemail"].value;

        if (fname == "" || lname == "" || !gender || phno == "" || wappno == "" ||
            door == "" || street == "" || district == "" || pin == "" || city == "" || state == "" || email == "" ) {
            alert("Please fill in all required fields.");
            return false;
        }

        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email)) {
            alert("Please enter a valid email address.");
            return false;
        }

        if (pass.length < 8) {
            alert("Password must be at least 6 characters long.");
            return false;
        }

        return true;
    }