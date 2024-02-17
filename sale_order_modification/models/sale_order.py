from odoo import api, fields, models, _
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = 'sale.order'

    delivery_charge = fields.Float(string='Delivery Charge', copy=False, store=True , compute='_compute_delivery_charge')


    @api.depends('amount_total')
    def _compute_delivery_charge(self):
        for order in self:
            del_charge = order.amount_total * 0.1
            self.delivery_charge = del_charge

    @api.depends('order_line.price_total', 'delivery_charge')
    def _amount_all(self):
        res = super(SaleOrder, self)._amount_all()
        for i in self:
            i.amount_total += i.delivery_charge
        return res


    def _prepare_invoice(self):
        vals = super(SaleOrder, self)._prepare_invoice()
        vals['delivery_charge'] = self.delivery_charge
        return vals




class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_brand = fields.Char(string='Brand', readonly=True)

    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.product_brand = self.product_id.product_tmpl_id.product_brand

    @api.constrains('price_unit')
    def _check_minimum_cost(self):
        for line in self:
            if line.price_unit < line.product_id.product_tmpl_id.minimum_cost:
                raise ValidationError('Unit Price must be greater than Minimum Cost of the product')
