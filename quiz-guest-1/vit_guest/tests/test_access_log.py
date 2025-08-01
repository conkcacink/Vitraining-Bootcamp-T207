from odoo.tests.common import TransactionCase
from odoo.addons.vit_guest.tests.common import VitGuestCommon

from odoo.exceptions import UserError
from odoo.tests import tagged

import logging
_logger = logging.getLogger(__name__)

@tagged('post_install', '-at_install')
class AccessLogTestCase(VitGuestCommon):

	def test_vit_access_log_count(cls):
		_logger.info(' -------------------- test record count -----------------------------------------')
		cls.assertEqual(
		    4,
		    len(cls.access_logs)
		)