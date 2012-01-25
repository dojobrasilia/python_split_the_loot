class Splitter(object):
    def split(self,loot,pirate_number):
        loot.sort()
        ret = []
        i = 0
        #init answer
        while i < pirate_number:
            ret.append([])
            i += 1
        #split the loot
        i =0
        while i < loot.__len__():
            ret[i%pirate_number].append(loot[i])
            i += 1
        print loot
        print ret
        return ret