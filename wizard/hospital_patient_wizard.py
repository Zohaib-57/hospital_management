from odoo import fields, models, api
from odoo.exceptions import UserError


class HospitalPatientWIzard(models.TransientModel):
    _name = "hospital.patient.wizard"
    _description = "Patient Status Update Wizard"

    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    current_status = fields.Selection(
        string='Current Status',
        related='patient_id.status',
        readonly=True,
    )
    new_status = fields.Selection(
        [
            ('under_treatment', 'Under Treatment'),
            ('discharged', 'Discharged'),
            ('admitted', 'Admitted'),

        ],
        string='New Status',
        required=True
    )
    notes = fields.Text(string="Notes")
    confirmation_date = fields.Datetime(
        string='Confirmation Date',
        default=fields.Datetime.now,
    )

    def action_confirm_status(self):
        self.ensure_one()
        if not self.patient_id:
            raise UserError("No patient selected.Please open this wizard from a valid Patient Record")

        self.patient_id.write({
            'status': self.new_status,
        })
        return {'type': 'ir.actions.act_window_close'}

    # @api.model
    # def default_get(self, fields_list):
    #     res = super().default_get(fields_list)
    #     active_id = self.env.context.get('active_id')
    #     active_model = self.env.contexxt.get('active_model')
    #     if active_model == 'hospital.patient' and active_id:
    #         res['patient_id'] = active_id
    #         return res
