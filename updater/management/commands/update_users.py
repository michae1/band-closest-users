import datetime
import json
from users.models import SocialUser, SocialGroup
from django.core.management.base import NoArgsCommand, BaseCommand
from optparse import make_option
import requests
import sys


class Command(NoArgsCommand):
    help = """
    Grab users from groups
    """
    option_list = BaseCommand.option_list + (
        make_option('--group',
            action='store',
            dest='group_id',
            default=False,
            help='Grab 1k users from group'),
        )

    def handle_noargs(self, **options):
        # theandersonband default
        # id  - 1
        print options["group_id"]
        group = SocialGroup.objects.get(name=options["group_id"])
        group_id = group.id
        group_name = group.name

        
        url = 'https://api.vk.com/method/groups.getMembers?group_id=%s&v=5.16&offset=0&count=1000&fields=sex,bdate,city,country,photo_200_orig,photo_max_orig&access_token='%group_name

        r = requests.get(url)

        users = json.loads(r.text)

        for user in users["response"]["items"]:
            # print user
            user_obj, created = SocialUser.objects.get_or_create(social_id = user["id"],
                 )

            user_obj.social_groups.add(group)
            user_obj.first_name = user["first_name"]
            user_obj.last_name = user["last_name"]
            if "city" in user:
                user_obj.city_name = user["city"]["title"]
                user_obj.city_id = user["city"]["id"]
            if "country" in user:    
                user_obj.country_name = user["country"]["title"]
                user_obj.country_id = user["country"]["id"]
            user_obj.save()


