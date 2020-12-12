function previewString(){
 
    var objResult = document.getElementById("result");
  
    var objText = document.getElementById("tbString");
  
    var objFontColor = document.getElementById("fontColor");
  
    var objFontSize = document.getElementById("fontSize");
  
    var objOptions = document.getElementsByName("fontOptions");
  
  
  
  
  
  
  
    //tag id name 이3개를 읽을수 있음
  
  
  
  
    var targetString = objText.value; 
  
    targetString = targetString.fontcolor(objFontColor.options[objFontColor.selectedIndex].value);
  
       targetString = targetString.fontsize(objFontSize.options[objFontSize.selectedIndex].value);
  
       
  
    if(objOptions[0].checked){
  
     targetString = targetString.strike();
  
    }
  
    if(objOptions[1].checked){
  
     targetString = targetString.big();
  
    }
  
    if(objOptions[2].checked){
  
     targetString = targetString.small();
  
    }
  
    if(objOptions[3].checked){
  
     targetString = targetString.bold();
  
    }
  
    if(objOptions[4].checked){
  
     targetString = targetString.italic();
  
    }
  
    if(objOptions[5].checked){
  
     targetString = targetString.sup();
  
    }
  
    if(objOptions[6].checked){
  
     targetString = targetString.sub();
  
    }
  
    if(objOptions[7].checked){
  
     targetString = targetString.toLowerCase();
  
    }
  
    if(objOptions[8].checked){
  
     targetString = targetString.toUpperCase();
  
    }
  
     objResult.innerHTML = targetString;
  
   
  
  
  
  
   }