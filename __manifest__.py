{
    "name": "Extensión de Órdenes de Compra para Combustible",
    "version": "1.0",
    "summary": "Extiende las órdenes de compra para gestionar recepciones de combustible",
    "description": "Este módulo agrega campos y modelos adicionales al módulo de Compras para gestionar la recepción y control de combustible.",
    "author": "Alphaqueb Consulting S.A.S.",
    "category": "Purchases",
    "website": "https://alphaqueb.com",
    "license": "LGPL-3",
    "depends": ["purchase"],
    "data": [
        "security/ir.model.access.csv",
        "views/purchase_order_view.xml"
    ],
    "installable": True,
    "auto_install": False,
    "application": False
}
