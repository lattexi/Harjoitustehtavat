import math
from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    jaollinen = False

    if luku != 2 and not luku % 2:
        jaollinen = True

    for i in range(2, int(math.sqrt(luku)) + 1, ):
        if luku % i == 0:
            jaollinen = True
            break

    vastaus = {
        "Luku": luku,
        "Alkuluku": not jaollinen
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, mimetype="application/json")


app.run(use_reloader=True, host='127.0.0.1', port=3000)
