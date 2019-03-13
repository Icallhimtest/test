# -*- coding: utf-8 -*-
from odoo import http

# class Module343(http.Controller):
#     @http.route('/module343/module343/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module343/module343/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module343.listing', {
#             'root': '/module343/module343',
#             'objects': http.request.env['module343.module343'].search([]),
#         })

#     @http.route('/module343/module343/objects/<model("module343.module343"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module343.object', {
#             'object': obj
#         })