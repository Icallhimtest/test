# -*- coding: utf-8 -*-
from odoo import http

# class Module393(http.Controller):
#     @http.route('/module393/module393/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module393/module393/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module393.listing', {
#             'root': '/module393/module393',
#             'objects': http.request.env['module393.module393'].search([]),
#         })

#     @http.route('/module393/module393/objects/<model("module393.module393"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module393.object', {
#             'object': obj
#         })