from flask import Flask
import time
app = Flask(__name__)


@app.route('/')
def hint_info():
    return 'Please refer to /time to check the current time.'

@app.route('/time')
def ret_time():
    return 'Time right now: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


app.run(host='0.0.0.0',
        port=8080,
        debug=True)