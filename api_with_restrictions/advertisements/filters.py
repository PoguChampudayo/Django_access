from django_filters import rest_framework as filters


from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = filters.DateFromToRangeFilter(field_name='created_at')
    creator = filters.CharFilter()
    status = filters.CharFilter()

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at', 'status']