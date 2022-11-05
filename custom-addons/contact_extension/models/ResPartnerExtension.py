from odoo import models, fields, api
# from ..services.distances_utils import DistanceUtils
import json
import pathlib

class ResPartnerExtension(models.Model):
    _inherit = 'res.partner'

    contact_type = fields.Selection([('customer', 'customer'),
                                     ('vendor', 'vendor'),
                                     ('employee', 'employee'),
                                     ('sales_rep', 'sales_rep')])
    customer = fields.Many2one('res.partner.customer')
    vendor = fields.Many2one('res.partner.vendor')
    employee = fields.Many2one('res.partner.employee')
    sales_rep = fields.Many2one('res.partner.sales_rep')


