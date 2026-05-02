# FlowOps

FlowOps is a full-stack application designed to streamline internal request workflows by centralizing request submission, tracking, and updates.

## Features
- User authentication (login, signup, logout)
- Create, view, update, and delete requests (full CRUD)
- Track request status (Requested → In Progress → Completed)
- Add updates/comments to requests
- Ownership-based access control (users can only modify their own data)
- Paginated dashboard for viewing requests
- React frontend connected to a Flask backend

## Tech Stack
**Frontend**
- React
- React Router
- CSS

**Backend**
- Flask
- SQLAlchemy
- Flask-Migrate
- Flask-Bcrypt

**Database**
- SQLite 

## How to Run

### Backend
cd server
source .venv/bin/activate
python app.py

### Frontend
cd client
npm install
npm run dev

## Test Login
Email: zachary@example.com  
Password: password123

## MVP Version
https://github.com/YOUR_USERNAME/flowops/tree/mvp-v1

## Author
Zachary Mowatt