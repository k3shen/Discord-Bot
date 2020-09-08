import constants
import itertools
from lib.exceptions import *

def nicenum(num):
    # Convert into num shorthand
    if num > 999999:
        num=str(round(num/1000000,2))
        num+='M'
    elif num <= 999999 and num > 999:
        num=str(round(num/1000,2))
        num+='K'
    else:
        num = str(round(num,2))
    return num

def closest(lst, k): 
    # Find skill level
    for level in lst:
        if level > k:
            return lst.index(level)-1
    return lst.index(level)

def skillbonus(skill, level):
    # Find skill bonus
    if skill == 'combat':
        return level*0.5
    elif skill == 'foraging' or skill == 'alchemy' or skill == 'enchanting' or skill == 'mining':
        if level > 14:
            return 14+2*(level-14)
        else:
            return level
    elif skill == 'farming' or skill == 'fishing':
        if level > 25:
            return 67 + 5*(level-25)
        elif level > 19 and level < 26:
            return 43 + 4*(level-19)
        elif level < 20 and level > 14:
            return 28 + 3*(level-14)
        else:
            return 2*level
    else:
        return None


def allskills(uuid,profilejson):
    # Info for all skills
    skills = ['combat','foraging','farming','fishing','alchemy','enchanting','mining','taming','runecrafting','carpentry']
    out = {}
    totalxp = 0
    skillsum = 0
    for skill in skills:
        try:
            xp = profilejson['profile']['members'][uuid]['experience_skill_{}'.format(skill)]
        except KeyError:
            return APIDisabledError
        if skill != 'runecrafting':
            level = closest(list(itertools.accumulate(constants.skillxp)),xp)
            if level < 50:
                nextxp = nicenum(xp-sum(constants.skillxp[:level+1]))
                nextlevel = nicenum(constants.skillxp[level+1])
            else:
                nextxp = None
                nextlevel = None
        else:
            level = closest(list(itertools.accumulate(constants.runecraftingxp)),xp)
            if level < 24:
                nextxp = nicenum(xp-sum(constants.runecraftingxp[:level+1]))
                nextlevel = nicenum(constants.runecraftingxp[level+1])
            else:
                nextxp = None
                nextlevel = None

        bonus = skillbonus(skill, level)
        totalxp += xp

        if skill != 'runecrafting' and skill != 'carpentry':
            skillsum += level


        out[skill.capitalize()] = [level, nicenum(xp), nextxp, nextlevel, bonus]
    
    out['True Skill Average'] = skillsum/8
    out['Total Skill XP'] = nicenum(totalxp)
    out['runetotal'] = nicenum(sum(constants.runecraftingxp))
    out['skilltotal'] = nicenum(sum(constants.skillxp))

    return out

def cleanskills(uuid,profilejson):
    # Info for all skills
    skills = ['combat','foraging','farming','fishing','alchemy','enchanting','mining','taming','runecrafting','carpentry']
    out = {}
    totalxp = 0
    skillsum = 0
    for skill in skills:
        try:
            xp = profilejson['profile']['members'][uuid]['experience_skill_{}'.format(skill)]
        except KeyError:
            return APIDisabledError
        if skill != 'runecrafting':
            level = closest(list(itertools.accumulate(constants.skillxp)),xp)
            if level < 50:
                nextxp = xp-sum(constants.skillxp[:level+1])
                nextlevel = constants.skillxp[level+1]
            else:
                nextxp = None
                nextlevel = None
        else:
            level = closest(list(itertools.accumulate(constants.runecraftingxp)),xp)
            if level < 24:
                nextxp = xp-sum(constants.runecraftingxp[:level+1])
                nextlevel = constants.runecraftingxp[level+1]
            else:
                nextxp = None
                nextlevel = None

        bonus = skillbonus(skill, level)
        totalxp += xp

        if skill != 'runecrafting' and skill != 'carpentry':
            skillsum += level


        out[skill.capitalize()] = [level, xp, nextxp, nextlevel, bonus]
    
    out['True Skill Average'] = skillsum/8
    out['Total Skill XP'] = totalxp
    out['runetotal'] = sum(constants.runecraftingxp)
    out['skilltotal'] = sum(constants.skillxp)

    return out

def sortbyxp(lst,indexlst,offset):
    if lst == []:
        return lst
    minval = min(indexlst)-1
    out = []
    for x in range(0,len(lst)):
        idx = indexlst.index(max(indexlst))
        level = closest([0]+list(itertools.accumulate(constants.petxp[offset:offset+99])),indexlst[idx])+1
        indexlst[idx] = minval
        out.append('[Lvl {}] {}'.format(level,lst[idx]))
    return out

def allpets(petsjson):
    pets = []
    rarities = {'LEGENDARY':20,'EPIC':16,'RARE':11,'UNCOMMON':6,'COMMON':0}
    for rarity in rarities:
        compare = []
        index = []
        for pet in petsjson:
            if pet['tier'] == rarity:
                compare.append('{} {}'.format(rarity.capitalize(),pet['type'].capitalize()))
                index.append(pet['exp'])
        pets += sortbyxp(compare,index,rarities[rarity])

    out = []
    allpets = pets
    petnames = []
    for pet in pets:
        c = pet.split(' ')
        petnames.append(c[-1])
    for pet in petnames:
        if pet not in out:
            out.append(pet)
        else:
            out.append(0)
    for item in out:
        if item != 0:
            out[out.index(item)] = pets[out.index(item)]
    out = [x for x in out if not isinstance(x, int)]
    
    for pet in allpets:
        allpets[allpets.index(pet)] = pet.replace('_',' ').title()

    petscore = 0
    for pets in out:
        if 'Legendary' in pets:
            petscore+=5
        elif 'Epic' in pets:
            petscore+=4
        elif 'Rare' in pets:
            petscore+=3
        elif 'Uncommon' in pets:
            petscore+=2
        elif 'Common' in pets:
            petscore+=1
                              
    return {'pets':allpets,'upets':out,'petscore':petscore}