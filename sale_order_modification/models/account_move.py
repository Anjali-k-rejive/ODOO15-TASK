from odoo import api, fields, models, _



class AccountMove(models.Model):
    _inherit = 'account.move'

    delivery_charge = fields.Float(string='Delievery charge', copy=False,
                                   store=True)

    @api.depends(
        'line_ids.matched_debit_ids.debit_move_id.move_id.payment_id.is_matched',
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_debit_ids.debit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.matched_credit_ids.credit_move_id.move_id.payment_id.is_matched',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual',
        'line_ids.matched_credit_ids.credit_move_id.move_id.line_ids.amount_residual_currency',
        'line_ids.debit',
        'line_ids.credit',
        'line_ids.currency_id',
        'line_ids.amount_currency',
        'line_ids.amount_residual',
        'line_ids.amount_residual_currency',
        'line_ids.payment_id.state',
        'line_ids.full_reconcile_id',
        'amount_total_signed','amount_total_in_currency_signed')

    def _compute_amount(self):
        res = super(AccountMove, self)._compute_amount()
        for val in self:
            val.amount_total_in_currency_signed += val.delivery_charge
            val.amount_total_signed += val.delivery_charge
            val.amount_total += val.delivery_charge
            val.amount_residual += val.delivery_charge
        return res


