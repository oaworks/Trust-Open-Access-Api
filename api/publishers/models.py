from django.db import models

class Publisher(models.Model):
	Title = models.CharField(max_length=100, blank=True, default='')
	URL = models.CharField(max_length=300, primary_key=True)
	DOAJurl = models.CharField(max_length=300, blank=True)
	DOAJapproved = models.BooleanField(blank=True, default=False)
	Predatory = models.BooleanField(blank=True, default=False)
	Hybrid = models.BooleanField(blank=True, default=False)
	OpenAccess = models.BooleanField(blank=True, default=False)
	OASPAapproved = models.BooleanField(blank=True, default=False)

	class Meta:
		ordering = ('URL',)

def save(self, *args, **kwargs):
    formatter = HtmlFormatter(Title=self.Title, URL=self.URL, DOAJurl = self.DOAJurl, DOAJapproved=self.DOAJapproved, Predatory=self.Predatory, OASPAapproved=self.OASPAapproved)
    super(Publisher, self).save(*args, **kwargs)