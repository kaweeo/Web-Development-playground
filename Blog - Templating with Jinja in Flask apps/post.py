import requests

class Post:
    def __init__(self, id):
        self.id = id

    def post_getter(self):
        response = requests.get("https://api.npoint.io/7701c4145b1e38a70bf9")
        all_posts = response.json()
        post_with_id = [post for post in all_posts if post["id"] == self.id][0]
        return post_with_id
# post_id_1 = Post(1)
# print(post_id_1.post_getter())