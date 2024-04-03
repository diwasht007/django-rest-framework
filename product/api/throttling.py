from rest_framework.throttling import UserRateThrottle

class ReviewDetailThrottle(UserRateThrottle):
    scope = 'throtteling_for_review_detail'

class ReviewListThrottle(UserRateThrottle):
    scope = 'throtteling_for_review_list'

