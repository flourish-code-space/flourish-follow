from django.db import models
from edc_constants.choices import YES_NO

from flourish_caregiver.models.model_mixins import CaregiverContactFieldsMixin
from ..choices import YES_NO_ST_NA, MAY_CALL


class Contact(CaregiverContactFieldsMixin):

    appt_scheduled = models.CharField(
        verbose_name='Is the participant willing to schedule an appointment',
        max_length=15,
        choices=YES_NO_ST_NA)

    appt_date = models.DateField(
        verbose_name='Appointment Date',
        blank=True,
        null=True)

    continue_contact = models.CharField(
        verbose_name='May we continue to contact the participant',
        choices=MAY_CALL,
        max_length=25)

    final_contact = models.CharField(
        verbose_name=('Is this the final contact attempt and no other calls '
                      'or home visits will be made for this participant'),
        choices=YES_NO,
        max_length=3)

    class Meta:
        app_label = 'flourish_follow'
        unique_together = ('subject_identifier', 'contact_datetime')
        verbose_name = 'Contact'
