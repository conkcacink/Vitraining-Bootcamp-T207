#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class room(models.Model):
    """
    {
    "menu" : 1
    }
    """

    _name = "vit.room"
    _description = "vit.room"


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    is_available = fields.Boolean( string=_("Is Available"), default=True)
    description = fields.Text(string=_("Description"))
    image = fields.Binary(string="Image", attachment=True)

    """
    {
        "kanban:ribbon": true
    }
    """

    room_type_id = fields.Many2one(comodel_name="product.product",  string=_("Room Type"))
    amenity_ids = fields.Many2many(comodel_name="product.template",  string=_("Amenity"))
