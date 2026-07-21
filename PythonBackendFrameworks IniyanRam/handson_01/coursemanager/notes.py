'''
TASK - 1
1. Request–Response Cycle

Every interaction between a user and a website follows the Request–Response Cycle.

Example:

When a user visits:

http://127.0.0.1:8000/api/courses/

the browser does not automatically know what information to display. Instead, it sends an HTTP GET request to the Django server requesting the required resource.

The request then passes through multiple layers before an HTTP response is returned to the browser.

Complete Request–Response Flow

Browser
    ↓
HTTP Request
    ↓
Web Server (Development Server during local development)
    ↓
WSGI / ASGI Interface
    ↓
Django Framework
    ↓
Middleware
    ↓
URL Router (urls.py)
    ↓
View (views.py)
    ↓
Model (models.py)
    ↓
Django ORM
    ↓
Database
    ↓
ORM converts SQL results into Python objects
    ↓
View processes the data
    ↓
HttpResponse / JsonResponse
    ↓
Middleware
    ↓
Browser receives the HTTP Response

This process is repeated every time a client interacts with a Django application.



# 2. Middleware

Middleware is a software layer that executes during both the request-processing and response-processing phases of every HTTP transaction.

It acts as an intermediary between the web server and Django's business logic, allowing common functionality to be performed before a request reaches the view and after a response is generated.

Since middleware is independent of individual views, it is mainly used for application-wide functionality such as:

• Authentication
• Authorization
• Security
• Session management
• Request logging
• Caching
• Response modification

Each middleware receives the incoming request, performs its assigned task, and either passes the request to the next middleware or stops further processing if necessary. After the response is created, middleware components execute again in reverse order before the response is returned to the client.

Every middleware can:

• Inspect the request
• Modify the request
• Reject the request
• Inspect the response
• Modify the response


Common Built-in Middleware

1. SecurityMiddleware

SecurityMiddleware automatically provides several security features such as:

• HTTPS redirection
• Security headers
• Protection against common web attacks


2. AuthenticationMiddleware

AuthenticationMiddleware identifies the currently logged-in user.

It connects the current HTTP request with Django's authentication system, making the logged-in user available through:

request.user

Without this middleware, Django cannot determine who made the request.



# 3. WSGI vs ASGI

The browser communicates using the HTTP protocol, whereas Django applications are written in Python.

A translator is therefore required to convert web server requests into Python calls that Django can understand.

That translator is either WSGI or ASGI.


WSGI (Web Server Gateway Interface)

WSGI is Django's traditional deployment interface.

It works synchronously, meaning one worker generally processes one request at a time.

WSGI is suitable for:

• Traditional websites
• REST APIs
• CRUD applications
• Django Admin

Examples include:

• Blog applications
• E-commerce websites
• School Management Systems
• Course Management Systems

WSGI is the default interface used by Django.


ASGI (Asynchronous Server Gateway Interface)

ASGI is the modern deployment interface that supports asynchronous programming.

Instead of blocking while waiting for slow operations, multiple requests can make progress simultaneously.

ASGI supports:

• WebSockets
• Real-time chat
• Live notifications
• Streaming responses
• Async views

ASGI should be used whenever an application requires real-time communication or asynchronous processing.



# 4. MVC and Django's MVT Architecture

Model-View-Controller (MVC) is a popular software architecture that separates an application into three independent components, improving modularity, maintainability, and separation of concerns.


MVC Components

Model

Represents the application's data layer and communicates with the database.

View

Represents the presentation layer responsible for displaying information to users.

Controller

Contains the application's business logic, processes requests, communicates with models, and determines which view should be displayed.


Django follows a closely related architecture called Model-View-Template (MVT).


Model

Represents database entities and communicates with the database using Django's ORM.

View

Receives HTTP requests, performs business logic, validates input, communicates with models, and generates the appropriate HTTP response.

In Django, the View performs responsibilities similar to the Controller in MVC.

Template

Represents the presentation layer responsible for rendering HTML pages.

Templates receive data from views and generate dynamic web pages by combining HTML with application data.


MVC vs Django MVT Mapping

MVC Model        → Django Model

MVC View         → Django Template

MVC Controller   → Django View


Django also manages URL routing, middleware execution, and request dispatching internally, reducing the amount of controller code developers need to write.



# 5. Django Project vs Django App

A Django Project represents the complete web application and contains all the global configuration required to run it.

Important project files include:

manage.py
    Executes Django management commands.

settings.py
    Contains project-wide configuration.

urls.py
    Defines the root URL routing.

wsgi.py
    Used for WSGI deployment.

asgi.py
    Used for ASGI deployment.


A Django App is a modular and reusable component responsible for implementing a specific feature within the project.

Examples of apps in a Course Management System include:

• Courses
• Students
• Departments
• Enrollments
• Authentication

Each app typically contains its own:

• models.py
• views.py
• urls.py
• admin.py
• migrations
• tests.py

This modular architecture promotes code reusability, simplifies maintenance, allows independent development of features, and enables multiple apps to work together within a single Django project.
'''