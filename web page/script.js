// Smooth Scroll to About Section
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId);
  window.scrollTo({
    top: section.offsetTop - 80,  // Adjusting the scroll position to account for navbar
    behavior: 'smooth'
  });
}

// Contact Form Submission
document.getElementById("contact-form").addEventListener("submit", function(event) {
  event.preventDefault();  // Prevent page reload

  // Simple form validation
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const message = document.getElementById("message").value;

  if (name && email && message) {
    alert("Message sent successfully!");
    document.getElementById("contact-form").reset();  // Reset the form
  } else {
    alert("Please fill out all fields.");
  }
});