import webapp2
import logging

DATALAB = "www.google.com"

class MainPage(webapp2.RequestHandler):
    def get(self):
        try:
            self.redirect(DATALAB)
            logging.info("Redirect Successful")
        except Exception as e:
            logging.error(e)

    def post(self):
        try:
            self.redirect(DATALAB)
            logging.info("Redirect Successful")
        except Exception as e:
            logging.error(e)

app = webapp2.WSGIApplication([
        ('/', MainPage),
], debug=True)

def main():
    logging.getLogger().setLevel(logging.DEBUG)
    webapp2.util.run_wsgi_app(app)

if __name__ == '__main__':
    main()
