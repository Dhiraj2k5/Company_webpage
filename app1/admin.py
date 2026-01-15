from django.contrib import admin
from app1.models import GeneralInfo,Service,Testimonials,FrequentlyAskedQuestions,ContactFormLog,Blogs,Author
# Register your models here.
@admin.register(GeneralInfo)
class GeneralInfo(admin.ModelAdmin):
    list_display = [
        "company_name",
        "location",
        "email" 
    ]

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass

@admin.register(Testimonials)
class TestimonialsInfo(admin.ModelAdmin):
    list_display = [

        "username",
        "user_job",
        "display_rating_count"

    ]
    def display_rating_count(self, obj):
        return "*" * obj.rating_count 
    display_rating_count.short_description = "Rating" 

@admin.register(FrequentlyAskedQuestions)
class FrequentlyAskedQuestionsAdmin (admin.ModelAdmin):
    list_display = [
        "question",
        "answer",
         
    ]

@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = [
         "email",
        "is_success",
        "is_error",
        "action_time"     
    ]

    def has_add_permission(self, request, obj = None):
        return False
    def has_change_permission(self, request, obj = None):
        return False
    def has_delete_permission(self, request, obj = None):
        return False

@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
    ]

@admin.register(Blogs)
class Blogs(admin.ModelAdmin):
    list_display = [
        "category",
        "title",
        "blog_image",
        "created_at"     
    ]