import datetime
import json
from users.models import SocialUser, SocialGroup
from django.core.management.base import NoArgsCommand, BaseCommand
from optparse import make_option
import requests
import sys


class Command(NoArgsCommand):
    help = """
    Import groups from txt (bot export)
    """
    option_list = BaseCommand.option_list + (
        make_option('--group',
            action='store',
            dest='group_id',
            default=False,
            help='Attach groups'),
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
        with open(options["fname"]) as f:
            content = f.readlines()

        # sys.exit()

        for user in content:
            print user.rstrip()
            group_obj, created = SocialGroup.objects.get_or_create(name = user.rstrip())
            print "created: %s"%created
            

