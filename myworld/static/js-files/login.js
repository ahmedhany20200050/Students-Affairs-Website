

function check() {
  var email = document.getElementById("email").value;
  // var pass = document.getElementById("password").value;
  // window.alert(email);
  // var employee={'email':email,'pass':pass};
  var x = new XMLHttpRequest();
  
  x.onload = function(){
    
    // var ok=false;
    if(x.responseText=='ok'){
      window.location.replace("homepage");
    }
    else{
      window.alert(
            "Employee not found   email:  ahmed@gmail.com   password: 12345678"
          );
    }

  }
  x.open("POST","../validate",false);
  x.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  x.send("email="+email);


  // var email = document.getElementById("email").value;
  // let pass = document.getElementById("password").value;
  // window.alert(pass);
  // let employee = { email: "ahmed@gmail.com", password: "12345678" };
  // if (email === employee.email && pass === employee.password) {
  //   window.location.replace("./Home.html");
  // } else {
  //   window.alert(
  //     "Employee not found   email:  ahmed@gmail.com   password: 12345678"
  //   );
  // }
}
