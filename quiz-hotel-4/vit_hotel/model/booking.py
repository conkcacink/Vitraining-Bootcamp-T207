#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class booking(models.Model):
    """
    {
    "menu" : 1
    }
    """

    _name = "sale.order"
    _description = "sale.order"


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

    def action_record_deposit(self, ):
        pass
    
    def action_return_deposit(self, ):
        pass

    def action_reload_view(self):
        pass


    _inherit = "sale.order"
    date_check_in = fields.Datetime( string=_("Date Check In"))
    date_check_out = fields.Datetime( string=_("Date Check Out"))
    is_booking = fields.Boolean( string=_("Is Booking"))
    deposit = fields.Monetary( string=_("Deposit"))
    deposit_journal_id = fields.Many2one( 'account.move', string=_("Deposit Journal"))
    return_deposit_journal_id = fields.Many2one( 'account.move', string=_("Return Deposit Journal"))

