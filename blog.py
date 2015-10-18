import os
import webapp2
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), 
										autoescape = True)




class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self,template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("blog_newentry.html")
    def post(self):
    	subject = self.request.get("subject")
    	content = self.request.get("content")
    	error = "You need a subject AND content!"
    	if subject!= "" and content != "":
    		self.response.out.write("thanks")
    	else:
    		self.render("blog_newentry.html", subject = subject, content = content, error= error)



app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
