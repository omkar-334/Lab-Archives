function validateRegister() {
    var username = document.getElementById("username").value;
    usernameRegex = /^[a-zA-Z0-9_]{8,}$/

    var password = document.getElementById("password").value;
    passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,}$/;

    var phone = document.getElementById("phone").value;
    phoneRegex = /^[6-9][0-9]{9}$/

    var email = document.getElementById("email").value;
    emailRegex = /^[a-zA-Z0-9]{1,64}@[a-z]{1,64}\.[a-z.]{2,}/

    var age = document.getElementById("age").value;

    if (username == "") {
        alert("Username cannot be empty.");
        return false;}
    if (!(username.match(usernameRegex))) {
        alert("Username must be of atleast 8 characters and can only contain letter, numbers or underscores.");
        return false}
    
    if (password == "") {
        alert("Password cannot be empty.");
        return false;}
    if (!(password.match(passwordRegex))) {
        alert("Password must be of atleast 8 characters and must contain 1 lowercase letter, 1 uppercase letter, 1 number and 1 special character.");
        return false;}
    
    if (email == "") {
        alert("Email cannot be empty.");
        return false;}
    if (!(email.match(emailRegex))) {
        alert("Invalid Email Format.");
        return false;}

    if (phone == "") {
        alert("Phone number cannot be empty.");
        return false;}
    if (!(phone.match(phoneRegex))) {
        alert("Phone number should contain 10 digits (without country code).");
        return false;}

    if (age == "") {
        alert("Age cannot be empty.");
        return false;}
    if (age <18) {
        alert("Age must atleast be 18.");
        return false;}

    return true;
}
function validateLogin() {
    var username = document.getElementById("username").value;
    usernameRegex = /^[a-zA-Z0-9_]{8,}$/

    var password = document.getElementById("password").value;
    passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,}$/;

    if (username == "") {
        alert("Username cannot be empty.");
        return false;}
    if (!(username.match(usernameRegex))) {
        alert("Username must be of atleast 8 characters and can only contain letter, numbers or underscores.");
        return false}
    
    if (password == "") {
        alert("Password cannot be empty.");
        return false;}
    if (!(password.match(passwordRegex))) {
        alert("Password must be of atleast 8 characters and must contain 1 lowercase letter, 1 uppercase letter, 1 number and 1 special character.");
        return false;}
    return true;
}