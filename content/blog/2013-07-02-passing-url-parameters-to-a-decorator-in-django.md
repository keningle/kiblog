Title: Passing URL Parameters to a Decorator in Django
Date: 2013-07-03 
Tags: django, python
Slug: passing-url-parameters-to-a-decorator-in-django

I have been working on a small project where I needed to pass a URL parameter to a decorator I was writing.  In an ongoing effort to follow the principal of DRY, I have found that decorators (when used at the right time) can really help.  I was able to find no shortage of examples where decorators made life easier in django applications (e.g. login_required).

After a bit of searching and asking around I came across a really great blog post by Charles Leifer describing in details how to accomplish almost exactly what I needed.

For the purposes of this example, let’s assume I have a Company model where I have defined a company_admin foreign key that relates to a user object as the admin for the company (in practice I would recommend using the groups and permissions already built into django, but this is just an example).

Let’s say I have a URL pattern that looks something like this:

```python
url(r'^example/(?P<slug>[a-z0-9-]+)/$', 'some.view'),
```

Initially my view (and probably many views) might have been checking to see if this logged-in user was an admin kind of like this:

```python
@login_required
def some_view(request, slug):
    # Get the company object based on slug
    company = get_object_or_404(Company, slug=slug)
    
    # Check and see if the logged in user is admin
    if company.admin_user != request.user:
        return HttpResponseForbidden()
        
    .... view logic ....
    
    return render(request, 'company/index.html', {'company': company})
```

I want to create a decorator that will wrap the view, take the slug and handle the verification that this user should have access to this company.  I will then want to return to the view the actual company object instead of the slug.  

This will give me the capability to re-use the authentication as well as have my company object (which is useful) instead of simply the slug:

```python
from django.utils.functional import wraps
...
 
def check_company_admin(view):
    @wraps(view)
    def inner(request, slug, *args, **kwargs):
        # Get the company object
        company = get_object_or_404(Company, slug=slug)
        
        # Check and see if the logged in user is admin
        if company.admin_user != request.user:
            return HttpResponseForbidden()
            
        # Return the actual company object to the view
        return view(request, company, *args, **kwargs)
    
    return inner
```

Finally, my view will change to use the decorator and remove the duplicate logic:

```python
@login_required
@check_company_admin
def some_view(request, company):
    # Even though the slug is in the URL. We are getting a company 
    # object back from the decorator
    
    .... view logic ....
    
    return render(request, 'company/index.html', {'company': company})
```

This creates a re-usable decorator that utilizes URL parameters.  I hope this helps more people than just me.  Feel free to comment if there is a better way to do this or if I should change something.
