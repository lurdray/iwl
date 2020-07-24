from django.contrib import admin
from main.models import *

# Register your models here.
admin.site.register(KitchenCategory)
admin.site.register(LivingCategory)
admin.site.register(BedRoomCategory)

admin.site.register(OfficeCategory)
admin.site.register(DinningCategory)
admin.site.register(DoorCategory)

admin.site.register(CenterCategory)
admin.site.register(TvCategory)
admin.site.register(ClientCategory)

admin.site.register(WardrobeCategory)


admin.site.register(ContactModel)
admin.site.register(ProjectModel)
admin.site.register(CategoryModel)

admin.site.register(FactoryModel)
