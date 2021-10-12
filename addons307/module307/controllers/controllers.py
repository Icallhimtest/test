# -*- coding: utf-8 -*-
from odoo import http

# class Module307(http.Controller):
#     @http.route('/module307/module307/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module307/module307/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module307.listing', {
#             'root': '/module307/module307',
#             'objects': http.request.env['module307.module307'].search([]),
#         })

#     @http.route('/module307/module307/objects/<model("module307.module307"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module307.object', {
#             'object': obj
#         })