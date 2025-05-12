from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    theme_color = "#c33764"  # ส่งไปที่ HTML ได้
    print("Loading index.html")
    return render_template('index.html', theme_color=theme_color)
    

@app.route('/spin', methods=['POST'])
def spin():
    print("Processing spin request...")
    data = request.json
    locked_number = data.get("locked_number")

    numbers = list(range(1, 11))

    if locked_number and 1 <= locked_number <= 10:
        print(f"Locked number: {locked_number}")
        return jsonify({"result": locked_number})

    result = random.choice(numbers)
    print(f"Random result: {result}")
    return jsonify({"result": result})

if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=True)
