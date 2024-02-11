from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api
import os
import subprocess
import sys

app = Flask(__name__)
api = Api(app)

class DbtCommand(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        cmd_list =  ['dbt deps']
        if type(request_data['cmd']) is str:
            cmd_list.append(request_data['cmd'])
        else:
            cmd_list = cmd_list + request_data['cmd']
        
        for c in cmd_list:
            if not c.startswith('dbt'):
                return {
                    'message': f'Command: <<{c}>> is not valid dbt command, command must starts with '
                }
        for c in cmd_list:
            run_cmd = subprocess.run(c, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            
            if run_cmd.returncode != 0:
                return {
                    'message': f'this is not correct {run_cmd.stdout}'
                }
                
        return {
            'message': f'Commands: <<{cmd_list}>> ran successfully'
        }
        
api.add_resource(DbtCommand, '/')

if __name__=='__main__':
    app.run(host='0.0.0.0', port='5050')