import sys

name = sys.argv[1]
verbose = sys.argv[2]


def underscore(str):
    return "".join(map(lambda x: "_" + x if x.isupper()  else x, str))[1:].lower()


model = """class {name}(CoreModel):

    class Meta:
        verbose_name = '{verbose}'
        verbose_name_plural = '{verbose}'""".format(name=name, verbose=verbose)

serializer = """class {name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {name}""".format(name=name, verbose=verbose)

view = """class {name}ViewSet(viewsets.ModelViewSet):
    serializer_class = {name}Serializer
    queryset = {name}.objects.all()""".format(name=name, verbose=verbose)

url = """router.register(r'{lower}', {name}ViewSet, base_name="{lower}")""".format(name=name, verbose=verbose,
                                                                                   lower=underscore(name) + 's')

try:
    with open('models.py', 'a') as f:
        f.write(model)
    with open('serializers.py', 'a') as f:
        f.write(serializer)
    with open('views.py', 'a') as f:
        f.write(view)
    with open('urls.py', 'a') as f:
        f.write(url)

    print("生成api接口{name}完毕".format(name=name))
except:
    print("代码生成过程出错")


#执行命令
#在模块目录下执行　python codeGen.py 模型单词　模型说明
#其中模型单词为托峰命名法.