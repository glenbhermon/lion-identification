
# ======================================================== #
# File automagically generated by GUI2Exe version 0.5.3
# Copyright: (c) 2007-2012 Andrea Gavana
# ======================================================== #

# Let's start with some default (for me) imports...

from distutils.core import setup
from py2exe.build_exe import py2exe

import glob
import os
import zlib
import shutil

# Remove the build folder
shutil.rmtree("build", ignore_errors=True)


class Target(object):
    """ A simple class that holds information on our executable file. """
    def __init__(self, **kw):
        """ Default class constructor. Update as you need. """
        self.__dict__.update(kw)
        

# Ok, let's explain why I am doing that.
# Often, data_files, excludes and dll_excludes (but also resources)
# can be very long list of things, and this will clutter too much
# the setup call at the end of this file. So, I put all the big lists
# here and I wrap them using the textwrap module.

data_files = [('LeoSpy', ['C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-crop-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-edit-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-new-picture-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-refresh-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-rotate-left-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-rotate-right-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-save-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\ai-search-txt.png',
                          'C:\\Users\\Glen\\Documents\\Visual Studio 2015\\Projects\\LeoSpy\\LeoSpy\\logo.png'])]

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['api-ms-win-core-errorhandling-l1-1-0.dll', 'api-ms-win-core-errorhandling-l1-1-1.dll',
                'api-ms-win-core-file-l1-2-1.dll', 'api-ms-win-core-heap-l2-1-0.dll',
                'api-ms-win-core-libraryloader-l1-2-1.dll', 'api-ms-win-core-processthreads-l1-1-2.dll',
                'api-ms-win-core-profile-l1-1-0.dll', 'api-ms-win-core-registry-l1-1-0.dll',
                'api-ms-win-core-string-l1-1-0.dll', 'api-ms-win-core-string-l2-1-0.dll',
                'api-ms-win-eventing-provider-l1-1-0.dll', 'api-ms-win-security-base-l1-2-0.dll',
                'libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll',
                'MSVCP90.dll', 'tcl84.dll', 'tk84.dll', 'api-ms-win-core-libraryloader-l1-2-0.dll',
                'api-ms-win-core-localization-l1-2-1.dll', 'api-ms-win-core-sysinfo-l1-2-1.dll',
                'api-ms-win-core-synch-l1-2-0.dll', 'api-ms-win-core-heap-l1-2-0.dll',
                'api-ms-win-core-handle-l1-1-0.dll', 'api-ms-win-core-io-l1-1-1.dll',
                'api-ms-win-core-com-l1-1-1.dll', 'api-ms-win-core-memory-l1-1-2.dll',
                'api-ms-win-core-version-l1-1-1.dll', 'api-ms-win-core-version-l1-1-0.dll']
icon_resources = []
bitmap_resources = []
other_resources = []


# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

# No custom code added


# Ok, now we are going to build our target class.
# I chose this building strategy as it works perfectly for me :-D

GUI2Exe_Target_1 = Target(
    # what to build
    script = "LeoSpy.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources,
    dest_base = "LeoSpy",    
    version = "0.1",
    company_name = "No Company",
    copyright = "No Copyrights",
    name = "Py2Exe Sample File",
    
    )

# No custom class for UPX compression or Inno Setup script

# That's serious now: we have all (or almost all) the options py2exe
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.
                    
setup(

    # No UPX or Inno Setup

    data_files = data_files,

    options = {"py2exe": {"compressed": 1, 
                          "optimize": 0,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 1,
                          "dist_dir": "newdist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },

    zipfile = None,
    console = [],
    windows = [GUI2Exe_Target_1],
    service = [],
    com_server = [],
    ctypes_com_server = []
    )

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

# No post-compilation code added


# And we are done. That's a setup script :-D

