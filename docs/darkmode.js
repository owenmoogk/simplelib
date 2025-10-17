darkmode = false
function toggleDarkMode(){
    $("*").toggleClass('darkMode')
    if (darkmode){
        darkmode = false
        document.getElementById("dark-mode-button").text = "Dark mode"
        localStorage.setItem("darkmode", "false")
    }
    else{
        darkmode = true
        document.getElementById("dark-mode-button").text = "Light mode"
        localStorage.setItem("darkmode", "true")
    }
}

function checkDarkMode(){
    if (localStorage.getItem("darkmode") == "true"){
        toggleDarkMode()
    }
}