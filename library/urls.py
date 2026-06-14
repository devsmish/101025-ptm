from django.urls import path
from rest_framework.routers import SimpleRouter, DefaultRouter


from library.views import book_list_view, book_list_create, BookDetailAPIView
from library.class_views import (
    BookListCreateAPIView,
    BookRetrieveUpdateDestroyAPIView,
    CategoryListCreateGenericAPIView,
    CategoryRetrieveUpdateDestroyGenericView,
    AuthorListCreateGenericView,
    UserListGenericView,
    BookListGenericView,
    PublisherViewSet
)


router = SimpleRouter()
# router = DefaultRouter()
router.register('publishers', PublisherViewSet)
#
# publishers/
# publishers/<regular expression>/


# api/v1/books/
urlpatterns = [
    # path('books/', BookListCreateAPIView.as_view()),
    path('books/', BookListGenericView.as_view()),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view()),
    path('categories/', CategoryListCreateGenericAPIView.as_view()),
    path('categories/<str:name>/', CategoryRetrieveUpdateDestroyGenericView.as_view()),
    path('authors/', AuthorListCreateGenericView.as_view()),
    path('users/', UserListGenericView.as_view()),
    # path('books/', book_list_view),
    # CRUD - 4
    # path('books/', book_list_create), # read all, create
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    # path('books/<int:pk>/', book_read_update_delete), # read id, update id, delete id
    path('books/<int:pk>/', BookDetailAPIView.as_view()), # read id, update id, delete id
]


# print(router.urls)
urlpatterns += router.urls


# PK = 1234
# PK (uuid) = 'asd8f6-865sms-sknjf6-alan27'
