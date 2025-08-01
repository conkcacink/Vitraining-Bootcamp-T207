#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class visit(models.Model):
    _name = "vit.visit"
    _inherit = "vit.visit"

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

