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
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/hospital_patient_data.xml',
        'views/hospital_patient_views.xml',
        'views/hospital_doctor_views.xml',
    ],
    'demo': [
        'demo/hospital_patient_demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}