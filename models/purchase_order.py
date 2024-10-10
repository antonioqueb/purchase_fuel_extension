from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    fecha_hora_recepcion = fields.Datetime(string='Fecha y Hora de Recepción')
    pipa = fields.Char(string='Pipa/Camión Cisterna')
    transportista = fields.Char(string='Transportista')
    chofer_name = fields.Char(string='Nombre del Chofer')
    chofer_license = fields.Char(string='Licencia del Chofer')
    sello_seguridad = fields.Char(string='Sello de Seguridad', size=20)
    tipo_combustible = fields.Selection([
        ('diesel', 'Diésel'),
        ('gasolina_magna', 'Gasolina Magna'),
        ('gasolina_premium', 'Gasolina Premium')
    ], string='Tipo de Combustible')
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
    temperatura_ambiente = fields.Float(string='Temperatura Ambiente')
    documentos_adjuntos = fields.Binary(string='Documentos Adjuntos')
    documentacion_regulatoria = fields.Binary(string='Documentación Regulatoria')
    fotos_recepcion = fields.Many2many('ir.attachment', string='Fotos de Recepción')
    firma_responsable = fields.Binary(string='Firma del Responsable')

    @api.depends('quantity_expected', 'quantity_received')
    def _compute_diferencia_merma(self):
        for record in self:
            record.diferencia_merma = record.quantity_expected - record.quantity_received
