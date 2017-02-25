# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details. Or not.
{
    'name': 'Tournament',
    'category': 'Tournament',
    'summary': 'Organise your Tournament',
    'sequence': 99,
    'version': '1.0',
    'description': """
Organise your Tournament
========================

Organise your tournament, have a complete schedule with match times ready to use in a few seconds.
        """,
    'depends': ['base', 'mail', 'report'],
    'data': [
        'data/tournament_data.xml',
        'security/tournament_security.xml',
        'security/ir.model.access.csv',
        # 'data/tournament_data.xml',
        'views/tournament_assets_backend.xml',
        'views/tournament_views.xml',
    ],
    'demo': [
        'data/tournament_demo.xml',
    ],
    'qweb': [
        "static/src/xml/tournament_templates.xml",
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    # 'license': 'OEEL-1', no clue
}
