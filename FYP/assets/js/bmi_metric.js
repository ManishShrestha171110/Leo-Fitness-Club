function bmi(){
    var weight = Number(document.getElementById("weight").value);
    var height = Number(document.getElementById("height").value);
    
    var h1=height/100;
    var result = weight/(h1*h1);
    
    document.getElementById("result").innerHTML = "Your BMI score is:  " +result;
    
    if(result<18.5)
    
    document.getElementById("bb").innerHTML = "You are underweight";
    
    if(result>24.5)
    document.getElementById("bb").innerHTML = "You are overweight";
    
    if(result<24.5 && result>18.5)
    document.getElementById("bb").innerHTML ="Your BMI is absolutely normal";
    }
    