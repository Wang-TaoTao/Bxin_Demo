import os
import yaml
from django.http import FileResponse
from django.http import Http404
from django.http import HttpResponse
from django.http import JsonResponse
from Bxin_one import settings
import utils.response
from Bxin_one.settings import BASE_DIR


def init_app_data():
    data_file = os.path.join(settings.BASE_DIR, 'app.yaml')
    with open(data_file, 'r', encoding='utf-8') as f:
        apps = yaml.load(f)
    return apps



def get_menu(request):
    global_app_data = init_app_data()
    published_app_data = global_app_data.get('published')
    response = utils.response.wrap_json_response(data=published_app_data,
                                                 code=utils.response.ReturnCode.SUCCESS)

    return JsonResponse(data=response, safe=False)



def get_images(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')
        imgfile = os.path.join(settings.STATICFILES_IMAGES, md5 + '.jpg')

        data = open(imgfile, 'rb').read()
        return HttpResponse(content=data, content_type='image/jpeg')
        # return FileResponse(data, content_type='image/jpg')


def get_image_text(request):
    if request.method == 'GET':
        md5 = request.GET.get('md5')

        response_data = {}
        response_data['name'] = md5 + '.jpg'
        response_data['url'] = '/service/image?md5=%s' % md5
        response = response_data
        return JsonResponse(data=response, safe=False)