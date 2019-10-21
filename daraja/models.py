from django.db import models
from djangotoolbox.fields import ListField

from ikwen.core.constants import PENDING
from ikwen.core.models import Model, Service, AbstractWatchModel
from ikwen.accesscontrol.models import Member


DARAJA = "daraja"
DARAJA_IKWEN_SHARE_RATE = 10
DARA_REQUESTED_ACCESS = "DaraRequestAccess"
REFEREE_JOINED_EVENT = "RefereeJoined"


class DarajaConfig(Model):
    service = models.ForeignKey(Service, unique=True, related_name='+')
    description = models.TextField(blank=True)
    annual_turnover = models.IntegerField(default=0)
    number_of_employees = models.IntegerField(default=1)
    location = models.CharField(blank=True)
    referrer_share_rate = models.FloatField(default=0)


class DaraRequest(Model):
    service = models.ForeignKey(Service, related_name='+')
    member = models.ForeignKey(Member)
    status = models.CharField(max_length=15, default=PENDING, db_index=True)

    class Meta:
        unique_together = ('service', 'member')


class Dara(AbstractWatchModel):
    member = models.ForeignKey(Member, unique=True)
    uname = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    share_rate = models.FloatField(default=0)

    orders_count_history = ListField(editable=False)
    items_traded_history = ListField(editable=False)
    turnover_history = ListField(editable=False)
    earnings_history = ListField(editable=False)

    total_orders_count = models.IntegerField(default=0)
    total_items_traded = models.IntegerField(default=0)
    total_turnover = models.IntegerField(default=0)
    total_earnings = models.IntegerField(default=0)

    last_transaction_on = models.DateTimeField(blank=True, null=True, db_index=True)


class AbuseReport(Model):
    service = models.ForeignKey(Service, related_name='+')
    member = models.ForeignKey(Member)
    details = models.TextField()
