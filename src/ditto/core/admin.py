from django.contrib import admin


class DittoItemModelAdmin(admin.ModelAdmin):
    @admin.display(description="Post year")
    def post_year_str(self, instance):
        "So Admin doesn't add a comma, like '2,016'."
        return str(instance.post_year)
