# NOW WE WANT TO: CLICK CHECK STRUCTURE ONLY WHEN DUMPING DATABASE

# NOTES: MAKE A SUMMARY SHEET OF THE WEEK 22 SLIDE A FOR CHECKLIST ON FRONT END/BACK END STEPS TO DEPLOY

from flask import Flask, make_response, jsonify
from dbhelpers import run_statement
from dbcreds import production_mode

app = Flask(__name__)

@app.get('/api/animals')
def get_animals():
    result = run_statement("CALL get_all_animals()")
    keys = ["animalName", "numberOfLegs"]
    response = []
    if (type(result) == list):
        for animal in result:
            response.append(dict(zip(keys, animal)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(response), 500)

if (production_mode == True):
    print("Running server in Production Mode")
    import bjoern #type:ignore
    bjoern.run(app, "0.0.0.0", 5000)
else:
    print("Running Server in Testing Mode.")
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
