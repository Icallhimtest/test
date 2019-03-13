# -*- coding: utf-8 -*-
from odoo import http

# class Module335(http.Controller):
#     @http.route('/module335/module335/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module335/module335/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module335.listing', {
#             'root': '/module335/module335',
#             'objects': http.request.env['module335.module335'].search([]),
#         })

#     @http.route('/module335/module335/objects/<model("module335.module335"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module335.object', {
#             'object': obj
#         })