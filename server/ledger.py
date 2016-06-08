import zipfile
import paradoxparser


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

def makeLedgerForSave(path):
    save = zipfile.ZipFile(path)
    f = save.open('gamestate')
    s = str(f.read(), 'utf-8')
    f.close()

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

    bgcolor = False
    
    for i in country_raw_data:
        if (i[1] != 'none'):
            country = Country()
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
                ret += '<tr align=center bgcolor="#113348">'
            else:
                ret += '<tr align=center>'
            ret += '<td><font size=3 color="#bbbbbb">%s</font></td>' % country.name
            ret += '<td><font color="#bbbbbb">{:10.2f}</font></td>'.format(country.score)
            ret += '<td><font color="#bbbbbb">{:10.2f}</font></td>'.format(country.militarypower)
            ret += '<td><font color="#bbbbbb">%d/%d</font></td>' % (country.numcolonies, country.numplanets)
            ret += '<td><font color="#bbbbbb">%d</font></td>' % country.numsubjects

            if (country.energyproduction >= 0):
                netincome = '<font color="#21a914">+{:10.2f}</font>'.format(country.energyproduction)
            else:
                netincome = '<font color="#d62114">{:10.2f}</font>'.format(country.energyproduction)
            ret += '<td><font color="#bbbbbb">{:10.2f}/</font>'.format(country.currentenergy) + netincome

            if (country.mineralproduction >= 0):
                netincome = '<font color="#21a914">+{:10.1f}</font>'.format(country.mineralproduction)
            else:
                netincome = '<font color="#d62114">{:10.1f}</font>'.format(country.mineralproduction)
            ret += '<td><font color="#bbbbbb">{:10.2f}/</font>'.format(country.currentminerals) + netincome

            if (country.influenceproduction >= 0):
                netincome = '<font color="#21a914">+{:10.1f}</font>'.format(country.influenceproduction)
            else:
                netincome = '<font color="#d62114">{:10.1f}</font>'.format(country.influenceproduction)
            ret += '<td><font color="#bbbbbb">{:10.2f}/</font>'.format(country.currentinfluence) + netincome

            
            ret += '</tr>'
            
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
    return ret

