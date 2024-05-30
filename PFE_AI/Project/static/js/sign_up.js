function verifmdps(){
    var Password = document.getElementById("Password").value;

    if (Password.length < 8) {
        alert("Password should containe at least 8 characters.");
        return false;
    
    }

    var specialchar = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
    if (!specialchar.test(Password)) {
        alert("Password should containe at least one special character.");
        return false;
    }
return true;
}

document.getElementById("sign_up_form").onsubmit = function(){
    return verifmdps();
};

