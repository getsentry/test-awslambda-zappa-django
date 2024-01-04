import boto3

from django.http import HttpResponse

from sentry_sdk.utils import logger

def error(request):
    # Read S3 bucket contents
    logger.warning("Reading S3 bucket contents")
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('antonpirker-test-zappa-ml4ue4qxn') # thats the zappa bucket
    for my_bucket_object in my_bucket.objects.all():
        logger.warning("S3 bucket object: ")
        logger.warning(my_bucket_object)

    # Raise an error
    1/0

    return HttpResponse("This should raise an errror!")
                        
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")