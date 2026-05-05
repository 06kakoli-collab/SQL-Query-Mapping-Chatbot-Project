from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


def run_query(query):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows



def is_dangerous(message):
    message = message.lower()
    if "drop" in message:
        return True
    if "delete" in message:
        return True
    if "update" in message:
        return True
    if "alter" in message:
        return True
    if "truncate" in message:
        return True
    if "insert" in message:
        return True
    return False



def find_query(message):
    message = message.lower()

    if "all students" in message or "show all students" in message or "list students" in message:
        query = "SELECT * FROM students"
        return query

    elif " show attendance" in message and "below 75%" in message:
        query = "SELECT name, department, attendance FROM students WHERE attendance < 75"
        return query

    elif "show low" in message and "attendance" in message:
        query = "SELECT name, department, attendance FROM students WHERE attendance < 75"
        return query

    elif "cse" in message:
        query = "SELECT * FROM students WHERE department = 'CSE'"
        return query

    elif "ece" in message:
        query = "SELECT * FROM students WHERE department = 'ECE'"
        return query

    elif "my" in message and "department" in message:
        query = "SELECT * FROM students WHERE department = 'ME'"
        return query

    elif "show cgpa" in message and "above 8.0" in message:
        query = "SELECT name, department, cgpa FROM students WHERE cgpa > 8"
        return query

    elif "show cgpa" in message and "greater than 8.0" in message:
        query = "SELECT name, department, cgpa FROM students WHERE cgpa > 8"
        return query

    elif "show cgpa" in message and "below 6.0" in message:
        query = "SELECT name, department, cgpa FROM students WHERE cgpa < 6"
        return query

    elif "show cgpa" in message and "lower than 6.0" in message:
        query = "SELECT name, department, cgpa FROM students WHERE cgpa < 6"
        return query

    elif "show students with pending fees" in message:
        query = "SELECT s.name, f.total_fee, f.paid_fee, (f.total_fee - f.paid_fee) FROM students s JOIN fees f ON s.student_id = f.student_id WHERE f.paid_fee < f.total_fee"
        return query

    elif " show students whose fee" in message and "is paid" in message:
        query = "SELECT s.name, f.total_fee, f.paid_fee, (f.total_fee - f.paid_fee) FROM students s JOIN fees f ON s.student_id = f.student_id WHERE f.paid_fee < f.total_fee"
        return query

    elif "show placed students" in message:
        query = "SELECT s.name, p.company_name, p.package_lpa FROM students s JOIN placements p ON s.student_id = p.student_id WHERE p.status = 'Placed'"
        return query

    elif "show placement of students" in message:
        query = "SELECT s.name, p.company_name, p.package_lpa FROM students s JOIN placements p ON s.student_id = p.student_id WHERE p.status = 'Placed'"
        return query

    elif "show highest package" in message:
        query = "SELECT s.name, p.company_name, p.package_lpa FROM students s JOIN placements p ON s.student_id = p.student_id ORDER BY p.package_lpa DESC LIMIT 1"
        return query

    elif "show best package" in message:
        query = "SELECT s.name, p.company_name, p.package_lpa FROM students s JOIN placements p ON s.student_id = p.student_id ORDER BY p.package_lpa DESC LIMIT 1"
        return query

    elif "show topper student" in message:
        query = "SELECT name, department, cgpa FROM students ORDER BY cgpa DESC LIMIT 1"
        return query

    elif "show student with highest cgpa" in message:
        query = "SELECT name, department, cgpa FROM students ORDER BY cgpa DESC LIMIT 1"
        return query

    elif "show students from first year" in message or "year 1 students" in message:
        query = "SELECT * FROM students WHERE year = 1"
        return query

    elif "show students from second year" in message or "year 2 students" in message:
        query = "SELECT * FROM students WHERE year = 2"
        return query

    elif "show subjects" in message:
        query = "SELECT * FROM subjects"
        return query

    else:
        return None



@app.route("/")
def home():
    with open("proj_templates/index.html", "r") as f:
        return f.read()



@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data["message"]

    
    if is_dangerous(user_message) == True:
        return jsonify({
            "response": "Sorry, I cannot run that kind of command. Please ask about students, fees, or placements.",
            "query": None,
            "data": []
        })

    
    query = find_query(user_message)

    
    if query == None:
        return jsonify({
            "response": "Sorry, I cannot understand your question. Try asking about attendance, fees, CGPA, department, or placement.",
            "query": None,
            "data": []
        })

    
    results = run_query(query)

    
    if len(results) == 0:
        return jsonify({
            "response": "No results found.",
            "query": query,
            "data": []
        })

    
    final = []
    for row in results:
        final.append(list(row))

    return jsonify({
        "response": "Here are the results:",
        "query": query,
        "data": final
    })


if __name__ == "__main__":
    app.run(debug=True)