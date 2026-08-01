from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"
    _order = "name asc"

    name = fields.Char(
        string="Name",
        required=True,
        index=True,
        help="Full Name of the Doctor")
    doctor_code = fields.Char(
        string="Doctor Code",
        required=True,
        index=True,
        default="DOC00",
        help="Unique Code for the Doctor")
    profile_image = fields.Image(string="Profile Image")

    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], string="Gender", help="Gender of the Doctor")
    date_of_birth = fields.Date(
        string="Date Of Birth",
        help="Date of Birth of the Doctor")

    phone = fields.Char(
        string="Phone Number",
        help="Contact Number of the Doctor")
    email = fields.Char(string="Email", help="Email Address of the Doctor")
    address = fields.Text(string="Address", help="Address of the Doctor")

    qualification = fields.Text(
        string="Qualification",
        help="Qualification of the Doctor")

    biography = fields.Html(string="Biography", help="Biography of the Doctor")
    specialty = fields.Char(string='Specialty')
    experience_years = fields.Integer(
        string="Experience Years",
        default=0,
        help="Total Experience of the Doctor in Years")

    currency_id = fields.Many2one(
        "res.currency",
        string="Currency",
        default=lambda self: self.env.company.currency_id)
    consultation_fee = fields.Monetary(
        string="Consultation Fee",
        currency_field="currency_id",
        help="Consultation Fee of the Doctor")

    joining_date = fields.Date(
        string="Joining Date",
        default=fields.Date.context_today,
        help="Joining Date of the Doctor")

    availability_status = fields.Selection(
        [
            ('available', 'Available'),
            ('not_available', 'Not Available')],
        string="Availability",
        default='available',
        help="Availability Status of the Doctor")

    active = fields.Boolean(
        string="Active",
        default=True,
        help="Is the Doctor Active?")

    additional_notes = fields.Text(
        string="Additional Notes",
        help="Any Additional Notes about the Doctor")

    patient_ids = fields.One2many(
        "hospital.patient",
        "doctor_id",
        string="Patients"
    )

    _doctor_code_unique = models.Constraint(
        'UNIQUE(doctor_code)',
        'Doctor Code must be unique! This code is already assigned to another doctor.',
    )
