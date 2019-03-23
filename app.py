from flask import request, Response, Flask
from pystress import *
import json
from threading import Timer


app = Flask(__name__)

processes = dict()

def stop(procs):
    for p in procs:
        p.terminate()
        processes.pop(p.pid)

@app.route('/start', methods=['POST'])
def start():
    try:
        exec_time = request.json["exec_time"]
        proc_num = request.json["proc_num"]
    except:
        msg = "Usage: 'exec_time' and 'proc_num are required"
        return Response(msg)
    procs = []
    conns = []
    for i in range(proc_num):
        parent_conn, child_conn = Pipe()
        p = Process(target=loop, args=(child_conn,))
        p.start()
        procs.append(p)
        conns.append(parent_conn)
        processes[p.pid] = {'is_alive': p.is_alive(), 'exec_time': exec_time}
    print(processes)
    for conn in conns:
        try:
            print(conn.recv())
        except EOFError:
            continue
    t = Timer(exec_time, stop, [procs])
    t.start()
    return Response("{} processes launched for {} seconds".format(proc_num, exec_time))

@app.route('/')
def index():
    return Response(json.dumps(processes))

app.run('0.0.0.0')
