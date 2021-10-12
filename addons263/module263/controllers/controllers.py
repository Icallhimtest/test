# -*- coding: utf-8 -*-
from odoo import http

# class Module263(http.Controller):
#     @http.route('/module263/module263/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module263/module263/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module263.listing', {
#             'root': '/module263/module263',
#             'objects': http.request.env['module263.module263'].search([]),
#         })

#     @http.route('/module263/module263/objects/<model("module263.module263"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module263.object', {
#             'object': obj
#         })