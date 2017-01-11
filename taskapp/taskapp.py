from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@postgres/taskapp'
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from views import *


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)



