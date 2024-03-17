from flask import Flask, render_template, request, jsonify , send_from_directory
from flask_cors import CORS
import os
from NBA import NBA

#wrapped app=Flask() into a function to make it more robust, allows for testing setups
def create_app():
    app = Flask(__name__)
    #!! self reminder -> windows cmd requires "python3 -m flask --app Project_API run" to work !!

    CORS(app,origins = "http://localhost:3000")
    #Homepage 
    #Goal is to have links/titles or some form of alert to highlight each project.
    #
    #TODO: place holder for home page change after figuring out vision
    @app.route('/')
    def home_page():
        return "<p>Hello World!</p>"


    '''
    NBA SECTION
    '''
    # Currently: loads and the webpage template for nba and populates data after script is ran
    # TODO: make it look pretty and figure out how to display for best results
    @app.route('/nba')
    def nba():
        return render_template('nba.html')

    @app.route('/nba_data')
    def nba_data():
        data = NBA.data_scrape()
        return jsonify(data)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    def shutdow():
        os._exit(0)


    @app.route('/favicon.ico')
    def favicon():
        return '',404

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)