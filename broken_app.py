# ABOUTME: Flask dashboard app for a company with departments, employees, and tasks.
# ABOUTME: Displays department-level statistics including headcount, salary, and task completion.

from flask import Flask, render_template_string
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), 'dashboard.db')


def init_db():
    """Create and seed the database with sample company data."""
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
                      (title, emp_id, status, f'2025-{month:02d}-{random.randint(1, 28):02d}'))

    conn.commit()
    conn.close()


def build_stat_collectors(departments, conn):
    """Create a list of query functions that each compute stats for one department."""
    collectors = []
    c = conn.cursor()

    for dept_id, dept_name, budget in departments:
        # Each collector queries the DB for one department's computed metrics
        def collect_metrics():
            c.execute('SELECT COUNT(*), COALESCE(SUM(salary), 0) FROM employees WHERE department_id = ?',
                      (dept_id,))
            headcount, total_salary = c.fetchone()

            c.execute('''SELECT COUNT(*) FROM tasks t
                         JOIN employees e ON t.employee_id = e.id
                         WHERE e.department_id = ?''', (dept_id,))
            total_tasks = c.fetchone()[0]

            c.execute('''SELECT COUNT(*) FROM tasks t
                         JOIN employees e ON t.employee_id = e.id
                         WHERE e.department_id = ? AND t.status = 'completed' ''', (dept_id,))
            completed_tasks = c.fetchone()[0]

            completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
            return headcount, total_salary, total_tasks, completed_tasks, round(completion_rate, 1)

        collectors.append((dept_name, budget, collect_metrics))

    return collectors


def get_department_stats():
    """Gather statistics for every department using collected stat functions."""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute('SELECT id, name, budget FROM departments ORDER BY name')
    departments = c.fetchall()

    collectors = build_stat_collectors(departments, conn)

    stats = []
    for dept_name, budget, collect in collectors:
        headcount, total_salary, total_tasks, completed_tasks, completion_rate = collect()
        stats.append({
            'name': dept_name,
            'budget': budget,
            'headcount': headcount,
            'total_salary': total_salary,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'completion_rate': completion_rate,
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
.summary { margin-top: 20px; color: #666; font-size: 14px; }
</style>
</head>
<body>
<h1>Company Dashboard</h1>
<table>
<tr>
    <th>Department</th><th>Budget</th><th>Headcount</th>
    <th>Total Salary</th><th>Tasks</th><th>Completed</th><th>Completion %</th>
</tr>
{% for dept in stats %}
<tr>
    <td>{{ dept.name }}</td>
    <td>PHP {{ "{:,.0f}".format(dept.budget) }}</td>
    <td>{{ dept.headcount }}</td>
    <td>PHP {{ "{:,.0f}".format(dept.total_salary) }}</td>
    <td>{{ dept.total_tasks }}</td>
    <td>{{ dept.completed_tasks }}</td>
    <td>{{ dept.completion_rate }}%</td>
</tr>
{% endfor %}
</table>
<p class="summary">{{ stats|length }} departments | Data from dashboard.db</p>
</body>
</html>
'''


@app.route('/')
def dashboard():
    stats = get_department_stats()
    return render_template_string(DASHBOARD_TEMPLATE, stats=stats)


if __name__ == '__main__':
    init_db()
    print("Dashboard running at http://localhost:5001")
    app.run(debug=False, host='0.0.0.0', port=5001)
