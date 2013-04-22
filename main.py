import sys
sys.path.insert(0, 'libs')

import webapp2
import jinja2
import os
from utils import version_image, get_pypi_package_version

jinja2_loader = jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
jinja2_environment = jinja2.Environment(autoescape=True, loader=jinja2_loader)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja2_environment.get_template('index.html')
        self.response.out.write(template.render({}))


class PyPIHandler(webapp2.RequestHandler):
    name = "PyPI"

    def get_version(self):
        name = self.request.get('name')
        return get_pypi_package_version(name)

    def get(self):
        image = version_image(self.name, self.get_version())
        self.response.headers['Content-Type'] = 'image/png'
        image.save(self.response, 'png')
        return self.response


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/pypi/', PyPIHandler)
], debug=True)
