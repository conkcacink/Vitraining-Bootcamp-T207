#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class booking(models.Model):
    _name = "sale.order"
    _inherit = "sale.order"

    def action_check_in(self, ):
        pass


    def action_check_out(self, ):
        pass


    def action_confirm(self, ):
        """
        {
        "super" : true
        }
        """
        res = super(booking, self).action_confirm()
        return res

