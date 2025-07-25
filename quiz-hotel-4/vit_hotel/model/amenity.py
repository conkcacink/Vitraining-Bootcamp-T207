#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class amenity(models.Model):
    """
    {
    "menu" : 2
    }
    """

    _name = "product.template"
    _description = "product.template"


    def action_reload_view(self):
        pass


    _inherit = "product.template"
    is_amenity = fields.Boolean( string=_("Is Amenity"))


