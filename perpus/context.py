from django.conf import settings

def context_utils(request):
    keywords = "ahmad rudi, django framework, python,"
    description = "Website ahmad rudi"
    return {
        'meta_keywords': keywords,
        'meta_description':description,
        'site_name':settings.SITE_NAME,
        'lang':settings.LANGUAGE_CODE.split("-")[0],
    }