from django.urls import reverse_lazy
from django.db import models

from backend.core.models import TimeStampedModel

STATUS = (
    ('A', 'Aprovado'),
    ('c', 'Cancelado'),
)


class Expense(TimeStampedModel):
    title = models.CharField('título', max_length=5)
    value = models.DecimalField(
        'valor',
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=1, choices=STATUS, default='A')
    photo = models.ImageField(upload_to='', null=True, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Despesa'
        verbose_name_plural = 'Despesas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('expense:expense_detail', kwargs={'pk': self.pk})
