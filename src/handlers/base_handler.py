# Copyright 2024 Volvo Cars
# SPDX-License-Identifier: Apache-2.0
from abc import ABC, abstractmethod

from src.models.base import BaseCpuUsageInfo, BootTimeInfo, SystemMemory, SystemUptimeInfo
from src.models.super import CpuList, MemoryList, ProcessCpuList, ProcessMemoryList


class BaseHandlerException(Exception):
    pass


class BaseHandler(ABC):
    @abstractmethod
    def get_boot_time(self) -> BootTimeInfo:
        """
        Retrieves the boot time in seconds

        :return: An object containing the system boot time in seconds
        :rtype: BootTimeInfo
        """

    def get_system_uptime(self) -> SystemUptimeInfo:
        """
        Retrieves the system uptime in seconds

        :return: An object containing the system uptime in seconds
        :rtype: SystemUptimeInfo
        """

    @abstractmethod
    def get_cpu_usage(self, interval: float) -> BaseCpuUsageInfo:
        """
        Retrieves basic CPU usage information over a specified interval.

        Parameters:
        interval (float): The time interval in seconds over which the CPU usage is measured. Defaults to 0.3 seconds.

        :return: An object containing basic information about the CPU usage.
        :rtype: BaseCpuUsageInfo

        Special Cases:
        --------------
        For Linux-based systems, the function returns a LinuxCpuModeUsageInfo wrapper model,
        which provides more detailed information about the CPU usage, including mode-specific usage statistics.
        """

    def get_mem_usage(self) -> SystemMemory:
        """
        Retrieves current memory usage information.


        :return: An object containing detailed information about the system's memory usage,
        including total, used, free, and available memory.
        :rtype: SystemMemory

        Special Cases:
        --------------
        For Linux-based systems, the function returns a ExtendedMemoryInfo wrapper model
        for the mem field, which provides more detailed information about memory usage, as well as swap.
        """

    @abstractmethod
    def get_cpu_usage_proc_wise(self, interval: float, **kwargs) -> ProcessCpuList:
        """
        Retrieves CPU usage information for all processes over a specified interval.

        Parameters:
        interval (float): The time interval in seconds over which the CPU usage is measured.

        :return: A list containing ProcessInfo objects with process information and cpu load samples.
        :rtype: ProcessCpuList
        """

    @abstractmethod
    def get_mem_usage_proc_wise(self, **kwargs) -> ProcessMemoryList:
        """
        Retrieves current memory usage information.

        :return: A list containing ProcessInfo objects with process information and memory samples.
        :rtype: ProcessMemoryList
        """

    @abstractmethod
    def start_cpu_measurement(self, interval: float) -> None:
        """
        Starts a new thread which takes CPU measurements at specified intervals.

        :param interval: The time interval, in seconds, between successive CPU measurements.
                        The interval must be a positive number.
        :type interval: float

        :raises PosixHandlerException: If a CPU measurement thread is already running.

        :example:
            To start collecting CPU measurements every 2 seconds::

                handler.start_cpu_measurement(2)

        .. note::
            The collected measurements are stored internally and can be retrieved
            by calling :meth:`stop_cpu_measurement`, which stops the measurement thread
            and returns the collected data.

        .. seealso::
            :meth:`stop_cpu_measurement` - Method to stop the CPU measurement thread and retrieve results.
        """

    @abstractmethod
    def start_mem_measurement(self, interval: float) -> None:
        """
        Starts a new thread which takes memory measurements at specified intervals.

        :param interval: The time interval, in seconds, between successive memory measurements.
                        The interval must be a positive number.
        :type interval: float

        :raises PosixHandlerException: If a memory measurement thread is already running.

        :example:
            To start collecting memory measurements every 2 seconds::

                handler.start_mem_measurement(2.0)

        .. note::
            The collected measurements are stored internally and can be retrieved
            by calling :meth:`stop_mem_measurement`, which stops the measurement thread
            and returns the collected data.

        .. seealso::
            :meth:`stop_mem_measurement` - Method to stop the memory measurement thread.
        """

    @abstractmethod
    def stop_cpu_measurement(self) -> CpuList:
        """
        Stops an existing CPU measuring thread and returns the results.

        :return: A list of CPU measurement results.
        :rtype: CpuList

        :raises PosixHandlerException: If a CPU measurement thread is not running.

        .. seealso::
            :meth:`start_cpu_measurement` - Method to start the CPU measurement thread.
        """

    @abstractmethod
    def stop_mem_measurement(self) -> MemoryList:
        """
        Stops an existing memory measuring thread and returns the results.

        :return: A list of memory measurement results.
        :rtype: MemoryList

        :raises PosixHandlerException: If a memory measurement thread is not running.

        .. seealso::
            :meth:`start_mem_measurement` - Method to start the memory measurement thread.
        """

    @abstractmethod
    def start_cpu_measurement_proc_wise(self, interval: float) -> None:
        """
        Starts a new thread which takes CPU measurements for each running process at specified intervals.

        :param interval: The time interval, in seconds, between successive CPU measurements.
                        The interval must be a positive number.
        :type interval: float

        :raises PosixHandlerException: If a CPU measurement thread is already running.

        :example:
            To start collecting CPU measurements every 2 seconds::

                handler.start_cpu_measurement_proc_wise(2.0)

        .. note::
            The collected measurements are stored internally and can be retrieved
            by calling :meth:`stop_cpu_measurement_proc_wise`, which stops the measurement thread
            and returns the collected data.

        .. seealso::
            :meth:`stop_cpu_measurement_proc_wise` - Method to stop the CPU measurement thread and retrieve results.
        """

    @abstractmethod
    def start_mem_measurement_proc_wise(self, interval: float) -> None:
        """
        Starts a new thread which takes memory measurements for each running process at specified intervals.

        :param interval: The time interval, in seconds, between successive memory measurements.
                        The interval must be a positive number.
        :type interval: float

        :raises PosixHandlerException: If a memory measurement thread is already running.

        :example:
            To start collecting memory measurements every 2 seconds::

                handler.start_mem_measurement_proc_wise(2.0)

        .. note::
            The collected measurements are stored internally and can be retrieved
            by calling :meth:`stop_mem_measurement_proc_wise`, which stops the measurement thread
            and returns the collected data.

        .. seealso::
            :meth:`stop_mem_measurement_proc_wise` - Method to stop the memory measurement thread.
        """

    @abstractmethod
    def stop_cpu_measurement_proc_wise(self) -> ProcessCpuList:
        """
        Stops an existing CPU measuring thread and returns the results.

        :return: A list of CPU measurement results.
        :rtype: ProcessCpuList

        :raises PosixHandlerException: If a CPU measurement thread is not running.

        .. seealso::
            :meth:`start_cpu_measurement_proc_wise` - Method to start the CPU measurement thread.
        """

    @abstractmethod
    def stop_mem_measurement_proc_wise(self) -> ProcessMemoryList:
        """
        Stops an existing memory measuring thread and returns the results.

        :return: A list of memory measurement results.
        :rtype: ProcessMemoryList

        :raises PosixHandlerException: If a memory measurement thread is not running.

        .. seealso::
            :meth:`start_mem_measurement_proc_wise` - Method to start the memory measurement thread.
        """
