# ✅ Hackathon Task Manager

A lightweight Flask-based task manager built for hackathon teams who need to track tasks, ownership, and progress without the overhead of a full project-management tool.

## Features
- Create and view tasks for your hackathon team
- Lightweight, single-server setup — no external dependencies beyond Flask
- Simple HTML templates for a fast, no-friction UI during time-pressured hackathon use

## Tech Stack
- Python 3
- Flask
- Jinja2 templates (HTML)

## Installation
```bash
git clone https://github.com/Bhavyashah2710/hackathon-task-manager.git
cd hackathon-task-manager
pip install -r requirements.txt
python app.py
```

Then open your browser to `http://localhost:5000`.

## Usage
1. Run `python app.py` to start the local server
2. Add tasks for your team through the web interface
3. Track task status as your hackathon progresses

## Screenshots
> _Add a screenshot of the task list / task creation view here._
> `![Task list](screenshots/task-list.png)`

## Project Structure
```
hackathon-task-manager/
├── app.py              # Flask application entry point and routes
├── templates/           # Jinja2 HTML templates
├── requirements.txt     # Python dependencies
└── README.md
```

## Future Improvements
- [ ] Add task ownership/assignment to specific team members
- [ ] Add task status (To Do / In Progress / Done) with a simple board view
- [ ] Add persistent storage (SQLite) instead of in-memory state, if not already present
- [ ] Add basic auth so each team's board is private
- [ ] Add a `pytest` test suite covering the core routes
- [ ] Deploy a live demo (Render/Railway/Heroku free tier)

## Author
**Bhavya Shah**
GitHub: [@Bhavyashah2710](https://github.com/Bhavyashah2710)
