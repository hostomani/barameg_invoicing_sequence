# -*- coding: utf-8 -*-
# from odoo import http


# class BaramegInvoicingSequence(http.Controller):
#     @http.route('/barameg_invoicing_sequence/barameg_invoicing_sequence/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barameg_invoicing_sequence/barameg_invoicing_sequence/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('barameg_invoicing_sequence.listing', {
#             'root': '/barameg_invoicing_sequence/barameg_invoicing_sequence',
#             'objects': http.request.env['barameg_invoicing_sequence.barameg_invoicing_sequence'].search([]),
#         })

#     @http.route('/barameg_invoicing_sequence/barameg_invoicing_sequence/objects/<model("barameg_invoicing_sequence.barameg_invoicing_sequence"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barameg_invoicing_sequence.object', {
#             'object': obj
#         })
