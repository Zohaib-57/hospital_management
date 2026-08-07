from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Hospital Appointment'

    name = fields.Char(string='Appointment Reference', required=True,
                       copy=False, readonly=True, default=lambda self: ('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', required=True)
    appointment_date = fields.Datetime(string='Appointment Date', required=True, default=fields.Datetime.now)
    reason = fields.Text(string='Reason for Appointment')
    notes = fields.Text(string='Additional Notes')

    active = fields.Boolean(default=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], string="Status", default='draft', readonly=True, copy=False, tracking=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', ('New')) == ('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or ('New')
        return super(HospitalAppointment, self).create(vals_list)

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirmed'

    def action_start(self):
        for rec in self:
            rec.state = 'in_progress'

    def action_complete(self):
        for rec in self:
            rec.state = 'completed'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancelled'

    def action_reset_to_draft(self):
        for rec in self:
            rec.state = 'draft'
