# models\purchase_contract.py
from odoo import models, fields

class PurchaseContract(models.Model):
    _name = 'purchase.contract'
    _description = 'Contrato de Compra'

    name = fields.Char(string='Referencia del Contrato', required=True)
    partner_id = fields.Many2one('res.partner', string='Proveedor', required=True)
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    fecha_fin = fields.Date(string='Fecha de Fin')
    terms = fields.Text(string='Términos y Condiciones')
