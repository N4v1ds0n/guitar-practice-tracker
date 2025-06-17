document.addEventListener("DOMContentLoaded", () => {
  console.log("Goal form script loaded");
  const goalTypeField = document.querySelector("#id_goal_type");
  const standardGoals = document.querySelector("#standard-goal");
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
    } else if (value === "technique") {
      console.log('Technique goal selected');
      standardGoals.classList.remove("hidden");
    } else if (value === "repertoire") {
      console.log('Repertoire goal selected');
      standardGoals.classList.remove("hidden");
    } else if (value === "routine") {
      console.log('Routine goal selected');
      standardGoals.classList.remove("hidden");
    }
  }

  // Attach change event to the goal type field
  goalTypeField.addEventListener("change", updateFormVisibility);

  // Run on initial load
  updateFormVisibility();
});
