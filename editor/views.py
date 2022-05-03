from rest_framework.decorators import api_view
from rest_framework.response import Response

from editor.models import UserFiles
from editor.serializers import UserFilesSerializers
from .authentication import FirebaseAuthentication

@api_view(['GET', 'POST'])
def save_data(request):
    try:
        if request.method == 'POST':
            if UserFiles.objects.filter(user=request.data.get('user')).exists():
                files = UserFiles.objects.get(user=request.data.get('user'))
                data = request.data
                js = ''
                html = ''
                css = ''
                user = request.data.get('user')
                if data.get('js'):
                    js = data.get('js')
                
                if data.get('html'):
                    html = data.get('html')

                if data.get('css'):
                    css = data.get('css')
                serializer = UserFilesSerializers(instance=files, data={
                    'user': user,
                    'js': js,
                    'html': html,
                    'css': css
                })

                if serializer.is_valid():
                    serializer.save()
                    data = {
                        'status': 'success'
                    }
                    return Response(data)
                else:
                    return Response({
                        'status': 'error',
                        'message': 'Please provide valid values'
                    })
            else:
                data = request.data
                js = ''
                html = ''
                css = ''
                user = request.data.get('user')
                if data.get('js'):
                    js = data.get('js')
                
                if data.get('html'):
                    html = data.get('html')

                if data.get('css'):
                    css = data.get('css')
                serializer = UserFilesSerializers(data={
                    'user': user,
                    'js': js,
                    'html': html,
                    'css': css
                })

                if serializer.is_valid():
                    serializer.save()
                    data = {
                        'status': 'success'
                    }
                    return Response(data)
                else:
                    data = {
                        'status': 'error',
                        'message': 'Please provide valid values'
                    }
                    return Response(data)
        else:
            return Response({
                'status': 'success',
                'format for data entry': {
                    'user': 'current user username',
                    'js': 'js data(optional)',
                    'html': 'html data(optional)',
                    'css': 'css data(optional)',
                }
            })
    except Exception as e:
        data = {
            'status': 'error',
            'message': str(e),
        }
        return Response(data)

@api_view(['GET', 'POST'])
def retrieve_data(request):
    if request.method == 'POST':
        try:
            if UserFiles.objects.filter(user=request.data.get('user')).exists():
                files = UserFiles.objects.get(user=request.data.get('user'))
                serializer = UserFilesSerializers(files)

                data = {
                    'status': 'sucess',
                    'data': serializer.data,
                }
                return Response(data)
            else:
                return Response({
                    'status': 'error',
                    'message': 'data is not present for given user',
                })
        except Exception as e:
            data = {
                'status': 'error',
                'message': str(e)
            }
            return Response(data)
    else:
        return Response({
            'status': 'success',
            'format for retrieve': {
                'user': 'current user',
            }
        })

@api_view(['POST'])
def authenticate(request):
    if request.method == 'POST':
        try:
            data = FirebaseAuthentication.authenticate(request)
            return Response(data)
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e),
            })
    else:
        return Response({
            'status': 'error',
            'message': 'GET not permitted on this url',
        })