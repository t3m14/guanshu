# markets/admin.py
from django.contrib import admin
from .models import Market, MarketCategory, MarketOutcome, UserBet

class MarketOutcomeInline(admin.TabularInline):
    model = MarketOutcome
    extra = 1

@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'outcome_type', 'volume', 'is_active')
    list_filter = ('category', 'outcome_type', 'is_active')
    search_fields = ('title', 'description')
    inlines = [MarketOutcomeInline]

admin.site.register(MarketCategory)
admin.site.register(UserBet)