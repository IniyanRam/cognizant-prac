import { useDispatch, useSelector } from "react-redux";

import { unenroll }
from "../redux/enrollmentSlice";

function ProfilePage() {

  const dispatch = useDispatch();

  const enrolledCourses =
    useSelector(
      state => state.enrollment.enrolledCourses
    );

  return (

    <div>

      <h2>Profile</h2>

      {
        enrolledCourses.length === 0
        ? (
          <p>No enrolled courses.</p>
        )
        : (
          <ul>

            {
              enrolledCourses.map(course => (

                <li key={course.id}>

                  {course.name}

                  {" "}

                  <button
                    onClick={() =>
                      dispatch(
                        unenroll(course.id)
                      )
                    }
                  >
                    Remove
                  </button>

                </li>

              ))
            }

          </ul>
        )
      }

    </div>

  );

}

export default ProfilePage;