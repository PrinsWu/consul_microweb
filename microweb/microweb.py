from flask import Flask, render_template, jsonify
from flask_cors import CORS
import json
import requests
import os
from consul import Consul
from consulservicefinder import ConsulServiceFinder

app = Flask(__name__)
CORS(app)

consul_url = (os.environ['CONSUL_HOST'] if 'CONSUL_HOST' in os.environ else "consul")
consul_port = (int(os.environ['CONSUL_PORT']) if 'CONSUL_PORT' in os.environ else 8500)
consul = Consul(host=consul_url, port=consul_port)
microuser_service_name = (os.environ['MICROUSER_SERVICE_NAME'] if 'MICROUSER_SERVICE_NAME' in os.environ else "microweb_microuser")
microtalk_service_name = (os.environ['MICROTALK_SERVICE_NAME'] if 'MICROTALK_SERVICE_NAME' in os.environ else "microweb_microtalk")
csf = ConsulServiceFinder(consul=consul)
# csf = ConsulServiceFinder()
service_prepared = False

 
def preparedServiceQuery():
    # if service_prepared == True:
    #     return
    # service_prepared = True
    querys = csf.getQueryByServiceName(service_name=microuser_service_name)
    if not querys:
        csf.createQueryByServiceName(service_name=microuser_service_name, query_name="user")
    querys = csf.getQueryByServiceName(service_name=microtalk_service_name)
    if not querys:
        csf.createQueryByServiceName(service_name=microtalk_service_name, query_name="talk")

def findUserServiceUrl():
    preparedServiceQuery()
    service_name = microuser_service_name
    app.logger.debug("----- findUserServiceUrl -----" + service_name)
    app.logger.debug(type(csf))
    rep = csf.requestOneServiceByServiceName(service_name)
    app.logger.debug(rep)
    url = csf.composeServiceUrl(rep)
    return url

def findTalkServiceUrl():
    preparedServiceQuery()
    service_name = microtalk_service_name
    app.logger.debug("----- findTalkServiceUrl  -----" + service_name)
    rep = csf.requestOneServiceByServiceName(service_name)
    app.logger.debug(rep)
    url = csf.composeServiceUrl(rep)
    return url

@app.route("/")
def hello():
    return "Hello World! I am MicroWeb!"

@app.route("/ui")
def ui():
    return render_template('ui.html')

@app.route("/consul/<command>", methods=["GET", "POST"])
def consul(command):
    app.logger.debug("-" * 30)
    if "dq" == command:
        object_dict = cs.consul_query_dict
        object_type = "Query"
    elif "ds" == command:
        object_dict = cs.consul_service_dict
        object_type = "Service"
    for _, data in object_dict.items():
        app.logger.debug(object_type + "[" + data.id + ":" + data.name + "] (" + 
            data.state + "," + str(data.used_count) + ")")
    
    return jsonify({})

@app.route("/test/<ip>", methods=["GET", "POST"])
def test(ip):
    app.logger.debug("-" * 30)
    # cs = ConsulServiceFinder(consul_ip=ip, port=8500)
    # cs.queryLoadFromConsul()
    # cs.displayQuery()
    # query_name = "my-query-mu" 
    # cs.executeQuery(query_name)
    # consulService = cs.requestOneService(query_name)
    # url = cs.composeServiceUrl(consulService) + "/users"

    # url = "http://172.17.0.4/users"
    url = "http://" + ip + "/users"
    # url = "http://localhost:8090/users"
    app.logger.debug("call API:" + url)
    data = {}
    # data = {'lang': 'zh-TW', 'sessionId': user_id, 'timezone': 'Asia/Hong_Kong', 'query': query}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    users = r.json()
    app.logger.debug(users)
    return jsonify(users)

@app.route("/load", methods=["GET", "POST"])
def getUsersAndTalks():
    app.logger.debug("-" * 30)
    # url = "http://172.17.0.4/users"
    # url = "http://172.17.0.5/users"
    url = findUserServiceUrl() + "/users"
    # url = "http://localhost:8090/users"
    app.logger.debug("call API:" + url)
    data = {}
    # data = {'lang': 'zh-TW', 'sessionId': user_id, 'timezone': 'Asia/Hong_Kong', 'query': query}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    users = r.json()
    app.logger.debug(users)

    # url = "http://172.17.0.6/talks"
    url = findTalkServiceUrl() + "/talks"
    # url = "http://localhost:8091/talks"
    app.logger.debug("call API:" + url)
    data = {}
    # data = {'lang': 'zh-TW', 'sessionId': user_id, 'timezone': 'Asia/Hong_Kong', 'query': query}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    talks = r.json()
    app.logger.debug(talks)

    result = {}
    result["users"] = users["users"]
    result["talks"] = talks["talks"]
    # app.logger.debug(type(users) + " " + type(talks))
    # app.logger.debug(result)
    return jsonify(result)

@app.route("/users", methods=["GET", "POST"])
def getUsers():
    app.logger.debug("-" * 30)
    # url = "http://172.17.0.4/users"
    # url = "http://172.17.0.6/users"
    url = "http://localhost:8090/users"
    app.logger.debug("call API:" + url)
    data = {}
    # data = {'lang': 'zh-TW', 'sessionId': user_id, 'timezone': 'Asia/Hong_Kong', 'query': query}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    users = r.json()
    app.logger.debug(users)

    result = {}
    result["users"] = users
    app.logger.debug(result)
    return jsonify(result)

@app.route("/talks", methods=["GET", "POST"])
def getTalks():
    app.logger.debug("-" * 30)
    # url = "http://172.17.0.5/talks"
    url = "http://localhost:8091/talks"
    app.logger.debug("call API:" + url)
    data = {}
    # data = {'lang': 'zh-TW', 'sessionId': user_id, 'timezone': 'Asia/Hong_Kong', 'query': query}
    headers = {'Content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    talks = r.json()
    app.logger.debug(talks)

    result = {}
    result["talks"] = talks
    app.logger.debug(result)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)