# -*- coding: utf-8 -*-
from odoo import http

# class Module478(http.Controller):
#     @http.route('/module478/module478/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module478/module478/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module478.listing', {
#             'root': '/module478/module478',
#             'objects': http.request.env['module478.module478'].search([]),
#         })

#     @http.route('/module478/module478/objects/<model("module478.module478"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module478.object', {
#             'object': obj
#         })