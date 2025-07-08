#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import logging
_logger = logging.getLogger(__name__)

class session(models.Model):
    _name = "vit.session"
    _inherit = "vit.session"

    @api.depends("seats","attendee_ids")
    def _get_taken_seats(self, ):
        """
        {
        "@api.depends" : ["seats" , "attendee_ids"]
        }
        """
        # pass
        for rec in self:
            if rec.seats <= 0:
                rec.taken_seats = 0
            else:
                rec.taken_seats = 100.0 * len(rec.attendee_ids) / rec.seats
                
    @api.constrains("instructor_id","attendee_ids")
    def _cek_instruktur(self, ):
        """
        {
        "@api.constrains" : ["instructor_id" , "attendee_ids"]
        }
        """
        # pass
        for session in self:
            x = [att.partner_id.id for att in session.attendee_ids]
            if session.instructor_id.id in x:
                raise ValidationError("Instructor cannot be Attendee.")
        
        return True