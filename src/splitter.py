class Splitter(object):
    def split(self,loot,pirate_number):
        loot.sort()
        
        ret = self.init_answer(pirate_number)
        
        bucket_size = 0
        for l in loot:
            bucket_size += l
        bucket_size = bucket_size/pirate_number
        
        i =0
        pirate_index = 0
        while i < loot.__len__():
            pirate_bucket = ret[pirate_index]
            sum = 0 
            while sum < bucket_size:
                pirate_bucket.append(loot[i])
                sum += loot[i]
                i += 1
            pirate_index += 1
                
        print bucket_size
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
    