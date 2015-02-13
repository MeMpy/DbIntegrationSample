from django.contrib import admin

# Register your models here.
from inspectdb_sample.models import IDictionary, ILanguage, IDictionaryLanguage, UUser, UArea, UUserArea

admin.site.register(IDictionary)
admin.site.register(ILanguage)
admin.site.register(UUser)
admin.site.register(UArea)
admin.site.register(UUserArea)
admin.site.register(IDictionaryLanguage) #not modifiable because it is a view
