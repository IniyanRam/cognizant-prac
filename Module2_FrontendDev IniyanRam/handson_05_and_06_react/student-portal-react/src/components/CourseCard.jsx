function CourseCard(props) {
  return (
    <div className="course-card">
      <h2>{props.name}</h2>

      <p><strong>Code:</strong> {props.code}</p>

      <p><strong>Credits:</strong> {props.credits}</p>

      <p><strong>Grade:</strong> {props.grade}</p>

      <button onClick={() => props.onEnroll(props.course)}>
        Enroll
      </button>
    </div>
  );
}

export default CourseCard;