#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class room_type(models.Model):
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
    is_room_type = fields.Boolean( string=_("Is Room Type"))


