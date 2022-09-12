from django.contrib import admin
from .models import Question,Choice,Voteinfo



class ChoiceTabular(admin.TabularInline):
    model = Choice


class VoteTabular(admin.TabularInline):
    model = Voteinfo
    

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
    (None,  {'fields':['question_text'] } ),
    ('Date information', {'fields':['pub_date']} ),
    ('poll status',{'fields':['status'], 'classes':['collapse']}),
    ]

    inlines = [ChoiceTabular,VoteTabular]
    list_display = ('question_text','pub_date','was_published_recently','status')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    actions= ['end_poll']

    @admin.action(description = 'close selected polls ?')
    def end_poll(modeladmin,request,queryset):
        queryset.update(status='E')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Voteinfo)


# Register your models here.
