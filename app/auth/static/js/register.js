// JavaScript to handle image preview
document.getElementById("file").addEventListener("change", function (event) {
  const [file] = event.target.files;
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const img = document.getElementById("imageDisplay");
      img.src = e.target.result;
      img.style.display = "block"; // Ensure the image is displayed
    };
    reader.readAsDataURL(file);
  }
});

// JavaScript to handle form submission alert
// document.getElementById("registerForm").addEventListener("submit", function (event) {
//   // Optionally prevent default form submission if needed
//   // event.preventDefault();
//   window.alert("Form submitted successfully");
// });

// Example of how to use Shery (if needed for other effects)
Shery.makeMagnet("button", {
  // Parameters are optional
  ease: "cubic-bezier(0.23, 1, 0.32, 1)",
  duration: 1,
});
