# -*- coding: utf-8 -*-

from odoo import models, fields, api

from . import monto_letra

class AddFieldAmountText(models.Model):
	_inherit = "account.invoice"

	cam_monto_letra = fields.Char(compute='_get_amount_to_text', string='Monto en letra', readonly=True, help='Amount of the invoice in letter')

	@api.one
	@api.depends('amount_total')
	def _get_amount_to_text(self):
		self.cam_monto_letra = monto_letra.get_amount_to_text(self, self.amount_total, self.currency_id.name)