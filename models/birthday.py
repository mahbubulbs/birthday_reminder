from odoo import api, fields, models


class BirthdayReminder(models.Model):
    _name = 'birthday.reminder'
    _description = 'Birthday Reminder'
    _inherit = ['mail.thread']
    _order = 'birth_date, name'

    name = fields.Char(required=True, tracking=True)
    email = fields.Char(tracking=True)
    birth_date = fields.Date(required=True, tracking=True)
    last_wish_year = fields.Integer(
        string='Last Wish Sent (Year)',
        readonly=True,
        help='Year when the last birthday wish email was sent.',
    )
    is_birthday_today = fields.Boolean(
        compute='_compute_is_birthday_today',
        search='_search_is_birthday_today',
    )

    @api.depends('birth_date')
    def _compute_is_birthday_today(self):
        today = fields.Date.context_today(self)
        for record in self:
            record.is_birthday_today = bool(
                record.birth_date
                and record.birth_date.month == today.month
                and record.birth_date.day == today.day
            )

    def _search_is_birthday_today(self, operator, value):
        if operator not in ('=', '!=') or not isinstance(value, bool):
            return NotImplemented

        today = fields.Date.context_today(self)
        records = self.search([('birth_date', '!=', False)])
        matching_ids = records.filtered(
            lambda r: r.birth_date.month == today.month and r.birth_date.day == today.day
        ).ids
        is_equal = (operator == '=' and value) or (operator == '!=' and not value)
        return [('id', 'in' if is_equal else 'not in', matching_ids)]

    def _send_birthday_wish(self):
        template = self.env.ref(
            'birthday_reminder.email_template_birthday_wish',
            raise_if_not_found=False,
        )
        if not template:
            return

        today = fields.Date.context_today(self)
        for record in self:
            if not record.email:
                continue
            template.send_mail(record.id, force_send=True)
            record.last_wish_year = today.year

    def action_send_birthday_wish(self):
        self._send_birthday_wish()

    @api.model
    def _cron_send_birthday_wishes(self):
        today = fields.Date.context_today(self)
        records = self.search([
            ('birth_date', '!=', False),
            ('email', '!=', False),
            '|',
            ('last_wish_year', '=', False),
            ('last_wish_year', '!=', today.year),
        ])
        birthday_records = records.filtered(
            lambda r: r.birth_date.month == today.month and r.birth_date.day == today.day
        )
        birthday_records._send_birthday_wish()
