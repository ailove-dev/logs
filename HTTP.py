import urllib2

class Browser:
    obj = None
    def __new__(cls,*dt,**mp):
        if cls.obj is None:
            cls.obj = object.__new__(cls,*dt,**mp)
        return cls.obj

    def setCredentials( self, username, password ):
        self.username = username
        self.password = password

    def curl( self, url ):
        passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
        passman.add_password(None, url, self.username, self.password)

        authhandler = urllib2.HTTPBasicAuthHandler(passman)
        opener = urllib2.build_opener(authhandler)

        urllib2.install_opener(opener)
        pagehandle = urllib2.urlopen(url)
        return pagehandle.read()
