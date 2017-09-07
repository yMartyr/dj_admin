#!/user/bin/env python
# -*- coding:utf-8 -*-

from manual.service import v1
from app01 import models

v1.site.register(models.UserInfo)
