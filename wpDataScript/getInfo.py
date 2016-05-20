import base

for key in base.versions:
    print key,"-----------"
    print "version: ", base.versions[key]
    print "users  : ", ",".join(base.users[key])
    print "-----------"
