import zipfile
import sys
import paradoxparser
import datetime

TECH_SCORE_MULTIPLIER = 10
ACCUMULATED_ENERGY_MULTIPLIER = 0.1
ACCUMULATED_MINERALS_MULTIPLIER = 0.05
ACCUMULATED_INFLUENCE_MULTIPLIER = 0.05
ENERGY_PRODUCTION_MULTIPLIER = 2
MINERAL_PRODUCTION_MULTIPLIER = 1.5
INFLUENCE_PRODUCTION_MULTIPLIER = 1
NUM_SUBJECTS_MULTIPLIER = 30
MILITARYPOWER_MULTIPLIER = 0.03
NUM_COLONIES_MULTIPLIER = 15
NUM_PLANETS_MULTIPLIER = 0.01

class Country:

    def __init__(self):
        self.name = ''
        self.score = 0
        self.techscore = 0
        self.currentenergy = 0
        self.currentminerals = 0
        self.currentinfluence = 0
        self.energyproduction = 0
        self.mineralproduction = 0
        self.influenceproduction = 0
        self.numsubjects = 0
        self.militarypower = 0
        self.numcolonies = 0
        self.numplanets = 0
        self.numarmies = 0
        self.type = ''
        self.id = '0'
        
    def calcscore(self):
        self.score += TECH_SCORE_MULTIPLIER * self.techscore
        self.score += ACCUMULATED_ENERGY_MULTIPLIER * self.currentenergy
        self.score += ACCUMULATED_MINERALS_MULTIPLIER * self.currentminerals
        self.score += ACCUMULATED_INFLUENCE_MULTIPLIER * self.currentinfluence
        self.score += ENERGY_PRODUCTION_MULTIPLIER * self.energyproduction
        self.score += MINERAL_PRODUCTION_MULTIPLIER * self.mineralproduction
        self.score += INFLUENCE_PRODUCTION_MULTIPLIER * self.influenceproduction
        self.score += NUM_SUBJECTS_MULTIPLIER * self.numsubjects
        self.score += MILITARYPOWER_MULTIPLIER * self.militarypower
        self.score += NUM_COLONIES_MULTIPLIER * self.numcolonies
        self.score += NUM_PLANETS_MULTIPLIER * self.numplanets

