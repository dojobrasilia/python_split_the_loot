class Splitter(object):
    def split(self,loot,pirate_number):
        #loot.sort()
        
        ret = self.init_answer(pirate_number)
        
        bucket_size = self.compute_bucket_size(loot, pirate_number)
        
        i =0
        pirate_index = 0
        loot_size = loot.__len__()
        while i < loot_size:
            pirate_bucket = ret[pirate_index]
            sum = 0 
            while sum < bucket_size:
                gem = loot.pop(0)
                if sum+gem > bucket_size:
                    loot.append(gem)
                else:
                    pirate_bucket.append(gem)
                    sum += gem
                    i += 1
            pirate_bucket.sort()
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
    
    def compute_bucket_size(self, loot, pirate_number):
        bucket_size = 0
        for l in loot:
            bucket_size += l
        return bucket_size/pirate_number