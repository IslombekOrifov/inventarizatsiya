import sys
import random 

from django.core.management.base import BaseCommand, CommandError

from accounts.models import CustomUser, Department

class Command(BaseCommand):
    
    def handle(self, count=1000, *args, **options):
        superuser = CustomUser.objects.get(username='admin1')
        
        desc = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do \
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad \
            minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip \
            ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate \
            velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat \
            non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
        
        a = list((Department(name=f'Department {i} ', group=superuser.groups.first()) for i in range(1,20)))
        Department.objects.bulk_create(a)
        print('done')



