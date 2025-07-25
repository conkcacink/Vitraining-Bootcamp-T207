#!/usr/bin/python
#-*- coding: utf-8 -*-

STATES = [('draft','Draft'),('open','Open'),('done','Done')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class maintenance(models.Model):
    _name = "vit.maintenance"
    _inherit = "vit.maintenance"

    @api.model_create_multi
    def create(self, vals):
        return super(maintenance, self).create(vals)

    def action_confirm(self):
        current_index=0
        current_state=self.state
        for st in STATES:

            current_index += 1
            if current_index >= len(STATES):
                current_index -= 1

            if current_state == st[0]:
                self.state = STATES[current_index][0]
                
        if self.state == STATES[1][0]:
            self.room_id.is_available = False
        elif self.state == STATES[2][0]:
            self.room_id.is_available = True

    def action_cancel(self):
        self.state = STATES[0][0]

    def unlink(self):
        for me_id in self :
            if me_id.state != STATES[0][0]:
                raise UserError("Cannot delete non draft record!")
        return super(maintenance, self).unlink()
