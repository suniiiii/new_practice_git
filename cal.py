from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("calculator.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        
        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid Operation"

        return render_template("calculator.html", result=result)
    except ValueError:
        return render_template("calculator.html", result="Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True)

