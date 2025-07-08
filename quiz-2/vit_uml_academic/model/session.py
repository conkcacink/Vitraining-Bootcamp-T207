#!/usr/bin/python
#-*- coding: utf-8 -*-

STATES = [('draft','Draft'),('open','Open'),('done','Done')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError
import time

class session(models.Model):
    """
    {
    "imports" : [ "import time" ]
    }
    """

    _name = "vit.session"
    _description = "vit.session"


    @api.depends("seats","attendee_ids")
    def _get_taken_seats(self, ):
        """
        {
        "@api.depends" : ["seats" , "attendee_ids"]
        }
        """
        pass


    @api.constrains("instructor_id","attendee_ids")
    def _cek_instruktur(self, ):
        """
        {
        "@api.constrains" : ["instructor_id" , "attendee_ids"]
        }
        """
        pass


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, default="New", readonly=True,  string=_("Name"))
    start_date = fields.Date( readonly=True, states={"draft" : [("readonly",False)]},  string=_("Start Date"), default=lambda self:time.strftime("%Y-%m-%d"))
    duration = fields.Integer( readonly=True, states={"draft" : [("readonly",False)]},  string=_("Duration"))
    seats = fields.Integer( readonly=True, states={"draft" : [("readonly",False)]},  string=_("Seats"))
    taken_seats = fields.Float( readonly=True, states={"draft" : [("readonly",False)]}, compute="_get_taken_seats",  string=_("Taken Seats"))
    image_small = fields.Binary( readonly=True, states={"draft" : [("readonly",False)]},  string=_("Image Small"))
    state = fields.Selection(selection=STATES,  readonly=True, default=STATES[0][0],  string=_("State"))


    @api.model
    def create(self, vals):
        if not vals.get("name", False) or vals["name"] == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("vit.session") or "Error Number!!!"
        return super(session, self).create(vals)

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
        return super(session, self).unlink()

    course_id = fields.Many2one(comodel_name="vit.course",  readonly=True, states={"draft" : [("readonly",False)]},  string=_("Course"))
    instructor_id = fields.Many2one(comodel_name="res.partner",  readonly=True, states={"draft" : [("readonly",False)]},  string=_("Instructor"))
    attendee_ids = fields.One2many(comodel_name="vit.attendee",  inverse_name="session_id",  readonly=True, states={"draft" : [("readonly",False)]},  string=_("Attendee"))
