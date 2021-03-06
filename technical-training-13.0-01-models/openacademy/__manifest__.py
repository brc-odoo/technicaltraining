# -*- coding: utf-8 -*-
{
    'name':        "OpenAcademy",

    'summary':
                   """
                   Openacademy
                   """,

    'description': """
        Manage course, classes, teachers, students, ...
    """,

    'author':      "Odoo",
    'website':     "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':    'OpenAcademy',
    'version':     '0.1',

    # any module necessary for this one to work correctly
    'depends':     ['contacts'],

    # always loaded
    'data':        [
        "views/openacademy_menu_views.xml",
        "views/openacademy_course_views.xml",
        "views/openacademy_session_views.xml",
        "views/openacademy_attendees_views.xml",
        "views/res_partner_views.xml"

    ],
    # only loaded in demonstration mode
    'demo':        [
    ],
    'license': 'AGPL-3',
}
