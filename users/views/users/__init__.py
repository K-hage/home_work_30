from .view import UserDetailView, UserListView
from .update import UserUpdateView
from .delete import UserDeleteView
from .create import UserCreateView

__all__ = [
    'UserDeleteView',
    'UserUpdateView',
    'UserCreateView',
    'UserListView',
    'UserDetailView'
]
