def packer(name = None, **kwargs):
    print(kwargs)

def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi NoName!")

packer(name="Will", num = 7, spanish_inquisition = None)
unpacker(**{"last_name": "Davis", "first_name": "William"})