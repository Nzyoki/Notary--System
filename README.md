# Notary System
The Notary System is a Flask-based web application designed to facilitate document management and notarization. Users can upload documents, manage them (create, read, update, delete), and have them notarized by registered notary users. The app features a modern, visually appealing interface with a vibrant color scheme (teal, coral, gold), a background image, smooth animations, and a responsive design, ensuring a delightful user experience.

## Features

- **User Authentication**:
  - Sign up as a regular user or notary.
  - Log in and log out securely with Flask-Login.
- **Document Management (CRUD)**:
  - **Create**: Upload documents (PDF, DOC, DOCX).
  - **Read**: View uploaded documents in a dashboard.
  - **Update**: Edit document filenames or replace files.
  - **Delete**: Remove documents from the database and filesystem.
- **Notary Functionality**:
  - Notaries can assign themselves to documents and approve them, updating the document status.
- **Error Handling**:
  - Flash messages for user feedback (success, error).
  - Secure file uploads with validation for allowed file types.


## Project Structure
Notary--System/
├── app/
│   ├── __init__.py          
│   ├── models.py           
│   ├── routes/
│   │   ├── auth.py          
│   │   ├── document.py     
│   │   ├── notary.py        
│   ├── templates/
│   │   ├── base.html        
│   │   ├── login.html       
│   │   ├── signup.html      
│   │   ├── dashboard.html   
│   │   ├── upload.html      
│   │   ├── edit_document.html 
│   │   ├── notary_dashboard.html 
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css    
│   │   ├── images/
│   │   │   ├── inaki-del-olmo-NIJuEQw0RKg-unsplash.jpg 
│   ├── uploads/             
├── config.py                
├── run.py                  
├── requirements.txt         
├── notary.db               

## Prerequisites

- **Python 3.12** 
- **Virtualenv**
- A modern web browser (e.g., Chrome, Firefox)


## Installation

### 1. Clone the Repository
Clone the project to your local machine (if using Git).

```bash
git clone git@github.com:Nzyoki/Notary--System.git
cd notary--system
Create and activate a virtual environment to manage dependencies.
python3 -m venv venv
source venv/bin/activate 
Install the required Python packages listed in `requirements.txt`.
pip install -r requirements.txt
**requirements.txt**:
Flask==2.3.3
Flask-SQLAlchemy==3.0.5
Flask-Login==0.6.2
Werkzeug==2.3.7
The app uses SQLite (`notary.db`) for data storage. Initialize the database by creating the necessary tables.
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
>>> exit()
```

This creates `notary.db` in the project root.

### 5. Run the Application
Start the Flask development server.
python run.py


**Expected Output**:

 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000


Open your browser and navigate to `http://127.0.0.1:5000/login`.

---

## Usage

### 1. Access the App
- **URL**: `http://127.0.0.1:5000/login`
- The app redirects to the login page (`/login`) if not authenticated.

### 2. Sign Up
- Navigate to `/signup`.
- Create a user:
  - Username: e.g., `testuser`
  - Email: e.g., `test@example.com`
  - Password: e.g., `password`
  - Optionally, check “Register as Notary” to create a notary user (e.g., `notary1`).
- Success message: “Account created! Please log in.”

### 3. Log In
- Go to `/login`.
- Enter credentials (e.g., `testuser`, `password`).
- Redirects to `/dashboard`.

### 4. Document Management (CRUD)
- **Upload a Document**:
  - Go to `/upload`.
  - Upload a PDF, DOC, or DOCX file.
  - Redirects to `/dashboard` with a success message.
- **View Documents**:
  - At `/dashboard`, see a table of your documents (filename, status, uploaded date).
- **Edit a Document**:
  - In `/dashboard`, click “Edit” on a document.
  - Update the filename or upload a new file.
  - Save changes to return to `/dashboard`.
- **Delete a Document**:
  - In `/dashboard`, click “Delete” on a document.
  - Confirm the deletion prompt.
  - Document is removed from the database and filesystem.

### 5. Notary Actions
- Log in as a notary user (e.g., `notary1`).
- Go to `/notary/dashboard`.
- **Assign**: Click “Assign” to take ownership of a document.
- **Approve**: Once assigned, click “Approve” to change the document’s status to “approved”.

### 6. Log Out
- Click “Logout” in the navbar to return to `/login`.

## Dependencies

- **Flask**: Web framework.
- **Flask-SQLAlchemy**: ORM for database management.
- **Flask-Login**: User authentication.
- **Werkzeug**: Password hashing.
- **Tailwind CSS**

## License
-This project is licensed under the MIT License. 

## Authors
-Andrew Ndarua
-Moureen Mutinda
-Gabriel Kinyua
-Scolastica Nzyoki
