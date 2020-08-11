from django import http
from django.shortcuts import render



def index(request):

    # token = request.META.get('HTTP_AUTHTOKEN','')
    # if token != 'apc':
    #     return http.HttpResponseForbidden()

    return render(request,'index.html')



def search(request):

    keyword = request.GET.get('search',' ')
    data = []
    print(keyword)
    if len(keyword) >= 3:
        print('大于等于三个字符了')
        # 查询相关用户uid和nickname
        data = [{'nickname': 'tarss', 'name': "tarsss", 'phone': "+8617600110411"},
                        {'nickname': 'asdg', 'name': "asdg", 'phone': "+8615041890909"},
                        {'nickname': 'abcde', 'name': "abcde", 'phone': "+861504189000"},]
        data = {'data':data}

    return http.JsonResponse(data=data, safe=False)
