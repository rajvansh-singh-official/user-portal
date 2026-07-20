/* ==========================================================
   QUESTION FORM
========================================================== */

const questionType = document.getElementById("question-type");
const optionFields = document.getElementById("option-fields");
const correctOptionGroup = document.getElementById("correct-option-group");
const correctOption = document.getElementById("correct-option");

function updateQuestionForm() {

    const type = questionType.value;

    switch (type) {

        case "mcq":

            optionFields.style.display = "block";
            correctOptionGroup.style.display = "block";

            correctOption.innerHTML = `
                <option value="1">Option 1</option>
                <option value="2">Option 2</option>
                <option value="3">Option 3</option>
                <option value="4">Option 4</option>
            `;

            break;

        case "true_false":

            optionFields.style.display = "none";
            correctOptionGroup.style.display = "block";

            correctOption.innerHTML = `
                <option value="true">True</option>
                <option value="false">False</option>
            `;

            break;

        default:

            optionFields.style.display = "none";
            correctOptionGroup.style.display = "none";
            correctOption.innerHTML = "";

    }

}


/* ==========================================================
   FORM PERSISTENCE
========================================================== */

const category = document.getElementById("id_category");
const difficulty = document.getElementById("id_difficulty");
const marks = document.getElementById("id_marks");
const isActive = document.getElementById("id_is_active");

function loadSavedFormData() {

    const savedQuestionType = localStorage.getItem("questionType");
    const savedCategory = localStorage.getItem("category");
    const savedDifficulty = localStorage.getItem("difficulty");
    const savedMarks = localStorage.getItem("marks");
    const savedIsActive = localStorage.getItem("isActive");

    if (savedQuestionType) {
        questionType.value = savedQuestionType;
    }

    if (savedCategory) {
        category.value = savedCategory;
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

}

function registerFormEvents() {

    questionType.addEventListener("change", () => {
        localStorage.setItem("questionType", questionType.value);
        updateQuestionForm();
    });

    category.addEventListener("change", () => {
        localStorage.setItem("category", category.value);
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

}


/* ==========================================================
   QUESTION ACCORDION
========================================================== */

function initializeAccordion() {

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

}


/* ==========================================================
   FILTER CHIP REMOVAL
========================================================== */

function removeFilter(key) {

    const params = new URLSearchParams(window.location.search);
    params.delete(key);

    // rebuild URL — if no params left go to base URL
    const newQuery = params.toString();
    window.location.search = newQuery;

}


/* ==========================================================
   CATEGORY MODAL
========================================================== */

const categoryModal = document.getElementById("category-modal");
const openCategoryModal = document.getElementById("open-category-modal");
const closeCategoryModal = document.getElementById("close-category-modal");

function initializeCategoryModal() {

    openCategoryModal.addEventListener("click", () => {
        categoryModal.classList.remove("hidden");
    });

    closeCategoryModal.addEventListener("click", () => {
        categoryModal.classList.add("hidden");
    });

    categoryModal.addEventListener("click", (event) => {
        if (event.target === categoryModal) {
            categoryModal.classList.add("hidden");
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            categoryModal.classList.add("hidden");
        }
    });

}


/* ==========================================================
   INITIALIZE
========================================================== */

if (
    document.querySelector(".field-error") ||
    document.querySelector("#category-modal .error-alert")
) {
    categoryModal.classList.remove("hidden");
}

loadSavedFormData();
registerFormEvents();
initializeAccordion();
initializeCategoryModal();