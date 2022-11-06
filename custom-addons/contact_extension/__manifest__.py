{
    'name': 'Contact Extension',
    'sequence': -100,
    'version': '16.0',
    'summary': 'extension on the contact Module',
    'description': 'Contact Extension',
    'category': 'Sales',
    'depends': ['contacts', 'stock'],
    'data': [
            'security/ir.model.access.csv',
            'views/contact_main_info.xml',
            'views/customer_sales_purchase_tab.xml',
            'views/customer_menu.xml',
            'views/employee_sales_purchase_tab.xml',
            'views/employee_menu.xml',
            'views/vendor_sales_purchase_tab.xml',
            'views/vendor_menu.xml',
            'views/sales_rep_sales_purchase_tab.xml',
            'views/sales_rep_menu.xml',
            'views/main_contact.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False





}
