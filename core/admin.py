from django.contrib import admin
from .models import Item, OrderItem, Order, UserProfile, Coupon, Payment, Refund, Address

# Register your models here.

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'

def order_being_delivered(modeladmin, request, queryset):
    queryset.update(being_delivered=True)


order_being_delivered.short_description = 'Update orders to being delivered'

def order_received(modeladmin, request, queryset):
    queryset.update(received=True)


order_received.short_description = 'Update orders to received'




class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                     'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon']
    list_display_links=[
                    'user',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
    ]
    list_filter = [
                    'ordered',
                     'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
    ]
    search_fields=[
        'user__username',
        'ref_code'
    ]
    actions=[
        make_refund_accepted,
        order_being_delivered,
        order_received
    ]

class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'appartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

admin.site.register(Item)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(UserProfile)
admin.site.register(Address, AddressAdmin)

