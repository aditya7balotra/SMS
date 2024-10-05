document.getElementById("file").addEventListener("change", function (event) {
  const [file] = event.target.files;
  if (file) {
    const reader = new FileReader();
    reader.onload = function (e) {
      const img = document.getElementById("imageDisplay");
      img.src = e.target.result;
      img.style.display = "block"; // Display the image
    };
    reader.readAsDataURL(file);
  }
});

document.getElementById("registerForm").addEventListener("submit", () => {
  window.alert("Form submitted SuccessFully");
});

Shery.makeMagnet("button" /* Element to target.*/, {
  //Parameters are optional.
  ease: "cubic-bezier(0.23, 1, 0.320, 1)",
  duration: 1,
});
