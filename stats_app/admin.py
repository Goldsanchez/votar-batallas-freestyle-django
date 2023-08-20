from django.contrib import admin
from .models import Country, Competition, Season, Group, Freestyler, Battle
# Register your models here.

class FreestylerAdmin(admin.ModelAdmin):
    list_display = ["aka", "country"]
    search_fields = ["aka"]

class BattleAdmin(admin.ModelAdmin):
    list_display = ["judge", "group", "freestyler_1", "freestyler_2", "score_freestyler_1", "score_freestyler_2", "winner_replica", "competition", "season", "created_at"]
    fields = ("judge", "group", "freestyler_1", "freestyler_2", "score_freestyler_1", "score_freestyler_2", "winner_replica", "competition", "season")

admin.site.register(Country)
admin.site.register(Competition)
admin.site.register(Season)
admin.site.register(Group)
admin.site.register(Freestyler, FreestylerAdmin)
admin.site.register(Battle, BattleAdmin)


