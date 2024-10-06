from odoo import api, fields, models
from odoo.exceptions import UserError


class EventAttendee(models.Model):
    _name = 'event.attendee'

    name = fields.Char(string='Attendee Name', required=True)
    email = fields.Char(string='Email', required=True)
    event_id = fields.Many2one('event.event', string='Event', required=True)
    ticket_type = fields.Selection([('regular', 'Regular'), ('vip', 'VIP')], string='Ticket Type', required=True)
    is_confirmed = fields.Boolean(string='Confirmed', default=False)

    def confirm_registration(self):
        if not self.is_confirmed:
            self.is_confirmed = True
