darkmode = false
function toggleDarkMode(){
    $("*").toggleClass('darkMode')
    if (darkmode){
        console.log("i got here")
        darkmode = false
        document.getElementById("dark-mode-button").text = "Dark mode"
    }
    else{
        darkmode = true
        document.getElementById("dark-mode-button").text = "Light mode"
    }
}


// xml request
function populateTable(xml, tableID) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			table(this, tableID);
		}
    };
    xmlhttp.open("GET", xml, true);
    xmlhttp.send();
}

// populate table
function table(xml, tableID) {
    var titles, links, i, xmlDoc; 
    
    // text that is appended to elements
    var txt = ''

    // xml variables
    xmlDoc = xml.responseXML;
    functions = xmlDoc.getElementsByTagName("function");
    descriptions = xmlDoc.getElementsByTagName('desc');
    console.log(functions)
    
    // loading text variable
    for (i = 0; i < functions.length; i++) { 
        txt += '<tr><td>'+functions[i].innerHTML+'</td><td>'+descriptions[i].innerHTML+'</td></tr>';
    }

    // put into container
    console.log(txt)
    console.log(tableID)
    console.log(document.getElementById(tableID).innerHTML)
    document.getElementById(tableID).innerHTML += txt
}