document.getElementById("predictionForm").addEventListener("submit", function (event) {
  event.preventDefault();

  let formData = {
    age: document.getElementById("age").value,
    gender: document.getElementById("gender").value,
    socioeconomic: document.getElementById("socioeconomic").value,
    drug_type: document.getElementById("drug_type").value,
    age_first_used: document.getElementById("age_first_used").value,
    drug_frequency: document.getElementById("drug_frequency").value,
    reason_for_use: document.getElementById("reason_for_use").value,
    family_support: document.getElementById("family_support").value,
    attendance: document.getElementById("attendance").value,
    gpa: document.getElementById("gpa").value
  };

  fetch("/predict", {
    method: "POST",
    body: JSON.stringify(formData),
    headers: {
      "Content-Type": "application/json"
    }
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").textContent = data.prediction;
    })
    .catch(error => console.error("Error:", error));
});
