# coding=gbk
# 9.5Python标准库

"""模块collections中的一个类OrderedDict"""

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sasah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name,language in favorite_languages.items():
    print("\n",name.title(),"'s favorite language is ",language.title(),".")
    

