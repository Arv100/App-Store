from django.db import migrations
from django.utils.text import slugify
from django.db import transaction
import itertools

def generate_unique_slug(apps, schema_editor):
    App = apps.get_model('store', 'App')
    with transaction.atomic():
        for app in App.objects.all():
            base_slug = slugify(app.name)
            slug = base_slug
            for i in itertools.count(1):
                if not App.objects.filter(slug=slug).exists():
                    break
                slug = f"{base_slug}-{i}"
            app.slug = slug
            app.save()

class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_app_slug'),
    ]

    operations = [
        migrations.RunPython(generate_unique_slug),
    ]

