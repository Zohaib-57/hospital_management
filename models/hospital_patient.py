from odoo import models, fields, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', default='male')

    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string='Age', compute='_compute_age', store=True)

    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    notes = fields.Text(string='Medical Notes')
    doctor_id = fields.Many2one('hospital.doctor', string='Primary Doctor')
    
    disease_ids = fields.Many2many(
        "hospital.disease",
        string="Diseases"
    )

# learn how it happened
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = fields.Date.today()
                record.age = today.year - record.date_of_birth.year - \
                    ((today.month, today.day) < (record.date_of_birth.month, record.date_of_birth.day))
            else:
                record.age = 0
