from flask import Flask, request

app = Flask(__name__)

def validate_user_data(age_text):
    """Calculates age for next year from input string."""
    try:
        current_age = int(age_text)
        next_year_age = current_age + 1
        return f"Next year you will be {next_year_age}."
    except ValueError:
        return "Please enter a valid number!"

@app.route('/')
def home():
    # This creates a simple web form with a box and a button
    return """
        <h1>Age Calculator</h1>
        <form action="/calculate" method="POST">
            <input type="text" name="user_age" placeholder="Enter your age">
            <button type="submit">Calculate</button>
        </form>
    """

@app.route('/calculate', methods=['POST'])
def calculate():
    # This gets the data from the box and runs your function
    age_input = request.form.get('user_age')
    result = validate_user_data(age_input)
    return f"<h1>Result</h1><p>{result}</p><a href='/'>Go Back</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
