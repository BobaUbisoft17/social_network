from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 30


class CommentPagination(PageNumberPagination):
    page_size = 10
