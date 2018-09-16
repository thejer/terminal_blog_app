import uuid
import datetime

from database import Database
from models.post import Post


class Blog(object):
    # class name extends object

    # init method
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    # creates a new post using in the blog
    def new_post(self):
        title = input("Enter post title: ")
        content = input("Enter post content: ")
        date = input("Enter post date or leave blank for today (in format (DDMMYYYY): ")
        if date == "":
            date = datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date, "%d%m%Y")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()

    # get the posts in the blog using the blog id
    def get_posts(self):
        return Post.from_blog(self.id)

    # saves the blog to DB
    def save_to_mongo(self):
        Database.insert(collection='blogs',
                        data=self.json())

    # Creates the json string of the blog details to be stored to the DB
    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    # it gets a blog data from the db using its provided id, it build the blog object from the cursor object

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})

        return cls(author=blog_data['author'],
                   title=blog_data['title'],
                   description=blog_data['description'],
                   id=blog_data['id'])
