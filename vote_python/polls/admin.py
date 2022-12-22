from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine (admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin (admin.ModelAdmin):
    fieldsets = (
        ('Question Data', {'fields': ['text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    )
    inlines = [ChoiceInLine]
    list_display = ('text', 'pub_date', 'was_published_recently')
    list_filter = ('pub_date',)
    search_fields = ('text',)


admin.site.register(Question, QuestionAdmin)
