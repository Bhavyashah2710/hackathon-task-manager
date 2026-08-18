# ✅ Hackathon Task Manager

A lightweight **Flask-based task manager** built for hackathon teams to create, track, complete, and delete tasks with a simple login-based dashboard.

## 🚀 Live Demo

👉 **[Open Hackathon Task Manager](https://hackathon-task-manager.onrender.com)**

The application is deployed on **Render** and is available online.

## ✨ Features

- 🔐 User registration and login
- 📋 Create new tasks
- 👤 Automatically assign tasks to the logged-in user
- ⏳ Track task status
- ✅ Mark tasks as completed
- 🗑️ Delete tasks
- 🚪 Logout functionality
- 🌐 Live deployment on Render
- 📱 Simple and lightweight web interface

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – Backend framework
- **Jinja2** – HTML templating
- **HTML/CSS** – Frontend
- **JSON** – Data storage
- **Render** – Deployment

## 📂 Project Structure

```text
hackathon-task-manager/
├── app.py                  # Flask application and routes
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Home page
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   └── dashboard.html       # Task dashboard
├── data/                    # User and task data files
├── README.md                # Project documentation
└── requiremnets.txt         # Duplicate requirements file
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Bhavyashah2710/hackathon-task-manager.git
cd hackathon-task-manager
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Start the application

```bash
python app.py
```

### 4. Open in browser

```text
http://localhost:5000
```

## 📖 How to Use

1. Open the application.
2. Create a new account using the **Register** page.
3. Login with your username and password.
4. Add tasks from the dashboard.
5. Mark tasks as **Completed** when finished.
6. Delete tasks when they are no longer needed.
7. Logout when finished.

## ☁️ Deployment

This project is deployed using **Render**.

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
gunicorn app:app
```

### Live URL

https://hackathon-task-manager.onrender.com

## 🔮 Future Improvements

- [ ] Add task priority levels
- [ ] Add due dates and deadlines
- [ ] Add team member assignment
- [ ] Add task categories
- [ ] Add a Kanban-style board
- [ ] Improve password security with password hashing
- [ ] Move data storage from JSON to SQLite/PostgreSQL
- [ ] Add proper database persistence for production deployment
- [ ] Add automated tests with `pytest`
- [ ] Improve responsive design

## 👨‍💻 Author

**Bhavya Shah**

- GitHub: [@Bhavyashah2710](https://github.com/Bhavyashah2710)
- Project: [Hackathon Task Manager](https://github.com/Bhavyashah2710/hackathon-task-manager)

---

⭐ If you found this project useful, consider giving the repository a star!
