
# -*- coding: utf-8 -*-
import re


def convert(input):

        tallAA = u'\u102B'
	AA = u'\u102C'
	vi = u'\u102D'
	# lone gyi tin
	ii = u'\u102E'
	u = u'\u102F'
	uu = u'\u1030'
	ve = u'\u1031'
	ai = u'\u1032'
	ans = u'\u1036'
	db = u'\u1037'
	visarga = u'\u1038'

	asat = u'\u103A'

	ya = u'\u103B'
	ra = u'\u103C'
	wa = u'\u103D'
	ha = u'\u103E'
	zero = u'\u1040'

	output = input
        output = output.replace(u'\u106A', u'\u1009')
	output = re.sub(u'[\u103D\u1087]', u'\u103E',output)
	output = re.sub(u'\u103C', u'\u103D',output)
	output = re.sub(u'[\u103B\u107E\u107F\u1080\u1081\u1082\u1083\u1084]',u'\u103C',output)
	output = re.sub(u'[\u103A\u107D]',u'\u103B',outpu)
	output = re.sub(u'[\u106B]',u'\u100A',output)
	output = re.sub(u'[\u108F]',u'\u1014',output)
	output = re.sub(u'\u1097', u'\u100B',output)
	output = re.sub(u'\u1092', u'\u100C',output)
	output = re.sub(u'\u1090', u'\u101B',output)
	output = re.sub(u'\u1033', u'\u102F',output)
	output = re.sub(u'\u1034', u'\u1030',output)
	output = re.sub(u'\u1086', u'\u103F',output)
	output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038',output)
	output = re.sub(u'\u1039', u'\u103A',output)
	output = re.sub(u'[\u1037\u1094\u1095]', u'\u1037',output)
	output = re.sub(u'\u1086', u'\u103F',output)
	output = re.sub(u'\u1039', u'\u103A',output)
	output = re.sub(u'\u105A', u'\u102B\u103A',output)
	output = re.sub(u'\u108A', u'\u103D\u103E',output)
	output = re.sub(u'\u1088', u'\u103E\u102F',output)
	output = re.sub(u'\u1089', u'\u103E\u1030',output)
	output = re.sub(u'\u104E', u'\u104E\u1004\u103A\u1038',output)
	output = re.sub(u'\u1060', u'\u1039\u1000',output)
	output = re.sub(u'\u1061', u'\u1039\u1001',output)
	output = re.sub(u'\u1062', u'\u1039\u1002',output)
	output = re.sub(u'\u1063', u'\u1039\u1003',output)
	output = re.sub(u'\u1065', u'\u1039\u1005',output)
	output = re.sub(u'[\u1066\u1067]', u'\u1039\u1006',output)
	output = re.sub(u'\u1068', u'\u1039\u1007',output)
	output = re.sub(u'\u1069', u'\u1039\u1008',output)
	output = re.sub(u'\u106C', u'\u1039\u100B',output)
	output = re.sub(u'\u106D', u'\u1039\u100C',output)
	output = re.sub(u'\u106E', u'\u100D\u1039\u100D',output)
	output = re.sub(u'\u106F', u'\u100E\u1039\u100D',output)
        output = re.sub(u'(\u103A)(\u1037)', u"\\2\\1", output)
	output = re.sub(u'\u1070', u'\u1039\u100F',output)
	output = re.sub(u'[\u1071\u1072]', u'\u1039\u1010',output)
	output = re.sub(u'[\u1073\u1074]', u'\u1039\u1011',output)
	output = re.sub(u'\u1075', u'\u1039\u1012',output)
	output = re.sub(u'\u1076', u'\u1039\u1013',output)
	output = re.sub(u'\u1077', u'\u1039\u1014',output)
	output = re.sub(u'\u1078', u'\u1039\u1015',output)
	output = re.sub(u'\u1079', u'\u1039\u1016',output)
	output = re.sub(u'\u107A', u'\u1039\u1017',output)
	output = re.sub(u'[\u107B\u1093]', u'\u1039\u1018',output)
	output = re.sub(u'\u107C', u'\u1039\u1019',output)
	output = re.sub(u'\u1085', u'\u1039\u101C',output)
	output = re.sub(u'((?:\u1031)?)((?:\u103C)?)([\u1000-\u1021])((?:\u103D)?)((?:\u103E)?)((?:\u102C)?)((?:\u103B)?)', u"\\3\\2\\7\\4\\5\\1\\6",output)
	output = re.sub(u'([\u1000-\u1021])\u1064', u'\u1064\\1',output)
	output = re.sub(u'\u1064', u'\u1004\u103A\u1039',output)
        output = output.replace(u'\u103A\u1037', u'\u1037\u103A')
	output = output.replace(u'\u1075', u'\u1039\u1012')
        return output 
