
// HANDS-ON 5 - MongoDB

use("college_nosql");

// TASK 1: Create Collection and Insert Documents

db.createCollection("feedback");

db.feedback.insertMany([
{
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent teaching. Highly recommended.",
    tags: ["well-structured", "interactive", "good-examples"],
    submitted_at: new Date("2022-11-30T10:15:00Z"),
    attachments: [
        { filename: "notes.pdf", size_kb: 240 }
    ]
},
{
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Very informative course.",
    tags: ["challenging", "useful"],
    submitted_at: new Date("2022-11-29T09:30:00Z"),
    attachments: [
        { filename: "assignment.pdf", size_kb: 180 }
    ]
},
{
    student_id: 3,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 3,
    comments: "Good but difficult.",
    tags: ["challenging", "fast-paced"],
    submitted_at: new Date("2022-11-28T14:20:00Z"),
    attachments: [
        { filename: "feedback.docx", size_kb: 75 }
    ]
},
{
    student_id: 4,
    course_code: "CS102",
    semester: "2023-EVEN",
    rating: 5,
    comments: "Loved every lecture.",
    tags: ["excellent", "interactive"],
    submitted_at: new Date("2023-05-15T11:00:00Z"),
    attachments: [
        { filename: "project.zip", size_kb: 520 }
    ]
},
{
    student_id: 5,
    course_code: "CS102",
    semester: "2023-EVEN",
    rating: 2,
    comments: "Needs more practical sessions.",
    tags: ["boring", "theory"],
    submitted_at: new Date("2023-05-16T13:40:00Z"),
    attachments: [
        { filename: "report.pdf", size_kb: 210 }
    ]
},
{
    student_id: 6,
    course_code: "CS103",
    semester: "2023-ODD",
    rating: 4,
    comments: "Interesting topics covered.",
    tags: ["interesting", "well-paced"],
    submitted_at: new Date("2023-11-01T09:00:00Z"),
    attachments: [
        { filename: "notes.docx", size_kb: 95 }
    ]
},
{
    student_id: 7,
    course_code: "CS104",
    semester: "2023-ODD",
    rating: 1,
    comments: "Very difficult course.",
    tags: ["hard", "confusing"],
    submitted_at: new Date("2023-11-02T15:45:00Z"),
    attachments: [
        { filename: "errors.txt", size_kb: 15 }
    ]
},
{
    student_id: 8,
    course_code: "CS105",
    semester: "2024-EVEN",
    rating: 5,
    comments: "Excellent lab sessions.",
    tags: ["practical", "excellent"],
    submitted_at: new Date("2024-04-20T12:15:00Z"),
    attachments: [
        { filename: "lab.pdf", size_kb: 320 }
    ]
},
{
    student_id: 9,
    course_code: "CS103",
    semester: "2024-EVEN",
    rating: 4,
    comments: "Very engaging instructor.",
    tags: ["interactive", "clear"],
    submitted_at: new Date("2024-04-21T10:30:00Z"),
    attachments: [
        { filename: "summary.pdf", size_kb: 140 }
    ]
},
{
    student_id: 10,
    course_code: "CS104",
    semester: "2024-EVEN",
    rating: 3,
    comments: "Average course with decent content.",
    tags: ["average", "theory"],
    submitted_at: new Date("2024-04-22T09:10:00Z")
}
]);

db.feedback.countDocuments();

// Output:
// 10 documents inserted successfully.



// TASK 2: CRUD Operations

// 65. Find all documents where rating = 5

db.feedback.find({
    rating: 5
});

// Output:
// Returned 3 documents with rating 5.


// 66. Find CS101 feedback containing the tag "challenging"

db.feedback.find({
    course_code: "CS101",
    tags: "challenging"
});

// Output:
// Returned 2 documents (student_id 2 and 3).


// 67. Projection

db.feedback.find(
    {},
    {
        student_id: 1,
        course_code: 1,
        rating: 1,
        _id: 0
    }
);

// Output:
// Returned only student_id, course_code and rating fields.


// 68. Add needs_review for ratings below 3

db.feedback.updateMany(
    {
        rating: { $lt: 3 }
    },
    {
        $set: {
            needs_review: true
        }
    }
);

// Output:
// matchedCount: 2
// modifiedCount: 2


// 69. Add reviewed tag

db.feedback.updateMany(
    {
        needs_review: true
    },
    {
        $push: {
            tags: "reviewed"
        }
    }
);

// Output:
// matchedCount: 2
// modifiedCount: 2


// Verify update

db.feedback.find({
    needs_review: true
});

// Output:
// Two documents now contain:
// needs_review : true
// tags include "reviewed"


// 70. Delete 2021-EVEN documents

db.feedback.deleteMany({
    semester: "2021-EVEN"
});

// Output:
// deletedCount: 0
// (No matching documents existed.)



// TASK 3: Aggregation Pipeline

// 71. Average rating per course for 2022-ODD

db.feedback.aggregate([
{
    $match: {
        semester: "2022-ODD"
    }
},
{
    $group: {
        _id: "$course_code",
        avg_rating: {
            $avg: "$rating"
        },
        feedback_count: {
            $sum: 1
        }
    }
},
{
    $sort: {
        avg_rating: -1
    }
}
]);

/* Output:
 {
   _id: "CS101",
   avg_rating: 4,
   feedback_count: 3
 }
*/

// 72. Rename avg_rating and round value

db.feedback.aggregate([
{
    $match: {
        semester: "2022-ODD"
    }
},
{
    $group: {
        _id: "$course_code",
        avg_rating: {
            $avg: "$rating"
        },
        feedback_count: {
            $sum: 1
        }
    }
},
{
    $project: {
        _id: 0,
        course_code: "$_id",
        average_rating: {
            $round: ["$avg_rating", 1]
        },
        feedback_count: 1
    }
},
{
    $sort: {
        average_rating: -1
    }
}
]);

/* Output:
 {
   course_code: "CS101",
   average_rating: 4,
   feedback_count: 3
 }
*/

// 73. Tag frequency leaderboard

db.feedback.aggregate([
{
    $unwind: "$tags"
},
{
    $group: {
        _id: "$tags",
        tag_count: {
            $sum: 1
        }
    }
},
{
    $sort: {
        tag_count: -1
    }
}
]);

/* Output (Top Results):
 interactive : 3
 challenging : 2
 excellent : 2
 reviewed : 2
 theory : 2
 Remaining tags appeared once.
*/

// 74. Create index and verify IXSCAN

db.feedback.createIndex({
    course_code: 1
});

// Output:
// course_code_1


db.feedback.find({
    course_code: "CS101"
}).explain("executionStats");

/* Output:
 Winning plan uses:
 stage : FETCH
 inputStage : IXSCAN
 indexName : course_code_1
 totalKeysExamined : 3
 totalDocsExamined : 3
 executionSuccess : true
*/
// IXSCAN confirms that the query uses the index instead of a collection scan (COLLSCAN).