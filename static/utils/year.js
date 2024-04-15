let currentDate = new Date();
let currentYear = currentDate.getFullYear();

// find element with the id "currentYear"
let currentYearElement = document.getElementById("currentYear");

// update content with the current year
currentYearElement.textContent = currentYear;

