#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class barcode(models.Model):

    _name = "vit.barcode"
    _description = "vit.barcode"


    def generate_unique_barcode(self, ):
        pass


    def validate_scan(self, ):
        pass


    def check_expiry(self, ):
        pass


    def deactivate_barcode(self, ):
        pass


    def generate_visit_barcode(self, ):
        pass


    def validate_barcode_scan(self, ):
        pass


    def print_barcode_label(self, ):
        pass


    def check_barcode_expiry(self, ):
        pass


    def regenerate_barcode(self, ):
        pass


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    barcode_value = fields.Char( string=_("Barcode Value"))
    generated_date = fields.Datetime( string=_("Generated Date"))
    expiry_date = fields.Datetime( string=_("Expiry Date"))
    active = fields.Boolean( string=_("Active"))
    entry_scanned = fields.Boolean( string=_("Entry Scanned"))
    exit_scanned = fields.Boolean( string=_("Exit Scanned"))
    entry_scan_time = fields.Datetime( string=_("Entry Scan Time"))
    exit_scan_time = fields.Datetime( string=_("Exit Scan Time"))
    scanner_location = fields.Char( string=_("Scanner Location"))


    visit_id = fields.Many2one(comodel_name="vit.visit",  string=_("Visit"))
