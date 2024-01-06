from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for user in (('admin', 'admin@mysite.com'),):
                username = user[0].replace(' ', '')
                email = user[1]
                password = 'admin'
                print('Creating account for %s (%s)' % (username, email))
                admin = User.objects.create_superuser(email=email, username=username, password=password)
                admin.is_active = True
                admin.is_staff = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
