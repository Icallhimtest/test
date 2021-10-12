# -*- coding: utf-8 -*-
from odoo import http

# class Module452(http.Controller):
#     @http.route('/module452/module452/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module452/module452/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module452.listing', {
#             'root': '/module452/module452',
#             'objects': http.request.env['module452.module452'].search([]),
#         })

#     @http.route('/module452/module452/objects/<model("module452.module452"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module452.object', {
#             'object': obj
#         })