from django import template
from ..models import CostCalculator

register = template.Library()


@register.filter
def single_prime_cost(value):
    cal_list = CostCalculator.objects.filter(material=value.material.pk)

    single_material_cost = 0

    for cal in cal_list:
        single_material_cost += cal.material.cost_per_one * cal.usage

    return single_material_cost


@register.filter
def total_prime_cost():
    cal_list = CostCalculator.objects.all()

    total_cost = 0

    for cal in cal_list:
        total_cost += cal.material.cost_per_one * cal.usage

    return total_cost


@register.filter
def get_margin(cost, price):
    margin = round((1 - (int(cost) / int(price))) * 100, 2)

    return margin


@register.filter
def get_profit(cost, price):
    profit = int(price) - int(cost)

    return profit

#
# @register.filter
# def margin_cost(value):
#     # 모든 재료값을 더한 원재료 가격
#     prime_costs = value.material.total_cost
#
#     margin = (1 - (prime_costs / 2000)) * 100
#
#     return margin
