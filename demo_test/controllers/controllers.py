# -*- coding: utf-8 -*-
from odoo import http

# class DemoTest(http.Controller):
#     @http.route('/demo_test/demo_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/demo_test/demo_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('demo_test.listing', {
#             'root': '/demo_test/demo_test',
#             'objects': http.request.env['demo_test.demo_test'].search([]),
#         })

#     @http.route('/demo_test/demo_test/objects/<model("demo_test.demo_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('demo_test.object', {
#             'object': obj
#         })