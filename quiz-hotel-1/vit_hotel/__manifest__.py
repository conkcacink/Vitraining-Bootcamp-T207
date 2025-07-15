#-*- coding: utf-8 -*-

{
	"name": "Hotel Management",
	"version": "1.0",
	"depends": [
		"sale",
		"stock",
		"account"
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
		"view/room.xml",
		"report/room.xml",
		"view/amenity.xml",
		"view/amenity_view_inherit.xml",
		"view/maintenance.xml",
		"report/maintenance.xml",
		"data/sequence_maintenance.xml",
		"view/order_line.xml",
		"view/booking.xml",
		"view/room_type.xml",
		"view/room_variant.xml"
	],
	"installable": True,
	"auto_install": False,
	"application": True,
	"odooVersion": 18,
	"menus": [
		"Front Office",
		"Back Office",
		"Inventory Management",
		"Accounting &amp; Finance",
		"Reporting &amp; Analysis"
	]
}