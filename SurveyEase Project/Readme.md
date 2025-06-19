# Project README

## Overview

This project is a web-based quiz application designed to facilitate user interaction with quizzes, scoring, and related functionalities. The application features modules for user authentication, quiz management, and a dashboard to track user performance. Below, each component of the project is described in detail.

---

### 1. `app.py`

**Purpose:** This is the main entry point for the application. It initializes the application, sets up routing, and starts the web server.

**Details:**

- Manages the overall application lifecycle.
- Configures the Flask application instance.
- Links various modules, such as user authentication (`login.py` and `register.py`), and quiz-related logic (`quiz.py` and `score.py`).
- Handles global configurations, such as database connectivity and secret keys.

**Usage:**
Run `app.py` to start the server and make the application accessible to users. Use `python app.py` from the command line to initiate the application.

---

### 2. `dashboard.py`

**Purpose:** Manages the user dashboard, providing insights into quiz performance and other personalized metrics.

**Details:**

- Displays user scores, progress, and overall statistics.
- May include features such as recent quizzes taken, leaderboard standings, and personalized recommendations.
- Interacts with `quiz.db` to fetch data and render it dynamically using templates from the `templates` directory.

**Usage:**
The dashboard is accessible after logging in. It provides a central interface for users to view their activities and progress.

---

### 3. `data.py`

**Purpose:** Handles data management tasks, including processing inputs and interacting with the database.

**Details:**

- Manages CRUD (Create, Read, Update, Delete) operations on `quiz.db`.
- Includes helper functions for data validation, transformation, and querying.
- Ensures data consistency and security.

**Usage:**
Used internally by other modules to abstract database operations and streamline data handling.

---

### 4. `login.py`

**Purpose:** Implements user authentication logic, enabling secure login functionality.

**Details:**

- Validates user credentials against the database.
- Implements session management to maintain user login states.
- Provides error handling for invalid login attempts.

**Usage:**
Accessed when users attempt to log in. It ensures secure access to the application.

---

### 5. `quiz.db`

**Purpose:** A SQLite database file that stores application data.

**Details:**

- Contains tables for user information, quiz questions, scores, and session data.
- Used by various modules to persist and retrieve data.

**Usage:**
Automatically accessed by the application. Ensure its integrity for the application to function correctly.

---

### 6. `quiz.py`

**Purpose:** Manages quiz logic, including question presentation and answer validation.

**Details:**

- Fetches quiz questions from the database.
- Processes user responses and calculates scores.
- Ensures proper sequencing and flow of quiz activities.

**Usage:**
Accessed during quiz-taking activities. It coordinates question delivery and score computation.

---

### 7. `register.py`

**Purpose:** Handles user registration, enabling new users to sign up.

**Details:**

- Validates user input, such as email and password.
- Inserts new user records into `quiz.db`.
- Prevents duplicate registrations by checking existing records.

**Usage:**
Used when users access the registration page. It ensures proper onboarding of new users.

---

### 8. `score.py`

**Purpose:** Manages score-related functionalities, including computation and storage.

**Details:**

- Calculates and updates user scores based on quiz performance.
- Fetches historical scores for display on the dashboard.
- Ensures score accuracy and consistency across the application.

**Usage:**
Integrated with quiz and dashboard modules. It is critical for tracking user performance.

---

### 9. `static` Directory

**Purpose:** Contains static assets, such as CSS, JavaScript, and images, used by the application.

**Details:**

- Enhances the visual and interactive aspects of the application.
- Provides shared resources for multiple pages.

**Usage:**
Assets from this directory are referenced in templates for styling and dynamic behavior.

---

### 10. `templates` Directory

**Purpose:** Houses HTML templates for rendering application pages.

**Details:**

- Includes templates for login, registration, quiz, dashboard, and error pages.
- Uses templating features like Jinja2 for dynamic content rendering.

**Usage:**
Templates are rendered by Flask routes to generate user-facing pages dynamically.

---

## How to Run the Project

1. Ensure Python and Flask are installed on your system.
2. Start the application using `python app.py`.
3. Access the application in your web browser at `http://localhost:5000/`.
