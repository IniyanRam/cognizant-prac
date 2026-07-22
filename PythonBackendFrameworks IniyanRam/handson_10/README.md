## Microservices Breakdown

- Student Service | student CRUD, enrollment | /api/students | student_db
- Course Service | department and course CRUD | /api/courses | course_db
- Auth Service | registration, login, token | /api/auth | user_db
- Notification Service | email confirmations | /api/notifications | notif_db

## Trade-offs of synchronous vs asynchronous inter-service communication

Synchronous inter-service calls create tight coupling — if Course Service is down, enrollment fails.
Message queues decouple services at the cost of eventual consistency.
Use a message queue like RabbitMQ or Kafka when you don't need immediate validation and want high availability and decoupling.
