#-*- coding: utf-8 -*-

{
	"name": "Addon Academic by UML",
	"version": "1.0",
	"depends": [
		"base",
		"crm"
	],
	"author": "Akhmad Daniel Sembiring",
	"category": "Utility",
	"website": "http://vitraining.com",
	"images": [
		"static/description/images/main_screenshot.jpg"
	],
	"price": "100",
	"license": "OPL-1",
	"currency": "USD",
	"summary": "",
	"description": "",
	"data": [
		"security/groups.xml",
		"security/ir.model.access.csv",
		"view/menu.xml",
		"view/course.xml",
		"report/course.xml",
		"view/session.xml",
		"report/session.xml",
		"data/sequence_session.xml",
		"view/user.xml",
		"view/partner.xml",
		"view/attendee.xml",
		"report/attendee.xml",
		"view/instructor.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True,
	"odooVersion": 16
}