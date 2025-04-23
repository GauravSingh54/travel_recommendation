from flask import Flask, render_template, request, jsonify
from model_utils import (
    predict_cluster, get_recommendations,
    get_all_states, get_all_significance, get_all_best_times,
    get_cities_by_state, get_significance_by_city, get_best_times_by_city
)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    states = get_all_states()
    significance_list = get_all_significance()
    best_times = get_all_best_times()
    selected_state = selected_city = selected_significance = selected_time = ""

    if request.method == 'POST':
        selected_state = request.form['state']
        selected_city = request.form['city']
        selected_significance = request.form['significance']
        selected_time = request.form['best_time']

        cluster_id = predict_cluster(selected_significance, selected_time)
        recommendations = get_recommendations(cluster_id)

        recommendations = [
            place for place in recommendations
            if (place['City'] == selected_city) 
            #    (place['Significance'] == selected_significance) and
            #    (place['Best Time to visit'] == selected_time)
        ]

        if not recommendations:
            recommendations = "Insufficient Data"

    return render_template('index.html',
                           states=states,
                           significance_list=significance_list,
                           best_times=best_times,
                           selected_state=selected_state,
                           selected_city=selected_city,
                           selected_significance=selected_significance,
                           selected_time=selected_time,
                           recommendations=recommendations)

@app.route('/get_cities', methods=['POST'])
def get_cities():
    data = request.get_json()
    state = data['state']
    cities = get_cities_by_state(state)
    return jsonify(cities)

@app.route('/get_significance', methods=['POST'])
def get_significance():
    data = request.get_json()
    city = data['city']
    significance = get_significance_by_city(city)
    return jsonify(significance)

@app.route('/get_best_times', methods=['POST'])
def get_best_times():
    data = request.get_json()
    city = data['city']
    times = get_best_times_by_city(city)
    return jsonify(times)

if __name__ == '__main__':
    app.run(debug=True)
