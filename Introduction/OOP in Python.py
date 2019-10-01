from abc import ABCMeta, abstractmethod
import BeautifulSoup
import urllib
import sys
import bleach

#################### Root Class (Abstract) ####################

class SkyThoughtCollector(object):
	__metaclass__ = ABCMeta
	baseURLString = "base_url"
	airlinesString = "air_lines"
	limitString = "limits"

    baseURl = ""
    airlines = []
    limit = 10
    
    @abstractmethod
    def collectThoughts(self):
        print "Something Wrong!! You're calling an abstract method"
        
    @classmethod
    def getConfig(self, configpath):
        #print "In get Config"
        config = {}
        conf = open(configpath)
        
        for line in conf:
            if ("#" not in line):
                words = line.strip().split('=')
                config[words[0].strip()] = words[1].strip()
 
        #print config
        self.baseURl = config[self.baseURLString]
        if config.has_key(self.airlinesString): 
            self.airlines = config[self.airlinesString].split(',')
            
        if config.has_key(self.limitString):
            self.limit = int(config[self.limitString])
            
            
        #print self.airlines
    def downloadURL(self, url):
        #print "downloading url"
        pageFile = urllib.urlopen(url)
        
        if pageFile.getcode() != 200:
            return "Problem in URL"
        pageHtml = pageFile.read()
        pageFile.close()
        return "".join(pageHtml)
        
    def remove_junk(self, arg):
        f = open('junk.txt')
        for line in f:
            arg.replace(line.strip(),'')
            return arg
        
    def print_args(self, args):
        out =''
        last = 0
        for arg in args:
            if args.index(arg) == len(args) -1:
                last = 1
                
        reload(sys)
        sys.setdefaultencoding("utf-8")
        arg = arg.decode('utf8','ignore').
e       ncode('ascii','ignore').strip()
        arg = arg.replace('\n',' ')
        arg = arg.replace('\r','')
        arg = self.remove_junk(arg)
        
        if last == 0:
            out = out + arg + '\t'
        else:
            out = out + arg    
            
        print out
        
        
        
        
####################### Airlines Chield #######################
class AirLineReviewCollector(SkyThoughtCollector):

    months = ['January', 'February', 'March', 'April', 'May','June', 'July', 
              'August', 'September', 'October', 'November','December' ]
        
    def __init__(self, configpath):
        #print "In Config"
        super(AirLineReviewCollector,self).getConfig(configpath)
    
    def parseSoupHeader(self, header):
        #print "parsing header"
        name = surname = year = month = date = country =''
        txt = header.find("h9")
        words = str(txt).strip().split(' ')
        
        for j in range(len(words)-1):   
            if words[j] in self.months:
                date = words[j-1]
                month= words[j]
                year = words[j+1]
                name = words[j+3]
                surname = words[j+4]
                
        if ")" in words[-1]:
            country = words[-1].split(')')[0]
        if "(" in country:
            country = country.split('(')[1]
        else:
            country = words[-2].split('(')[1] + country
        return (name, surname, year, month, date, country)
        
    def parseSoupTable(self, table):
        #print "parsing table"
        images = table.findAll("img")
        over_all = str(images[0]).split("grn_bar_")[1].
        split(".gif")[0]
        money_value = str(images[1]).split("SCORE_")[1].
        split(".gif")[0]
        seat_comfort = str(images[2]).split("SCORE_")[1].
        split(".gif")[0]
        staff_service = str(images[3]).split("SCORE_")[1].
        split(".gif")[0]
        catering = str(images[4]).split("SCORE_")[1].
        split(".gif")[0]
        entertainment = str(images[4]).split("SCORE_")[1].
        split(".gif")[0]

        if 'YES' in str(images[6]):
            recommend = 'YES'
        else:
            recommend = 'NO'
            
        status = table.findAll("p", {"class":"text25"})
        stat = str(status[2]).split(">")[1].split("<")[0]
        return (stat, over_all, money_value, seat_comfort,
        staff_service, catering, entertainment, recomend)
        
        
        