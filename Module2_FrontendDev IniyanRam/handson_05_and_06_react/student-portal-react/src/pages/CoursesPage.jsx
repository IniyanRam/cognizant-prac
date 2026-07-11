import { Link } from "react-router-dom";

function CoursesPage() {

  return (
    <div>

      <h2>Courses</h2>

      <ul>

        <li>
          <Link to="/courses/1">
            React Fundamentals
          </Link>
        </li>

        <li>
          <Link to="/courses/2">
            Java Programming
          </Link>
        </li>

        <li>
          <Link to="/courses/3">
            Database Systems
          </Link>
        </li>

      </ul>

    </div>
  );
}

export default CoursesPage;