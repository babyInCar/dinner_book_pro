# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Shop(models.Model):
    _name = "res.shop"

    name = fields.Char("店家名")
    goods_ids = fields.One2many("dinner.goods", 'shop_id', string="菜单")


# class DishMenu(models.Model):
#     _name = "dish.menu"
#     _description = '菜单'

    # menu_id = fields.Many2one('res.shop', string="菜单id")
    # category = fields.Selection([('meat', '荤菜'), ('vegetables', '素菜'), ('drink', '饮品')], '类别')
    # goods_ids = fields.One2many("dinner.goods", string="晕菜/素菜/饮品")


class DinnerGoods(models.Model):
    _name = "dinner.goods"
    _description = '菜品名称'
    _rec_name = "goods_name"

    shop_id = fields.Many2one('res.shop', string="菜单id")
    category = fields.Selection([('meat', '荤菜'), ('vegetables', '素菜'), ('drink', '饮品')], '类别')
    goods_name = fields.Char(string="菜品名")

    @api.model
    def _search(self, domain, offset=0, limit=None, order=None):
        """修改search的内容"""
        if self.env.context.get('shop_id'):
            domain += [('shop_id', '=', self.env.context.get('shop_id'))]
        return super()._search(domain, offset=offset, limit=limit, order=order)


class DinnerBookProLine(models.Model):
    _name = "dinner.book.pro.line"
    _description = 'dinner_book_pro_line'

    book_id = fields.Many2one('dinner.book.pro', string="订餐单")
    book_date = fields.Date(string="订餐日期", default=fields.Date.today)
    book_option = fields.Selection([('launch', '午餐'), ('dinner', '晚餐')], string='订餐时间')
    shop_id = fields.Many2one('res.shop', string="商家")
    meat = fields.Many2one('dinner.goods', string="荤菜", domain=[('category', '=', 'meat')])
    vegetables = fields.Many2one('dinner.goods', string="素菜", domain=[('category', '=', 'vegetables')])
    drink = fields.Many2one('dinner.goods', string="饮品", domain=[('category', '=', 'drink')])
    price = fields.Float(string="价格", compute='_compute_price', store=True, precompute=True)

    @api.depends('book_option')
    def _compute_price(self):
        """设置对应的价格"""
        for line in self:
            if line.book_option == 'launch':
                line.price = 20
            elif line.book_option == 'dinner':
                line.price = 0
            else:
                line.price = 0

    # @api.onchange('shop_id')
    # def onchange_shop_id(self):
    #     """选择不同的商家，荤菜和素菜对应的下拉框修改"""
    #     self.env["dinner.goods"].with_context({"shop_id": self.shop_id})._search([])


class DinnerBookPro(models.Model):
    _name = 'dinner.book.pro'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'dinner_book_pro'

    sn_no = fields.Char(string="流水号", default=lambda self: self.env['ir.sequence'].next_by_code('dinner.book.pro'))
    user = fields.Many2one('res.users', string="订餐人", default=lambda self: self.env.user)
    book_line = fields.One2many('dinner.book.pro.line', 'book_id', string="订餐明细")
    pay_status = fields.Selection([('unpaid', '待支付'), ('paid', '已支付'), ('not_pay', '无需支付')], '支付状态', compute='_compute_total_price', store=True)
    status = fields.Selection([('draft', '草稿'),
                               ('book', '已提交'),
                               ('committed', '已截止'),
                               ('cancel', '已取消')], default='draft', string="点餐状态")
    total_price = fields.Float(string="总价", compute='_compute_total_price')

    @api.depends('book_line.price')
    def _compute_total_price(self):
        """计算总价"""
        for item in self:
            item.total_price = sum(line.price for line in item.book_line)
            if item.pay_status == 'paid':
                continue
            else:
                item.pay_status = 'unpaid' if item.total_price>0 and item.pay_status != 'paid' else 'not_pay'

    # @api.onchange("book_option")
    # def _onchange_book_option(self):
    #     """设置对应的荤菜下拉框"""
    #     self.ensure_one()
    #     if self.book_option == 'launch':
    #         self.pay_status = 'not_pay'
    #     elif self.book_option == 'dinner':
    #         self.pay_status = 'unpaid'

    def submit(self):
        """提交当前单据"""
        self.ensure_one()
        # if self.search([('book_date', '=', self.book_date), ('status', '=', 'book')]):
        #     raise Exception("该日期已有订餐记录，请修改日期")
        self.write({'status': 'book'})

    def revoke(self):
        """当前订单撤回"""
        self.ensure_one()
        self.write({'status': 'draft'})

    def cancel(self):
        """撤回当前订单"""
        self.ensure_one()
        self.write({'status': 'cancel'})

    # def commit(self):
    #     """自动提交当前所有的订单"""
    #     for item in self:
    #         item.status = "committed"

    #api.onchange('shop_id')
    #ef _inverse_dinner_info(self):
    #   """设置对应的荤菜下拉框"""
        # TODO: 待1.15完成
    #   pass
