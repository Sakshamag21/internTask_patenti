# Task 1: To-Do Application

## Project Overview

The To-Do Application has been successfully completed, meeting the following deliverables:

### 1. Task Operations

Users can perform the following operations on tasks:

- **Create**: Users can create new tasks.
- **Edit**: Users can edit existing tasks, modifying title, description, priority level, and deadline.
- **Delete**: Users can delete tasks that are no longer needed.

### 2. Task Attributes

Tasks are defined by the following attributes:

- **Title**: Each task has a title.
- **Description**: Tasks can include a detailed description.
- **Priority Level**: Tasks are categorized by priority levels.
- **Deadline**: Tasks have an associated deadline.

### 3. Task Completion

Users can mark tasks as complete, providing a clear indication of finished tasks.

### 4. Task Filtering

Users have the capability to filter tasks based on:

- **Priority**: Users can filter tasks by priority level.
- **Deadline**: Tasks can be filtered based on the deadline.
- **Completion Status**: Users can filter tasks based on whether they are finished or unfinished.

### 5. User Interface

The application boasts a clean and intuitive user interface, ensuring a seamless user experience.

### 6. Django's MVT Architecture

The application is implemented following Django's Model-View-Template (MVT) architecture. This ensures a structured and organized codebase, promoting maintainability and scalability.

### 7. Rate Limiting

To enhance security and prevent abuse, the application includes a Rate Limiting feature on its endpoints. This helps control the rate at which users can make requests.

### 8. Docker Containerization

The application is containerized using Docker, providing a consistent and isolated environment. This ensures that the application can run seamlessly across different environments without dependency issues.

## Getting Started

To run the application, follow these steps:

1. Ensure you have Docker installed on your machine.
2. Clone the repository: `git clone <repository-url>`
3. Navigate to the project directory: `cd <project-directory>`
4. Create Virtual enviroment: `python -m venv venv`
5. Install requirements:- `pip install -r requirements.txt`
6. Make migrations:- `python manage.py migrate`
7. Start the server:- `python manage.py runserver`

Using docker:

1. Follow first 3 steps.
2. Build the Docker image: `docker build -t todoapp .`
3. Run the Docker container: `docker run -p 8000:8000 todoapp`

The application will be accessible at [http://localhost:8000](http://localhost:8000).
