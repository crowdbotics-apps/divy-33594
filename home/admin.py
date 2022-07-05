from django.contrib import admin
from .models import Accounts, ClosingValue, Dividends, Drip, Holdings, HoldingValue

admin.site.register(Holdings)
admin.site.register(Accounts)
admin.site.register(Drip)
admin.site.register(HoldingValue)
admin.site.register(Dividends)
admin.site.register(ClosingValue)

# Register your models here.
