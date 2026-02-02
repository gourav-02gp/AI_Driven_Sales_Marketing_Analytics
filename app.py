from flask import Flask, render_template, request
from src.data_preprocessing import load_and_clean_data
from src.model import train_model, predict_sales

app = Flask(__name__)

df = load_and_clean_data()
model = train_model(df)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        spend = float(request.form["spend"])
        prediction = round(predict_sales(model, spend), 2)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
