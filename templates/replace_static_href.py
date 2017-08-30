# _*_ coding: utf-8 _*_
__author__ = 'maoxie'
__date__ = '2017/5/13 16:01'

import re
import os

MEDIA_URL_REGEX = r'^.*?<img.*src="(\S*)".*/>'
CSS_URL_REGEX = r'^.*?<link.*href="(\S*.css)".*>'
JS_URL_REGEX = r'^.*?<script.*src="(\S*.js)".*></script>'
REGEX = [MEDIA_URL_REGEX,
         CSS_URL_REGEX,
         JS_URL_REGEX]
url_pattern = re.compile(REGEX[2])

filename = 'usercenter-base.html'
dir_path = os.path.abspath(os.path.curdir)
full_path = os.path.join(dir_path, filename)
with open(full_path) as f_read, open(full_path+'_new.html','w') as f_write:
    new_lines = []
    for line in f_read.readlines():
        result = url_pattern.match(line.strip())
        if result is not None:
            media_url = result.group(1)
            new_url = re.match('^.*?/(\S*)', media_url).group(1)
            replace_url = "{{% static '{}' %}}".format(new_url)
            line = re.sub(media_url,replace_url,line)
            pass
        new_lines.append(line)
    f_write.writelines(new_lines)


