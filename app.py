from flask import Flask, render_template, request, redirect, url_for, session
import json
import os

app = Flask(__name__)
app.secret_key = "hackathon_pro_key"

DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
TASKS_FILE = os.path.join(DATA_DIR, 'tasks.json')

# Create folders and files if they don't exist
if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)
if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w') as f: json.dump({}, f)
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f: json.dump([], f)

def read_json(filepath):
    with open(filepath, 'r') as file: return json.load(file)

def write_json(filepath, data):
    with open(filepath, 'w') as file: json.dump(data, file, indent=4)

@app.route('/')
def home():
    if 'username' in session: 
        return redirect(url_for('dashboard'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_json(USERS_FILE)
        
        if username in users: 
            return "User already exists! <br><br> <a href='/login'>Go to Login</a>"
            
        users[username] = {'password': password}
        write_json(USERS_FILE, users)
        return redirect(url_for('login')) # Auto-redirect to login after register
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = read_json(USERS_FILE)
        
        if username in users and users[username]['password'] == password:
            session['username'] = username
            return redirect(url_for('dashboard'))
            
        return "Invalid Username or Password! <br><br> <a href='/login'>Try again</a>"
        
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session: 
        return redirect(url_for('login'))
        
    username = session['username']
    tasks = read_json(TASKS_FILE)
    
    if request.method == 'POST':
        task_desc = request.form['task_desc']
        tasks.append({
            'id': len(tasks) + 1, 
            'description': task_desc, 
            'assignee': username, 
            'status': 'Pending'
        })
        write_json(TASKS_FILE, tasks)
        return redirect(url_for('dashboard'))
        
    return render_template('dashboard.html', username=username, tasks=tasks)

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 'username' not in session: return redirect(url_for('login'))
    tasks = read_json(TASKS_FILE)
    for t in tasks:
        if t['id'] == task_id: 
            t['status'] = 'Completed'
    write_json(TASKS_FILE, tasks)
    return redirect(url_for('dashboard'))
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 'username' not in session: 
        return redirect(url_for('login'))
        
    tasks = read_json(TASKS_FILE)
    # Sirf wahi tasks rakho jinka ID match nahi karta (matlab matching ID wala delete ho gaya)
    updated_tasks = [t for t in tasks if t['id'] != task_id]
    
    write_json(TASKS_FILE, updated_tasks)
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
