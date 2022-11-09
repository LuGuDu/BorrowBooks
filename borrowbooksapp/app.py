from flask import Flask


app = Flask(__name__)

MONGO_STRING = "mongodb+srv://borrowbooks:tOKlwpoiQan7Nt60@cluster0.gozlc.mongodb.net/borrowbooksdb"
app.config["MONGO_URI"] = MONGO_STRING
mongodb_client = PyMongo(app)
mongo = mongodb_client.db



@app.route('/api', methods=['GET'])
def index():
    return {
        "tutorial": "Flask React Heroku"
    }
if __name__ == '__main__':
    app.run()
