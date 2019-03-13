# -*- coding: utf-8 -*-
from odoo import http

# class Module517(http.Controller):
#     @http.route('/module517/module517/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module517/module517/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module517.listing', {
#             'root': '/module517/module517',
#             'objects': http.request.env['module517.module517'].search([]),
#         })

#     @http.route('/module517/module517/objects/<model("module517.module517"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module517.object', {
#             'object': obj
#         })