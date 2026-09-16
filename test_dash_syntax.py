# Let's test the dashboard HTML structure for unclosed tags and syntax
from html.parser import HTMLParser

class StrictParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.voids = {'meta','link','img','br','hr','input','source','col'}
    def handle_starttag(self, tag, attrs):
        if tag not in self.voids: self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag not in self.voids and self.stack and self.stack[-1] == tag: self.stack.pop()

print("Parser test module ready")
