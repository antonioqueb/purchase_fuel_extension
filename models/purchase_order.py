# models\purchase_order.py
from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    pipa_id = fields.Many2one('fleet.vehicle', string='Pipa/Camión Cisterna')
    transportista_id = fields.Many2one('res.partner', string='Transportista')
    chofer_id = fields.Many2one('hr.employee', string='Chofer')
    fecha_hora_recepcion = fields.Datetime(string='Fecha y Hora de Recepción')
    fuel_source = fields.Selection([
        ('compra_directa', 'Compra Directa'),
        ('subsidio_gubernamental', 'Subsidio Gubernamental'),
        ('devolucion', 'Devolución'),
        ('transferencia_interna', 'Transferencia Interna')
    ], string='Origen del Combustible')
    quantity_expected = fields.Float(string='Cantidad Esperada (L)')
    quantity_received = fields.Float(string='Cantidad Recibida (L)')
    diferencia_merma = fields.Float(string='Diferencia/Merma', compute='_compute_diferencia_merma', store=True)
    motivo_diferencia = fields.Selection([
        ('evaporacion', 'Evaporación'),
        ('fugas', 'Fugas'),
        ('errores_medicion', 'Errores de Medición'),
        ('otros', 'Otros')
    ], string='Motivo de la Diferencia')
    densidad_combustible = fields.Float(string='Densidad del Combustible')
    temperatura_combustible = fields.Float(string='Temperatura del Combustible')
    documentos_adjuntos = fields.Binary(string='Documentos Adjuntos')
    sello_seguridad = fields.Char(string='Sello de Seguridad', size=20)
    tipo_combustible = fields.Selection([
        ('diesel', 'Diésel'),
        ('gasolina_magna', 'Gasolina Magna'),
        ('gasolina_premium', 'Gasolina Premium')
    ], string='Tipo de Combustible')
    proveedor_secundario_id = fields.Many2one('res.partner', string='Proveedor Secundario')
    documentacion_regulatoria = fields.Binary(string='Documentación Regulatoria')
    fotos_recepcion = fields.Many2many('ir.attachment', string='Fotos de Recepción')
    firma_responsable = fields.Binary(string='Firma del Responsable')
    historial_inspecciones_ids = fields.One2many('fuel.inspection', 'purchase_order_id', string='Historial de Inspecciones')
    comentarios_auditoria = fields.Text(string='Comentarios de Auditoría')
    conformidad = fields.Boolean(string='Conformidad')
    contrato_id = fields.Many2one('purchase.contract', string='Contrato')
    temperatura_ambiente = fields.Float(string='Temperatura Ambiente')
    notas_adicionales = fields.Text(string='Notas Adicionales')

    @api.depends('quantity_expected', 'quantity_received')
    def _compute_diferencia_merma(self):
        for record in self:
            record.diferencia_merma = record.quantity_expected - record.quantity_received
