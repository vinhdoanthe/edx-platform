from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import (
        RichTextBlock, TextBlock, CharBlock,
        BooleanBlock, URLBlock, ListBlock,
        StructBlock, IntegerBlock
        )
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock


class FeatureItem(StructBlock):
    icon = ImageChooserBlock()
    title = CharBlock(max_length=1000)
    description = TextBlock()
    link = URLBlock()
    active = BooleanBlock(default=True, required=False)


class MenuItem(StructBlock):
    title = CharBlock(max_length=1000)
    enable = BooleanBlock(default=True, required=False)


class MissionItem(StructBlock):
    icon = ImageChooserBlock()
    title = CharBlock(max_length=1000)
    description = TextBlock()
    enable = BooleanBlock(default=True, required=False)


class WhyItem(StructBlock):
    icon = ImageChooserBlock()
    title = CharBlock(max_length=1000)
    description = TextBlock()
    enable = BooleanBlock(default=True, required=False)


class ProofPointItem(StructBlock):
    icon = ImageChooserBlock()
    number = IntegerBlock(max_length=1000)
    description = TextBlock()
    enable = BooleanBlock(default=True, required=False)


class CaseStudyItem(StructBlock):
    title = CharBlock(max_length=1000)
    description = TextBlock()
    thumbnail = ImageChooserBlock()
    video = URLBlock()
    enable = BooleanBlock(default=True, required=False)


class TestimonialItem(StructBlock):
    quote = TextBlock()
    user_avatar = ImageChooserBlock()
    user_name = TextBlock()
    enable = BooleanBlock(default=True, required=False)


class FooterItem(StructBlock):
    title = CharBlock(max_length=1000)
    item = ListBlock(
            StructBlock([
                ('title', CharBlock(max_length=1000)),
                ('link', URLBlock()),
                ])
            )
    enable = BooleanBlock(default=True, required=False)


class HomePage(Page):
    active = models.BooleanField(default=True)

    menu = StreamField(
            [
                ('logo', ImageChooserBlock()),
                ('key_selling_points', MenuItem()),
                ('why', MenuItem()),
                ('mission', MenuItem()),
                ('proof_points', MenuItem()),
                ('services', MenuItem()),
                ('case_studies', MenuItem()),
                ('testimonials', MenuItem()),
                ('subscription_form', MenuItem())
                ],
            block_counts={
                'logo': {'max_num': 1},
                'key_selling_points': {'max_num': 1},
                'why': {'max_num': 1},
                'mission': {'max_num': 1},
                'proof_points': {'max_num': 1},
                'services': {'max_num': 1},
                'case_studies': {'max_num': 1},
                'testimonials': {'max_num': 1},
                'subscription_form': {'max_num': 1}
            },
            use_json_field=True,
            blank=True
            )

    banner = StreamField(
            [
                ('title', RichTextBlock(features=['bold', 'italic', 'link', 'h1', 'h2', 'link', 'embed'])),
                ('description', TextBlock()),
                ('image', ImageChooserBlock()),
                ('background_image', ImageChooserBlock()),
                ('button_text', CharBlock(max_length=1000)),
                ('button_link', URLBlock()),
                ('enable', BooleanBlock(required=False))
                ],
            block_counts={
                'title': {'max_num': 1},
                'description': {'max_num': 1},
                'image': {'max_num': 1},
                'button_text': {'max_num': 1},
                'button_link': {'max_num': 1}
                },
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    features = StreamField(
            [
                ('list_items', ListBlock(FeatureItem())),
                ('enable', BooleanBlock(required=False))
                ],
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    why = StreamField(
            [
                ('image', ImageChooserBlock()),
                ('title', CharBlock(max_length=1000)),
                ('description', TextBlock()),
                ('list_items', ListBlock(WhyItem())),
                ('enable', BooleanBlock(required=False))
                ],
            block_counts={
                'image': {'max_num': 1},
                'title': {'max_num': 1},
                'description': {'max_num': 1},
                },
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    mission = StreamField(
            [
                ('title', CharBlock(max_length=1000)),
                ('description', TextBlock()),
                ('image', ImageChooserBlock()),
                ('list_items', ListBlock(MissionItem())),
                ('enable', BooleanBlock(required=False))
                ],
            block_counts={
                'title': {'max_num': 1},
                'description': {'max_num': 1},
                'image': {'max_num': 1},
                },
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    proof_points = StreamField([
        ('list_items', ListBlock(ProofPointItem())),
        ('enable', BooleanBlock(required=False))
        ], use_json_field=True, blank=True)

    services = StreamField(
            [
                ('image', ImageChooserBlock()),
                ('title', CharBlock(max_length=1000)),
                ('description', TextBlock()),
                ('list_items', ListBlock(WhyItem())),
                ('enable', BooleanBlock(required=False))
                ],
            block_counts={
                'image': {'max_num': 1},
                'title': {'max_num': 1},
                'description': {'max_num': 1},
                },
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    case_studies = StreamField(
            [
                ('title', CharBlock(max_length=1000)),
                ('list_items', ListBlock(CaseStudyItem())),
                ('enable', BooleanBlock(required=False))
                ],
            block_counts={
                'title': {'max_num': 1}
                },
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    testimonials = StreamField(
            [
                ('title', CharBlock(max_length=1000)),
                ('description', TextBlock()),
                ('list_items', ListBlock(TestimonialItem())),
                ('enable', BooleanBlock(required=False))
                ], 
            block_counts={
                'title': {'max_num': 1},
                'description': {'max_num': 1},
                },
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    subscription_form = StreamField(
            [
                ('title', CharBlock(max_length=1000)),
                ('description', TextBlock()),
                ('enable', BooleanBlock(required=False)),
                ],
            block_counts={
                'title': {'max_num': 1},
                'description': {'max_num': 1},
                },
            use_json_field=True,
            default=[('enable', True)],
            blank=True)

    footer = StreamField([
        ('description', TextBlock()),
        ('facebook_contact', StructBlock([
            ('url', URLBlock()),
            ('enable', BooleanBlock(default=True, required=False)),
            ])),
        ('instagram_contact', StructBlock([
            ('url', URLBlock()),
            ('enable', BooleanBlock(default=True, required=False)),
            ])),
        ('linkedin_contact', StructBlock([
            ('url', URLBlock()),
            ('enable', BooleanBlock(default=True, required=False)),
            ])),
        ('list_items', ListBlock(FooterItem())),
        ('location', TextBlock()),
        ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + [
            FieldPanel('menu'),
            FieldPanel('banner'),
            FieldPanel('features'),
            FieldPanel('mission'),
            FieldPanel('why'),
            FieldPanel('proof_points'),
            FieldPanel('services'),
            FieldPanel('case_studies'),
            FieldPanel('testimonials'),
            FieldPanel('subscription_form'),
            FieldPanel('footer'),
            ]
