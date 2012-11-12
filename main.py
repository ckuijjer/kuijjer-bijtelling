#!/usr/bin/env python
import jinja2
import json
import os
import webapp2
import yaml
from licenseplate import *

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


class BaseHandler(webapp2.RequestHandler):
    def render_str(self, template, **kw):
        t = jinja_env.get_template(template)
        return t.render(kw)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)


class MainHandler(BaseHandler):
    def get(self, plate):
        if plate:
            try:
                plate = LicensePlate(plate)
            except ValueError:
                self.redirect('/')

        self.render('index.html', number = plate)


class ApiHandler(webapp2.RequestHandler):
    def get(self, number):
        pass

app = webapp2.WSGIApplication([
    ('/api/(.*)', ApiHandler),
    ('/(.*)', MainHandler)
], debug=True)
