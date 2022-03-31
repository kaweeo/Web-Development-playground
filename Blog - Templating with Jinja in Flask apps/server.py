from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

# There is a list of Python dictionries pre-uploaded to npoint.io represiting our blog posts. Using request module to get them.
# Then render their titles and subtitles in to index page using Jinja expressions.
@app.route('/')
def blog_getter():
    resp_blog = requests.get("https://api.npoint.io/7701c4145b1e38a70bf9")
    posts = resp_blog.json()
    return render_template("index.html", posts = posts)

#Using Class Post to get via API the requested post by id and than render it dynamically in a new url with post.html template.
@app.route('/post/<int:blog_id>')
def blog_post(blog_id):
    post = Post(blog_id)
    post_with_id = post.post_getter()
    post_title = post_with_id["title"]
    post_body = post_with_id["body"]
    return render_template("post.html", post_with_id = post_with_id, post_title = post_title, post_body = post_body, blog_id = blog_id)

# Runnig Flask app with debugger and on a free port
if __name__ == "__main__":
    app.run(debug=True, port=5008)
