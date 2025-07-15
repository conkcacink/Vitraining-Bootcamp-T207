#-*- coding: utf-8 -*-

{
	"name": "Hotel Management Inherited",
	"version": "1.0",
	"depends": [
		"sale",
		"stock",
		"account",
		"vit_hotel"
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
		#"view/room.xml",
		#"view/amenity.xml",
		#"view/maintenance.xml",
		#"data/sequence_maintenance.xml",
		#"view/order_line.xml",
		#"view/booking.xml",
		#"view/room_type.xml",
		#"view/room_variant.xml"
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