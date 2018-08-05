#!/usr/bin/python3
import argparse
import os
import json

home = os.path.expanduser('~')
configLocation = home+"/.config/AnimeUpdater"

def config_exists(location):
  if os.path.exists(location):
    if os.path.exists(location+"/cDir"):
      if os.path.exists(location+"/data"):
        return True
  return False

def init_config(location):
  os.mkdir(location)
  with open(location+"/cDir", "w") as f:
    pass
  with open(location+"/data", "w") as f:
    f.write( json.dumps({ 'watching':[], 'watched':[], 'dropped':[] }) )

def is_path_set(location):
  with open(location, "r") as f:
    if f.read() == "":
      return False
  return True

def set_path(location, where):
  with open(location, "w") as f:
    f.write(where)

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-s", "--set", help="sets anime folder", type=str)
  parser.add_argument("-r", "--remove", help="removes the show and adds it to dropped", type=str)
  parser.add_argument("-l", "--list", help="lists watching/watched/dropped anime", action="store_true")
  args = parser.parse_args()

  if args.set:
    if os.path.exists(args.set):
      set_path(configLocation+"/cDir", args.set)
    else:
      raise Warning("Path does not exist")

  if not config_exists(configLocation):
    init_config(configLocation)
  if not is_path_set(configLocation+"/cDir"):
    raise Warning("Path to Animes not set, read README.md")

  # rest of stuff
