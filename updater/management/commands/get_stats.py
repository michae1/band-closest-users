import datetime
import json
from users.models import SocialUser, SocialGroup
from django.core.management.base import NoArgsCommand, BaseCommand
from optparse import make_option
import requests
import sys
from django.db.models import Count
import math

def cosine_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v1)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)


def get_vector(obj_metrics, vector_tpl):
    '''
    obj_metrics = [2,3,4] - ids
    vector_tpl = [1,2,3,4,5,6,7]
    returns [0,1,1,1,0,0,0]
    '''
    result = []
    for x in vector_tpl:
        if x in obj_metrics:
            result.append(1)
        else:
            result.append(0)

    return result            

def get_possible_user(possible_users,vector_tpl,ref_vectors,good_similarity, test_run = False):
    candidate_users = []
    for pu in possible_users:
        ug = [x.id for x in pu.social_groups.all()]
        u_vector = get_vector(ug, vector_tpl)
        if test_run:
            u_vector[0] = 0
            
        max_sim = None
        for rv in ref_vectors:
            similarity = cosine_similarity(u_vector, rv)
            if not max_sim:
                max_sim = similarity
            if max_sim and max_sim<similarity:
                max_sim = similarity    

        # print max_sim        
        if max_sim > good_similarity:
            candidate_users.append(pu.social_id) 

    return candidate_users        

class Command(NoArgsCommand):
    help = """
    Get closest to group
    """
    option_list = BaseCommand.option_list + (
        make_option('--group',
            action='store',
            dest='group_id',
            default=False,
            help='Get closest users to group'),
        )

    def handle_noargs(self, **options):
        # theandersonband default
        # id  - 1
        good_similarity = 0.7
        group = SocialGroup.objects.get(pk=1)
        all_groups = SocialGroup.objects.all()
        vector_tpl = [x.id for x in all_groups]
        print "vector tmpl: %s"%vector_tpl
        
        print "test efficient"
        test_users = SocialUser.objects.annotate(count=Count('social_groups')).filter(social_groups__in=[1,], count__gt=2)
        test_ref_users = test_users[:200]
        test_possible_users = test_users[200:]
        print "tpu:%s"%len(test_ref_users)
        test_ref_vectors = []
        for ru in test_ref_users:
            ug = [x.id for x in ru.social_groups.all()]
            test_ref_vectors.append(get_vector(ug, vector_tpl))

        test_candidate_users = get_possible_user(test_possible_users,vector_tpl,test_ref_vectors,good_similarity,test_run=True)    
        print "eff (of 163):%s"%len(test_candidate_users)
        # sys.exit()


        ref_users = SocialUser.objects.annotate(count=Count('social_groups')).filter(social_groups__in=[1,], count__gt=3)
        possible_users = SocialUser.objects.annotate(count=Count('social_groups')).exclude(social_groups__in=[1,]).filter(count__gt=2,city_id=314)
        print "ref users: %s"%len(ref_users)
        print "possible users: %s"%len(possible_users)
        candidate_users = []
        ref_vectors = []
        for ru in ref_users:
            ug = [x.id for x in ru.social_groups.all()]
            ref_vectors.append(get_vector(ug, vector_tpl))


        candidate_users = get_possible_user(possible_users,vector_tpl,ref_vectors,good_similarity)    

        print "users"
        print len(candidate_users)
        # (for) get ref users vectors
        # for each possible candidate users get vector, 
        # get distances list
        # get median or minimum distance save 
        # return users with distance less than x
        with open('users.txt', 'wb') as outfile:
            for item in candidate_users:
                outfile.write("%s\n" % item)
            

