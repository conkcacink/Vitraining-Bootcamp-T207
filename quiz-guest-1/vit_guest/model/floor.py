#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class floor(models.Model):

    _name = "vit.floor"
    _description = "vit.floor"


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    floor_number = fields.Char( string=_("Floor Number"))
    description = fields.Text( string=_("Description"))
    is_accessible = fields.Boolean( string=_("Is Accessible"))
    security_level = fields.Selection(selection=[('level1','Level 1'),('level2','Level 2')],  string=_("Security Level"))
    active = fields.Boolean( string=_("Active"))


    tenant_ids = fields.One2many(comodel_name="vit.tenant",  inverse_name="floor_id",  string=_("Tenant"))
