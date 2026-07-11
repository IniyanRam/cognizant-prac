import { courses } from "./data.js";

const courseGrid = document.querySelector(".course-grid");
const totalCredits = document.querySelector("#total-credits");
const searchInput = document.querySelector("#search-courses");
const sortButton = document.querySelector("#sort-btn");
const selectedCourse = document.querySelector("#selected-course");

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

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <span>Credits: ${course.credits}</span>
        `;

        courseGrid.appendChild(article);

    });

    totalCredits.textContent = `Total Credits: ${courseList.reduce((sum, course) => sum + course.credits, 0)}`;

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