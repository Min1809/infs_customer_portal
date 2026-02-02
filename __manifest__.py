# -*- coding: utf-8 -*-
{
    'name': "infs_customer_portal",
    'version': '1.0.0',
    'category': 'infs',
    'author': "INFS",
    'summary': 'INFS Module for Customer Portal Customization',
    'description': """
        INFS module for Customer Portal Customization.
        - 
    """,
    'depends': ['base', 'project','portal','website','helpdesk', ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/portal_templates.xml',
    ],
    'icon': '/infs_customer_portal/static/description/icon.png',
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': True,
    'sequence': 10,
}

