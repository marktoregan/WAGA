from src import journeystop as js, journeystops as jss, ev_charge_point as evp
from datetime import datetime
import random


CLASS JourneyAllocation(object):
ENDCLASS


    FUNCTION __init__(self, **kwargs):
         journey_allocation <- []
         journey_manager <- kwargs.get("journey_manager")
         available_stops <- kwargs.get("available_stops")
        for i in range(0,  journey_manager.number_of_stops()):
             journey_allocation.append(None)
    ENDFUNCTION

        ENDFOR

    FUNCTION set_individual(self, stops):
        stop <- random.choice(stops)
        RETURN stop
    ENDFUNCTION


    FUNCTION get_allocation(self, allocation_pos):
        RETURN  journey_allocation[allocation_pos]
    ENDFUNCTION


    FUNCTION set_allocation(self, allocation_pos, allocation):
         journey_allocation[allocation_pos] <- allocation
        # fitness <- 0.0
        # distance <- 0
    ENDFUNCTION


    FUNCTION save_allocation(self, index, stop):
         journey_allocation[index] <- stop
    ENDFUNCTION


    FUNCTION generate_individual(self):
        for i in range(0,  journey_manager.number_of_stops()):
            allocated_stop <-  set_individual( available_stops)
             save_allocation(i, allocated_stop)
    ENDFUNCTION

        ENDFOR

    FUNCTION get_journey(self, index):
        journey <-  journey_manager[index]
        RETURN journey
    ENDFUNCTION


    FUNCTION get_fitness(self):
        arrival_time <- datetime.now()
        journeys <- list()
        for index, allocation in enumerate( journey_allocation):
            ev_point <- evp.EvChargePoint(id=allocation)
            journey <-  journey_manager.get_journey(index)
            journey.stop <- [allocation]
            stop <- js.JourneyStop(ev_point_id=allocation,
                                        arrival_time=arrival_time,
                                        departure_time=0,
                                        wait_time=0,
                                        charge_time=ev_point.charge_time_required)
            journeys.append(stop)
        ENDFOR
        jstops <- jss.JourneyStops()
        charge_time_total <- jstops.total_time_of_stops(journeys)
        journey_time <- 0
        for index, alloc in enumerate( journey_allocation):
            a_journey <-  journey_manager.get_journey(index)
            journey_time += a_journey.distance()
        ENDFOR
        total_time <- charge_time_total + journey_time
        RETURN total_time
    ENDFUNCTION


    FUNCTION journey_allocation_size(self):
        RETURN len( journey_allocation
