from sys import exit
from cpu_create import create_processes
from cpu_fifo import do_fifo

processes=create_processes()
do_fifo(processes)