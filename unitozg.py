# -*- coding: utf-8 -*-
def replace(input);

    output = input 
    output = re.sub(u'\u103A',u'\u1039',output)
    output = re.sub(u'\u103B',u'\u103A',output)
    output = re.sub(u'\u103C',u'\u103B',output)
    output = re.sub(u'\u103D',u'\u103C',output)
    output = re.sub(u'\u103E',u'\u103D',output)
    output = re.sub(u'\u103F',u'\u1086',output)
    output = re.sub(u'(\u103D\u103E)',u'\u108A',output)
    output = re.sub(u'(\u103B\u1039)',u'\u105A', output)

return output

def precompose(input):

    output = input
    output = re.sub(u'(\u1004\u103A\u1039)',u'\u1064',output)
    output = re.sub(u'(\u1064)(\u1000-\u1021)',u'\\2\\1',output)

def logical2visual(input):

    output = input 
    output = re.sub(u'(\u1039\u1000)',u'\u1060',output)
    output = re.sub(u'(\u1039\u1001)',u'\u1061',output)
    output = re.sub(u'(\u1039\u1002)',u'\u1062',output)
    output = re.sub(u'(\u1039\u1003)',u'\u1063',output)
    output = re.sub(u'(\u1039\u1005)',u'\u1065',output)
    output = re.sub(u'(\u1039\u1006)',u'\u1066',output)
    output = re.sub(u'(\u1039\u1007)',u'\u1068',output)
    output = re.sub(u'(\u1039\u1008)',u'\u1069',output)
    output = re.sub(u'(\u1039\u1009)',u'\u106A',output)
    output = re.sub(u'(\u1039\u100A)',u'\u106B',output)
    output = re.sub(u'(\u1039\u100B)',u'\u106C',output)
    output = re.sub(u'(\u1039\u100C)',u'\u106D',output)
    output = re.sub(u'(\u1039\u100D)',u'\u106E',output)
    output = re.sub(u'(\u1039\u100E)',u'\u106F',output)
    output = re.sbu(u'(\u1039\u100F)',u'\u1070',output)
    output = re.sub(u'(\u1039\u1010)',u'\u1071',output)
    output = re.sub(u'(\u1039\u1011)',u'\u1072',output)
    output = re.sub(u'(\u1039\u1012)',u'\u1073',output)
    output = re.sub(u'(\u1039\u1013)',u'\u1074',output)
    output = re.sub(u'(\u1039\u1014)',u'\u1075',output)
    output = re.sub(u'(\u1039\u1015)',u'\u1076',output)
    output = re.sub(u'(\u1039\u1016)',u'\u1077',output)
    output = re.sub(u'(\u1039\u1017)',u'\u1078',output)
    output = re.sub(u'(\u1039\u1018)',u'\u1079',output)
    output = re.sub(u'(\u1039\u1019)',u'\u107A',output)
    output = re.sub(u'(\u1039\u101A)',u'\u107B',output)
    output = re.sub(u'(\u1039\u101B)',u'\u107C',output)
    output = re.sub(u'(\u1039\u101C)',u'\u1085',output)
    
    return output 

def shape(input):

    output = input 
    output = re.sub(u'\u103A([\u103C\u103D])',u'\u107D\\1',output)
    output = re.sub(u'\u103B([\u1000])',u'\u107E\\1',output)
    output = re.sub(u'\u103B([\u1000-\u1021])([\u102D\u102E\u1036])',u'\u107F\\1',output)
    output = re.sub(u'\u107E([\u1000-\u1021])([\u102D\u102E\u102F])',u'\u1080\\1',output)
    output = re.sub(u'([\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084])([\u1000-\u1021])((?:[\u102D\u102E\u1036])?)\u102F', u'\\1\\2\\3\u1033', output)
    output = re.sub(u'([\u103A\u107D])((?:[\u102D\u102E\u1036])?)\u102F', u'\\1\\2\u1033', output)
    output = re.sub(u'\u103D\u102F', u'\u1088', output)
    output = re.sub(u'([\u1060-\u1063])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u1065-\u1069])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u106C\u106D])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u1070-\u107C])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u1085\u1093])((?:[\u102D\u102E])?)\u102f', u'\\1\\2\u1033', output)
    output = re.sub(u'([\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084])([\u1000-\u1021])((?:[\u102D\u102E\u1036])?)\u1030',u'\\1\\2\\3\u1034', output)
    output = re.sub(u'([\u103A\u107D])((?:[\u102D\u102E\u1036])?)\u1030', u'\\1\\2\u1034', output)
    output = re.sub(u'([\u1014\u101B\u1008\u1030\u1033\u102F\u1034])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1094', output)
    output = re.sub(u'([\u103C\u103D\u108A\u1088])((?:[\u1032\u1036])?)\u1037', u'\\1\\2\u1095', output)
    output = re.sub(u'\u1014([\u103C\u103D\u108A])', u'\u108F\\1', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1060-\u1063])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1065-\u1069])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u106C\u106D])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1070-\u107C])', u'\u108F\\1\\2', output)
    output = re.sub(u'\u1014((?:[\u102D\u102E])?)([\u1085\u1093])', u'\u108F\\1\\2', output)
    output = re.sub(u'(\u100A)\u103D', u'\\1\u1087', output)
    output = re.sub(u'\u1009(\u1039)', u'\u1025\\1', output)
    output = re.sub(u'\u101B\u108A', u'\u1090\u108A', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1060-\u1063])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1065-\u1069])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u106C\u106D])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1070-\u107C])', u'\u1090\\1\\2', output)
    output = re.sub(u'\u101B((?:[\u102D\u102E])?)([\u1085\u1093])', u'\u1090\\1\\2', output)


	return output

def convert(input):
    output = input

    output = precompose(output)
    output = replace(output)
    output = logical2visual(output)
    output = shape(output)
    return output
