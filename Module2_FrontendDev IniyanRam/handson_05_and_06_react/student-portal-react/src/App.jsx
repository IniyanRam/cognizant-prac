import './App.css';

import Header from './components/Header';
import Footer from './components/Footer';

import HomePage from './pages/HomePage';
import CoursesPage from './pages/CoursesPage';
import ProfilePage from './pages/ProfilePage';
import CourseDetailPage from './pages/CourseDetailPage';

import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <>
      <Header />

      <Routes>
        <Route path="/" element={<HomePage />} />

        <Route path="/courses" element={<CoursesPage />} />

        <Route path="/profile" element={<ProfilePage />} />

        <Route
          path="/courses/:courseId"
          element={<CourseDetailPage />}
        />
      </Routes>

      <Footer />
    </>
  );
}

export default App;