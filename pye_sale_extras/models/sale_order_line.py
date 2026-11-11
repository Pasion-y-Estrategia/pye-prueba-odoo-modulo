from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_discount = fields.Float(
        string='Desc. adicional (%)',
        digits='Discount',
        default=0.0,
        help='Descuento adicional que se aplica sobre el precio ya descontado.',
    )
    discount_reason_id = fields.Many2one(
        'pye.discount.reason',
        string='Motivo de descuento',
    )

    def _prepare_base_line_for_taxes_computation(self, **kwargs):
        # Aplica el descuento adicional sobre el descuento estándar.
        kwargs['discount'] = 100 - (100 - self.discount) * (100 - self.extra_discount) / 100
        return super()._prepare_base_line_for_taxes_computation(**kwargs)

    def _prepare_invoice_line(self):
        res = super()._prepare_invoice_line()
        if self.extra_discount:
            res['discount'] = self.extra_discount
        return res
