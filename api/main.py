from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/bfhl":

            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)
            body_json = json.loads(body.decode("utf-8"))  
            data = body_json.get("data", [])
            

            user_id = "arjay_jg_13112004"
            email = "arjayjg1311@gmail.com"
            college_roll_number = "22BCE1510"

            arr_of_even_numbers = [str(int(i)) for i in data if i.isdigit() and int(i) % 2 == 0]
            arr_of_odd_numbers = [str(int(i)) for i in data if i.isdigit() and int(i) % 2 != 0]
            sum_of_numbers = str(sum(int(i) for i in data if i.isdigit()))

            alphabets = [i.upper() for i in data if i.isalpha()]

            arr_of_special_characters = [i for i in data if not i.isalnum()]

            concat_raw = ''.join([i for i in data if i.isalpha()])[::-1]
            concat_string = ""
            for idx, c in enumerate(concat_raw):
                if idx % 2 == 0:
                    concat_string += c.upper()
                else:
                    concat_string += c.lower()


            response = {
                "is_success": True,
                "user_id": user_id,
                "email": email,
                "college_roll_number": college_roll_number,
                "odd_numbers": arr_of_odd_numbers,
                "even_numbers": arr_of_even_numbers,
                "alphabets": alphabets,
                "special_characters": arr_of_special_characters,
                "sum": sum_of_numbers,
                "concat_string": concat_string
            }

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
