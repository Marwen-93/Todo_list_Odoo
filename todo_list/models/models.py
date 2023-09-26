# -*- coding: utf-8 -*-

from odoo import models, fields, api


class todo_list(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char('Task Name')
    description = fields.Char("Description")
    is_completed = fields.Boolean()
    color = fields.Char()

