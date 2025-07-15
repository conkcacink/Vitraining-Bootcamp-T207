#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class order_line(models.Model):
    _name = "sale.order.line"
    _inherit = "sale.order.line"

    @api.onchange("room_id")
    def onchange_room_id(self, ):
        """
        {
        "@api.onchange" : ["room_id"]
        }
        """
        pass

