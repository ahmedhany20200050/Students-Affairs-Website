
$("#ser").change(function(){
  console.log($(this).val());
});
let update = document.getElementById("update");
let del = document.getElementById("delete");
update.addEventListener("click", function (e) {
  let valid = validation();
  if (!valid) {
    e.preventDefault();
  }
});
del.addEventListener("click", function (e) {
  let valid = validation();
  if (valid) {
    let confirmMsg = confirm("Are you sure to delete your data?");
    if (!confirmMsg) {
      e.preventDefault();
    }
  }
  if (!valid) {
    e.preventDefault();
  }
});
function validation() {
  let isvalidate = true;
  let Student_name = document.getElementById("name");
  let Student_id = document.getElementById("num");
  let Student_gpa = document.getElementById("gpa");
  let Student_email = document.getElementById("Email");
  let Student_phone_number = document.getElementById("phone");
  var inputs = [
    Student_name,
    Student_id,
    Student_gpa,
    Student_email,
    Student_phone_number
  ];
  for (var i = 0; i < 5; i++) {
    let parent = inputs[i].parentElement;
    let small_Elements = parent.getElementsByTagName("small");
    if (small_Elements.length > 0) {
      small_Elements[0].remove();
      inputs[i].style.borderBottom = "solid rgb(132, 140, 146)";
    }
  }
  isvalidate = check_name(Student_name, isvalidate, /\d+/i);
  isvalidate = check_id(Student_id, isvalidate, /[^0-9]/);
  isvalidate = check_Information(Student_gpa, isvalidate, /^[0-4][.]\d{2}/);
  isvalidate = check_Information(Student_email, isvalidate, /\w+@\w+[.]\w+/i);
  isvalidate = check_Information(
    Student_phone_number,
    isvalidate,
    /01(1|2|0|5)\d{8}/
  );
  return isvalidate;
}
function check_id(input_child, isvalidate, pattern) {
  if (pattern.test(input_child.value) || input_child.value == "") {
    isvalidate = false;
    Create_message(input_child);
  } else {
    if (input_child.value < 20200000 || input_child.value > 20209999) {
      isvalidate = false;
      Create_message(input_child);
    }
  }
  return isvalidate;
}
function check_name(input_child, isvalidate, pattern) {
  if (input_child.value.length === 0 || pattern.test(input_child.value)) {
    isvalidate = false;
    Create_message(input_child);
  } else if (input_child.value.length > 15 || input_child.value.length < 2) {
    isvalidate = false;
    Create_message(input_child);
  }
  return isvalidate;
}
function check_Information(input_child, isvalidate, pattern) {
  if (input_child.value === "" || !pattern.test(input_child.value)) {
    isvalidate = false;
    Create_message(input_child);
  } else if (
    (input_child.id === "phone" && input_child.value.length > 11) ||
    (input_child.id === "gpa" && input_child.value.length > 4) ||
    (input_child.value[0] == "4" && input_child.value[3] != "0")
  ) {
    isvalidate = false;
    Create_message(input_child);
  }
  return isvalidate;
}
function Create_message(input_child) {
  let papa = input_child.parentElement;
  let small_Elements = papa.getElementsByTagName("small");
  if (small_Elements.length === 0) {
    let errorMsg = document.createElement("small");
    errorMsg.innerHTML = message(input_child);
    input_child.after(errorMsg);
    input_child.style.borderBottom = " solid crimson";
  }
}
function message(input_child) {
  if (input_child.value == "") {
    return "The field is required";
  }
  if (input_child.id === "name") {
    if (input_child.value.length > 15 || input_child.value.length < 2) {
      return "The name must be at least 6 characters and atmost 15 characters";
    }
    return "Your name cannot have a number";
  }
  if (input_child.id === "num") {
    return "You must enter a numeric value between 20200000 and 20209999";
  }
  if (input_child.id === "gpa") {
    if (input_child.value.length != 4) {
      return "You must enter 4 characters like this (3.44,1.23,2.66) ";
    }
    return "You must enter a numeric value between 0 and 4.00";
  }
  if (input_child.id === "Email") {
    return "Invalid Email,the email pattern must be (numbers or characters)@(Mail server).(Top-level Domain)";
  }
  if (input_child.id === "phone") {
    if (input_child.value.length > 11) {
      return "You must enter an egyptian mobile number of 11 numbers";
    }
    return "Invalid number, please write a valid egyptian mobile number";
  }
}
