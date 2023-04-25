from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ###FAQATGINA KO'RISH UCHUN RUXSAT BERILADI
        if request.method in permissions.SAFE_METHODS:
            return True
        ##o'zgartirish faqatgina post avtoriga ruxsat beriladi
        return obj.author == request.user
        

        