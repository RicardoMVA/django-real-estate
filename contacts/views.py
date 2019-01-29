from django.shortcuts import redirect

from django.contrib import messages

from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made inquiry already
        if request.user.is_authenticated:
            # check current user's ID
            user_id = request.user.id
            # check if the user has made contact before
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id,
                user_id=user_id,
            )

            if has_contacted:
                messages.error(
                    request,
                    'You have already made an inquiry for this listing'
                )
            return redirect('/listings/' + listing_id)

        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id
        )

        contact.save()

        messages.success(
            request,
            'Your request has been submitted, a realtor will get back to you soon')

        return redirect('/listings/' + listing_id)
