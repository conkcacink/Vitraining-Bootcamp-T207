"""
To perform the sample basic tests, execute this command:
    odoo-bin -c yourodoo.conf -d yourdb -u vit_uml_academic --test-tags /vit_uml_academic

When you have implemented the detailed test cases on your inherited addon, then execute this:
    odoo-bin -c yourodoo.conf -d yourdb -u vit_uml_academic_inherited --test-tags /vit_uml_academic_inherited

"""
from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged

import logging
_logger = logging.getLogger(__name__)

@tagged('post_install', '-at_install')
class VitUmlAcademicCommon(TransactionCase):

	@classmethod
	def setUpClass(cls):
		# add env on cls and many other things
		super(VitUmlAcademicCommon, cls).setUpClass()

		# create the data for each tests. By doing it in the setUpClass instead
		# of in a setUp or in each test case, we reduce the testing time and
		# the duplication of code.