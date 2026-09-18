from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        distance = float(request.form["distance"])
        consumption = float(request.form["consumption"])
        fuel_price = float(request.form["fuel_price"])

        liters = distance / 100 * consumption
        costs = liters * fuel_price

        result = {
            "distance": distance,
            "consumption": consumption,
            "fuel_price": fuel_price,
            "liters": liters,
            "costs": costs
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)