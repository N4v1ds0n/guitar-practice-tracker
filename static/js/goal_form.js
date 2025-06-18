document.addEventListener("DOMContentLoaded", () => {
  console.log("Goal form script loaded");
  const goalTypeField = document.querySelector("#id_goal_type");
  const standardGoals = document.querySelector("#standard-goal");
  const standardGoal = document.querySelector("#id_standard_goal");
  const goalTitle = document.querySelector("#goal-title");
  const goalDescription = document.querySelector("#goal-description");
  const targetTempo = document.querySelector("#target-tempo");
  const targetAccuracy = document.querySelector("#target-accuracy");
  const targetDuration = document.querySelector("#target-duration");
  const routineTargetDays = document.querySelector("#routine-target-days");

  function updateFormVisibility() {
    const value = goalTypeField.value;

    // Hide all by default
    standardGoals.classList.add("hidden");
    goalTitle.classList.add("hidden");
    goalDescription.classList.add("hidden");
    targetTempo.classList.add("hidden");
    targetAccuracy.classList.add("hidden");
    targetDuration.classList.add("hidden");
    routineTargetDays.classList.add("hidden");

    if (value === "custom") {
      console.log('Custom goal selected');
      goalTitle.classList.remove("hidden");
      goalDescription.classList.remove("hidden");
      targetTempo.classList.remove("hidden");
      targetAccuracy.classList.remove("hidden");
      targetDuration.classList.remove("hidden");
    } else  {
      console.log('Standard goal selected');
      standardGoals.classList.remove("hidden");
      targetTempo.classList.remove("hidden");
      targetAccuracy.classList.remove("hidden");
      targetDuration.classList.remove("hidden");
    }
  }

  function autofillStandardGoalFields() {
    const selectedId = standardGoal.value;
    console.log(`Selected standard goal ID: ${selectedId}`);

    if (!selectedId) return;

    fetch(`/api/standard-goal/?id=${selectedId}`)
      .then(res => res.json())
      .then(data => {
        if (data.title) {
          goalTitle.classList.remove("hidden");
          document.querySelector("#id_title").value = data.title.replace(/^\d+\.\s*/, "");
          console.log(`Autofilled title: ${data.title}`);
        };
        if (data.description) {
          goalDescription.classList.remove("hidden");
          document.querySelector("#id_description").value = data.description;
          console.log(`Autofilled description: ${data.description}`);
        }

        if (data.target_tempo !== undefined) targetTempo.value = data.target_tempo;
        if (data.target_accuracy !== undefined) targetAccuracy.value = data.target_accuracy;
        if (data.target_duration !== undefined) targetDuration.value = data.target_duration;
      })
      .catch(err => {
        console.error("Failed to fetch standard goal data", err);
      });
  };

  // Attach change event to the goal type field
  goalTypeField.addEventListener("change", updateFormVisibility);
  standardGoal.addEventListener("change", autofillStandardGoalFields);

  // Run on initial load
  updateFormVisibility();
  if (goalTypeField.value !== "custom") {
    autofillStandardGoalFields();
  }
});
