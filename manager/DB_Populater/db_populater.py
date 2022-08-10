import os
from datetime import date
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GraduationProject.settings')
import django
django.setup()

from django.contrib.auth.models import User
from apps.models.modelsFee import UtilityType, Provider, UtilityBill, Payment


def populate_utility_bills():
    electricity_type = add_type("Electricity")
    owner_user = add_user("hegemon88676", "user@user.com")
    tentant_user = add_user("tenant", "tenant@user.com")
    provider = add_provider("Enel", electricity_type)
    bill_deadline = date.today()
    bill = add_bill(False, django.utils.timezone.now(), bill_deadline, value=200, payee_user=tentant_user,
                    owner=owner_user, provider=provider)
    payment = add_payment(payment_date=django.utils.timezone.now(), bill=bill)
    print(payment.bill.propriety_owner_user.username)


def add_type(type: str) -> UtilityType:
    t = UtilityType.objects.get_or_create(name=type)[0]
    t.save()
    return t


def add_user(username: str, email: str, password: str = "1234"):
    u = User.objects.get_or_create(username=username, email=email)[0]
    u.set_password(raw_password=password)
    u.save()
    return u


def add_provider(name: str, type: UtilityType):
    p = Provider.objects.get_or_create(name=name, type=type)[0]
    p.save()
    return p


def add_bill(is_payed: bool, post_date, bill_deadline, value: float, payee_user: User, owner: User, provider: Provider,
             file=None):
    b = UtilityBill.objects.get_or_create(is_payed=is_payed, post_date=post_date, bill_deadline=bill_deadline, value=value,
                                   payee_user=payee_user, propriety_owner_user=owner, provider=provider, file=file)[0]
    b.save()
    return b


def add_payment(payment_date, bill: UtilityBill):
    p = Payment.objects.get_or_create(payment_date=payment_date, bill=bill)[0]
    p.save()
    return p


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate_utility_bills()

    # write "python db_populater.py" in shell in Django project’s root
    # make sure to have the right migrations
