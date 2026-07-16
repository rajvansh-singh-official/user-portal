const questionType = document.getElementById("question-type");
const optionFields = document.getElementById("option-fields");
const correctOption = document.getElementById("correct-option");

function updateQuestionForm() {

    const type = questionType.value;

    if (type === "mcq") {

        optionFields.style.display = "block";

        correctOption.innerHTML = `
            <option value="1">Option 1</option>
            <option value="2">Option 2</option>
            <option value="3">Option 3</option>
            <option value="4">Option 4</option>
        `;

    }

    else if (type === "true_false") {

        optionFields.style.display = "none";

        correctOption.innerHTML = `
            <option value="true">True</option>
            <option value="false">False</option>
        `;

    }

    else {

        optionFields.style.display = "none";
        correctOption.innerHTML = "";

    }

}

questionType.addEventListener("change", updateQuestionForm);

updateQuestionForm();