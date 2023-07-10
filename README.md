# django_getuitkit
A lightweight wrapper for getuitkit.com including some default views and templates.  It has an auto-generating set of templates and views on board.

Detailed documentation is in the "docs" directory. (TODO)

Quick start
-----------

1. Add "getuikit" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...,
        "getuikit",
    ]

2. Subclass the views used from the package.

    from getuikit.views import DetailView, UpdateView, ListView, CreateView, DeleteView

    class MyDetailView(DetailView):
        # Set the fields you wish to show
        fields = ['name', 'colour']


3. Run ``python manage.py migrate`` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.