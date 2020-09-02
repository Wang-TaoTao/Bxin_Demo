




class ReturnCode:

    SUCCESS = 0
    FAILED = -1


    @classmethod
    def message(cls, code):
        if code == cls.SUCCESS:
            return 'success'
        elif code == cls.FAILED:
            return 'failed'
        else:
            return ''



def wrap_json_response(data=None, code=None, message=None):

    response = {}
    if not code:
        code = ReturnCode.SUCCESS

    if not message:
        message = ReturnCode.message(code)

    if data:
        response['data'] = data

    response['code'] = code
    response['message'] = message
    return response