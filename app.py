templates = [
    {
        "inputs": 5,
        "category": "sports",
        "word": "chess"
    },
    {
        "inputs": 6,
        "category": "european country name",
        "word": "france"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status": "success",
        "word": random.choice(templates)
    })