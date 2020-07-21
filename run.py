from castlabs_proxy import create_app
from os import environ

if __name__ == '__main__':
    HTTP_PORT = environ.get('HTTP_PORT')
    if HTTP_PORT:
        HTTP_PORT = int(HTTP_PORT)

    app = create_app()

    # For demo purposes.
    # On a real app it must be configured with NGINX
    # See: https://flask.palletsprojects.com/en/1.1.x/deploying/#deployment
    app.run(port=HTTP_PORT)

