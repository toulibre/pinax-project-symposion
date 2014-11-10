# -*- coding: utf-8 -*-
# monkey_patching Speaker add organisation field

from django.db import models
from symposion.speakers.models import Speaker

Speaker.add_to_class('organisation', models.CharField(max_length=100,blank=True))
