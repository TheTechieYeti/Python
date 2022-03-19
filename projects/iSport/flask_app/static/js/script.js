console.log ("page loaded")
function loading(params) {
    console.log ("This is WOrking")
    
}
// function bring_to_top(params) {
//     document.getElementById("reg_wrapper").style.zIndex = "auto";
//     document.getElementById("login_wrapper").style.zIndex = "auto";
//     document.getElementById(params).style.zIndex=1;
// }

function display_tab(tab, box) {
    var tabs = document.querySelectorAll(".event_box_tab")
    var boxes = document.querySelectorAll(".box")
    tabs.forEach(tab => {
        tab.style.backgroundColor = "grey";
        tab.style.color = "white";
        tab.style.zIndex = -2;
    })
    boxes.forEach(box => {
        box.style.zIndex = 1;
        box.style.display = "none";
    })
    document.getElementById(tab).style.backgroundColor = "white";
    document.getElementById(tab).style.color = "black";
    document.getElementById(tab).style.width = '100%';
    document.getElementById(tab).style.zIndex = 9;
    document.querySelector(box).style.zIndex = 8;
    document.querySelector(box).style.display = "block";

    
}
display_tab('info_tab','.info_box')