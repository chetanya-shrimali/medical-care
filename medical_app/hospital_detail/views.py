from django.shortcuts import render

from hospital_detail.models import Detail, Hospital, Tag, Review


def hospital_list(request):
    h_list = Hospital.objects.all()
    detail_list = Detail.objects.all()
    return render(request, 'hospital_list.html',
                  {'h_list': h_list, 'detail_list': detail_list})


def hospital_detail(request, pk):
    details = Detail.objects.get(pk=pk)
    tag = Tag.objects.filter(details=details)
    review = Review.objects.filter(details=details)
    return render(request, 'hospital_detail.html',
                  {'details': details, 'tag': tag, 'review': review})
