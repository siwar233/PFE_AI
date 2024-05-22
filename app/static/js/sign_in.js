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

document.getElementById("sign_in_form").onsubmit = function(){
    return verifmdps();
};

function togglePasswordVisibility() {
    var passwordInput = document.getElementById("Password");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else{
        passwordInput.type = "password"
    }
};

