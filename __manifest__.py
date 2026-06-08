# -*- coding: utf-8 -*-
{
    'name': 'Birthday Reminder',
    'version': '1.0.0',
    'summary': 'Store birthdays and send automatic email wishes',
    'description': """
        Birthday Reminder & Wish automation.
        Store contact birthdays and automatically send email wishes via a daily cron job.
    """,
    'author': 'Md Mahbubul Hasan',
    'website': 'https://erp23.com/',
    'category': 'Human Resources',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'data/birthday_cron.xml',
        'views/birthday_views.xml',
        'views/birthday_menus.xml',
    ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
