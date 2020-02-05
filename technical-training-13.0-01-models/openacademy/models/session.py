# -*- coding: utf-8 -*-

from odoo import models, fields, api, constrains, _

    
class OpenAcademySession(models.Model):
    _name = 'openacademy.session'
    _description =  'OpenAcademy Sessions'
    _order = 'id, start_date'
    
    name = fields.Char(string='Name', required=True, 
                        index=True, help='Enter your course title on this field.')
    active = fields.Boolean(string='Active', default=True)
    course_id = fields.Many2one(comodel_name='openacademy.course', required=True)
    insructor_id = fields.Many2one(comodel_name='res.partner', required=True,
                        string='Instructor', ondelete='restrict', copy=False)
    location_id = fields.Many2one(comodel_name='res.partner', ondelete='restrict')
    code = fields.Char(string='Code', size=32)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    avail_seat_per = fields.Float(string='Avaliable Seats (%)')
    max_seats = fields.Integer(string='Maximum Seats')
    min_seats = fields.Integer(string='Minimum Required Seats')
    syllabus_notes = fields.Html(string='Syllabus')
    state = fields.Selection(selection=[
                            ('draft', 'New'),
                            ('approve', 'Approved'),
                            ('confirm', 'Confirmed'),
                            ('cancel', 'Cancelled'),
                            ('done', 'Done'),
                        ])
#     _sql_coonstraints = {
#         ('openacademy_Session_unique_code', 'UNIQUE (code)', 'Code must be unique !'),
#     }
#     @api.constrains('start_date', 'end_date')
#     def _check_dates(self):
#         for session in self:
#             if session.start_date > session.end_date:
#                 raise exceptions.ValidationError(_('Start date "%s" can not be after end date "%s"')%(session.start_date, session.end_date))
#     @api.model_create_multi
#     def create(self, vals_list):
#         _logger.warining('*'*)