import aiohttp
from aiohttp_server import create_app
from aiohttp_server import settings

host = settings.default_host
port = settings.default_port


app = create_app()
if __name__ == '__main__':
    aiohttp.web.run_app(app, host = host, port = port)