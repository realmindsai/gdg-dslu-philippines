# ABOUTME: Deliberately broken Flask app with N+1 query performance bug.
# ABOUTME: Used as exercise material for "Debug Like Pike" (Exercise 4, Slide 14).

from flask import Flask, render_template_string
import sqlite3
import os
import time

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'dashboard.db')


def init_db():
    """Create sample data for the dashboard."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT,
        budget REAL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department_id INTEGER,
        salary REAL,
        hire_date TEXT,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        title TEXT,
        employee_id INTEGER,
        status TEXT,
        created_date TEXT,
        FOREIGN KEY (employee_id) REFERENCES employees(id)
    )''')

    # Only seed if empty
    c.execute('SELECT COUNT(*) FROM departments')
    if c.fetchone()[0] == 0:
        departments = [
            ('Engineering', 500000), ('Marketing', 200000), ('Sales', 300000),
            ('HR', 150000), ('Finance', 250000), ('Operations', 350000),
            ('Support', 180000), ('Research', 400000), ('Legal', 220000),
            ('Product', 280000),
        ]
        c.executemany('INSERT INTO departments (name, budget) VALUES (?, ?)', departments)

        import random
        random.seed(42)
        first_names = ['Juan', 'Maria', 'Jose', 'Ana', 'Pedro', 'Rosa', 'Carlos', 'Elena',
                       'Miguel', 'Sofia', 'Diego', 'Lucia', 'Marco', 'Isabella', 'Rafael',
                       'Carmen', 'Gabriel', 'Teresa', 'Antonio', 'Patricia']
        last_names = ['dela Cruz', 'Santos', 'Reyes', 'Garcia', 'Mendoza', 'Torres',
                      'Villanueva', 'Ramos', 'Cruz', 'Lopez', 'Gonzales', 'Hernandez',
                      'Aquino', 'Bautista', 'Fernandez', 'Rivera', 'Castillo', 'Morales',
                      'Flores', 'Navarro']

        for i in range(200):
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            dept_id = random.randint(1, 10)
            salary = round(random.uniform(25000, 120000), 2)
            month = random.randint(1, 12)
            year = random.randint(2018, 2025)
            c.execute('INSERT INTO employees (name, department_id, salary, hire_date) VALUES (?, ?, ?, ?)',
                      (name, dept_id, salary, f'{year}-{month:02d}-01'))

        statuses = ['pending', 'in_progress', 'completed', 'blocked']
        task_titles = ['Review code', 'Update docs', 'Fix bug', 'Deploy feature', 'Write tests',
                       'Design mockup', 'Client call', 'Sprint planning', 'Code review', 'Database migration']

        for i in range(2000):
            emp_id = random.randint(1, 200)
            title = f"{random.choice(task_titles)} #{random.randint(1000, 9999)}"
            status = random.choice(statuses)
            month = random.randint(1, 12)
            c.execute('INSERT INTO tasks (title, employee_id, status, created_date) VALUES (?, ?, ?, ?)',
                      (title, emp_id, status, f'2025-{month:02d}-{random.randint(1,28):02d}'))

    conn.commit()
    conn.close()


# BUG: N+1 query problem - fetches each employee's tasks one at a time
def get_department_stats():
    """Get stats for each department. This is where the performance bug lives."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('SELECT id, name, budget FROM departments')
    departments = c.fetchall()

    stats = []
    for dept_id, dept_name, budget in departments:
        c.execute('SELECT id, name, salary FROM employees WHERE department_id = ?', (dept_id,))
        employees = c.fetchall()

        dept_tasks_total = 0
        dept_tasks_completed = 0
        dept_salary_total = 0

        # BUG: N+1 query - one query per employee to count their tasks
        for emp_id, emp_name, salary in employees:
            dept_salary_total += salary

            c.execute('SELECT COUNT(*) FROM tasks WHERE employee_id = ?', (emp_id,))
            task_count = c.fetchone()[0]
            dept_tasks_total += task_count

            c.execute('SELECT COUNT(*) FROM tasks WHERE employee_id = ? AND status = "completed"',
                      (emp_id,))
            completed = c.fetchone()[0]
            dept_tasks_completed += completed

        completion_rate = (dept_tasks_completed / dept_tasks_total * 100) if dept_tasks_total > 0 else 0

        stats.append({
            'name': dept_name,
            'budget': budget,
            'headcount': len(employees),
            'total_salary': dept_salary_total,
            'total_tasks': dept_tasks_total,
            'completed_tasks': dept_tasks_completed,
            'completion_rate': round(completion_rate, 1),
        })

    conn.close()
    return stats


DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head><title>Company Dashboard</title>
<style>
body { font-family: Arial, sans-serif; margin: 40px; background: #f4f6fa; }
h1 { color: #1e2235; }
table { border-collapse: collapse; width: 100%; background: white; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
th, td { padding: 12px 16px; text-align: left; border-bottom: 1px solid #eee; }
th { background: #1e2235; color: white; }
tr:hover { background: #f8f9fc; }
.metric { font-size: 13px; color: #666; margin-top: 20px; }
.slow-warning { color: #e76f51; font-weight: bold; }
</style>
</head>
<body>
<h1>Company Dashboard</h1>
<p class="metric">Rendered in <span class="{{ 'slow-warning' if render_time > 0.5 else '' }}">{{ "%.2f"|format(render_time) }}s</span></p>
<table>
<tr>
    <th>Department</th><th>Budget</th><th>Headcount</th>
    <th>Total Salary</th><th>Tasks</th><th>Completed</th><th>Completion %</th>
</tr>
{% for dept in stats %}
<tr>
    <td>{{ dept.name }}</td>
    <td>PHP {{ "{:,.0f}"|format(dept.budget) }}</td>
    <td>{{ dept.headcount }}</td>
    <td>PHP {{ "{:,.0f}"|format(dept.total_salary) }}</td>
    <td>{{ dept.total_tasks }}</td>
    <td>{{ dept.completed_tasks }}</td>
    <td>{{ dept.completion_rate }}%</td>
</tr>
{% endfor %}
</table>
</body>
</html>
'''


@app.route('/')
def dashboard():
    start = time.time()
    stats = get_department_stats()
    render_time = time.time() - start
    return render_template_string(DASHBOARD_TEMPLATE, stats=stats, render_time=render_time)


if __name__ == '__main__':
    init_db()
    print("Dashboard running at http://localhost:5000")
    print("Notice how slow it is? That's the bug you need to find.")
    app.run(debug=False, port=5000)
