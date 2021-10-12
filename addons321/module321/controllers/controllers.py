# -*- coding: utf-8 -*-
from odoo import http

# class Module321(http.Controller):
#     @http.route('/module321/module321/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module321/module321/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module321.listing', {
#             'root': '/module321/module321',
#             'objects': http.request.env['module321.module321'].search([]),
#         })

#     @http.route('/module321/module321/objects/<model("module321.module321"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module321.object', {
#             'object': obj
#         })