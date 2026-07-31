from odoo import fields, models


class HospitalDisease(models.Model):
    _name = "hospital.disease"
    _description = "Hospital Disease"
    _order = "name asc"

    name = fields.Char(string="Disease Name")
    disease_code = fields.Char(string="Disease Code")
    description = fields.Text(string='Descrition')
    active = fields.Boolean(string="Active", default="True")
