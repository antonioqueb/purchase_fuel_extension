# models\fuel_inspection.py
from odoo import models, fields

class FuelInspection(models.Model):
    _name = 'fuel.inspection'
    _description = 'Inspección de Combustible'

    purchase_order_id = fields.Many2one('purchase.order', string='Orden de Compra')
    fecha_inspeccion = fields.Datetime(string='Fecha de Inspección')
    inspector_id = fields.Many2one('hr.employee', string='Inspector')
    resultados = fields.Text(string='Resultados')
    notas = fields.Text(string='Notas')
