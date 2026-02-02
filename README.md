# LearnHub – Online Course / Learning Platform

A fully responsive learning platform built with **Django** (backend) and **Bootstrap 5, HTML, CSS** (frontend). Admins can upload courses and lessons; students can enroll, learn, and track progress.

## Features

- **User roles:** Admin, Student
- **Courses:** Title, category, description, thumbnail, level (Beginner/Intermediate/Advanced), duration, status (draft/published)
- **Lessons:** Title, video URL, text notes, order; access restricted to enrolled students
- **Enrollment:** Browse courses, enroll (free), confirmation page, My Learning dashboard
- **Progress:** Mark lessons complete, progress bar per course, percentage completion, resume from last lesson
- **UI:** Bootstrap 5 navbar (Courses, My Learning, Login/Logout), course cards, progress bars, responsive layout

## Project structure

```
learning_platform/     # Django project config
accounts/              # Auth: register, login, logout; custom User (Admin/Student)
courses/               # Course list, detail, categories; admin CRUD
lessons/               # Lessons per course; admin CRUD
enrollments/           # Enroll, My Learning, confirmation
progress/              # Lesson view, mark complete, progress tracking
templates/             # Base + app templates
static/css/            # Custom CSS (style.css)
media/                 # Uploaded thumbnails (created at runtime)
```

## Setup

1. **Create and activate virtual environment** (if not already):

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Seed 10 sample courses** (optional):

   ```bash
   python manage.py seed_courses
   ```

5. **Create a superuser** (Admin):

   ```bash
   python manage.py createsuperuser
   ```

   When prompted, set username, email, and password. To act as **Admin** on the platform, set the user’s **role** to **Admin** in Django Admin:  
   http://127.0.0.1:8000/admin/ → Users → edit your user → Role: Admin.

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   - **Site:** http://127.0.0.1:8000/  
   - **Admin:** http://127.0.0.1:8000/admin/

## Sample courses (after `seed_courses`)

1. **Python for Beginners** – Programming, Beginner, 6 hours  
2. **Web Development with Django** – Web Development, Intermediate, 12 hours  
3. **JavaScript Fundamentals** – Programming, Beginner, 8 hours  
4. **Data Science with Python** – Data Science, Intermediate, 10 hours  
5. **SQL and Databases** – Databases, Beginner, 5 hours  
6. **React.js for Frontend** – Web Development, Intermediate, 14 hours  
7. **Git and GitHub** – DevOps, Beginner, 4 hours  
8. **Machine Learning Basics** – Data Science, Advanced, 15 hours  
9. **HTML and CSS** – Web Development, Beginner, 7 hours  
10. **REST APIs with Django REST Framework** – Web Development, Advanced, 9 hours  

## Quick test flow

1. Open http://127.0.0.1:8000/ → browse courses.  
2. Sign up (Register) as a student.  
3. Open a course → **Enroll Now** → see confirmation → **Start first lesson**.  
4. Watch lesson, click **Mark as completed** → use **Next** / **Previous**.  
5. **My Learning** shows enrolled courses and progress bars; **Resume** continues from the next lesson.

## Tech stack

- **Backend:** Django 5.x, SQLite (default; can switch to PostgreSQL in `settings.py`)  
- **Frontend:** Bootstrap 5, HTML5, custom CSS  
- **Media:** Django `ImageField` for course thumbnails; static and media configured in `settings.py`
