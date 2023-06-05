from wagtail.images.models import Image

import json


def get_stream_field_data(obj, field_name):
    """Return the data for a StreamField"""
    """ Example: StreamField => ListBlock => StructBlock """

    field = obj._meta.get_field(field_name)
    raw_data = field.get_prep_value(getattr(obj, field_name))
    data = json.loads(raw_data)
    replace_image_with_object(data)
    result = handle_list_data(data)

    return list_to_dict(result)


def replace_image_with_object(data):
    """Replace image value which is image id """
    """from method get_prep_value with image object"""

    if isinstance(data, dict):
        image_id = 0
        key = 'value'
        if data.get('type') in ['image', 'icon', 'thumbnail', 'logo', 'user_avatar', 'background_image']:
            image_id = data['value']

        if data.get('logo') and image_id == 0:
            key = 'logo'
            image_id = data['icon']

        if data.get('icon') and image_id == 0:
            key = 'icon'
            image_id = data['icon']

        if data.get('thumbnail') and image_id == 0:
            key = 'thumbnail'
            image_id = data['thumbnail']

        if data.get('user_avatar') and image_id == 0:
            key = 'user_avatar'
            image_id = data['user_avatar']

        if data.get('background_image') and image_id == 0:
            key = 'background_image'
            image_id = data['background_image']

        if isinstance(image_id, int) and image_id > 0:
            try:
                image_object = Image.objects.get(id=image_id)
                data[key] = image_object
            except Image.DoesNotExist:
                data[key] = None

        if data.get('value', None):
            if isinstance(data['value'], dict):
                replace_image_with_object(data['value'])
            elif isinstance(data, list):
                for item in data:
                    replace_image_with_object(item)

        for key, value in data.items():
            replace_image_with_object(value)
    elif isinstance(data, list):
        for item in data:
            replace_image_with_object(item)


def handle_list_data(data):
    """Return human readable data from StreamField data"""
    """Example data input: [
    {
        'id': '6cfe0a2e-bd49-4823-b1d3-bd92f6b04314',
        'type': 'key_selling_points',
        'value': {'title': 'Selling', 'enable': True}
    },
    [
        {
            'id': '65eca13c-7f5f-47a3-a349-517322c76ad5',
            'type': 'why',
            'value': {'title': 'Reasons', 'enable': True}
        },
        {
            'id': '5c6df80e-d6bc-44a9-8c1e-3e9fe041d8c2',
            'type': 'nested',
            'value': [
                {'nested_key': 'Nested value 1'},
                {'nested_key': 'Nested value 2'}
            ]
        }
    ]
    ]"""
    result = data

    if isinstance(data, dict):
        if 'type' in data and 'value' in data:
            result[data['type']] = handle_list_data(data['value'])
    elif isinstance(data, list):
        result = []
        for item in data:
            if isinstance(item, dict):
                if 'type' in item and 'value' in item:
                    result.append({item['type']: handle_list_data(item['value'])})
                else:
                    result.append(item['value'])
            elif isinstance(item, list):
                result.append(handle_list_data(item))
    return result


def list_to_dict(data):
    """Convert list of dicts which unique key to dict"""
    result = {}

    for item in data:
        for key, value in item.items():
            result[key] = value

    return result
