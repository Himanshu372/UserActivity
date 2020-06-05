import json

from django.core.management.base import BaseCommand, CommandError

from user_activity.models import user, activity_period

class Command(BaseCommand):
    help = 'This command is used for populating database'

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        with open(options['file']) as json_file:
            json_obj = json.load(json_file)
            try:
                if json_obj['ok']:
                    members = json_obj['members']
                    for member in members:
                        user_id, name, timezone = member['id'], member['real_name'], member['tz']
                        user_obj = user(user_id=user_id, real_name=name, timezone=timezone)
                        user_queryset = user.objects.all()
                        if not user_queryset.filter(user_id=user_id, real_name=name, timezone=timezone).exists():
                            user_obj.save()
                        activity_periods = member['activity_periods']
                        for period in activity_periods:
                            start_time, end_time = period['start_time'], period['end_time']
                            activity_period_obj = activity_period(user_id=user_id, start_time=start_time,
                                                                  end_time=end_time)
                            activity_period_queryset = activity_period.objects.all()
                            if not activity_period_queryset.filter(user_id=user_id, start_time=start_time,
                                                                   end_time=end_time):
                                activity_period_obj.save()
            except Exception:
                raise CommandError('Format of file is not correct')




