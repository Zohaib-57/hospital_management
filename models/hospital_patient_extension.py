from odoo import fields, models , api
from odoo.exceptions import ValidationError


class HospitalPatientExtension(models.Model):
    _inherit = "hospital.patient"

    emergency_contact_name = fields.Char(
        string="Emergency Contacct Name",
        help="Full name of the person to contact in case of emergency"
    )

    emergency_contact_phone = fields.Char(
        string="Emergency Contact Phone",
        help="Phone number of the emergency contact"
    )
    emergency_contact_relation = fields.Selection([
        ('parent', 'Parent'),
        ('spouse', 'Spouse'),
        ('sibling', 'Sibling'),
        ('child', 'Child'),
        ('friend', 'Friend'),
        ('other', 'Other'),
    ], string="Relation", help="Relationship of the emergency contact to the patient")

    @api.constrains('emergency_contact_phone')
    def _check_emergency_contact_phone(self):
        for record in self:
            if record.emergency_contact_phone and not record.emergency_contact_phone.isdigit():
                raise ValidationError(
                    'Emergency Contact Phone should contain only digits.'
                )
