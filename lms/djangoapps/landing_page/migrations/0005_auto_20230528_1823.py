# Generated by Django 3.2.18 on 2023-05-28 18:23

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0004_auto_20230527_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='banner',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.RichTextBlock()), ('description', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('button_text', wagtail.blocks.CharBlock(max_length=1000)), ('button_link', wagtail.blocks.URLBlock()), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='case_studies',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.CharBlock(max_length=1000)), ('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('thumbnail', wagtail.images.blocks.ImageChooserBlock()), ('video', wagtail.blocks.URLBlock()), ('enable', wagtail.blocks.BooleanBlock(default=True, required=False))]))), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='features',
            field=wagtail.fields.StreamField([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('link', wagtail.blocks.URLBlock()), ('active', wagtail.blocks.BooleanBlock(default=True, required=False))]))), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='mission',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('enable', wagtail.blocks.BooleanBlock(default=True, required=False))]))), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='proof_points',
            field=wagtail.fields.StreamField([('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('number', wagtail.blocks.IntegerBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('enable', wagtail.blocks.BooleanBlock(default=True, required=False))]))), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='services',
            field=wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('enable', wagtail.blocks.BooleanBlock(default=True, required=False))]))), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subscription_form',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='testimonials',
            field=wagtail.fields.StreamField([('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('quote', wagtail.blocks.TextBlock()), ('user_avatar', wagtail.images.blocks.ImageChooserBlock()), ('user_name', wagtail.blocks.TextBlock()), ('enable', wagtail.blocks.BooleanBlock(default=True, required=False))]))), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='why',
            field=wagtail.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('list_items', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('icon', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.blocks.CharBlock(max_length=1000)), ('description', wagtail.blocks.TextBlock()), ('enable', wagtail.blocks.BooleanBlock(default=True, required=False))]))), ('enable', wagtail.blocks.BooleanBlock(required=False))], blank=True, default=[('enable', True)], use_json_field=True),
        ),
    ]
