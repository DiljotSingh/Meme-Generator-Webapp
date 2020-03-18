import webapp2
import jinja2
import os
from models import Meme


the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        welcome_template = the_jinja_env.get_template('templates/welcome.html')
        a_variable_dict = {"greeting": "Howdy",
                           "adjective": "amazing"}
        self.response.write(welcome_template.render(a_variable_dict))

    def post(self):
        self.response.write("A post request to the EnterInfoHandler")


class ShowMemeHandler(webapp2.RequestHandler):
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        meme_first_line = self.request.get('user-first-ln')
        meme_second_line = self.request.get('user-second-ln')
        meme_img_choice = self.request.get('meme-type')

        user_meme = Meme(first_line = meme_first_line,
                         second_line = meme_second_line,
                         pic_type = meme_img_choice)
        user_meme.put()
        the_variable_dict = {"line1": meme_first_line,
                             "line2": meme_second_line,
                             "img_url": user_meme.get_meme_url()}
        self.response.write(results_template.render(the_variable_dict))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/memeresult', ShowMemeHandler),
], debug=True)
