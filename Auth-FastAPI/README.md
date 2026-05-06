# FastAPI JWT Authentication Module 

A robust, stateless authentication module built with FastAPI. This project implements a secure user registration and login system utilizing JSON Web Tokens (JWT) and the standard OAuth2 "Password Bearer" flow.

## Features

*   **User Registration (`/signup`):** Securely creates new users and stores passwords using `bcrypt` hashing. Never stores plain-text credentials.
*   **Authentication & Token Generation (`/token`):** Validates user credentials and issues a cryptographically signed JWT with a configurable expiration time.
*   **Protected Routes (`/users/me`):** Demonstrates endpoint security by requiring a valid Bearer token in the Authorization header to access user data.
*   **Interactive API Docs:** Fully integrated with FastAPI's automatic Swagger UI for seamless testing in the browser.

## Tech Stack

*   **Framework:** [FastAPI](https://fastapi.tiangolo.com/)
*   **Server:** Uvicorn
*   **Cryptography & JWT:** `python-jose`, `passlib[bcrypt]`

## Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your machine.

### 2. Installation
Clone the repository and navigate to the project directory:

```bash
cd Auth-FastAPI 
```

### Some Screenshots :
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/54c3e9ee-a46b-41f2-86f3-32933b6ead4c" />

## Sign up:
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/6b3a420b-c4d4-44a2-afcb-50890f2f85c9" />

## Authorize:
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/ace2b552-9619-415d-ab07-e236859cce1f" />

## Get Method with JWT visible :
<img width="1470" height="956" alt="image" src="https://github.com/user-attachments/assets/aeb131da-9108-4ebc-b92b-89e5fb90c34a" />



