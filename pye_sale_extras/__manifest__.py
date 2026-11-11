{
    'name': 'PyE - Extras de ventas',
    'summary': 'Descuento adicional por línea y motivo de descuento',
    'version': '19.0.1.0.0',
    'category': 'Sales/Sales',
    'author': 'Proveedor anterior',
    'license': 'LGPL-3',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'data/discount_reason_data.xml',
        'views/discount_reason_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable': True,
}
