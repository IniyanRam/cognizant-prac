import { useNavigate, useParams } from "react-router-dom";
import { useDispatch } from "react-redux";

import { enroll } from "../redux/enrollmentSlice";

function CourseDetailPage() {

  const { courseId } = useParams();

  const navigate = useNavigate();

  const dispatch = useDispatch();

  const handleEnroll = () => {

    dispatch(
      enroll({
        id: Number(courseId),
        name: `Course ${courseId}`,
      })
    );

    navigate("/profile");

  };

  return (

    <div>

      <h2>Course Details</h2>

      <p>Course ID : {courseId}</p>

      <button onClick={handleEnroll}>

        Enroll

      </button>

    </div>

  );

}

export default CourseDetailPage;