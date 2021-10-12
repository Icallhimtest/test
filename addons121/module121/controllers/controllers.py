# -*- coding: utf-8 -*-
from odoo import http

# class Module121(http.Controller):
#     @http.route('/module121/module121/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module121/module121/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module121.listing', {
#             'root': '/module121/module121',
#             'objects': http.request.env['module121.module121'].search([]),
#         })

#     @http.route('/module121/module121/objects/<model("module121.module121"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module121.object', {
#             'object': obj
#         })