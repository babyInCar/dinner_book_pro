# -*- coding: utf-8 -*-
# from odoo import http


# class DinnerBookPro(http.Controller):
#     @http.route('/dinner_book_pro/dinner_book_pro', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dinner_book_pro/dinner_book_pro/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dinner_book_pro.listing', {
#             'root': '/dinner_book_pro/dinner_book_pro',
#             'objects': http.request.env['dinner_book_pro.dinner_book_pro'].search([]),
#         })

#     @http.route('/dinner_book_pro/dinner_book_pro/objects/<model("dinner_book_pro.dinner_book_pro"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dinner_book_pro.object', {
#             'object': obj
#         })

