from flask import Flask
from flask_restful import Api
from web.reminders_api import RemindersResource

app = Flask(__name__)
api = Api(app)


api.add_resource(RemindersResource, '/reminders')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
