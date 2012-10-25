from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from password_policies.managers import PasswordHistoryManager


class PasswordHistory(models.Model):
    """
Stores a single password history entry, related to :model:`auth.User`.

Has the following fields:
"""
    password = models.CharField(max_length=128, verbose_name=_('password'),
                                help_text=_('The encrypted password.'))
    user = models.ForeignKey(User, verbose_name=_('user'),
                             help_text=_('The user this password history '
                                         'entry belongs to.'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'),
                                   db_index=True,
                                   help_text=_('The date the entry was '
                                               'created.'))

    objects = PasswordHistoryManager()

    class Meta:
        get_latest_by = 'created'
        ordering = ['-created']
        verbose_name = _('password history entry')
        verbose_name_plural = _('password history entries')