firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.

    document.getElementById("user_div").style.display = "block";
    document.getElementById("signup_div").style.display = "none";
    document.getElementById("menu_notloggedin").style.display = "none";
    document.getElementById("menu-notloggedin").style.display = "none";
    document.getElementById("menu_loggedin").style.display = "block";

    var user = firebase.auth().currentUser;

    if(user != null){

      var email_id = user.email;
      document.getElementById("user_para").innerHTML = "Welcome User : " + email_id;

    }

  } else {
    // No user is signed in.

    document.getElementById("user_div").style.display = "none";
    document.getElementById("signup_div").style.display = "block";
    document.getElementById("menu_notloggedin").style.display = "block";
    document.getElementById("menu-notloggedin").style.display = "block";
    document.getElementById("menu_loggedin").style.display = "none";

  }
});

function signup(){

  var userName = document.getElementById("name_field").value;
  var userName_len = userName.length;
  var userSobrenome = document.getElementById("sobrenome_field").value;
  var userSobrenome_len = userSobrenome.length;
  var userEmail = document.getElementById("email_field").value;
  var userPass = document.getElementById("password_field").value;
  var userConfirmPass = document.getElementById("confirm_field").value;
  
  if (userName_len != 0){
      if (userSobrenome_len != 0){
          if (userPass == userConfirmPass){
              firebase.auth().createUserWithEmailAndPassword(userEmail, userPass).catch(function(error) {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMessage = error.message;
                
                window.alert("Error : " + errorMessage);
                // ...
                
              });
          } else {
              window.alert("Error : The passwords do not match! Please try again...");
          }
      } else {
          window.alert("Error : O sobrenome não pode ser vazio! Please try again...");
          
      }
  } else {
          window.alert("Error : O nome não pode ser vazio! Please try again...");
          
      }
  
}

function logout(){
  firebase.auth().signOut();
}
