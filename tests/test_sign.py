# -*- coding: utf-8 -*-

import copy

from pywe_sign import calculate_signature, check_signature, fill_signature


class TestSignCommands(object):

    def test_signature_relative(self):
        params = {
            'appid': 'wxd930ea5d5a258f4f',
            'mch_id': 10000100,
            'device_info': 1000,
            'body': 'test',
            'nonce_str': 'ibuaiVcKdpRxkhJA'
        }
        api_key = '192006250b4c09247ec02edce69f6a2d'
        sign = '9A0A8659F005D6984697E2CA0A9CF3B7'
        assert calculate_signature(params, api_key) == sign
        params2 = copy.deepcopy(params)
        params2['sign'] = sign
        assert check_signature(params2, api_key)
        assert check_signature(params, api_key, sign)
        assert fill_signature(params, api_key) == params2
