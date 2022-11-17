from apps.user.models import User


def upload_images(instance, filename):
    prefix = f"{instance.id_card.id_user.email}/{instance.id_card.slug}/{filename}"
    return f"user/users/{prefix}"
