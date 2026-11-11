from odoo import fields, models


class PyeDiscountReason(models.Model):
    _name = 'pye.discount.reason'
    _description = 'Motivo de descuento'
    _order = 'sequence, name'

    name = fields.Char(string='Motivo', required=True, translate=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
