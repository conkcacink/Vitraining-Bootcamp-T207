#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class add_attendee_wizard(models.TransientModel):
    """
    {
    "is_a_wizard" : true
    }
    """

    _name = "vit.add_attendee_wizard"
    _description = "vit.add_attendee_wizard"


    def action_add_attendees(self, ):
        pass


    def action_reload_view(self):
        pass



    session_id = fields.Many2one(comodel_name="vit.session",  string=_("Session"))
    partner_ids = fields.Many2many(comodel_name="res.partner",  string=_("Partner"))
