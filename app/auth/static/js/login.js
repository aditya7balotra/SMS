// YOUR JS CODE WRITE BELOW :-- BE REMEMBER =>  DO NOT TOUCH ABOVE CODE OR ANY CHANGES...
// console.log('hhh')
var x = document.getElementById("email_ln");
x.onblur = function f_event6() {
  var y = document.getElementById("email_ln").value;
  var z = document.getElementById("email_ln");
  var k = document.getElementById("f_iconln");
  var a = y.length;

  if (y != "") {
    z.style.borderColor = "gray";
    k.style.opacity = "0";
  } else {
    z.style.borderColor = "red";
    k.style.opacity = "1";
  }

  z.oninput = function () {
    z.style.borderColor = "gray";
    k.style.opacity = "0";
  };

  a >= 1 ? (z.style.borderColor = "green") : (z.style.borderColor = "red");
};

var x = document.getElementById("pass_ln");
x.onblur = function f_event7() {
  var y = document.getElementById("pass_ln").value;
  var z = document.getElementById("pass_ln");
  var k = document.getElementById("f_iconln1");
  var a = y.length;

  if (y != "") {
    z.style.borderColor = "gray";
    k.style.opacity = "0";
  } else {
    z.style.borderColor = "red";
    k.style.opacity = "1";
  }

  z.oninput = function () {
    z.style.borderColor = "gray";
    k.style.opacity = "0";
  };

  a >= 1 ? (z.style.borderColor = "green") : (z.style.borderColor = "red");
};

var userForm = document.getElementById("userForum");
var adminForm = document.getElementById("adminForum");

var userFormBtn = document.getElementById("adnBtn");
var adminFormBtn = document.getElementById("back");

userFormBtn.onclick = function () {
  userForm.style.display = "none";
  adminForm.style.display = "block";
};

adminFormBtn.onclick = function () {
  userForm.style.display = "block";
  adminForm.style.display = "none";
};
