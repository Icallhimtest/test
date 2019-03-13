# -*- coding: utf-8 -*-
from odoo import http

# class Module484(http.Controller):
#     @http.route('/module484/module484/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module484/module484/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module484.listing', {
#             'root': '/module484/module484',
#             'objects': http.request.env['module484.module484'].search([]),
#         })

#     @http.route('/module484/module484/objects/<model("module484.module484"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module484.object', {
#             'object': obj
#         })