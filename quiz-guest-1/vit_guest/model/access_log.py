#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class access_log(models.Model):

    _name = "vit.access_log"
    _description = "vit.access_log"


    def log_entry_attempt(self, ):
        pass


    def log_exit_attempt(self, ):
        pass


    def log_access_denied(self, ):
        pass


    def generate_security_report(self, ):
        pass


    def log_security_event(self, ):
        pass


    def analyze_security_patterns(self, ):
        pass


    def get_failed_access_attempts(self, ):
        pass


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    action_type = fields.Selection(selection=[('action1','Action 1'),('action2','Action 2')],  string=_("Action Type"))
    timestamp = fields.Datetime( string=_("Timestamp"))
    barcode_scanned = fields.Char( string=_("Barcode Scanned"))
    scanner_location = fields.Char( string=_("Scanner Location"))
    success = fields.Boolean( string=_("Success"))
    failure_reason = fields.Text( string=_("Failure Reason"))
    security_officer = fields.Char( string=_("Security Officer"))


    guest_id = fields.Many2one(comodel_name="vit.guest",  string=_("Guest"))
    visit_id = fields.Many2one(comodel_name="vit.visit",  string=_("Visit"))
