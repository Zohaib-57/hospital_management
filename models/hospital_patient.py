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

    doctor_specialty = fields.Char(
        string='Doctor Specialty',
        readonly=True
    )

    currency_id = fields.Many2one(
        'res.currency',
        string='Currency',
        related='doctor_id.currency_id',
        store=True,
        readonly=True
    )

    consultation_fee = fields.Monetary(
        string='Consultation Fee',
        currency_field='currency_id',
        readonly=True
    )

    @api.onchange('doctor_id')
    def _onchange_doctor_id(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_specialty = rec.doctor_id.specialty
                rec.consultation_fee = rec.doctor_id.consultation_fee
            else:
                rec.doctor_specialty = False
                rec.consultation_fee = 0.0

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = fields.Date.today()
                dob = record.date_of_birth
                # dob is a date object
                record.age = (
                    today.year - dob.year -
                    ((today.month, today.day) < (dob.month, dob.day))
                )
            else:
                record.age = 0

    @api.model
    def create(self, vals):
        return super().create(vals)

    def write(self, vals):
        return super().write(vals)

    def unlink(self):
        return super().unlink()
