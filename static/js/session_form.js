const goalTypes = JSON.parse(document.getElementById("goal-types").textContent);
console.log(goalTypes);

document.addEventListener("DOMContentLoaded", () => {
  const goalSelect = document.getElementById("id_goal");
  const tempoField = document.getElementById("id_tempo")?.closest("p");
  const accuracyField = document.getElementById("id_accuracy")?.closest("p");

  function updateFormFields(goalId) {
    const type = goalTypes[goalId];
    if (type === "repertoire") {
      tempoField.classList.add("hidden");
      accuracyField.classList.add("hidden");
    }
  }

  goalSelect.addEventListener("change", (e) => {
    updateFormFields(e.target.value);
  });

  if (goalSelect.value) updateFormFields(goalSelect.value);
});