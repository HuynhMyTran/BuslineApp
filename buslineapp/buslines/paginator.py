from rest_framework.pagination import PageNumberPagination


class BuslinePaginator(PageNumberPagination):
    page_size = 3
