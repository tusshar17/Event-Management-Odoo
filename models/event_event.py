from odoo import api, fields, models

class EventEvent(models.Model):
    _name = 'event.event'

    name = fields.Char(string="Event Name", required=True)
    date_start = fields.Datetime(string='Start Time', required=True)
    date_end = fields.Datetime(string='End Time', required=True)
    venue = fields.Char(string='Venue')
    description = fields.Char(string='Event Description')
    max_attendees = fields.Integer(string='Max Attendees', default=50)
    attendees_ids = fields.One2many('event.attendee', 'event_id', string='Attendees')
    tickets_available = fields.Integer(string='Tickets Available', compute='_compute_tickets_available')

    def _compute_tickets_available(self):
        for event in self:
            event.tickets_available = event.max_attendees - len(event.attendees_ids)
