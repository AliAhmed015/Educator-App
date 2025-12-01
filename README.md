# **Educator App**

This is a **FastAPI** project that demonstrates a scalable web application with authentication, rate-limiting, and role-based access control. It is organized with clear separation of concerns, including routers, controllers, repositories, and services.

## **Project Structure**

The project is organized in the following structure:

```
app
  ├── __init__.py
  ├── controllers
  │   ├── admin_controller.py
  │   ├── auth_controller.py
  │   ├── course_controller.py
  │   └── student_controller.py
  ├── database
  │   ├── database.py
  │   └── seeder.py
  ├── main.py
  ├── middleware
  │   └── middleware.py
  ├── models
  │   ├── admin_model.py
  │   ├── course_model.py
  │   └── student_model.py
  ├── repositories
  │   ├── admin_repository.py
  │   ├── course_repository.py
  │   └── student_repository.py
  ├── routers
  │   ├── admin_router.py
  │   ├── auth_router.py
  │   ├── course_router.py
  │   └── student_router.py
  ├── services
  │   ├── auth.py
  │   └── helping_functions.py
  ├── static
  │   └── favicon.png
  ├── validation
  │   └── validation.py
```

### **Key Components**

1. **app/main.py**

   * **Entry Point**: This is the main entry point of the application where the FastAPI app is created and configured. It includes:

     * **Lifespan function** to seed the database if it's empty.
     * **Favicon** management for the app.
     * **Routers** are mounted to the FastAPI app, imported from the routers folder.

2. **app/middleware/middleware.py**

   * **Middleware**: Contains a middleware for rate-limiting using **Redis**. The middleware applies rate limiting to protect the app from abuse and ensures scalability.

3. **app/routers/**

   * **Routers**: The folder contains different routers for handling user requests. These include:

     * **admin_router**: Routes for admin operations.
     * **student_router**: Routes for student operations.
     * **auth_router**: Routes for user authentication (login and registration).
     * **course_router**: Routes for course-related actions.
   * **Authentication**: Handled by dependency injection using JWT tokens. The token is verified using the `get_jwt_token` function in the `services/auth.py` file.
   * **Role Validation**: Ensures that only admins can access specific routes using role-based access control.

4. **app/controllers/**

   * **Controllers**: Each router is connected to a controller that processes incoming requests and interacts with the database through repositories.

     * `auth_controller.py`: Handles user authentication and registration.
     * `admin_controller.py`: Admin-specific operations (unused, but can be expanded in the future).
     * `student_controller.py`: Handles student-related operations.
     * `course_controller.py`: Handles course-related operations.

5. **app/repositories/**

   * **Repositories**: These files contain database querying functions to perform CRUD operations. Each controller interacts with these repository functions to handle data.

6. **app/services/**

   * **Services**: Contains utility functions:

     * **auth.py**: Functions for token creation and verification.
     * **helping_functions.py**: Functions for password hashing and other common tasks.

7. **app/validation/**

   * **Validation**: Contains functions for validating user roles and other business logic before processing requests.

8. **app/static/**

   * **Static Files**: Contains the favicon for the application.

---

## **Features**

* **JWT Authentication**: Secure user login and registration with token-based authentication.
* **Role-Based Access Control (RBAC)**: Ensures that only users with specific roles (e.g., admin) can access certain resources.
* **Rate Limiting**: Limits the number of requests a user can make within a specific time window, preventing abuse and protecting system resources.
* **Database Seeding**: Automatically seeds the database with initial values if it is empty on startup.
* **Modular and Scalable**: The application is divided into different modules, making it easy to scale and add more features.

---

## **Setup Instructions**

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. **Create and Activate a Virtual Environment**

It's recommended to use a virtual environment to isolate project dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. **Install Dependencies**

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. **Set Up the Database**

Ensure that your database is set up and the necessary tables are created. The database can be set up manually or use the provided seeder script.

### 5. **Run the Application**

To start the application, run:

```bash
uvicorn app.main:app --reload
```

This will start the FastAPI development server, and you can access the app at `http://127.0.0.1:8000`.

---

## **Authentication**

* **Registration**: Users can register via the `/register` endpoint, providing necessary details (username, password, etc.).
* **Login**: After registration, users can log in via the `/login` endpoint to receive a JWT token.
* **JWT Token**: Use the JWT token in the `Authorization` header for all protected routes.

Example of `Authorization` header:

```bash
Authorization: Bearer <your-token>
```

---

## **Testing**

To run the tests for the application, use the following command:

```bash
pytest
```

Make sure to set up the testing environment and database before running tests.

---

## **Contributing**

Feel free to fork the repository, create an issue, or submit a pull request if you want to contribute.
