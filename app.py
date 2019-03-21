from flask import request, Response, Flask
from pystress import *
import json

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start():
    try:
        exec_time = request.json["exec_time"]
        proc_num = request.json["proc_num"]
    except:
        msg = "Usage: pystress [exec_time] [proc_num]\n"
        sys.stderr.write(msg)
        sys.exit(1)
    procs = []
    conns = []
    for i in range(proc_num):
        parent_conn, child_conn = Pipe()
        p = Process(target=loop, args=(child_conn,))
        p.start()
        procs.append(p)
        conns.append(parent_conn)

    for conn in conns:
        try:
            print(conn.recv())
        except EOFError:
            continue

    time.sleep(exec_time)

    for p in procs:
        p.terminate()
    return Response(json.dumps({"message": "loaded had been finished", "procs": len(procs)}))

app.run('0.0.0.0')