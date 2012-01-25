class Splitter(object):
    def split(self,loot,pirate_number):
        loot.sort()
        ret = self.init_answer(pirate_number)

        i =0
        while i < loot.__len__():
            ret[i%pirate_number].append(loot[i])
            i += 1
            
        print loot
        print ret
        return ret
    
    def init_answer(self,pirate_number):
        ret = []
        i = 0
        #init answer
        while i < pirate_number:
            ret.append([])
            i += 1
        return ret
    