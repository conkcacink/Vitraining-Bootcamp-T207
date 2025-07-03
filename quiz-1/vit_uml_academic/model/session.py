#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class session(models.Model):

    _name = "vit.session"
    _description = "vit.session"


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    start_date = fields.Date( string=_("Start Date"))
    duration = fields.Integer( string=_("Duration"))
    seats = fields.Integer( string=_("Seats"))
    taken_seats = fields.Float( string=_("Taken Seats"))
    image_small = fields.Binary( string=_("Image Small"))


    course_id = fields.Many2one(comodel_name="vit.course",  string=_("Course"))
    instructor_id = fields.Many2one(comodel_name="res.partner",  string=_("Instructor"))
    attendee_ids = fields.One2many(comodel_name="vit.attendee",  inverse_name="session_id",  string=_("Attendee"))
