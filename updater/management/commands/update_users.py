import datetime
import json
from users.models import SocialUser, SocialGroup
from django.core.management.base import NoArgsCommand, BaseCommand
from optparse import make_option
import requests
import sys
import time


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
        ) + (make_option('--all',
            action='store_true',
            dest='all_groups',
            default=False,
            help='Grab 1k users from group'),
        )

    def handle_noargs(self, **options):
        # theandersonband default
        # id  - 1
        if options["group_id"]:
            groups = SocialGroup.objects.filter(name=options["group_id"])
        
        elif options["all_groups"]:   
            groups = SocialGroup.objects.filter(processed=False) 

        else:
            print "No groups"
            sys.exit()    

        for group in groups:        
            print "Processing group %s"%group.name
            url = 'https://api.vk.com/method/groups.getMembers?group_id=%s&v=5.16&offset=0&count=1000&fields=sex,bdate,city,country,photo_200_orig,photo_max_orig&access_token='%group.name

            r = requests.get(url)
            time.sleep(5)
            users = json.loads(r.text)

            for user in users["response"]["items"]:
                print user["id"]
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

            group.processed = 1
            group.save()    


