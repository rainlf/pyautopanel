# -*- coding: UTF-8 -*-
import oathtool
import pyperclip


def get_auth_code():
    with open('rain.txt', 'r') as f:
        password = f.readline().strip()
        token = f.readline().strip()
        code = oathtool.generate_otp(token)
        auth_code = '%s %s' % (password, code)
        pyperclip.copy(auth_code)
        print('Auth code copied to clipboard: %s' % auth_code)
        return auth_code


if __name__ == '__main__':
    get_auth_code()
    pass
