#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class course(models.Model):
    _name = "vit.course"
    _inherit = "vit.course"

    _sql_constraints = [
        ('cek_name_desc', 'CHECK(name <> description)', 'Field name dan description tidak boleh sama.'),
        ('cek_unik_name', 'UNIQUE(name)', 'Nama harus unik.')
    ]