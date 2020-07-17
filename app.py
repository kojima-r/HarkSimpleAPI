from flask import Flask, render_template, request, redirect, url_for,make_response,jsonify
import numpy as np
import os
from datetime import datetime
import werkzeug
import subprocess
import glob
import json
import hashlib
import random, string

def randomname(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

def calculate_key(filename):
    text=(filename+randomname(5)).encode('utf-8')
    result = hashlib.md5(text).hexdigest()
    saveFileName = werkzeug.utils.secure_filename(result)
    return saveFileName



template_dir = os.path.abspath('view')
app = Flask(__name__,template_folder=template_dir)
import data
app.register_blueprint(data.public_data)

worker={}
latest_setting={}
app_base_name=""
public_path="/hark_api/public/index.html"
@app.route(app_base_name+'/')
def index():
    return redirect(public_path)


@app.route(app_base_name+'/run/create_pj', methods=['GET','POST'])
def post_run_create_pj():
    global worker
    if request.method == 'POST':
        name=request.form["name"]
        target=request.form["target"]
        tf=request.form["tf"]
        thresh=request.form["thresh"]
    else:
        name=request.args.get('name')
        target=request.args.get('target')
        tf=request.args.get('tf')
        thresh=request.args.get('thresh')
    print(['sh', 'run.create_pj.sh',name,target,tf,thresh])
    p = subprocess.Popen(['sh', 'run.create_pj.sh',name,target,tf,thresh])
    worker[name]={"process":p,"setting":[]}
    print(worker)
    return make_response(jsonify({'worker_id':name}))

UPLOAD_WAV_DIR="./audio/"
@app.route(app_base_name+'/upload/wav', methods=['POST'])
def post_wav_up():
    print("===")
    print(request)
    print(request.files)
    print(request.form)
    if 'files' in request.files:
        file = request.files['files']
        #wid=calculate_key(fileName)
        #file.save(os.path.join(UPLOAD_WAV_DIR, wid+".wav"))
        filename = file.filename
        name,_=os.path.splitext(filename)
        file.save(os.path.join(UPLOAD_WAV_DIR, name+".wav"))
        #return make_response(jsonify({'result':wid}))
        return make_response(jsonify({'result':name}))

@app.route(app_base_name+'/status/<wid>', methods=['GET'])
def status(wid=None):
    print(worker)
    if wid not in worker or  worker[wid] is None:
        return make_response(jsonify({'worker_id':wid,'status':"not found"}))
    if worker[wid]["process"].poll() is None:
        lines=[l for l in open("log/"+wid+".txt","r")]
        return make_response(jsonify({'worker_id':wid,'status':"running","log":lines}))
    worker[wid]=None
    return make_response(jsonify({'worker_id':wid,'status':"finished"}))

@app.route(app_base_name+'/list/wav', methods=['GET'])
def list_wav():
    l=glob.glob(UPLOAD_WAV_DIR+"*.wav")
    return make_response(jsonify(l))
@app.route(app_base_name+'/list/tf', methods=['GET'])
def list_tf():
    l=glob.glob("./tf/*.zip")
    return make_response(jsonify(l))
@app.route(app_base_name+'/list/project', methods=['GET'])
def list_project():
    path="public/"
    files = os.listdir(path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
    return make_response(jsonify(files_dir))

if __name__ == '__main__':
    #app.debug = True
    app.run(host='0.0.0.0',port=8080)

