#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class guest(models.Model):
    _name = "vit.guest"
    _inherit = "vit.guest"

    def validate_identification(self, ):
        pass

