from odoo import fields, models


class HospitalMedicalHistory(models.Model):
    _name = "hospital.medical.history"
    _description = "Hospital Medical History"
    _order = "visit_date desc"

    name = fields.Char(string="History Title", required=True, help="Enter the title of the medical history")

    disease = fields.Char(string="Disease")
    treatment = fields.Text(string="Treatment")
    notes = fields.Text(string="Notes")
    visit_date = fields.Date(string="Visit Date", default=fields.Date.context_today, help="Enter the date of the visit")
    status = fields.Selection(
        [("ongoing", "Ongoing"),
         ("recovered", "Recovered"),
         ("chronic", "Chronic")],
        string="Status",
        default="ongoing",
        required=True,
    )
    patient_id = fields.Many2one(
        "hospital.patient", string="Patient", required=True, ondelete="cascade"
    )
