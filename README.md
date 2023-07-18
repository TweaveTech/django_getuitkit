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


Adjusting the top-menu
----------------------

Create in one of your apps a path `templates/includes` and add the following file: `navbar_main.html` with content

```html
  <li><a href="#">My App</a>
    <div class="uk-navbar-dropdown">
        <ul class="uk-nav uk-navbar-dropdown-nav">
            <li><a href="{% url 'company_list' %}">thing to do</a></li>
            <li><a href="{% url 'contact_list' %}">another menu item</a></li>
        </ul>
    </div>
  </li>
```


Adding extra css
----------------

Add a file `local_css_overrides.css` in your templates root.
And either find the overrides in the original css in the package or use these as a cheat-sheet to override the primary colour:

```css



a,
.uk-link {
  color: #ff7f00;
  text-decoration: none;
  cursor: pointer;
}
a:hover,
.uk-link:hover,
.uk-link-toggle:hover .uk-link {
  color: #ff7f00;
  text-decoration: underline;
}

::selection {
  background: #ff7f00;
  color: #fff;
  text-shadow: none;
}

a.uk-link-heading:hover,
.uk-link-heading a:hover,
.uk-link-toggle:hover .uk-link-heading {
  color: #ff7f00;
  text-decoration: none;
}

.uk-list-primary > ::before {
  color: #ff7f00 !important;
}

.uk-input:focus,
.uk-select:focus,
.uk-textarea:focus {
  outline: none;
  background-color: #fff;
  color: #666;
  border-color: #ff7f00;
}

.uk-radio:focus,
.uk-checkbox:focus {
  background-color: rgba(0, 0, 0, 0);
  outline: none;
  border-color: #ff7f00;
}

/*
 * Checked
 */
.uk-radio:checked,
.uk-checkbox:checked,
.uk-checkbox:indeterminate {
  background-color: #ff7f00;
  border-color: transparent;
}

.uk-button-primary {
  background-color: #ff7f00;
  color: #fff;
  border: 1px solid transparent;
}

.uk-button-primary:hover {
  background-color: #ff7f00;
  color: #fff;
}

/*
 * Progress bar
 * 1. Remove right border in IE11 and Edge
 */
.uk-progress::-webkit-progress-value {
  background-color: #ff7f00;
  transition: width 0.6s ease;
}
.uk-progress::-moz-progress-bar {
  background-color: #ff7f00;
}
.uk-progress::-ms-fill {
  background-color: #ff7f00;
  transition: width 0.6s ease;
  /* 1 */
  border: 0;
}

/*
 * Primary
 */
.uk-section-primary {
  background: #ff7f00;
}

.uk-tile-primary {
  background-color: #ff7f00;
}

.uk-card-badge {
  /* 1 */
  position: absolute;
  top: 15px;
  right: 15px;
  z-index: 1;
  /* 2 */
  height: 22px;
  padding: 0 10px;
  /* 3 */
  background: #ff7f00;
  color: #fff;
  font-size: 0.875rem;
  /* 4 */
  display: flex;
  justify-content: center;
  align-items: center;
  line-height: 0;
  border-radius: 2px;
  text-transform: uppercase;
}

.uk-card-primary {
  background-color: #ff7f00;
  color: #fff;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
}
.uk-card-primary .uk-card-title {
  color: #fff;
}
.uk-card-primary.uk-card-hover:hover {
  background-color: #ff7f00;
  box-shadow: 0 14px 25px rgba(0, 0, 0, 0.16);
}

.uk-alert-primary {
  background: #d8eafc;
  color: #ff7f00;
}

.uk-badge {
  box-sizing: border-box;
  min-width: 18px;
  height: 18px;
  padding: 0 5px;
  border-radius: 500px;
  vertical-align: middle;
  /* 1 */
  background: #ff7f00;
  color: #fff !important;
  font-size: 11px;
  /* 2 */
  display: inline-flex;
  justify-content: center;
  align-items: center;
  line-height: 0;
}

.uk-label {
  display: inline-block;
  padding: 0 10px;
  background: #ff7f00;
  line-height: 1.5;
  font-size: 0.875rem;
  color: #fff;
  vertical-align: middle;
  white-space: nowrap;
  border-radius: 2px;
  text-transform: uppercase;
}

.uk-search-default .uk-search-input:focus {
  background-color: rgba(0, 0, 0, 0);
  border-color: #ff7f00;
}

.uk-notification-message-primary {
  color: #ff7f00;
}

/* Active */
.uk-subnav-pill > .uk-active > a {
  background-color: #ff7f00;
  color: #fff;
}

.uk-tab > .uk-active > a {
  color: #333;
  border-color: #ff7f00;
}

.uk-text-primary {
  color: #ff7f00 !important;
}

.uk-text-background {
  /* 1 */
  -webkit-background-clip: text;
  /* 2 */
  display: inline-block;
  /* 3 */
  color: #ff7f00 !important;
}
@supports (-webkit-background-clip: text) {
  .uk-text-background {
    background-color: #ff7f00;
    color: transparent !important;
  }
}

.uk-background-primary {
  background-color: #ff7f00;
}
```

## Creating a ListView

1. Inherit `from getuikit.views import ListView`
2. Create your template in the relevant folder.
3. Extend you template like this example:

```html
{% extends "base_list.html" %}

{% block title %}Customers{% endblock %}

{% block list_title %}Customers{% endblock %}

{% block list_add_button_link %}{% url 'customer_create' %}{% endblock %}
{% block list_add_button_content %}<i class="fa-solid fa-clock"></i> Add Customer{% endblock %}

{% block thead %}
<th>sku</th>
<th>Hours Worked</th>
<th>Hours last month</th>
<th>Hours this month</th>
<th>Hours Invoiced</th>
<th>Pending Payment</th>
<th>Total Revenue</th>
<th>Total Worked Price</th>
<th>Budget Last Month</th>
<th>Budget This Month</th>
<th>Budget available</th>
<th></th>
{% endblock %}

{% block tbody %}
{% for comp in page_obj %}
<tr>
    <td>{{ comp.name }}</td>
    <td>{{ comp.total_time_spent_in_hours|floatformat:2 }}</td>
    <td>{{ comp.hours_last_month }}</td>
    <td>{{ comp.hours_this_month }}</td>
    <td>{{ comp.total_hours_invoiced|floatformat:2 }}</td>
    <td>{{ comp.pending_revenue|floatformat:2}}</td>
    <td>{{ comp.total_revenue_billed|floatformat:2 }}</td>
    <td>{{ comp.total_price_worktime|floatformat:2 }}</td>
    <td>{{ comp.total_price_worktime_last_month|floatformat:2 }}</td>
    <td>{{ comp.total_price_worktime_this_month|floatformat:2 }}</td>
    <td><span class="{% if comp.total_budget_available < 0 %}tweave-red-text{% endif %}">{{ comp.total_budget_available|floatformat:2 }}</span></td>
    <td><a href="{% url 'customer_detail' comp.pk %}">View</a></td>
</tr>
{% endfor %}
{% endblock %}
```


## Creating a DetailView

1. Inherit `from getuikit.views import DetailView`
2. Create your template in the relevant folder.
3. Set the fields you wish to show on the view with `fields = ['name', 'field', 'another_field']`
4. Extend you template like this example:

```html
{% extends "base_detail.html" %}


```