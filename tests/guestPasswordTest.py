# File: guessPasswordTests.py
#    from chapter 1 of _Genetic Algorithms with Python_
#
# Author: Clinton Sheppard <fluentcoder@gmail.com>
# Copyright (c) 2016 Clinton Sheppard
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.  See the License for the specific language governing
# permissions and limitations under the License.

import datetime
import random
import unittest

from src import genetic


def get_fitness(guess, target):
    return sum(1 for expected, actual in zip(target, guess)
               if expected == actual)


def display(candidate, start_time):
    time_diff = datetime.datetime.now() - start_time
    print("{}\t{}\t{}".format(
        candidate.Genes, candidate.Fitness, time_diff))


class GuessPasswordTests(unittest.TestCase):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.,"

    def test_Hello_World(self):
        target = "Hello World!"
        self.guess_password(target)

    def test_For_I_am_fearfully_and_wonderfully_made(self):
        target = "For I am fearfully and wonderfully made."
        self.guess_password(target)

    def guess_password(self, target):
        start_time = datetime.datetime.now()

        def fn_get_fitness(genes):
            return get_fitness(genes, target)

        def fn_display(candidate):
            display(candidate, start_time)

        optimal_fitness = len(target)
        best = genetic.get_best(fn_get_fitness, len(target), optimal_fitness,
                                self.gene_set, fn_display)
        self.assertEqual(best.Genes, target)

    def test_Random(self):
        length = 150
        target = ''.join(random.choice(self.gene_set)
                         for _ in range(length))

        self.guess_password(target)

    def test_benchmark(self):
        genetic.Benchmark.run(self.test_Random)


if __name__ == '__main__':
    unittest.main()
