firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.

    document.getElementById("loggedin_div").style.display = "block";
    document.getElementById("notloggedin_div").style.display = "none";
    document.getElementById("menu_notloggedin").style.display = "none";
    document.getElementById("menu-notloggedin").style.display = "none";
    document.getElementById("menu_loggedin").style.display = "block";


  } else {
    // No user is signed in.

    document.getElementById("loggedin_div").style.display = "none";
    document.getElementById("notloggedin_div").style.display = "block";
    document.getElementById("menu_notloggedin").style.display = "block";
    document.getElementById("menu-notloggedin").style.display = "block";
    document.getElementById("menu_loggedin").style.display = "none";

  }
});

function logout(){
  firebase.auth().signOut();
}