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
