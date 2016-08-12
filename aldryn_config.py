# -*- coding: utf-8 -*-
from functools import partial
from aldryn_client import forms


class Form(forms.BaseForm):

    def to_settings(self, data, settings):
        from aldryn_addons.utils import djsenv, boolean_ish
        from aldryn_haystack import haystack_url
        s = settings
        env = partial(djsenv, settings=settings)

        if env('DJANGO_MODE') == 'local' or env('DJANGO_MODE') == 'build':
            s['HAYSTACK_CONNECTIONS'] = {
                'default': {
                    'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
                }
            }
            return s

        if not env('DEFAULT_HAYSTACK_URL'):
            return s

        s['ALDRYN_HAYSTACK_DEBUG'] = boolean_ish(
            env('ALDRYN_HAYSTACK_DEBUG', s['DEBUG']))

        s['DEFAULT_HAYSTACK_URL'] = env('DEFAULT_HAYSTACK_URL')
        s.setdefault('HAYSTACK_CONNECTIONS', {})
        s['HAYSTACK_CONNECTIONS']['default'] = haystack_url.parse(
            url=s['DEFAULT_HAYSTACK_URL']
        )

        if s['ALDRYN_HAYSTACK_DEBUG']:
            s['LOGGING']['loggers']['elasticsearch.trace'] = {
                'handlers': ['console'],
                'level': 'INFO',
            }
        return s