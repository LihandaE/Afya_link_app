from rest_framework.permissions import BasePermission


class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role =='super_admin'
    
class IsHospitalAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'hospital_admin'
    

class IsReceptionist(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'receptionist'
 
class IsNurse(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'nurse'

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'doctor'

class IsLabTech(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'lab_tech'

class IsRadiologist(BasePermission):
    def has_permission(self,request,view):
        return request.user.role =='radiologist'

class IsPharmacist(BasePermission):
    def has_permission(self,request,view):
        return request.user.role == 'pharmacist'
    
class IsPatient(BasePermission):
    def has_permission(self, request, view):
        return request.user.role =='patient'
    
           