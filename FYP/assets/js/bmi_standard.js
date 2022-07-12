
    function bmi() {
        var weight = Number(document.getElementById("weight").value);
        var height = Number(document.getElementById("height").value);
        var height1 = Number(document.getElementById("height1").value);
  
        var h1 = height * 12;
        var h2 = h1 + height1;
        var w2 = weight * 2.205;
        var result = (w2 * 705) / h2;
        var result1 = result / h2;
        document.getElementById("result").innerHTML = "Your BMI score is:  " + result1;
        if (result1 < 18.5)
  
          document.getElementById("bb").innerHTML = "You are underweight";
  
        if (result1 > 24.5)
          document.getElementById("bb").innerHTML = "You are overweight";
  
        if (result1 < 24.5 && result1 > 18.5)
          document.getElementById("bb").innerHTML = "Your BMI is absolutely normal";
  
      }
   
  
  