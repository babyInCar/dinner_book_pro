# -*- coding: utf-8 -*-
{
    'name': "Dinner Order System",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
      Order dinner for your employees，from now on and from here！
    """,

    'author': "Gaoshuang(gaoshuang916@gmail.com)",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'OA',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/ir_module_data.xml',        
        'security/access_security.xml',
        'security/ir.model.access.csv',
        'wizard/pay_wizard.xml',
        'views/login_edit.xml',
        'views/menu.xml',
        'views/views.xml',
        'demo/shop.xml',
        'data/dinner_sequence_data.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'price': 29.99,
    'currency': 'USD',
    "installable": True,
    "application": True
}

