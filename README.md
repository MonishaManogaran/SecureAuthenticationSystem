# Django Custom User Authentication Project

This Django project implements a custom user authentication system with both web views and REST API endpoints. It uses a custom user model with email as the unique identifier and includes additional fields such as first name, last name, and phone number. The project supports JWT-based authentication for secure API access.

---

## Features

- Custom User model with email, first name, last name, and phone number
- User registration and login with validation via Django views
- JWT authentication with token obtain and refresh endpoints
- REST API endpoints for user registration and fetching authenticated user data
- Login-protected views and API endpoints

---

## Project Details

### API Views and Endpoints

| Endpoint            | Method | Description                                      | Authentication            |
|---------------------|--------|------------------------------------------------|---------------------------|
| `/register/`        | POST   | Register a new user                             | Public                    |
| `/loginn/`          | POST   | Obtain JWT access and refresh tokens           | Public                    |
| `/token/refresh/`   | POST   | Refresh JWT access token                         | Public                    |
| `/homeapi/`         | GET    | Retrieve authenticated user details             | Requires JWT authentication|



