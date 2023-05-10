import sys

python_version_major           = 3
python_version_minor_min       = 6

voxl_esc_bin_version_major_min = 1
voxl_esc_bin_version_minor_min = 1

print('Detected Python version : %s' %(sys.version))

if (sys.version_info.major != python_version_major):
    print("Python%d.%d or later is a requirement for this application" %(python_version_major,python_version_minor_min))
    print(sys.version_info)
    sys.exit(1)

if (sys.version_info.minor < python_version_minor_min):
    print("Python%d.%d or later is a requirement for this application" %(python_version_major,python_version_minor_min))
    print(sys.version_info)
    sys.exit(1)

def voxl_esc_setup_paths():
    sys.path.append('./voxl-esc-tools-bin/python%d.%d'%(sys.version_info.major,sys.version_info.minor))
    sys.path.append('./voxl-esc-tools-bin/python%d.%d/libesc' %(sys.version_info.major,sys.version_info.minor))

    #print(sys.path)

voxl_esc_setup_paths()
from libesc import *
voxl_esc_bin_version = get_voxl_esc_tools_bin_version()
print('Found voxl-esc tools bin version: %s' % (voxl_esc_bin_version))

voxl_esc_bin_version_int = voxl_esc_bin_version.split('.')
voxl_esc_bin_version_major = int(voxl_esc_bin_version_int[0])
voxl_esc_bin_version_minor = int(voxl_esc_bin_version_int[1])

if voxl_esc_bin_version_major < voxl_esc_bin_version_major_min:
    print('ERROR: voxl_esc_bin_version_major  %d < %d' %(voxl_esc_bin_version_major, voxl_esc_bin_version_major_min))
    sys.exit(1)

if voxl_esc_bin_version_minor < voxl_esc_bin_version_minor_min:
    print('ERROR: voxl_esc_bin_version_minor  %d < %d' %(voxl_esc_bin_version_minor, voxl_esc_bin_version_minor_min))
    sys.exit(1)
