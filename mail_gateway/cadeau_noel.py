# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models
# import random


class Partner(models.Model):

    _inherit = "res.partner"

    def unlink(self):
        # emails = [
        #     ('debouckm@gmail.com', 'Manon'),
        #     ('nicolas.pinte@uclouvain.be', 'Nico'),
        #     ('coralie.renders@gmail.com', 'Coralie'),
        #     ('malotauxmichael@gmail.com', 'Mika'),
        # ]
        # import ipdb; ipdb.set_trace()
        # MailServer = self.env['ir.mail_server'].sudo()
        # mail_server_id = MailServer.env.ref('base.ir_mail_server_localhost0').id
        # a = [i for i in range(len(emails))]
        # notok = True
        # while notok:
        #     random.shuffle(a)
        #     notok=False
        #     for j in range(len(a)):
        #         if j == a[j]:
        #             notok=True
        # for i in range(len(emails)):
        #     email = MailServer.build_email(
        #         email_from=emails[i][0],
        #         email_to=[emails[i][0]],
        #         subject='Cadeau Noel (test)',
        #         body='Coucou moi,\n\nCette année pour Noël je vais devoir offrir un cadeau à %s !\n\nPour rappel, le budget était estimé à 10-15€.\n\nJe me souhaite une bonne recherche!\n%s' % (emails[a[i]][1], emails[i][1])
        #     )
        #     MailServer.send_email(email, mail_server_id=mail_server_id)
        return super(Partner, self).unlink()
