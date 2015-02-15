from django.contrib import admin

# Register your models here.
from inspectdb_sample.models import IDictionary, ILanguage, IDictionaryLanguageView, UUser, UArea

admin.site.register(IDictionary)
admin.site.register(ILanguage)
admin.site.register(UUser)
admin.site.register(UArea)
admin.site.register(IDictionaryLanguageView) #not modifiable because it is a view
