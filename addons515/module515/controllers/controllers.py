# -*- coding: utf-8 -*-
from odoo import http

# class Module515(http.Controller):
#     @http.route('/module515/module515/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module515/module515/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module515.listing', {
#             'root': '/module515/module515',
#             'objects': http.request.env['module515.module515'].search([]),
#         })

#     @http.route('/module515/module515/objects/<model("module515.module515"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module515.object', {
#             'object': obj
#         })