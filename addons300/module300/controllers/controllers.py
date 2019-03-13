# -*- coding: utf-8 -*-
from odoo import http

# class Module300(http.Controller):
#     @http.route('/module300/module300/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module300/module300/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module300.listing', {
#             'root': '/module300/module300',
#             'objects': http.request.env['module300.module300'].search([]),
#         })

#     @http.route('/module300/module300/objects/<model("module300.module300"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module300.object', {
#             'object': obj
#         })