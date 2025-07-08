#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class course(models.Model):

    _name = "vit.course"
    _description = "vit.course"


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    description = fields.Text( string=_("Description"))


    responsible_id = fields.Many2one(comodel_name="res.users",  string=_("Responsible"))
    session_ids = fields.One2many(comodel_name="vit.session",  inverse_name="course_id",  string=_("Session"))
