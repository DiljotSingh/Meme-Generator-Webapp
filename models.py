#models.py
from google.appengine.ext import ndb

class Meme(ndb.Model):
  first_line = ndb.StringProperty(required=False)
  second_line = ndb.StringProperty(required=False)
  pic_type = ndb.StringProperty(required=False)

  def get_meme_url(self):
    if self.pic_type == 'old-class':
        url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
    elif self.pic_type == 'college-grad':
        url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
    elif self.pic_type == 'thinking-ape':
        url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
    elif self.pic_type == 'coding':
        url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
    elif self.pic_type == "computer-expert":
        url = "https://pbs.twimg.com/media/DgKOl_5XkAQJbC5.jpg"
    elif self.pic_type == "pika-surprise":
        url = "https://i.imgur.com/sohWhy9.jpg"
    elif self.pic_type == "cat-cry":
        url = "https://pbs.twimg.com/media/Dxe69DhV4AEis7e.jpg"
    return url
