
from odoo import api, fields, models


class PayWizard(models.TransientModel):
    _name = "pay.wizard"
    _description = "支付"

    total_amount = fields.Float(string="总价", default=lambda self: self.env.context.get('total_price'))


    def action_pay(self):
        """支付"""
        active_id = self.env.context.get('active_id')
        active_model = self.env.context.get('active_model')
        flow_id = self.env[active_model].search([('id', '=', active_id)])
        # book_id = self.env['dinner.book.pro'].browse(self._context.get('active_id'))
        flow_id.pay_status = 'paid'
        flow_id.commit()
