from flask import Flask, render_template, request

app = Flask(__name__)

def feng_shui_number(date_of_birth):
    try:
        year, month, day = map(int, date_of_birth.split('-'))
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."

    initial_sum = year + month + day

    while initial_sum > 9:
        initial_sum = sum(int(digit) for digit in str(initial_sum))

    return initial_sum

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    date_of_birth = request.form['dob']
    result = feng_shui_number(date_of_birth)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
