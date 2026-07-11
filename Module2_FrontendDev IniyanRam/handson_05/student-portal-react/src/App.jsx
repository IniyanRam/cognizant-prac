import { useState, useEffect } from 'react';
import './App.css';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import courseData from './data/courses';
import StudentProfile from './components/StudentProfile';

function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  
  useEffect(() => {
  fetch('https://jsonplaceholder.typicode.com/posts')
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch courses");
      }
      return response.json();
    })
    .then((data) => {
      const courseList = data.slice(0, 5).map((post, index) => ({
        id: post.id,
        name: post.title,
        code: `CS20${index + 1}`,
        credits: 4,
        grade: "A",
      }));

      setCourses(courseList);
      setLoading(false);
    })
    .catch(() => {
      setError("Unable to load courses.");
      setLoading(false);
    });
  }, []);

  useEffect(() => {
  console.log("Courses updated");
  }, [courses]);
  
  const handleEnroll = (course) => {
    setEnrolledCourses((prevCourses) => [...prevCourses, course]);
  };

  if (loading) {
  return <h2>Loading...</h2>;
  }
  if (error) {
  return <h2>{error}</h2>;
  }
  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <input
        type="text"
        placeholder="Search courses..."
        value={searchTerm}
        onChange={(event) => setSearchTerm(event.target.value)}
      />

      {courses
        .filter((course) =>
          course.name.toLowerCase().includes(searchTerm.toLowerCase())
        )
        .map((course) => (
          <CourseCard
            key={course.id}
            name={course.name}
            code={course.code}
            credits={course.credits}
            grade={course.grade}
            course={course}
            onEnroll={handleEnroll}
          />
        ))}
      <StudentProfile />
      <Footer />
    </>
  );
}

export default App;