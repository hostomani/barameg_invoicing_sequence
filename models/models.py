# -*- coding: utf-8 -*-
import datetime
from odoo import models, fields, api, exceptions


class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.model
    def create(self, values):
        name = ''
        ct = datetime.datetime.now()
        for segment in str(ct).split(' ')[0].split('-'):
            name += segment
        name += str(values['partner_id'])
        for segment in str(ct).split(' ')[1].split('.')[0].split(':'):
            name += segment
        values['name'] = name
        rec = super(AccountMove, self).create(values)
        return rec
