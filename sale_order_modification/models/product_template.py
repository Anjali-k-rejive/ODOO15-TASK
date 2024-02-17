from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    minimum_cost = fields.Float(string='Minimum Cost')
    product_brand = fields.Char(string='Brand')