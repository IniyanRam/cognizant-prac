import apiClient from "./apiClient";

/*
Task 139 - Centralized Course API

All course-related API operations are defined in this file.
Components communicate only with these functions and never
directly with Axios.

The API response is transformed into the format required by
the Student Portal application.
*/

function mapCourse(post) {

    const courseNames = [
        "Web Development",
        "Database Systems",
        "Operating Systems",
        "Computer Networks",
        "Machine Learning"
    ];

    const courseCodes = [
        "CS101",
        "CS102",
        "CS103",
        "CS104",
        "CS105"
    ];

    const credits = [4, 3, 4, 3, 4];

    const grades = [
        "A",
        "A+",
        "B+",
        "A",
        "O"
    ];

    const index = (post.id - 1) % 5;

    return {
        id: post.id,
        name: courseNames[index],
        code: courseCodes[index],
        credits: credits[index],
        grade: grades[index]
    };

}

export async function getAllCourses() {

    const posts = await apiClient.get("/posts");

    return posts.slice(0, 5).map(mapCourse);

}

export async function getCourseById(id) {

    const post = await apiClient.get(`/posts/${id}`);

    return mapCourse(post);

}

export async function enrollStudent(studentId, courseId) {

    return await apiClient.post("/posts", {
        studentId,
        courseId
    });

}