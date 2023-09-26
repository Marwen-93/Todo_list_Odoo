# -*- coding: utf-8 -*-
# from odoo import http


# class Tutorials/todoList(http.Controller):
#     @http.route('/tutorials/todo_list/tutorials/todo_list', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tutorials/todo_list/tutorials/todo_list/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tutorials/todo_list.listing', {
#             'root': '/tutorials/todo_list/tutorials/todo_list',
#             'objects': http.request.env['tutorials/todo_list.tutorials/todo_list'].search([]),
#         })

#     @http.route('/tutorials/todo_list/tutorials/todo_list/objects/<model("tutorials/todo_list.tutorials/todo_list"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tutorials/todo_list.object', {
#             'object': obj
#         })
