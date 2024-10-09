document.addEventListener("DOMContentLoaded", function () {
  // Select all menu items with a submenu
  const submenuToggles = document.querySelectorAll(".submenu-toggle");

  submenuToggles.forEach((toggle) => {
    toggle.addEventListener("click", function (e) {
      e.preventDefault();

      const parent = this.parentElement;
      parent.classList.toggle("open"); // Toggle open class to show/hide submenu
    });
  });
});

// Stacking The Pages

//Buttons
var dashbtn = document.getElementById("dashbrd");
var homebtn = document.getElementById("home");
var addStuBtn = document.getElementById("Add-Student");
var addTeaBtn = document.getElementById("Add-Teacher");
var addAdmBtn = document.getElementById("Add-Admin");
var classMngBtn = document.getElementById("Class-Management");

//Pages
var dashpage = document.getElementById("dashPage");
var homepage = document.getElementById("homePage");
var addStupage = document.getElementById("addStudent-Page");
var addTeapage = document.getElementById("addTeacher-Page");
var addAdmpage = document.getElementById("addAdmin-Page");
var classMngpage = document.getElementById("classManagement-Page");

dashbtn.addEventListener("click", () => {
  homepage.style.display = "none";
  dashpage.style.display = "block";
});

homebtn.addEventListener("click", () => {
  dashpage.style.display = "none";
  homepage.style.display = "block";
});

addStuBtn.addEventListener("click", () => {
  dashpage.style.display = "none";
  homepage.style.display = "none";
  addStupage.style.display = "block";
});

addTeaBtn.addEventListener("click", () => {
  dashpage.style.display = "none";
  homepage.style.display = "none";
  addStupage.style.display = "none";
  addTeapage.style.display = "block";
});

addAdmBtn.addEventListener("click", () => {
  dashpage.style.display = "none";
  homepage.style.display = "none";
  addStupage.style.display = "none";
  addTeapage.style.display = "none";
  addAdmpage.style.display = "block";
});

classMngBtn.addEventListener("click", () => {
  dashpage.style.display = "none";
  homepage.style.display = "none";
  addStupage.style.display = "none";
  addTeapage.style.display = "none";
  addAdmpage.style.display = "none";
  classMngpage.style.display = "block";
});

// Class Management System

document.addEventListener("DOMContentLoaded", function () {
  const classForm = document.getElementById("classForm");
  const classList = document.getElementById("classList");
  let classes = JSON.parse(localStorage.getItem("classes")) || [];

  // Function to display classes in the table
  function displayClasses() {
    // Sort the classes array in ascending order based on the 'class' property
    classes.sort((a, b) => a.class.localeCompare(b.class));

    classList.innerHTML = "";
    classes.forEach((cls, index) => {
      const row = document.createElement("tr");
      row.innerHTML = `
              <td>${cls.class}</td>
              <td>${cls.section}</td>
              <td>${cls.subjects.join(", ")}</td>
              <td>
                  <button class="btn btn-warning btn-sm" data-index="${index}" onclick="editClass(${index})">Edit</button>
                  <button class="btn btn-danger btn-sm" data-index="${index}" onclick="deleteClass(${index})">Delete</button>
              </td>
          `;
      classList.appendChild(row);
    });
  }

  // Function to add a new class
  function addClass(newClass) {
    classes.push(newClass);
    localStorage.setItem("classes", JSON.stringify(classes));
    displayClasses();
  }

  // Function to delete a class
  window.deleteClass = function (index) {
    if (confirm("Are you sure you want to delete this class?")) {
      classes.splice(index, 1);
      localStorage.setItem("classes", JSON.stringify(classes));
      displayClasses();
    }
  };

  // Function to edit a class
  window.editClass = function (index) {
    const cls = classes[index];
    document.getElementById("classInput").value = cls.class;
    document.getElementById("sectionInput").value = cls.section;
    document.getElementById("subjectsInput").value = cls.subjects.join(", ");
    classForm.onsubmit = function (event) {
      event.preventDefault();
      updateClass(index);
    };
  };

  // Function to update a class
  function updateClass(index) {
    const updatedClass = {
      class: document.getElementById("classInput").value,
      section: document.getElementById("sectionInput").value,
      subjects: document
        .getElementById("subjectsInput")
        .value.split(",")
        .map((subject) => subject.trim()),
    };
    classes[index] = updatedClass;
    localStorage.setItem("classes", JSON.stringify(classes));
    displayClasses();
    classForm.reset();
    classForm.onsubmit = handleFormSubmit; // Restore the default form submission for adding new classes
  }

  // Handle form submit for adding a new class
  function handleFormSubmit(event) {
    event.preventDefault();
    const newClass = {
      class: document.getElementById("classInput").value,
      section: document.getElementById("sectionInput").value,
      subjects: document
        .getElementById("subjectsInput")
        .value.split(",")
        .map((subject) => subject.trim()),
    };
    addClass(newClass);
    classForm.reset();
  }

  classForm.onsubmit = handleFormSubmit;
  displayClasses(); // Display classes when page is loaded
});
