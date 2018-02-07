class CalculateTotalMinutes:

    def __init__(self, ev_points):
        self.ev_points = ev_points

    def _sum_of_normal_numbers(self, n):
        num_sum = n*(n+1)/2
        return num_sum

    def _count_ev_points(self, ev_points_lst):
        ev_point_dict = {i:ev_points_lst.count(i) for i in ev_points_lst}
        return ev_point_dict

    def _total_minutes(self, my_dict, wait_time):
        ls = [self._sum_of_normal_numbers(x) for x in my_dict.values()]
        total = sum(ls)
        collective_wait_timeval = total * wait_time
        return collective_wait_timeval

    def total_wait_time(self, wait_time):
        dct = self._count_ev_points(self.ev_points)
        total = self._total_minutes(dct, wait_time)
        return total
