import glob
import collections
import os
from post import Post

class Resources(object):
    """ resource
    """
    def __init__(self, post_path="./_post/"):
        self.post_path = post_path
        self.post_pattern = "*markdown"
        self.post_mapping = {}
        self.categories_mapping = collections.defaultdict(list)
        self.notes = None

    def load_post(self):
        """ load post
        """
        for post_source in glob.glob(self.post_path + self.post_pattern):
            post = Post()
            post.load_from_file(post_source)
            # self.posts.append(post)
            self.post_mapping[post.link] = post

    def load_note(self):
        """ load note
        """
        self.notes = Post()
        self.notes.load_from_file(self.post_path + "note/note.markdown")

    def make_categories(self):
        for post in self.post_mapping.values():
            for category in post.categories:
                self.categories_mapping[category].append(post)

    def init(self):
        self.load_post()
        self.load_note()
        self.make_categories()

    def get_note(self):
        return self.notes

    def get(self, link):
        return self.post_mapping.get(link)

    def posts(self):
        return sorted(self.post_mapping.values(), key=lambda x: x.date, reverse=True)

    def categories(self):
        return [(k, v) for k, v in self.categories_mapping.items()]

if __name__ == "__main__":
    resource = Resources()
    resource.init()
    for link in resource.post_mapping:
        post = resource.post_mapping[link]
    for category in resource.categories_mapping:
        print category, resource.categories_mapping[category]
        # print post.title, post.date, link
