// static/js/script.js

// Disease Detection Form
document.addEventListener("DOMContentLoaded", () => {
  const diseaseForm = document.getElementById("diseaseForm");
  const chatForm = document.getElementById("chatForm");

  if (diseaseForm) {
    diseaseForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const symptoms = e.target.symptoms.value;

      fetch("/detect", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `symptoms=${encodeURIComponent(symptoms)}`,
      })
        .then((res) => res.json())
        .then((data) => {
          if (data.error) {
            alert("Disease Detection Error: " + data.error);
            return;
          }

          document.getElementById("disease").innerText = data.disease;
          document.getElementById("prescription").innerText = data.prescription;
          document.getElementById("diet").innerText = data.diet;
          document.getElementById("urgency").innerText = data.urgency;
          document.getElementById("resultBox").classList.remove("hidden");
        })
        .catch((err) => {
          alert("❌ Could not contact server.");
          console.error(err);
        });
    });
  }

  // Chatbot Form
  if (chatForm) {
    chatForm.addEventListener("submit", function (e) {
      e.preventDefault();
      const input = document.getElementById("chatInput");
      const msg = input.value.trim();
      const chatBox = document.getElementById("chatBox");

      if (!msg) return;

      chatBox.innerHTML += `<div><strong>You:</strong> ${msg}</div>`;
      input.value = "";

      fetch("/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
        body: `message=${encodeURIComponent(msg)}`,
      })
        .then((res) => res.json())
        .then((data) => {
          chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.reply}</div>`;
          chatBox.scrollTop = chatBox.scrollHeight;
        })
        .catch((err) => {
          chatBox.innerHTML += `<div><strong>Bot:</strong> ❌ Error</div>`;
          console.error(err);
        });
    });
  }
});
