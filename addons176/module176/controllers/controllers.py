# -*- coding: utf-8 -*-
from odoo import http

# class Module176(http.Controller):
#     @http.route('/module176/module176/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module176/module176/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module176.listing', {
#             'root': '/module176/module176',
#             'objects': http.request.env['module176.module176'].search([]),
#         })

#     @http.route('/module176/module176/objects/<model("module176.module176"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module176.object', {
#             'object': obj
#         })