import glob
from post import Post

class Resources(object):
    """ resource
    """
    def __init__(self, post_path="./_post/"):
        self.post_path = post_path
        self.post_pattern = "*markdown"
        self.post_mapping = {}

    def load_post(self):
        """ load post
        """
        for post_source in glob.glob(self.post_path + self.post_pattern):
            post = Post()
            post.load_from_file(post_source)
            # self.posts.append(post)
            self.post_mapping[post.link] = post

    def get(self, link):
        return self.post_mapping.get(link)

    def posts(self):
        return sorted(self.post_mapping.values(), key=lambda x: x.date, reverse=True)

if __name__ == "__main__":
    resource = Resources()
    resource.load_post()
    for link in resource.post_mapping:
        post = resource.post_mapping[link]
        # print post.title, post.date, link
