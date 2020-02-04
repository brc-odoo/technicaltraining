# -*- coding: utf-8 -*-
# from odoo import http


# class Trainingmodule(http.Controller):
#     @http.route('/trainingmodule/trainingmodule/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trainingmodule/trainingmodule/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('trainingmodule.listing', {
#             'root': '/trainingmodule/trainingmodule',
#             'objects': http.request.env['trainingmodule.trainingmodule'].search([]),
#         })

#     @http.route('/trainingmodule/trainingmodule/objects/<model("trainingmodule.trainingmodule"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trainingmodule.object', {
#             'object': obj
#         })
