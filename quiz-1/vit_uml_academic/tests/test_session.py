from odoo.tests.common import TransactionCase
from odoo.addons.vit_uml_academic.tests.common import VitUmlAcademicCommon

from odoo.exceptions import UserError
from odoo.tests import tagged

import logging
_logger = logging.getLogger(__name__)

@tagged('post_install', '-at_install')
class SessionTestCase(VitUmlAcademicCommon):

	def test_vit_session_count(cls):
		_logger.info(' -------------------- test record count -----------------------------------------')
		cls.assertEqual(
		    4,
		    len(cls.sessions)
		)