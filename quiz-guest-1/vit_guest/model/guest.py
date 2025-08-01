#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class guest(models.Model):

    _name = "vit.guest"
    _description = "vit.guest"


    def validate_identification(self, ):
        pass


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    email = fields.Char( string=_("Email"))
    identification_number = fields.Char( string=_("Identification Number"))
    phone = fields.Char( string=_("Phone"))
    company = fields.Char( string=_("Company"))
    photo = fields.Binary( string=_("Photo"))
    is_blacklisted = fields.Boolean( string=_("Is Blacklisted"))
    registration_date = fields.Datetime( string=_("Registration Date"))
    last_visit_date = fields.Datetime( string=_("Last Visit Date"))
    total_visits = fields.Integer( string=_("Total Visits"))
    active = fields.Boolean( string=_("Active"))


