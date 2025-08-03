FastAPI & PostgreSQL Todo Application

A full-stack Todo application built with a modern Python backend using FastAPI, a PostgreSQL database with Alembic for migrations, and a stylish vanilla JavaScript frontend.

Features

    FastAPI Backend: A high-performance, easy-to-use API framework.

    PostgreSQL Database: A powerful, open-source relational database.

    SQLAlchemy ORM: Interact with the database using Python objects.

    Alembic Migrations: Manage database schema changes systematically.

    Pydantic Validation: Robust data validation and settings management.

    CORS Middleware: Securely handle requests from the frontend.

    Vanilla JS Frontend: A beautiful and responsive UI built with HTML, CSS, and JavaScript, styled with Tailwind CSS.

Prerequisites

Before you begin, ensure you have the following installed on your system:

    Python 3.8+

    PostgreSQL

    Git

Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing.
1. Clone the Repository

Clone this repository to your local machine:

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
cd YOUR_REPOSITORY_NAME

2. Set Up the Backend
Create a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

# Create the virtual environment
python -m venv venv

# Activate it (On Windows)
venv\Scripts\activate

# Activate it (On macOS/Linux)
source venv/bin/activate

Install Dependencies

Install all the required Python packages.

pip install -r requirements.txt

Configure Environment Variables

The application requires a .env file for the database connection string. Create a file named .env in the root of the project directory.

Copy the example below and replace the placeholder values with your actual PostgreSQL credentials.

# .env
DATABASE_URL="postgresql://YOUR_POSTGRES_USER:YOUR_POSTGRES_PASSWORD@localhost/YOUR_DATABASE_NAME"

Note: You will need to create a new database in PostgreSQL for this project (e.g., FSD or todo_db).
Run Database Migrations

Alembic is used to manage the database schema. Run the following command to apply all migrations and create the necessary tables.

alembic upgrade head

Run the Backend Server

You can now start the FastAPI server using Uvicorn.

uvicorn app.main:app --reload

The API will be running at http://127.0.0.1:8000. You can view the interactive API documentation at http://127.0.0.1:8000/docs.
3. Run the Frontend

The frontend is a single HTML file that communicates with the backend API.

    Make sure the backend server is running.

    Open the index.html file in your web browser.

You should now see the Todo application running, and you can start adding, updating, and deleting tasks!