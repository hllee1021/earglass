import services
from pprint import pprint

# pprint(services.admin.get_waiting_dsf_by_estimator_index(3))
# pprint(services.admin.get_completed_dsf_by_estimator_index(3))
# for i in range(4):
#     pprint(services.admin.get_participating_tasks_by_user_index(i))
pprint(services.admin.get_origin_data_types(3, 'task1'))