def makeLedgerForSave(path, basePath):
    save = zipfile.ZipFile(path)
    f = save.open('gamestate')
    s = str(f.read(), 'utf-8')
    f.close()
    
    
    playertaglocation = s.find('player={')
    playertag = s[playertaglocation:s.find('}', playertaglocation)]
    
    
    playercountry = playertag[playertag.find('country=')+len('country='):playertag.find('}')].strip()
    
    countries = s[s.find('country={'):]

    t = 1
    cdata = []
    csdata = ''
    instring = False
    for i in range(len('country={') + 1, len(countries)):
        if countries[i] == '{' and not instring:
            if (t == 1):
                csdata = ''
                k = countries[i-1]
                j = i-1
                while(k != '\t'):
                    csdata = k + csdata
                    j -= 1
                    k = countries[j]
            t += 1
        elif countries[i] == '}' and not instring:
            t -= 1
            if (t == 1):
                cdata.append(csdata + '}')
        elif countries[i] == '"':
            instring = not instring
        
        csdata += countries[i]
        if (t == 0):
            countries = countries[:i+1]
            break
    
    
    result = paradoxparser.psr.parse(countries)
    

    country_raw_data = result[0][1]

    
    ret = ''
    
    retlist = []
    
    contactlist = []
    
    bgcolor = False

    num = 1
    
    for i in country_raw_data:
        if (i[1] != 'none'):
            
            ret2 = ''
            isUs = False
            if (i[0] == playercountry):
                isUs = True
                contactlist.append(i[0])
                relman_part = paradoxparser.paradox_dict_get_child_by_name(i[1], 'relations_manager')
                if (relman_part is not None):
                    for j in relman_part:
                        countryid = paradoxparser.paradox_dict_get_child_by_name(j[1], 'country')
                        commun = paradoxparser.paradox_dict_get_child_by_name(j[1], 'communications')
                        if (commun != None):
                            contactlist.append(countryid)
                            
            country = Country()
            
            country.id = i[0]
            
            namepart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'name')
            if (namepart is not None):
                country.name = namepart.replace('"', '')

            techpart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'tech_status')
            if (techpart is not None):
                country.techscore = sum(int(j[1]) for j in techpart if j[0] == 'level')

            militarypowerpart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'military_power')
            if (militarypowerpart is not None):
                country.militarypower = float(militarypowerpart)

            empiretype = paradoxparser.paradox_dict_get_child_by_name(i[1], 'type')
            if (empiretype is not None):
                country.type = empiretype.replace('"', '')
                if (country.type not in ('fallen_empire', 'default')):
                    continue
            
            subjectpart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'subjects')
            if (subjectpart is not None):
                country.numsubjects = len(subjectpart)

            armiespart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'owned_armies')
            if (armiespart is not None):
                country.numarmies = len(armiespart)

            planetsspart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'controlled_planets')
            if (planetsspart is not None):
                country.numplanets = len(planetsspart)

            controlledplanetsspart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'owned_planets')
            if (controlledplanetsspart is not None):
                country.numcolonies = len(controlledplanetsspart)

            modulespart = paradoxparser.paradox_dict_get_child_by_name(i[1], 'modules')
            if (modulespart is not None):
                economymodule = paradoxparser.paradox_dict_get_child_by_name(modulespart, 'standard_economy_module')
                if (economymodule is not None):
                    resourcesmodule = paradoxparser.paradox_dict_get_child_by_name(economymodule, 'resources')
                    if (resourcesmodule is not None):
                        energy = paradoxparser.paradox_dict_get_child_by_name(resourcesmodule, 'energy')
                        if (energy is not None):
                            if (type(energy) == str):
                                country.currentenergy = float(energy)
                            else:
                                country.currentenergy = float(energy[0])
                                
                        minerals = paradoxparser.paradox_dict_get_child_by_name(resourcesmodule, 'minerals')
                        if (minerals is not None):
                            if (type(minerals) == str):
                                country.currentminerals = float(minerals)
                            else:
                                country.currentminerals = float(minerals[0])
                                
                        influence = paradoxparser.paradox_dict_get_child_by_name(resourcesmodule, 'influence')
                        if (influence is not None):
                            if (type(influence) == str):
                                country.currentinfluence = float(influence)
                            else:
                                country.currentinfluence = float(influence[0])
                                
                    lastmonthmodule = paradoxparser.paradox_dict_get_child_by_name(economymodule, 'last_month')
                    if (lastmonthmodule is not None):
                        energy = paradoxparser.paradox_dict_get_child_by_name(lastmonthmodule, 'energy')
                        if (energy is not None):
                            if (type(energy) == str):
                                country.energyproduction = float(energy)
                            else:
                                country.energyproduction = float(energy[0])
                                
                        minerals = paradoxparser.paradox_dict_get_child_by_name(lastmonthmodule, 'minerals')
                        if (minerals is not None):
                            if (type(minerals) == str):
                                country.mineralproduction = float(minerals)
                            else:
                                country.mineralproduction = float(minerals[0])
                                
                        influence = paradoxparser.paradox_dict_get_child_by_name(lastmonthmodule, 'influence')
                        if (influence is not None):
                            if (type(influence) == str):
                                country.influenceproduction = float(influence)
                            else:
                                country.influenceproduction = float(influence[0])

            country.calcscore()
            if (bgcolor):
                ret2 += '<tr align=center bgcolor="#113348">'
            else:
                ret2 += '<tr align=center>'

            ret2 += '<td><font color="#bbbbbb">%s</font></td>' % num
            if (isUs):
                ret2 += '<td hiddenvalue=%s><font color="#bbbbbb">&#9733;</font></td>' % num
            else:
                ret2 += '<td hiddenvalue=%s><font color="#bbbbbb">&nbsp;</font></td>' % num
            ret2 += '<td><font size=3 color="#bbbbbb">%s</font></td>' % country.name
            ret2 += '<td><font color="#bbbbbb">{:10.2f}</font></td>'.format(country.score)
            ret2 += '<td><font color="#bbbbbb">{:10.2f}</font></td>'.format(country.militarypower)
            ret2 += '<td><font color="#bbbbbb">%d</font></td>' % country.techscore
            ret2 += '<td><font color="#bbbbbb">%d</font></td>' % country.numcolonies
            ret2 += '<td><font color="#bbbbbb">%d</font></td>' % country.numplanets
            ret2 += '<td><font color="#bbbbbb">%d</font></td>' % country.numsubjects

            production = ('{:10.1f}'.format(country.energyproduction)).strip()
            if (country.energyproduction >= 0):
                netincome = '<td><font color="#21a914">+%s</font></td>' % production
            else:
                netincome = '<td><font color="#d62114">%s</font></td>' % production
            ret2 += '<td><font color="#bbbbbb">{:10.2f}</font></td>'.format(country.currentenergy) + netincome


            production = ('{:10.1f}'.format(country.mineralproduction)).strip()
            if (country.mineralproduction >= 0):
                netincome = '<td><font color="#21a914">+%s</font></td>' % production
            else:
                netincome = '<td><font color="#d62114">%s</font></td>' % production
            ret2 += '<td><font color="#bbbbbb">{:10.2f}</font></td>'.format(country.currentminerals) + netincome

            production = ('{:10.1f}'.format(country.influenceproduction)).strip()
            if (country.influenceproduction >= 0):
                netincome = '<td><font color="#21a914">+%s</font></td>' % production
            else:
                netincome = '<td><font color="#d62114">%s</font></td>' % production
            ret2 += '<td><font color="#bbbbbb">{:10.2f}</font></td>'.format(country.currentinfluence) + netincome

            
            ret2 += '</tr>'
            retlist.append((country.id, ret2))
            num += 1
            bgcolor = not bgcolor
##            print(country.name)
##            print(country.techscore)
##            print(country.militarypower)
##            print(country.type)
##            print(country.numsubjects)
##            print(country.numarmies)
##            print(country.numplanets)
##            print(country.numcolonies)
##            print(country.currentenergy)
##            print(country.currentminerals)
##            print(country.currentinfluence)
##            print(country.energyproduction)
##            print(country.mineralproduction)
##            print(country.influenceproduction)
    retlist2 = []
    
    for i in retlist:
        if (i[0] in contactlist):
            retlist2.append(i[1])
    
    ret = "\n".join(retlist2)
    return ret

