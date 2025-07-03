#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class attendee(models.Model):

    _name = "vit.attendee"
    _description = "vit.attendee"


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))


    session_id = fields.Many2one(comodel_name="vit.session",  string=_("Session"))
    partner_id = fields.Many2one(comodel_name="res.partner",  string=_("Partner"))
