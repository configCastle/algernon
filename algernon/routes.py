from api.hello import HelloAPI


def init_routes(app):
    app.router.add_view('/hello', HelloAPI)
