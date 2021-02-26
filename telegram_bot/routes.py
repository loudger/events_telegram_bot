from .aiohttp_server_API import API_methods

def setup_routes(app):
    # app.router.add_route('GET', '/ping', client_interface.ping)
    app.router.add_route('GET', '/get_new_event_id', API_methods.get_new_event_id)
    