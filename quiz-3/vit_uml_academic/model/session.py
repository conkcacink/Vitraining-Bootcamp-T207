#!/usr/bin/python
#-*- coding: utf-8 -*-

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
    
    def print_session_action(self):
        return self.env.ref('vit_uml_academic.action_report_vit_session').report_action(self)

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


    def action_add_attendees(self, ):
        """
        {
        "wizard:name" : "add_attendee_wizard"
        }
        """
        # opening wizard....add_attendee_wizard
        self.ensure_one()
        view = self.env.ref('vit_uml_academic.view_vit_add_attendee_wizard_form')
        wizard = self.env['vit.add_attendee_wizard'].create({
            'session_id': self.id
        })
        return {
            'name': _('Add Attendee Wizard'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'vit.add_attendee_wizard',
            'views': [(view.id, 'form')],
            'view_id': view.id,
            'target': 'new',
            'res_id': wizard.id,
            'context': self.env.context,
        }


    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, default="New", readonly=True,  string=_("Name"))
    start_date = fields.Date( string=_("Start Date"), default=lambda self:time.strftime("%Y-%m-%d"))
    duration = fields.Integer( string=_("Duration"))
    seats = fields.Integer( string=_("Seats"))
    taken_seats = fields.Float(compute="_get_taken_seats",  string=_("Taken Seats"))
    image_small = fields.Binary( string=_("Image Small"))
    stage_is_draft = fields.Boolean(related="stage_id.draft", store=True,  string=_("Stage Is Draft"))
    stage_is_done = fields.Boolean(related="stage_id.done", store=True,  string=_("Stage Is Done"))
    allow_confirm = fields.Boolean(related="stage_id.allow_confirm", store=True,  string=_("Allow Confirm"))
    allow_cancel = fields.Boolean(related="stage_id.allow_cancel", store=True,  string=_("Allow Cancel"))
    stage_name = fields.Char(related="stage_id.name", store=True,  string=_("Stage Name"))


    @api.model
    def create(self, vals):
        if not vals.get("name", False) or vals["name"] == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("vit.session") or "Error Number!!!"
        return super(session, self).create(vals)

    def _get_first_stage(self):
        try:
            data_id = self.env["vit.session_stage"].sudo().search([], limit=1, order="sequence asc")
            if data_id:
                return data_id
        except KeyError:
            return False

    def action_confirm(self):
        stage = self._get_next_stage()
        self.stage_id=stage
        if self.stage_id.execute_enter and hasattr(self, self.stage_id.execute_enter) and callable(getattr(self, self.stage_id.execute_enter)):
            eval(f"self.{self.stage_id.execute_enter}()")

    def action_cancel(self):
        stage = self._get_previous_stage()
        self.stage_id=stage

    def _get_next_stage(self):
        current_stage_seq = self.stage_id.sequence
        data_id = self.env["vit.session_stage"].sudo().search([("sequence",">",current_stage_seq)], limit=1, order="sequence asc")
        if data_id:
            return data_id
        else:
            return self.stage_id

    def _get_previous_stage(self):
        current_stage_seq = self.stage_id.sequence
        data_id = self.env["vit.session_stage"].sudo().search([("sequence","<",current_stage_seq)], limit=1, order="sequence desc")
        if data_id:
            return data_id
        else:
            return self.stage_id

    @api.model
    def _group_expand_states(self, stages, domain, order):
        return self.env['brap.penawaran_stage'].search([])

    def unlink(self):
        for me_id in self :
            if not me_id.stage_id.draft:
                raise UserError("Cannot delete non draft record!  Make sure that the Stage draft flag is checked.")
        return super(session, self).unlink()

    course_id = fields.Many2one(comodel_name="vit.course",  string=_("Course"))
    instructor_id = fields.Many2one(comodel_name="res.partner",  string=_("Instructor"))
    stage_id = fields.Many2one(comodel_name="vit.session_stage",  default=_get_first_stage, copy=False, group_expand="_group_expand_states",  string=_("Stage"))
    attendee_ids = fields.One2many(comodel_name="vit.attendee",  inverse_name="session_id",  string=_("Attendee"))
