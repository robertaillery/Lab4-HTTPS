from flask import Flask, request, jsonify

app = Flask(__name__)

def trial_division(n):
    n = int(n)
    factors = []
    if n == 1:
        return [1]
        
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
        
    return factors

@app.route("/")
def hello():
   return "you called \n"

@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

@app.route("/factors", methods=['POST'])
def factors():
    if 'inINT' not in request.form:
        return "Error: 'inINT' not found in request.", 400
        
    try:
        in_int = int(request.form['inINT'])
        
        factor_list = trial_division(in_int)
        
        return jsonify(factor_list)
        
    except ValueError:
        return "Error: Invalid input. 'inINT' must be an integer.", 400

if __name__ == "__main__":
   app.run(host='0.0.0.0')