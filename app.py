from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop', methods=['GET'])
def htop():
    name = "Anuj Tiwari"
    user = os.getenv("USER", "codespace")
    tz_ist = pytz.timezone("Asia/Kolkata")
    server_time_ist = datetime.datetime.now(tz_ist).strftime("%Y-%m-%d %H:%M:%S.%f")
    top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")

    return f"""
    <h3>Name: {name}</h3>
    <h3>Username: {user}</h3>
    <h3>Server Time (IST): {tz_ist}</h3>
    <pre>{top_output}</pre>
    """
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)