import urllib2

def getDef():
	con = urllib2.urlopen("http://www.defconwarningsystem.com/");
	content = con.read();
	pos = content.find("This is the DEFCON Warning System.")
	pos2 = content.find("<", pos)
	stat = content[pos:pos2]
	status = stat.replace("&nbsp;", "")
	return status

print getDef()
