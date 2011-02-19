#!/usr/bin/env python
srcdir = "."
blddir = "build"
VERSION = "0.0.1"

def set_options(opt):
  opt.tool_options("compiler_cxx")

def configure(conf):
  conf.check_tool("compiler_cxx")
  conf.check_tool("node_addon")

def build(bld):
  ### bsd_glob
  bsd_glob = bld.new_task_gen("cxx")
  bsd_glob.source = "deps/glob/glob.c"
  bsd_glob.includes = "deps/glob/"
  bsd_glob.name = "bsd_glob"
  bsd_glob.target = "bsd_glob"
  bsd_glob.install_path = None

  obj = bld.new_task_gen("cxx", "shlib", "node_addon")
  obj.add_objects = "bsd_glob"
  obj.includes = """
    src/
    deps/glob/
  """
  obj.cxxflags = ["-D_FILE_OFFSET_BITS=64", "-D_LARGEFILE_SOURCE"]
  obj.target = "glob"
  obj.source = "src/glob.cc"
