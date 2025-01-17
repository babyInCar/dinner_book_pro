# coding: utf-8
##############################################################################
{
    'name': '加班订餐',
    'version': '18.0.1.0.0',
    'category': 'Warehouse',
    'summary': 'This module allows to split a stock.picking',
    'description': """With this module you can split a "stock.picking" as many times as necessary, reducing it to a stock.move.""",
    'license': 'AGPL-3',
    'author': "GaoShuang (www.todooweb.com)",
    'website': "https://todooweb.com/",
    'contributors': [
        "Equipo Dev <devtodoo@gmail.com>",
        "Edgar Naranjo <edgarnaranjof@gmail.com>",
    ],
    'support': 'devtodoo@gmail.com',
    'depends': ['base', 'sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_view.xml',
    ],
    'images': [
       'static/description/screenshot_split.png'
    ],
    'live_test_url': 'https://youtu.be/HNGusvLC6ag',
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 19.99,
    'currency': 'EUR',
}