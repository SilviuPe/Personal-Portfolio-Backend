from flask import Flask
from database import Database
app = Flask(__name__)

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

            return projects

    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }, 400

if __name__ == '__main__':
    app.run()