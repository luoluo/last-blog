import markdown
import markdown2
import frontmatter
import json
import hashlib
import pypandoc

class Post(object):
    """ post
    """
    def __init__(self):
        self.title = ""
        self.date = ""
        self.content = ""
        self.uri = ""
        self.link = ""

    def load_from_file(self, filename):
        """
        INPUT:
        ---
        layout: post
        title: title
        date: 2011-12-11 22:49
        comments: true
        categories: categories
        ---
        content

        OUTPUT:
            {
              "layout": "post", 
              "title": "title", 
              "comments": true, 
              "content": "content", 
              "date": "2011-12-11 22:49", 
              "categories": "categories"
            }
        """

        infos = frontmatter.load(filename)
        infos = infos.to_dict()
        self.title = infos.get("title")
        self.content = infos.get("content")
        if self.content:
            markdowner = markdown2.Markdown()
            # markdowner.set_output_format("html5")
            # self.content = markdowner.convert(self.content)
            self.content = pypandoc.convert(self.content, 'html', format="md")
        self.date = infos.get("date") # TODO
        self.link = hashlib.md5(filename.encode("utf-8")).hexdigest()

if __name__ == "__main__":
    p = Post()
    p.load_from_file("demo.md")
    # print p.title
    # print p.date
    # print p.content
    # print p.link
