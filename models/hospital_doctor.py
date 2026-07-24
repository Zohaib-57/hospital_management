from odoo import models, fields

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string='Doctor Name', required=True)
    specialty = fields.Char(string='Specialty')
    phone = fields.Char(string='Phone Number')
    patient_ids = fields.One2many('hospital.patient', 'doctor_id', string='Patients')
