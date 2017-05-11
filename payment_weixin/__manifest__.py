# -*- coding: utf-8 -*-

{
    'name': 'Weixin Payment Acquirer',
    'category': 'Website',
    'summary': 'Payment Acquirer: Weixin Implementation',
    'version': '1.0',
    'description': """Weixin Payment Acquirer""",
    'author': 'Odoo CN Community, Jeffery <jeffery9@gmail.com>',
    'depends': ['payment'],
    'data': [
        'views/payment_acquirer.xml',
        'views/weixin.xml',
        'data/weixin.xml',
    ],
    'installable': True,
    'price': 499.99,
    'currency': 'EUR',
}
