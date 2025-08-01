#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class tenant(models.Model):
    _name = "vit.tenant"
    _inherit = "vit.tenant"

    def notify_visitor_arrival(self, ):
        pass


    def check_business_hours(self, ):
        pass


    def send_visitor_notification(self, ):
        pass


    def send_security_alert(self, ):
        pass


    def validate_visitor_approval(self, ):
        pass

