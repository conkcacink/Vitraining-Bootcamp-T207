#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class room_variant(models.Model):
    """
    {
    "menu" : 2
    }
    """

    _name = "product.product"
    _description = "product.product"


    def action_reload_view(self):
        pass


    _inherit = "product.product"


