from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Sample questions
questions = [
    {"question": "What does 'PEP' stand for?", "options": ["Python Enhancement Proposal", "Python Extended Program", "Python Easy Project"], "answer": "Python Enhancement Proposal"},
    {"question": "Which of the following is not a valid Python data type?", "options": ["List", "Tuple", "ArrayList"], "answer": "ArrayList"},
    {"question": "What is the output of print(type([]))?", "options": ["<class 'list'>", "<class 'dict'>", "<class 'set'>"], "answer": "<class 'list'>"},
    {"question": "What is the correct file extension for Python files?", "options": [".py", ".pt", ".python"], "answer": ".py"},
    {"question": "Which keyword is used to create a function in Python?", "options": ["func", "def", "define"], "answer": "def"},
    {"question": "What is the output of 2 ** 3?", "options": ["8", "9", "6"], "answer": "8"},
    {"question": "Which of the following is a mutable data type?", "options": ["List", "Tuple", "String"], "answer": "List"},
    {"question": "What is the built-in function to get the length of a list?", "options": ["len()", "length()", "count()"], "answer": "len()"},
    {"question": "Which operator is used to concatenate strings?", "options": ["+", "*", "&"], "answer": "+"},
    {"question": "What will be the output of print(bool(''))?", "options": ["True", "False"], "answer": "False"},
    {"question": "Which module is used for regular expressions?", "options": ["regex", "re", "regexp"], "answer": "re"},
    {"question": "What is the purpose of the 'pass' statement in Python?", "options": ["To skip the current loop iteration", "To terminate a function", "To create a placeholder for future code"], "answer": "To create a placeholder for future code"},
    {"question": "What does the 'self' keyword refer to in a class?", "options": ["The class itself", "The current instance of the class", "The parent class"], "answer": "The current instance of the class"},
    {"question": "Which of the following can be used to create a generator?", "options": ["List comprehension", "Function with yield", "Both"], "answer": "Both"},
    {"question": "What will be the output of print([1, 2, 3] + [4, 5, 6])?", "options": ["[1, 2, 3, 4, 5, 6]", "[1, 2, 3][4, 5, 6]", "[1, 2, 3 4, 5, 6]"], "answer": "[1, 2, 3, 4, 5, 6]"},
    {"question": "What is the default value of the 'break' statement in a loop?", "options": ["True", "False", "None"], "answer": "None"},
    {"question": "What is the output of print(type(()))?", "options": ["<class 'list'>", "<class 'tuple'>", "<class 'set'>"], "answer": "<class 'tuple'>"},
    {"question": "How do you start a comment in Python?", "options": ["//", "#", "/*"], "answer": "#"},
    {"question": "What is the purpose of the 'return' statement?", "options": ["To exit a function", "To return a value from a function", "Both"], "answer": "Both"},
    {"question": "Which function can be used to read a file in Python?", "options": ["open()", "read()", "file()"], "answer": "open()"},
    {"question": "Which of the following is not a loop in Python?", "options": ["for", "while", "repeat"], "answer": "repeat"},
    {"question": "What is the correct way to import a module in Python?", "options": ["import module_name", "include module_name", "using module_name"], "answer": "import module_name"},
    {"question": "What will be the output of print(1 == 1 and 2 == 2)?", "options": ["True", "False"], "answer": "True"},
    {"question": "Which method is used to remove whitespace from the beginning and end of a string?", "options": ["trim()", "strip()", "clear()"], "answer": "strip()"},
    {"question": "Which built-in function can be used to convert a string to an integer?", "options": ["int()", "str()", "float()"], "answer": "int()"},
]

@app.route('/')
def index():
    session['score'] = 0
    session['questions_answered'] = 0
    session['used_questions'] = []
    return render_template('index.html', question=get_question())

def get_question():
    if len(session['used_questions']) >= len(questions):
        return None  
    while True:
        question = random.choice(questions)
        if question not in session['used_questions']:
            session['used_questions'].append(question)
            return question

@app.route('/answer', methods=['POST'])
def answer():
    selected_answer = request.form.get('answer')
    current_question = session['used_questions'][-1]

    if selected_answer == current_question['answer']:
        session['score'] += 1

    session['questions_answered'] += 1

    if session['questions_answered'] < 5:
        return render_template('index.html', question=get_question())
    else:
        return redirect(url_for('result'))

@app.route('/result')
def result():
    result_text = 'Pass' if session['score'] >= 3 else 'Fail'
    return render_template('result.html', score=session['score'], result=result_text)

if __name__ == '__main__':
    app.run(debug=True)
