const questionType = document.getElementById("question-type");
const optionFields = document.getElementById("option-fields");
const correctOptionGroup = document.getElementById("correct-option-group");
const correctOption = document.getElementById("correct-option");
const difficulty = document.getElementById("id_difficulty");
const marks = document.getElementById("id_marks");
const isActive = document.getElementById("id_is_active");

function updateQuestionForm() {

    const type = questionType.value;

    if (type === "mcq") {

        optionFields.style.display = "block";
        correctOptionGroup.style.display = "block";

        correctOption.innerHTML = `
                <option value="1">Option 1</option>
                <option value="2">Option 2</option>
                <option value="3">Option 3</option>
                <option value="4">Option 4</option>
            `;

    }

    else if (type === "true_false") {

        optionFields.style.display = "none";
        correctOptionGroup.style.display = "block";

        correctOption.innerHTML = `
                <option value="true">True</option>
                <option value="false">False</option>
            `;

    }

    else {

        optionFields.style.display = "none";
        correctOptionGroup.style.display = "none";
        correctOption.innerHTML = "";

    }

}

const savedQuestionType = localStorage.getItem("questionType");
const savedDifficulty = localStorage.getItem("difficulty");
const savedMarks = localStorage.getItem("marks");
const savedIsActive = localStorage.getItem("isActive");

if (savedQuestionType) {
    questionType.value = savedQuestionType;
}

if (savedDifficulty) {
    difficulty.value = savedDifficulty;
}

if (savedMarks) {
    marks.value = savedMarks;
}

if (savedIsActive !== null) {
    isActive.checked = savedIsActive === "true";
}

updateQuestionForm();

questionType.addEventListener("change", () => {
    localStorage.setItem("questionType", questionType.value);
    updateQuestionForm();
});

difficulty.addEventListener("change", () => {
    localStorage.setItem("difficulty", difficulty.value);
});

marks.addEventListener("input", () => {
    localStorage.setItem("marks", marks.value);
});

isActive.addEventListener("change", () => {
    localStorage.setItem("isActive", isActive.checked);
});

const questionItems = document.querySelectorAll(".q-item");
const questionHeaders = document.querySelectorAll(".q-header");

questionHeaders.forEach((header) => {

    header.addEventListener("click", () => {

        const item = header.closest(".q-item");

        questionItems.forEach((other) => {

            if (other !== item) {
                other.classList.remove("open");
            }

        });

        item.classList.toggle("open");

    });

});