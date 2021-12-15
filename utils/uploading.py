


class ImageUploadHelper:

    FIELD_TO_COMBINE_MAP = {
        'defaults': {
            'upload_postfix': 'uploads'
        },
        'Member': {
            'fields': 'slug',
            'upload_postfix': 'members_images'
        },
        'Artist': {
            'fields': 'slug',
            'upload_postfix': 'artist_images'
        },
        'Album': {
            'fields': 'slug',
            'upload_postfix': 'album_images'
        },
    }

    def __init__(self, field_name_to_combine, instance, filename, upload_postfix):
        self.field_name_to_combine = field_name_to_combine
        self.instance = instance
        self.extention = filename.split('.')[-1]
        self.upload_postfix = f"{upload_postfix}"

    @classmethod
    def get_field_to_combine_and_upload_postfix(cls, klass):
        field_to_combine = cls.FIELD_TO_COMBINE_MAP[klass]['field']
        upload_postfix = cls.FIELD_TO_COMBINE_MAP.get(
            'upload_postfix', cls.FIELD_TO_COMBINE_MAP['default']['upload_postfix']
        )
        return field_to_combine, upload_postfix

    @property
    def path(self):
        field_to_combine = getattr(self.instance, self.field_name_to_combine)
        filename = '.'.join([field_to_combine, self.extention])
        return f"images/{self.instance.__class__.__name__.lower()}{self.upload_postfix}/{field_to_combine}/{filename}"


def upload_function(instance, filename):
    if hasattr(instance, "content_object"):
        instance = instance.content_object
    field_to_combine, upload_postfix = ImageUploadHelper.get_field_to_combine_and_upload_postfix(instance.__class__.__name__)
    image = ImageUploadHelper(field_to_combine, instance, filename, upload_postfix)
    return image.path
