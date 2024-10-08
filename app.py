from flask import Flask, render_template, request

from src.pipelines.prediction_pipeline import CustomData, PredictionPipeline

application = Flask(__name__)

app = application

## Route for a home page


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
            gender=request.form.get("gender"),
            race_ethnicity=request.form.get("ethnicity"),
            parental_level_of_education=request.form.get("parental_level_of_education"),
            lunch=request.form.get("lunch"),
            test_preparation_course=request.form.get("test_preparation_course"),
            reading_score=float(request.form.get("writing_score")),
            writing_score=float(request.form.get("reading_score")),
        )
        pred_df = data.get_dataframe()
        print(pred_df)
        print("before Prediction")

        predict_pipeline = PredictionPipeline()
        print("mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template("home.html", results=results[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port="7500")
