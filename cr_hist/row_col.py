from todloop.event import LoadRaDec, NPixelFilter, CoeffFilter
from todloop.base import TODLoop
from todloop.routines import DataLoader, Logger
from routines import SpatialStudy


loop = TODLoop()
loop.add_tod_list("../data/s16_pa3_list.txt")
# loop.add_skip([340, 956, 1041, 1066, 1099, 1609])  # problematic ones
loop.add_routine(DataLoader(input_dir="../outputs/s16_pa3_list/events/", output_key="events"))
loop.add_routine(NPixelFilter(min_pixels=1, max_pixels=20, input_key="events", output_key="events"))
# loop.add_routine(CoeffFilter(min_coeff=0.9, input_key="events", output_key="events"))
# loop.add_routine(Logger(input_key="events"))

loop.add_routine(SpatialStudy(input_key="events"))
loop.run(0, 5000)
