from DataLayer.configMysql import app
from routes.PersonaNatural_Api import *
from routes.Usuario_Api import *
from dotenv import load_dotenv


# app.register_blueprint(routes_auth, url_prefix="/api")
# app.register_blueprint(users_github, url_prefix="/api")

# if __name__ == "__main__":
#     app.run(port=3030, debug=True)
if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True, port="4000", host="0.0.0.0")