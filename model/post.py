from model.user import User

class Post:

    def __init__(self, body: str, author: User):
        self.body = body
        self.author = author
