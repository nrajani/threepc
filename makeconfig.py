print "#this is property file"
N=7;
print "binPath="
print "logPath="
print "NumProcesses="+str(N)
#procNum=2
for n in xrange(N):
	print "host"+str(n)+"=localhost"

initialport=11234;
for n in xrange(N):
	print "port"+str(n)+"="+str(initialport+n)

