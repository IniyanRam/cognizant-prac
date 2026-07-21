import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");
const totalCredits = document.querySelector("#total-credits");
const searchInput = document.querySelector("#search-courses");
const sortButton = document.querySelector("#sort-btn");
const selectedCourse = document.querySelector("#selected-course");
const menuToggle = document.querySelector("#menu-toggle");
const mainMenu = document.querySelector("#main-menu");
// ES6 Destructuring
courses.forEach(course => {
    const { name, credits } = course;
    console.log(name, credits);
});

// map()
const formattedCourses = courses.map(
    course => `${course.code} — ${course.name} (${course.credits} credits)`
);

console.log(formattedCourses);

// filter()
const creditCourses = courses.filter(course => course.credits >= 4);

console.log("Courses with 4 or more credits:", creditCourses.length);

// reduce()
const total = courses.reduce((sum, course) => sum + course.credits, 0);

console.log("Total Credits:", total);

let displayedCourses = [...courses];

function renderCourses(courseList) {

    courseGrid.innerHTML = "";

    courseList.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";
        article.dataset.id = course.id;

        // Task 129
        article.setAttribute("tabindex", "0");

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <span>Credits: ${course.credits}</span>
        `;

        // Pressing Enter performs the same action as clicking
        article.addEventListener("keydown", event => {

            if (event.key === "Enter") {

                selectedCourse.textContent =
                    `Selected Course: ${course.name} | Grade: ${course.grade}`;

            }

        });

        courseGrid.appendChild(article);

    });

    // Task 130
    totalCredits.textContent =
        `${courseList.length} course(s) found | Total Credits: ${courseList.reduce(
            (sum, course) => sum + course.credits,
            0
        )}`;

}

renderCourses(displayedCourses);

// Search

searchInput.addEventListener("input", () => {

    const searchText = searchInput.value.toLowerCase();

    displayedCourses = courses.filter(course =>
        course.name.toLowerCase().includes(searchText)
    );

    renderCourses(displayedCourses);

});

// Sort

sortButton.addEventListener("click", () => {

    displayedCourses.sort((a, b) => b.credits - a.credits);

    renderCourses(displayedCourses);

});

// Event Delegation

courseGrid.addEventListener("click", event => {

    const card = event.target.closest(".course-card");

    if (!card) {
        return;
    }

    const id = Number(card.dataset.id);

    const course = courses.find(course => course.id === id);

    selectedCourse.textContent =
        `Selected Course: ${course.name} | Grade: ${course.grade}`;

});

// Task 131

menuToggle.addEventListener("click", () => {

    const expanded =
        menuToggle.getAttribute("aria-expanded") === "true";

    menuToggle.setAttribute(
        "aria-expanded",
        String(!expanded)
    );

    mainMenu.classList.toggle("show");
    console.log(mainMenu.classList.contains("show"));

});