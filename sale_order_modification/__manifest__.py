{
    'name': "sale order modification",
    'version': '15.0.',
    'summary': """sale order modification""",
    'description': """Zinfog Machine Test""",
    'depends': ['base', 'sale', 'account', 'stock'],

    'data': [
        'views/sale_order.xml',
        'views/account_move.xml',
        'views/product_template.xml'
    ],

    'installable': True,
    'application': True,
    'auto_install': False

}