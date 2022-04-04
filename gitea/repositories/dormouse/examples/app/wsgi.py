
from app import create_app

app = create_app(config_name='production')
socketio = app.socketio


if __name__ == "__main__":
    socketio.run(app=app)
