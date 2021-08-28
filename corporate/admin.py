from django.contrib import admin
from .models.pricing import Pricing
from .models.fask import Asks
from .models.team import TeamMembers
from .models.contact import ContactModel
from .models.services import Services
from .models.call_action import CallAction
from corporate.models import call_action
from .models.hero import HeroSection
from .models.why_us import WhyUs
from .models import WhyUsAsks
from .models.about import AboutText, AboutDetail

@admin.register(Asks)
class AskAdmin(admin.ModelAdmin):
    list_display = ('title','detail',)
    search_fields = ('title','detail',)


@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ('plan_name','price','detail1','detail2','detail3','detail4','detail5',)
    search_fields = ('plan_name','price',)


@admin.register(TeamMembers)
class TeamMembersAdmin(admin.ModelAdmin):
    list_display = ('full_name','jobs',)
    search_fields = ('full_name','jobs',)


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email','subject','message','created_date',)
    search_fields = ('email','subject','message')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title','content',)
    search_fields = ('title','content',)
    

@admin.register(CallAction)
class CallAction(admin.ModelAdmin):
    list_display = ('call_action_title','call_action_text',)
    search_fields = ('call_action_title','call_action_text',)


@admin.register(AboutText)
class AboutTextAdmin(admin.ModelAdmin):
    list_display = ('content',)
    search_fields = ('content',)


@admin.register(AboutDetail)
class AboutDetailAdmin(admin.ModelAdmin):
    list_display = ('title','detail',)
    search_fields = ('title','detail',)


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('header','text',)   
    search_fields = ('header','text',)


@admin.register(WhyUs)
class WhyUsAdmin(admin.ModelAdmin):
    list_display = ('header','content',)
    search_fields = ('header','content',)


@admin.register(WhyUsAsks)
class WhyUsAsks(admin.ModelAdmin):
    list_display = ('title','detail',)
    search_fields = ('title','detail',)


