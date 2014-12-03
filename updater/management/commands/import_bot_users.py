import datetime
import json
from users.models import SocialUser, SocialGroup
from django.core.management.base import NoArgsCommand, BaseCommand
from optparse import make_option
import requests
import sys


class Command(NoArgsCommand):
    help = """
    Import users from txt (bot export)
    """
    option_list = BaseCommand.option_list + (
        make_option('--group',
            action='store',
            dest='group_id',
            default=False,
            help='Attach users to group'),
        ) + (
        make_option('--file',
            action='store',
            dest='fname',
            default=False,
            help='Source file'),
        )

    def handle_noargs(self, **options):
        # theandersonband default
        # id  - 1
        print options["group_id"]
        group = SocialGroup.objects.get(pk=options["group_id"])
        group_id = group.id
        group_name = group.name

        
        
        with open(options["fname"]) as f:
            content = f.readlines()

        # sys.exit()

        for user in content:
            print user.rstrip()
            user_obj, created = SocialUser.objects.get_or_create(social_id = user.rstrip())
            print "created: %s"%created
            user_obj.social_groups.add(group)
            # user_obj.first_name = user["first_name"]
            # user_obj.last_name = user["last_name"]
            user_obj.save()


