#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class order_line(models.Model):
    """
    {
    "menu" : 0
    }
    """

    _name = "sale.order.line"
    _description = "sale.order.line"


    @api.onchange("room_id")
    def onchange_room_id(self, ):
        """
        {
        "@api.onchange" : ["room_id"]
        }
        """
        pass


    def action_reload_view(self):
        pass


    _inherit = "sale.order.line"


    room_id = fields.Many2one(comodel_name="vit.room",  string=_("Room"))
