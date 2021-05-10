from django.core.urlresolvers import reverse


def admin_url(model, action, object_id=None):
    """
    Returns the URL for the given model and admin url name.
    From mezzanine.utils.urls.admin_url.
    """
    urlname = f"admin:{model._meta.app_label}_{model._meta.model_name}_{action}"
    args = () if object_id is None else (object_id,)
    return reverse(urlname, args=args)
