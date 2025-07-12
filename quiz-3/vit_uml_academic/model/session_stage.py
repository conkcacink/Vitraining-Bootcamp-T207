#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class session_stage(models.Model):
    """
    {
    "is_a_stage" : true,
    "data" : [
    	{"name":"Draft", "sequence":1, "draft":true, "done":false, "open":false, "fold":false, "allow_confirm":true, "allow_cancel":false, "execute_enter":"", "confirmation":"" },
    	{"name":"Open", "sequence":2, "draft":false, "done":false, "open":true, "fold":false, "allow_confirm":true, "allow_cancel":true, "execute_enter":"", "confirmation":"" },
    	{"name":"Verifikasi", "sequence":3, "draft":false, "done":false, "open":true, "fold":false, "allow_confirm":true, "allow_cancel":true, "execute_enter":"", "confirmation":"" },
    	{"name":"Done", "sequence":4, "draft":false, "done":true, "open":false, "fold":false, "allow_confirm":false, "allow_cancel":false, "execute_enter":"", "confirmation":"" }
    ]
    }
    """

    _name = "vit.session_stage"
    _description = "vit.session_stage"

    _order = "sequence asc"

    def action_reload_view(self):
        pass

    name = fields.Char( required=True, copy=False, string=_("Name"))
    sequence = fields.Integer( string=_("Sequence"))
    draft = fields.Boolean( string=_("Draft"))
    done = fields.Boolean( string=_("Done"))
    open = fields.Boolean( string=_("Open"))
    fold = fields.Boolean( string=_("Fold"))
    allow_confirm = fields.Boolean( string=_("Allow Confirm"))
    allow_cancel = fields.Boolean( string=_("Allow Cancel"))
    execute_enter = fields.Char( string=_("Execute Enter"))
    confirmation = fields.Char( string=_("Confirmation"))


