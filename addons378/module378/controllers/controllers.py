# -*- coding: utf-8 -*-
from odoo import http

# class Module378(http.Controller):
#     @http.route('/module378/module378/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module378/module378/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('module378.listing', {
#             'root': '/module378/module378',
#             'objects': http.request.env['module378.module378'].search([]),
#         })

#     @http.route('/module378/module378/objects/<model("module378.module378"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module378.object', {
#             'object': obj
#         })