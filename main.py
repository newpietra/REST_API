
from flask import Flask, jsonify

from flask_restful import Resource, reqparse, Api

from model.post import Post


postes= []

app = Flask(__name__)
api = Api(app)
api.init_app(app)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"response": "pong"})


class User():

    def __init__(self, username: str):
        self.username = username

class Post():

    def __init__(self, body: str, author: User):
        self.body = body
        self.author = author

@app.route('/posts', methods=['POST'])
def create_post():
    '''{"body": "Hello Wold", "author": "tanya"}
    '''
    parser = reqparse.RequestParser()
    parser.add_argument("body", type = str)
    parser.add_argument("author", type = str)
    posts = parser.parse_args()
    postes.append(posts)
    return postes


@app.route('/posts', methods=['GET'])
def read_posts():
    return postes

@app.route('/posts', methods=['PUT'])
def change_posts():
    parser = reqparse.RequestParser()
    parser.add_argument("body", type=str)
    parser.add_argument("author", type=str)
    params = parser.parse_args()
    for author in postes:
        if (params["author"] == postes[0]["author"]):
           postes[0]["author"] = params["author"]
           postes[0]["body"] = params["body"]
           return postes
    return postes

def delete():
    global postes
    postes = [body for body in postes if body["author"] != "author"]
    return f"Post with author {"author"} is deleted."

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="127.0.0.1")




