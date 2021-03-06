# Generated by Django 3.2.6 on 2022-01-05 12:31

from django.db import migrations


def forwards_func(apps, schema_editor):
    Employee = apps.get_model("crm_app", "Employee")
    Status = apps.get_model("crm_app", "Status")
    Tasks = apps.get_model("crm_app", "Tasks")
    Company = apps.get_model("crm_app", "Company")
    Contacts = apps.get_model("crm_app", "Contacts")
    Funnel = apps.get_model("crm_app", "Funnel")
    Proposal = apps.get_model("crm_app", "Proposal")
    Deal = apps.get_model("crm_app", "Deal")
    Payment = apps.get_model("crm_app", "Payment")
    Employee.objects.bulk_create([
        Employee(name="Svirydzetski Kanstantsin", date_of_birth="1998-05-05", phone_number=447458212,
                 post='Developer', e_mail='john591998@mail.ru'),
        Employee(name="Bobkovich Ivan", date_of_birth="1999-02-11", phone_number=293700818,
                 post='Marketing', e_mail='ivanbobko@mail.ru'),
        Employee(name="Gordievich Vladislav", date_of_birth="1999-04-8", phone_number=441234567,
                 post='Finance', e_mail='vladgor@mail.ru'),
    ])
    Status.objects.bulk_create([
        Status(name='Без статуса'),
        Status(name='Всё по плану'),
        Status(name='Есть вопросы'),
        Status(name='Есть проблемы'),
        Status(name='недозвон'),
        Status(name='необходима ежемесячная оплата'),
    ])
    Tasks.objects.bulk_create([
        Tasks(name='Выполнить все задачи', employee=Employee.objects.get(name="Svirydzetski Kanstantsin"),
              text="Всё нужно сделать сегодня", status=Status.objects.get(name='Всё по плану'), deadline='2022-03-01')
    ])
    Company.objects.bulk_create([
        Company(full_name='ОАО Минсктрактор', name='ОАО МинскТрактор',
                responsible=Employee.objects.get(name="Svirydzetski Kanstantsin"),
                type_of_activity='Производство тракторов', city='Минск', phone_number_or_fax=123456789,
                address='г. Минск, ул.Тракторная 59', e_mail='tractor@mail.ru', ynp=123456789, kpp=123456789),
        Company(full_name='ОАО Облгаз', name='ОАО Облгаз', responsible=Employee.objects.get(name="Bobkovich Ivan"),
                type_of_activity='Газ', city='Минск', phone_number_or_fax=123456789,
                address='г. Минск, ул.Газовая 44', e_mail='gaz@mail.ru', ynp=123456789, kpp=123456789),
    ])
    Contacts.objects.bulk_create([
        Contacts(name='Иван Иванович', post='Менеджер', phone_number=1234567, e_mail='ivanovivan@mail.ru',
                 status='Холодный'),
        Contacts(name='Сергей Николаев', post='Продавец', phone_number=1234567, e_mail='sergei@mail.ru',
                 status='Горячий'),
        Contacts(name='Артём Дмитриев', post='Директор', phone_number=1234567, e_mail='arteam@mail.ru',
                 status='Постоянный клиент'),
    ])
    Funnel.objects.bulk_create([
        Funnel(name='Не обработанна'),
        Funnel(name='Квалификация'),
        Funnel(name='Переговоры'),
        Funnel(name='Согласование документов'),
        Funnel(name='Счёт выставлен'),
        Funnel(name='Выиграна'),
        Funnel(name='Проиграна'),
    ])
    Proposal.objects.bulk_create([
        Proposal(name='Ремонт здания', price=100000, source='Тендер', funnel=Funnel.objects.get(name='Не обработанна'),
                 employee=Employee.objects.get(name="Svirydzetski Kanstantsin"),
                 contacts=Contacts.objects.get(name='Иван Иванович'),
                 company=Company.objects.get(name='ОАО МинскТрактор')),
        Proposal(name='Капитальный ремонт', price=1000000, source='Тендер',
                 funnel=Funnel.objects.get(name='Не обработанна'),
                 employee=Employee.objects.get(name="Svirydzetski Kanstantsin"),
                 contacts=Contacts.objects.get(name='Сергей Николаев'),
                 company=Company.objects.get(name='ОАО Облгаз')),
    ])
    Deal.objects.bulk_create([
        Deal(proposal=Proposal.objects.get(name='Ремонт здания'), status=Status.objects.get(name='Всё по плану'),
             profit=10000, description='Нужно выполнить ремонд сдания указанный в тендере'),
        Deal(proposal=Proposal.objects.get(name='Капитальный ремонт'), status=Status.objects.get(name='Всё по плану'),
             profit=100000, description='Нужно выполнить капитальный ремонд сдания указанный в тендере'),
    ])
    Payment.objects.bulk_create([
        Payment(deal=Deal.objects.get(profit=10000), date='2022-01-05', price=10000),
        Payment(deal=Deal.objects.get(profit=100000), date='2022-02-05', price=100000),
    ])


def reverse_func(apps, schema_editor):
    Employee = apps.get_model("crm_app", "Employee")
    Status = apps.get_model("crm_app", "Status")
    Tasks = apps.get_model("crm_app", "Tasks")
    Company = apps.get_model("crm_app", "Company")
    Contacts = apps.get_model("crm_app", "Contacts")
    Funnel = apps.get_model("crm_app", "Funnel")
    Proposal = apps.get_model("crm_app", "Proposal")
    Deal = apps.get_model("crm_app", "Deal")
    Payment = apps.get_model("crm_app", "Payment")
    Employee.objects.filter(name="Svirydzetski Kanstantsin").delete()
    Employee.objects.filter(name="Bobkovich Ivan").delete()
    Employee.objects.filter(name="Gordievich Vladislav").delete()
    Status.objects.filter(name='Без статуса').delete()
    Status.objects.filter(name='Всё по плану').delete()
    Status.objects.filter(name='Есть вопросы').delete()
    Status.objects.filter(name='Есть проблемы').delete()
    Status.objects.filter(name='недозвон').delete()
    Status.objects.filter(name='необходима ежемесячная оплата').delete()
    Tasks.objects.filter(name='Выполнить все задачи').delete()
    Company.objects.filter(name='ОАО МинскТрактор').delete()
    Company.objects.filter(name='ОАО Облгаз').delete()
    Contacts.objects.filter(name='Иван Иванович').delete()
    Contacts.objects.filter(name='Сергей Николаев').delete()
    Contacts.objects.filter(name='Артём Дмитриев').delete()
    Funnel.objects.filter(name='Не обработанна').delete()
    Funnel.objects.filter(name='Квалификация').delete()
    Funnel.objects.filter(name='Переговоры').delete()
    Funnel.objects.filter(name='Согласование документов').delete()
    Funnel.objects.filter(name='Счёт выставлен').delete()
    Funnel.objects.filter(name='Выиграна').delete()
    Funnel.objects.filter(name='Проиграна').delete()
    Proposal.objects.filter(name='Ремонт здания').delete()
    Proposal.objects.filter(name='Капитальный ремонт').delete()
    Deal.objects.filter(profit=10000).delete()
    Deal.objects.filter(profit=100000).delete()
    Payment.objects.filter(price=10000).delete()
    Payment.objects.filter(price=100000).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('crm_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
