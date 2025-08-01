#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class barcode(models.Model):
    _name = "vit.barcode"
    _inherit = "vit.barcode"

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

