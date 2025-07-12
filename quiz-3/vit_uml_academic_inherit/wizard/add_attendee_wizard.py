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
    _inherit = "vit.add_attendee_wizard"


    def action_add_attendees(self, ):
        self.session_id.attendee_ids = [(0,0,{'name':partner.name,'partner_id':partner.id}) for partner in self.partner_ids]        

    # session_id = fields.Many2one(comodel_name="vit.session",  string=_("Session"))
    # partner_ids = fields.Many2many(comodel_name="res.partner",  string=_("Partner"))
