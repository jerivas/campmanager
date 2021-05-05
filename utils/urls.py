from django.core.urlresolvers import reverse


def admin_url(model, url, object_id=None):
    """
    Returns the URL for the given model and admin url name.
    From mezzanine.utils.urls.admin_url.
    """
    opts = model._meta
    url = f"admin:{opts.app_label}_{opts.object_name.lower()}_{url}"
    args = ()
    if object_id is not None:
        args = (object_id,)
    return reverse(url, args=args)
