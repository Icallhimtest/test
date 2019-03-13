# -*- coding: utf-8 -*-
from odoo import http

# class Module65(http.Controller):
#     @http.route('/module65/module65/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module65/module65/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module65.listing', {
#             'root': '/module65/module65',
#             'objects': http.request.env['module65.module65'].search([]),
#         })

#     @http.route('/module65/module65/objects/<model("module65.module65"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module65.object', {
#             'object': obj
#         })