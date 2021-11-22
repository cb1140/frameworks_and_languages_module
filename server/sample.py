import falcon

class QuoteResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        quote = {
            'quote': (
                "I've always been more interested in "
                "the future than in the past."
            ),
            'author': 'Grace Hopper'
        }

        resp.media = quote

api = falcon.API()
api.add_route('/quote', QuoteResource())



if __name__ == '__main__':

    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8000, api)
    try:
        
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass