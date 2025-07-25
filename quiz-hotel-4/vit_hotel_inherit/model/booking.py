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
        # pass
        # check tanggal check-in if not empty
        if not self.date_check_in:
            raise UserError(_("Check-In date cannot be empty."))
        
        # check product line is
        if not self.order_line:
            raise UserError(_("Please add at least one room to the booking order."))

    def action_check_out(self, ):
        # menghitung jumlah hari antara check-in dan check-out
        if not self.date_check_in or not self.date_check_out:
            raise UserError(_("Check-in and check-out dates must be set."))
        if self.date_check_out <= self.date_check_in:
            raise UserError(_("Check-out date must be after check-in date."))
        days = (self.date_check_out - self.date_check_in).days
        
        for line in self.order_line:
            if line.room_id:
                # update quantity and price based on the number of days
                line.product_uom_qty = days
                line.price_unit = line.room_id.room_type_id.list_price * days
        # pass

    def action_confirm(self, ):
        """
        {
        "super" : true
        }
        """
        self.action_check_in()
        
        for line in self.order_line:
            if line.room_id:
                line.room_id.is_available = False
        
        res = super(booking, self).action_confirm()
        return res

    def action_record_deposit(self, ):
        #create account move to record deposit, must install om_account_acountant
        if not self.deposit:
            raise UserError(_("Deposit amount must be set."))
        
        move_vals = {
            'move_type' : 'entry',
            'ref' : _('Deposit for Booking %s') % self.name,
            'date' : fields.Date.context_today(self),
            'journal_id' : self.env['account.journal'].search([('type', '=', 'bank')], limit=1).id,
            
            'line_ids' : [
                (0, 0, {
                    'account_id' : self.env['account.account'].search([('account_type', '=', 'asset_cash')], limit=1).id,
                    'name' : _('Deposit Received'),
                    'debit' : self.deposit,
                    'credit' : 0.0,
                    'partner_id' : self.partner_id.id,
                }),  
                (0 ,0, {
                    'account_id' : self.partner_id.property_account_receivable_id.id,
                    'name' : _('Deposit Liability'),
                    'debit' : 0.0,
                    'credit' : self.deposit,
                    'partner_id' : self.partner_id.id,
                }),
            ],
        }
        
        move = self.env['account.move'].create(move_vals)
        move.action_post()
        self.deposit_journal_id = move.id
        
    def action_return_deposit(self):
        #create account move to return deposit, must install om_account_acountant
        if not self.deposit:
            raise UserError(_("Deposit amount must be set."))
        
        move_vals = {
            'move_type' : 'entry',
            'ref' : _('Return Deposit for Booking %s') % self.name,
            'date' : fields.Date.context_today(self),
            'journal_id' : self.env['account.journal'].search([('type', '=', 'bank')], limit=1).id,
            
            'line_ids' : [
                (0, 0, {
                    'account_id' : self.env['account.account'].search([('account_type', '=', 'asset_cash')], limit=1).id,
                    'name' : _('Deposit Returned'),
                    'debit' : 0.0,
                    'credit' : self.deposit,
                    'partner_id' : self.partner_id.id,
                }),  
                (0 ,0, {
                    'account_id' : self.partner_id.property_account_receivable_id.id,
                    'name' : _('Deposit Return Liability'),
                    'debit' : self.deposit,
                    'credit' : 0.0,
                    'partner_id' : self.partner_id.id,
                }),
            ],
        }
        
        move = self.env['account.move'].create(move_vals)
        move.action_post()
        self.return_deposit_journal_id = move.id