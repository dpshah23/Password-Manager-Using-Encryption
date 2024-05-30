# Django Password Manager

A secure password manager built with Django, integrated with Firebase for database storage and authentication. This project ensures the encryption of passwords using the Python Cryptography library and follows best practices for security.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#usage)

## Features

- Secure user authentication with Firebase
- Password encryption using the Python Cryptography library
- Real-time database storage with Firebase
- Password management (add, view, update, delete)
- Environment variables for storing sensitive information

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Firebase account
- [Python Cryptography library](https://cryptography.io/)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-password-manager.git
    cd django-password-manager
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your Firebase project and obtain the Firebase credentials JSON file.

### Environment Variables

Store your Firebase credentials and other sensitive information in a `.env` file located in the project root directory. Create a `.env` file with the following structure:

```env
FIREBASE_API_KEY=your_firebase_api_key
FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
FIREBASE_DATABASE_URL=your_firebase_database_url
FIREBASE_PROJECT_ID=your_firebase_project_id
FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
FIREBASE_APP_ID=your_firebase_app_id
FIREBASE_MEASUREMENT_ID=your_firebase_measurement_id
SECRET_KEY=your_django_secret_key
```

> **Note:** Never share your `.env` file or its contents publicly.

### Firebase Configuration

1. Go to your Firebase project settings and find your project's credentials.
2. Download the `serviceAccountKey.json` file and place it in the project directory.

## Usage

1. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

2. Access the application in your web browser at `http://127.0.0.1:8000/`.

3. Register a new account or log in with your credentials.

4. Use the interface to manage your passwords securely.

