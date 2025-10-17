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
    
    // loading text variable
    for (i = 0; i < functions.length; i++) { 
        txt += '<tr><td>'+functions[i].innerHTML+'</td><td>'+descriptions[i].innerHTML+'</td></tr>';
    }

    // put into container
    document.getElementById(tableID).innerHTML += txt
}