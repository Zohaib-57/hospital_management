{
    'name': 'Hospital Management System',
    'version': '19.0.1.0.0',
    'category': 'Healthcare/Hospital',
    'summary': 'Comprehensive hospital management solution for patient records and doctor profiles.',
    'description': """
Hospital Management System
--------------------------
A comprehensive module designed for healthcare facilities to manage:
- Patient Profiles & Medical Records
- Doctor Profiles & Specialties
- Hospital Workflows
    """,
    'author': 'NerithonX Technologies (Pvt.) Ltd.',
    'website': 'https://www.nerithonx.com',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',         # 1. Load security first
        'views/hospital_patient_views.xml',     # 2. Load patient views & actions
        'views/hospital_doctor_views.xml',      # 3. Load doctor views & actions
        'views/hospital_disease_views.xml',      # 4. Load disease views and actions
        # 4. Load menus LAST (they reference the actions above)
        'views/hospital_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
