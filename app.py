from flask import Flask
from flask_cors import CORS
from database import Database
from utils import gather_information_about_repo
app = Flask(__name__)

CORS(app)

@app.route('/projects', methods=['GET'])
def index():

    try:
        projects = Database().get_projects()

        if 'error' in projects:

            return {
                'status': 'error',
                'message': projects['error']
            }, 400

        else:
            data = gather_information_about_repo(projects[0]['github_link'])

            if data:
                return data, 200

            else:
                return {
                    'status': 'error',
                    'message': "Something went wrong."
                }, 400

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }, 400

if __name__ == '__main__':
    app.run()