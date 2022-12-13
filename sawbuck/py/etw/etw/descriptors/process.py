#!/usr/bin/python2.6
# Copyright 2010 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Generated event descriptor file for a MOF event class.

DO NOT EDIT. This is an ETW event descriptor file generated by
sawbuck/py/etw/generate_descriptor.py. It contains event descriptions for
MOF GUID {3d6fa8d0-fe05-11d0-9dda-00c04fd7ba7c}.
"""


from etw.descriptors import event
from etw.descriptors import field


class Event(object):
  GUID = '{3d6fa8d0-fe05-11d0-9dda-00c04fd7ba7c}'
  Start = (GUID, 1)
  End = (GUID, 2)
  DCStart = (GUID, 3)
  DCEnd = (GUID, 4)
  PerfCtr = (GUID, 32)
  PerfCtrRundown = (GUID, 33)
  InSwap = (GUID, 35)
  Defunct = (GUID, 39)


class Process_V1(event.EventCategory):
  GUID = Event.GUID
  VERSION = 1

  class TypeGroup1(event.EventClass):
    _event_types_ = [Event.DCEnd,
                     Event.DCStart,
                     Event.End,
                     Event.Start]
    _fields_ = [('PageDirectoryBase', field.Pointer),
                ('ProcessId', field.UInt32),
                ('ParentId', field.UInt32),
                ('SessionId', field.UInt32),
                ('ExitStatus', field.Int32),
                ('UserSID', field.Sid),
                ('ImageFileName', field.String)]


class Process_V0(event.EventCategory):
  GUID = Event.GUID
  VERSION = 0

  class TypeGroup1(event.EventClass):
    _event_types_ = [Event.DCEnd,
                     Event.DCStart,
                     Event.End,
                     Event.Start]
    _fields_ = [('ProcessId', field.Pointer),
                ('ParentId', field.Pointer),
                ('UserSID', field.Sid),
                ('ImageFileName', field.String)]


class Process(event.EventCategory):
  GUID = Event.GUID
  VERSION = 3

  class TypeGroup1(event.EventClass):
    _event_types_ = [Event.DCEnd,
                     Event.DCStart,
                     Event.Defunct,
                     Event.End,
                     Event.Start]
    _fields_ = [('UniqueProcessKey', field.Pointer),
                ('ProcessId', field.UInt32),
                ('ParentId', field.UInt32),
                ('SessionId', field.UInt32),
                ('ExitStatus', field.Int32),
                ('DirectoryTableBase', field.Pointer),
                ('UserSID', field.Sid),
                ('ImageFileName', field.String),
                ('CommandLine', field.WString)]


class Process_V2(event.EventCategory):
  GUID = Event.GUID
  VERSION = 2

  class TypeGroup2(event.EventClass):
    _event_types_ = [Event.PerfCtr,
                     Event.PerfCtrRundown]
    _fields_ = [('ProcessId', field.UInt32),
                ('PageFaultCount', field.UInt32),
                ('HandleCount', field.UInt32),
                ('Reserved', field.UInt32),
                ('PeakVirtualSize', field.Int32),
                ('PeakWorkingSetSize', field.Int32),
                ('PeakPagefileUsage', field.Int32),
                ('QuotaPeakPagedPoolUsage', field.Int32),
                ('QuotaPeakNonPagedPoolUsage', field.Int32),
                ('VirtualSize', field.Int32),
                ('WorkingSetSize', field.Int32),
                ('PagefileUsage', field.Int32),
                ('QuotaPagedPoolUsage', field.Int32),
                ('QuotaNonPagedPoolUsage', field.Int32),
                ('PrivatePageCount', field.Int32)]

  class TypeGroup1(event.EventClass):
    _event_types_ = [Event.DCEnd,
                     Event.DCStart,
                     Event.Defunct,
                     Event.End,
                     Event.Start]
    _fields_ = [('UniqueProcessKey', field.Pointer),
                ('ProcessId', field.UInt32),
                ('ParentId', field.UInt32),
                ('SessionId', field.UInt32),
                ('ExitStatus', field.Int32),
                ('UserSID', field.Sid),
                ('ImageFileName', field.String),
                ('CommandLine', field.WString)]

  class TypeGroup3(event.EventClass):
    _event_types_ = [Event.InSwap]
    _fields_ = [('DirectoryTableBase', field.Pointer),
                ('ProcessId', field.UInt32)]
