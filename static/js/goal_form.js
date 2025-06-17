document.addEventListener("DOMContentLoaded", function () {
    const goalTypeField = document.querySelector("#id_goal_type");

    // Mapping goal types to the field classes they need
    const fieldGroups = {
        'routine': ['.field-routine-target-days'],
        'technical': ['.field-target-tempo', '.field-target-accuracy', '.field-target-duration'],
        'custom': ['.field-target-tempo', '.field-target-accuracy', '.field-target-duration'],
        'repertoire': []
    };

    function updateFieldVisibility() {
        const selectedType = goalTypeField.value;

        // All conditional fields
        const allSelectors = ['.field-target-tempo', '.field-target-accuracy', '.field-target-duration', '.field-routine-target-days'];
        
        // Hide all first
        allSelectors.forEach(selector => {
            const field = document.querySelector(selector);
            if (field) {
                field.closest('p').style.display = 'none';
            }
        });

        // Show the ones needed for this type
        const visibleFields = fieldGroups[selectedType] || [];
        visibleFields.forEach(selector => {
            const field = document.querySelector(selector);
            if (field) {
                field.closest('p').style.display = '';
            }
        });
    }

    // Initial call
    updateFieldVisibility();

    // Change handler
    goalTypeField.addEventListener("change", updateFieldVisibility);
});
