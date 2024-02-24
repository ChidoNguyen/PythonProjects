from flask import Flask, render_template, request, jsonify
from NBA import NBA
app = Flask(__name__)

#!! self reminder -> windows cmd requires "python3 -m flask run" to work !!
#Homepage 
#Goal is to have links/titles or some form of alert to highlight each project.
@app.route('/')
def home_page():
    return "<p>Hello World!</p>"

@app.route('/nba')
def nba():
    return render_template('nba.html')
@app.route('/nba_data')
def nba_data():
    data = NBA.main()
    return jsonify(data)
    #return render_template('nba.html', data=data)



if __name__ == "__main__":
    app.run(debug=True)