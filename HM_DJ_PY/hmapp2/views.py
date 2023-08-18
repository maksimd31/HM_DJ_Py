import random
import logging

from django.shortcuts import render
from django.http import HttpResponse

# logger = logging.getLogger(__name__)
logger = logging.getLogger('myapp2')


# Create your views here.
def coin_flip(request):
    """
    :param request:
    :return:
    """
    # try:
    #     logger.info(f'Result')
    result = random.choice(['Орел', 'Решко'])
    logger.info(f'Выпало {str(result)}')
    return HttpResponse(result)
# except Exception as e:
#     logger.exception(f'{e}')
#     return HttpResponse('Opps')
# else:
#     logger.debug('debag')
#     return HttpResponse('Debag')


def dice_roll(request):
    result = random.randint(1, 6)
    return HttpResponse(result)


def random_number(request):
    result = random.randint(0, 100)
    return HttpResponse(result)
