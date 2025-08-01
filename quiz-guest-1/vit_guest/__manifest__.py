#-*- coding: utf-8 -*-

{
	"name": "Guest Management",
	"version": "1.0",
	"depends": [
		"base"
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
		"view/guest.xml",
		"report/guest.xml",
		"view/floor.xml",
		"report/floor.xml",
		"view/tenant.xml",
		"report/tenant.xml",
		"view/visit.xml",
		"report/visit.xml",
		"view/barcode.xml",
		"report/barcode.xml",
		"view/access_log.xml",
		"report/access_log.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True,
	"odooVersion": 18
}