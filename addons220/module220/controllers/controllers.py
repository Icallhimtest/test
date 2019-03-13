# -*- coding: utf-8 -*-
from odoo import http

# class Module220(http.Controller):
#     @http.route('/module220/module220/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module220/module220/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module220.listing', {
#             'root': '/module220/module220',
#             'objects': http.request.env['module220.module220'].search([]),
#         })

#     @http.route('/module220/module220/objects/<model("module220.module220"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module220.object', {
#             'object': obj
#         })