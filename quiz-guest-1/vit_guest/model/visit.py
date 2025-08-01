#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class visit(models.Model):

    _name = "vit.visit"
    _description = "vit.visit"


    def generate_visit_barcode(self, ):
        pass


    def validate_barcode_entry(self, ):
        pass


    def validate_barcode_exit(self, ):
        pass


    def mark_as_entered(self, ):
        pass


    def mark_as_exited(self, ):
        pass


    def check_barcode_validity(self, ):
        pass


    def send_host_notification(self, ):
        pass


    def calculate_visit_duration(self, ):
        pass


    def expire_visit(self, ):
        pass


    def process_entry_scan(self, ):
        pass


    def process_exit_scan(self, ):
        pass


    def expire_old_visits(self, ):
        pass


    def validate_visits_permissions(self, ):
        pass


    def send_visits_reminder(self, ):
        pass


    def log_security_event(self, ):
        pass


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    visit_date = fields.Datetime( string=_("Visit Date"))
    purpose = fields.Text( string=_("Purpose"))
    expected_duration = fields.Float( string=_("Expected Duration"))
    entry_time = fields.Datetime( string=_("Entry Time"))
    exit_time = fields.Datetime( string=_("Exit Time"))
    status = fields.Selection(selection=[('draft','Draft'),('inprogress','In Progress'),('done','Done')],  string=_("Status"))
    barcode = fields.Char( string=_("Barcode"))
    barcode_used_entry = fields.Boolean( string=_("Barcode Used Entry"))
    barcode_used_exit = fields.Boolean( string=_("Barcode Used Exit"))
    host_notified = fields.Boolean( string=_("Host Notified"))
    security_notes = fields.Text( string=_("Security Notes"))


    tenant_id = fields.Many2one(comodel_name="vit.tenant",  string=_("Tenant"))
    floor_id = fields.Many2one(comodel_name="vit.floor",  string=_("Floor"))
    guest_id = fields.Many2one(comodel_name="vit.guest",  string=_("Guest"))
    barcode__ids = fields.One2many(comodel_name="vit.barcode",  inverse_name="visit_id",  string=_("Barcode"))
