from flask import Flask
from flask_restplus import Api, Resource

from server.instance import server

app, api = server.app, server.api

lista = [
    {'id': 0, 'texto': 'aquiiii'},
    {'id': 0, 'texto': 'aquiiii'},
]

@api.route('/new')
class NewTest():
    def get(self):
        return lista