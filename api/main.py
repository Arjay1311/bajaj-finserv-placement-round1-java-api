from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/bf", methods=["POST"])
def foo():
    data = request.json

    user_id = "arjay_jg_13112004"
    email = "arjayjg1311@gmail.com"
    college_roll_number = "22BCE1510"

    arr_of_even_numbers = [str(int(i)) for i in data if i.isdigit() and int(i) % 2 == 0]
    arr_of_odd_numbers = [str(int(i)) for i in data if i.isdigit() and int(i) % 2 != 0]
    alphabets = [i for i in data if i.isalpha()]
    arr_of_special_characters = [i for i in data if not i.isalnum()]
    sum_of_numbers = str(sum(int(i) for i in data if i.isdigit()))
    concat_string = ''.join(alphabets)[::-1]

    response = {
        "is_success": "true",
        "user_id": user_id,
        "email": email,
        "college_roll_number": college_roll_number,
        "even_numbers": arr_of_even_numbers,
        "odd_numbers": arr_of_odd_numbers,
        "alphabets": alphabets,
        "special_characters": arr_of_special_characters,
        "sum_of_numbers": sum_of_numbers,
        "concat_string": concat_string
    }

    return jsonify(response)

def handler(request, response):
    return app(request, response)
