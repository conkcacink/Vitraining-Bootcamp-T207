#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class tenant(models.Model):

    _name = "vit.tenant"
    _description = "vit.tenant"


    def notify_visitor_arrival(self, ):
        pass


    def check_business_hours(self, ):
        pass


    def send_visitor_notification(self, ):
        pass


    def send_security_alert(self, ):
        pass


    def validate_visitor_approval(self, ):
        pass


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    contact_person = fields.Char( string=_("Contact Person"))
    contact_email = fields.Char( string=_("Contact Email"))
    contact_phone = fields.Char( string=_("Contact Phone"))
    office_number = fields.Char( string=_("Office Number"))
    business_hours_start = fields.Float( string=_("Business Hours Start"))
    business_hours_end = fields.Float( string=_("Business Hours End"))
    is_accessible = fields.Boolean( string=_("Is Accessible"))
    requires_approval = fields.Boolean( string=_("Requires Approval"))
    active = fields.Boolean( string=_("Active"))


    floor_id = fields.Many2one(comodel_name="vit.floor",  string=_("Floor"))
