# -*- coding: utf-8 -*-
from odoo import http

# class Module76(http.Controller):
#     @http.route('/module76/module76/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module76/module76/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module76.listing', {
#             'root': '/module76/module76',
#             'objects': http.request.env['module76.module76'].search([]),
#         })

#     @http.route('/module76/module76/objects/<model("module76.module76"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module76.object', {
#             'object': obj
#         })