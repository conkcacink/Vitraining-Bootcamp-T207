#!/usr/bin/python
#-*- coding: utf-8 -*-

STATES = [('draft','Draft'),('open','Open'),('done','Done')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError

class maintenance(models.Model):
    """
    {
    "menu" : 2
    }
    """

    _name = "vit.maintenance"
    _description = "vit.maintenance"


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, default="New", readonly=True,  string=_("Name"))
    start_date = fields.Datetime( readonly="state=='draft'",  string=_("Start Date"))
    end_date = fields.Datetime( readonly="state=='draft'",  string=_("End Date"))
    state = fields.Selection(selection=STATES,  readonly=True, default=STATES[0][0],  string=_("State"))


    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            if not val.get("name", False) or val["name"] == "New":
                val["name"] = self.env["ir.sequence"].next_by_code("vit.maintenance") or "Error Number!!!"
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

    def action_cancel(self):
        self.state = STATES[0][0]

    def unlink(self):
        for me_id in self :
            if me_id.state != STATES[0][0]:
                raise UserError("Cannot delete non draft record!")
        return super(maintenance, self).unlink()

    room_id = fields.Many2one(comodel_name="vit.room",  readonly="state=='draft'",  string=_("Room"))
