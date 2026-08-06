from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _rec_name = 'name'

    registration_no = fields.Char(string="Registration Number", required=True, default="New", readonly=True, copy=True)

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
    active = fields.Boolean(string='Active', default=True)
    registration_date = fields.Date(string='Registration Date', default=fields.Date.context_today)

    status = fields.Selection([
        ('new', 'New'),
        ('admitted', 'Admitted'),
        ('discharged', 'Discharged'),
        ('under_treatment', 'Under Treatment'),
    ], string='Status', default='new')

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
    medical_history_ids = fields.One2many(
        'hospital.medical.history',
        "patient_id",
        string="Medical History"
    )

    # onchange methid for the doctor_id field
    @api.onchange('doctor_id')
    def _onchange_doctor_id(self):
        for rec in self:
            if rec.doctor_id:
                rec.doctor_specialty = rec.doctor_id.specialty
                rec.consultation_fee = rec.doctor_id.consultation_fee
            else:
                rec.doctor_specialty = False
                rec.consultation_fee = 0.0

    # compute method for the age field
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = fields.Date.today()
                dob = record.date_of_birth
                record.age = (
                    today.year - dob.year -
                    ((today.month, today.day) < (dob.month, dob.day))
                )
            else:
                record.age = 0

    # constraint method for the age field
    @api.constrains('age')
    def _check_age(self):
        for record in self:
            if record.age < 0:
                raise ValidationError(
                    'Age cannot be negative. Please check the Date of Birth.')
            if record.age > 120:
                raise ValidationError(
                    'Patient Age seems unrealistic (over 120 years ). Please check the Date of Birth.')

    # validation method for the phone field
    @api.constrains('phone')
    def _check_phone(self):
        for record in self:
            if not record.phone:
                raise ValidationError(
                    'Phone number is required. Please provide a valid Phone number.')
            if record.phone and not record.phone.isdigit():
                raise ValidationError(
                    'Phone number should contain only digits. Please check the Phone field.')

    # validation method for the date_of_birth field
    @api.constrains('date_of_birth')
    def _check_date_of_birth(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth > fields.Date.today():
                raise ValidationError(
                    'Date of Birth cannot be in the future. Please check the Date of Birth field.')

    # override create, write and unlink methods
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('registration_no', 'New') == 'New':
                vals['registration_no'] = self.env['ir.sequence'].next_by_code(
                    'hospital.patient') or 'New'
        return super().create(vals_list)

    def write(self, vals):
        return super().write(vals)

    def unlink(self):
        return super().unlink()
