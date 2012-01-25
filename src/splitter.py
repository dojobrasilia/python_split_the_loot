class Splitter(object):
    def split(self,loot,pirate_number):
        ret = []
        i = 0
        while i < pirate_number:
            j = 0
            ret.append([])
            while j < (loot.__len__()/pirate_number):
                ret[i].append(loot[i+j])
                j += 1
            i += 1
        return ret