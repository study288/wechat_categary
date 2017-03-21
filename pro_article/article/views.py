from django.shortcuts import render
from article import models
from django.template import loader, Context
from django.http import HttpResponse



dic_cat={'hdkp':'核电科普','hhyw':'海核要闻', 'hhqn':'海核青年','hhxf':'海核先锋','hhwy':'海核文苑','hhgy':'海核光影','gsjj':'公司简介','qywh':'企业文化','lxwm':'联系我们'}


def archive(request, **kwargs):
    posts = models.Article.objects.filter(cat__Categary_text__iexact=dic_cat[kwargs['cat']]).order_by('-pub_date')[:10]
    t = loader.get_template("archive.html")
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))



