import json

from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from user_activity.models import user, activity_period



def home(request):
    return render(request, 'user_activity/index.html')



class UserActivity(viewsets.ModelViewSet):
    queryset = user.objects.all()
    activity_queryset = activity_period.objects.all()

    def list(self, request, *args, **kwargs):
        d = {}
        d['ok'] = True
        d['members'] = []
        for member in self.queryset:
            user_dict = {}
            user_dict['id'], user_dict['real_name'], user_dict['tz'] = member.user_id, member.real_name, member.timezone
            activity_queryset = self.activity_queryset.filter(user_id=member.user_id)
            if activity_queryset.exists():
                user_dict['activity_periods'] = []
                for activity in activity_queryset:
                    activity_period = {}
                    activity_period['start_time'], activity_period['end_time'] = activity.start_time, activity.end_time
                    user_dict['activity_periods'].append(activity_period)
            d['members'].append(user_dict)

        return Response(d)








