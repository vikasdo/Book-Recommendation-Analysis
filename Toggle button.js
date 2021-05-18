<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
   body {
      padding: 25px;
      background-color: white;
      color: black;
      font-size: 25px;
      font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
   }
   .dark-mode {
      background-color: black;
      color: white;
   }
   .toggleButton {
      padding: 12px;
      font-size: 18px;
      border: 2px solid green;
   }
</style>
</head>
<body>
<h1>Toggle Dark/Light Mode Example</h1>
<button class="toggleButton">Toggle dark mode</button>
<h2>Click the above button to toggle dark mode</h2>
<script>
   document .querySelector(".toggleButton") .addEventListener("click", toggleDarKMode);
   function toggleDarKMode() {
      var element = document.body;
      element.classList.toggle("dark-mode");
   }
</script>
</body>
</html>