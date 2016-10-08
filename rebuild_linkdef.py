#! /usr/bin/env python

from __future__ import print_function

import argparse
import os
import shutil
import re

def fullPath(path):
    return os.path.realpath(os.path.abspath(os.path.expanduser(path)))

def RebuildLinkDef():
    base_dir = os.path.dirname(fullPath(__file__))
    classes_h = os.path.join(base_dir,"src","classes.h")
    classes_def_xml = os.path.join(base_dir,"src","classes_def.xml")
    link_def = os.path.join(base_dir,"src","CombinedLimit_LinkDef.h")
    shutil.copy(classes_h, link_def)
    with open(link_def, "a") as fout, open(classes_def_xml, "r") as fin:
        fout.write('\n\n#ifdef __CINT__\n')
        fout.write('#pragma link off all globals;\n')
        fout.write('#pragma link off all classes;\n')
        fout.write('#pragma link off all functions;\n')

        regex = re.compile(r'.*?<.*?(class|function).*?name.*?=.*?"(?:function |)(.*?)".*?/>.*?')
        for line in fin:
            match = regex.search(line)
            if not match: continue
            obj_type = match.group(1)
            obj_name = match.group(2)
            fout.write('#pragma link C++ '+obj_type+' '+obj_name)
            if obj_type == "class":
                fout.write("+;\n")
            else:
                fout.write(";\n")
        fout.write('#endif\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Regenerates src/CombinedLimit_LinkDef.h",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    args = parser.parse_args()

    RebuildLinkDef()
