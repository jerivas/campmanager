from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from siterelated.utils import current_site_id

from logistics.choices import GENERATION_MATCHING, GENERATIONS, STRUCTURES
from logistics.models import SmallGroup
from signup.models import Guest


@method_decorator(cache_page(60 * 15, key_prefix=current_site_id()), name="dispatch")
class CampOverview(TemplateView):
    """
    Presents an overview of the camp signup stats.
    """

    template_name = "overview.html"

    def get_context_data(self, **kwargs):
        """
        Get all the totals into the template context.
        """
        guest_total = Guest.objects.filter(signed_up=True).count()
        member_total = 0
        generation_totals = []
        structure_totals = []

        # Drill down through structures and generations
        for structure, structure_display in STRUCTURES:
            structure_total = 0
            generations = dict(GENERATION_MATCHING).get(structure)
            for generation in generations:
                generation_display = dict(GENERATIONS).get(generation)
                groups = (
                    SmallGroup.objects.filter(generation=generation)
                    .select_related("counselor")
                    .prefetch_related("camper_set")
                )
                generation_total = sum(len(group.get_attendants()) for group in groups)
                structure_total += generation_total
                generation_totals.append((generation_display, generation_total))
            structure_totals.append((structure_display, structure_total))
            member_total += structure_total

        kwargs.update(
            {
                "generation_totals": generation_totals,
                "structure_totals": structure_totals,
                "member_total": member_total,
                "guest_total": guest_total,
                "total": member_total + guest_total,
            }
        )
        return super().get_context_data(**kwargs)
