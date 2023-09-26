# -*- coding: utf-8 -*-
{
    'name': "todo_list",

    'description': """
        This to-do task involves the creation of a task entry with specific details, including a task name, description, and color.""",

    'author': "Marwen Weslati",
    'website': "https://flowcv.me/pythondevloper",
    'sequence': 10,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
   'assets': {
                'web.assets_backend': [
                    'todo_list/static/src/components/*/*.js',
                    'todo_list/static/src/components/*/*.xml',
                    'todo_list/static/src/components/*/*.scss',
                ]
            },
    'application': True,

}
