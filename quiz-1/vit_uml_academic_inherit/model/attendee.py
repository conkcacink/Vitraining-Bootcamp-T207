#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class attendee(models.Model):
    _name = "vit.attendee"
    _inherit = "vit.attendee"
