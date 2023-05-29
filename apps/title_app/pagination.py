from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class TitlesPagination(PageNumberPagination):
    """ Pagination for main page """
    page_size = 20

    def get_paginated_response(self, data):
        if self.page.has_previous():
            previous_page = self.page.previous_page_number()
        else:
            previous_page = None
        if self.page.has_next():
            next_page = self.page.next_page_number()
        else:
            next_page = None

        return Response({
            'total_count': self.page.paginator.count,
            'page_size': self.page_size,
            'next_page': next_page,
            'previous_page': previous_page,
            'total_pages': self.page.paginator.num_pages,
            'current_page': self.page.number,
            'results': data
        })
