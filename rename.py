import glob, os

files = glob.glob('filtered/*.jpg')

for i, old_name in enumerate(files):
    new_name = "filtered/{0:03d}.jpg".format(i + 1)
    os.rename(old_name, new_name)
    print(old_name + "→" + new_name)

files = glob.glob('raw/*.jpg')

for i, old_name in enumerate(files):
    new_name = "raw/{0:03d}.jpg".format(i + 1)
    os.rename(old_name, new_name)
    print(old_name + "→" + new_name)