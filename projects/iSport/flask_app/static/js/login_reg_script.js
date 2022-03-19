console.log ("page loaded")
function loading(params) {
    console.log ("This is WOrking")
    
}
function bring_to_top(params) {
    document.getElementById("reg_wrapper").style.zIndex = "auto";
    document.getElementById("login_wrapper").style.zIndex = "auto";
    document.getElementById(params).style.zIndex=1;
}