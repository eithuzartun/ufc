
# -*- coding: utf-8 -*-
import re


def replace(input):

	output = input

	output = output.replace(u'\u0075', u'\u1000')
	output = re.sub(u'\u0063', u'\u1001', output)
	output = output.replace(u'\u002A', u'\u1002')
	output = re.sub(u'\u0043', u'\u1003', output)
        output = re.sub(u'\u0069', u'\u1004', output)
	output = re.sub(u'\u0070', u'\u1005', output)
	output = re.sub(u'\u0071', u'\u1006', output)
        output = re.sub(u'\u005A', u'\u1007', output)
	output = re.sub(u'\u00DA', u'\u1009', output)
	output = re.sub(u'[\u006E\u00F1]', u'\u100A', output)
	output = re.sub(u'\u0023', u'\u100B', output)
        Output = re.sub(u'\u0058', u'\u100C', output)
        Output = re.sub(u'\u0021', u'\u100D', output)
	output = re.sub(u'\u00A1', u'\u100E', output)
	output = re.sub(u'\u0050', u'\u100F', output)
	output = re.sub(u'\u0077', u'\u1010', output)
	output = re.sub(u'\u0078', u'\u1011', output)
	output = re.sub(u'\u0027', u'\u1012', output)
	output = re.sub(u'\u0022', u'\u1013', output)
	output = re.sub(u'\u0065', u'\u1014', output)
	output = re.sub(u'\u0079', u'\u1015', output)
	output = re.sub(u'\u007A', u'\u1016', output)
	output = re.sub(u'\u0041', u'\u1017', output)
	output = re.sub(u'\u0062', u'\u1018', output)
	output = re.sub(u'\u0072', u'\u1019', output)
	output = re.sub(u'\u002C', u'\u101A', output)
        output = re.sub(u'[\u0026\u00C9]', u'\u101B', output)
	output = re.sub(u'\u0076', u'\u101C', output)
        Output = re.sub(u'\0030', u'\u101D', output)
	output = re.sub(u'\u006F', u'\u101E', output)
	output = output.replace(u'\u005B', u'\u101F')
	output = re.sub(u'\u0056', u'\u1020', output)
	output = re.sub(u'\u0074', u'\u1021', output)
	output = re.sub(u'\u00A3', u'\u1023', output)
	output = re.sub(u'\u00FE', u'\u1024', output)
	output = re.sub(u'\u004F', u'\u1025', output)
	output = re.sub(u'\u007B', u'\u1027', output)
	output = re.sub(u'\u0067', u'\u102B', output)
	output = re.sub(u'\u006D', u'\u102C', output)
	output = re.sub(u'\u0064', u'\u102D', output)
	output = re.sub(u'\u0044', u'\u102E', output)
        output = re.sub(u'[\u004B\u006B]', u'\u102F', output)
	output = re.sub(u'[\u004C\u006C]', u'\u1030', output)
	output = re.sub(u'\u0061', u'\u1031', output)
	output = re.sub(u'\u004A', u'\u1032', output)
	output = re.sub(u'\u0048', u'\u1036', output)
	output = re.sub(u'[\u0055\u0059\u0068]', u'\u1037', output)
	output = re.sub(u'\u003B', u'\u1038', output)
	output = re.sub(u'\u0066', u'\u103A', output)
	output = re.sub(u'[\u00DF\u0073]', u'\u103B', output)
	output = re.sub(u'[\u0042\u004D\u004E\u0060\u006A\u007E\u00EA]', u'\u103C', output)
	output = re.sub(u'\u0047', u'\u103D', output)
	output = re.sub(u'[\u0053\u00A7]', u'\u103E', output)
	output = re.sub(u'\u00F3', u'u103F', output)
	output = output.replace(u'\u003F', u'\u104A')
	output = re.sub(u'\u002F', u'\u104B', output)
	output = re.sub(u'\u00ED', u'\u104D', output)
	output = re.sub(u'\u00A4', u'\u104E', output)
        output = output.replace(u'\u005C', u'\u104F')
        output = re.sub(u'\u00FC', u'\u104C', output)
	output = re.sub(u'\u003A', u'\u102B\u103A', output) 
	output = re.sub(u'\u0054', u'\u103D\u103E',output)
	output = re.sub(u'\u0049', u'\u103E\u102F',output)
	output = re.sub(u'\u00AA', u'\u103E\u1030',output)
	output = re.sub(u'[\u003C\003E]', u'\u103C\u103D', output)
        output = re.sub(u'\u00FB', u'\u103C\u102F', output)
	output = re.sub(u'\u0051', u'\u103B\u103E', output)
	output = re.sub(u'\u0052', u'\u103B\u103D', output)
	output = re.sub(u'\u0057', u'\u103B\u103D\u103E', output)


	return output

def visual2logical(input):
	output = input
	output = re.sub(u'((?:\u1031)?)((?:\u103C)?)([\u1000-\u1021])((?:\u103D)?)((?:\u103B)?)((?:\u103E)?)((?:\u102C)?)', u"\\3\\2\\5\\4\\6\\1\\7", output);
	return output

def decompose(input):
	output = input
	output = re.sub(u'\u00FA', u'\u1039\u1000',output)
	output = re.sub(u'\u00A9', u'\u1039\u1001',output)
	output = re.sub(u'\u00BE', u'\u1039\u1002',output)
	output = re.sub(u'\u00A2', u'\u1039\u1003',output
	output = re.sub(u'\u00F6', u'\u1039\u1005',output)
	output = re.sub(u'\u00E4', u'\u1039\u1006',output)
	output = re.sub(u'\u00C6', u'\u1039\u1007',output)
	output = re.sub(u'\u00D1', u'\u1039\u1008',output)
	output = re.sub(u'\u00B3', u'\u1039\u100B',output)
	output = re.sub(u'\u00B2', u'\u1039\u100C',output)
	output = re.sub(u'\u00D7', u'\u100D\u1039\u100D',output)
	output = re.sub(u'\u00B9', u'\u100E\u1039\u100D',output)
	output = re.sub(u'\u00D6', u'\u1039\u100F',output)
	output = re.sub(u'[\u00C5\u00E5]', u'\u1039\u1010',output)
	output = re.sub(u'[\u00A6\u00AC]', u'\u1039\u1011',output)
	output = re.sub(u'\u00B4', u'\u1039\u1012',output)
	output = re.sub(u'\u00A8', u'\u1039\u1013',output)
	output = re.sub(u'\u00E9', u'\u1039\u1014',output)
	output = re.sub(u'\u00DC', u'\u1039\u1015',output)
	output = re.sub(u'\u006E', u'\u1039\u1016',output)
	output = re.sub(u'\u00C1', u'\u1039\u1017',output)
	output = re.sub(u'\u00C7', u'\u1039\u1018',output)
	output = re.sub(u'\u00AE', u'\u1039\u1019',output)
	output = re.sub(u'\u0019', u'\u1039\u101C',output)
	#ngr_sint
	output = re.sub(u'([\u1000-\u1021])\u0046', u'\u0046\\1',output)
	output = re.sub(u'\u0046', u'\u1004\u103A\u1039',output)
	output = re.sub(u'([\u1000-\u1021])\u00D8', u'\u0046\\1\u102d', output)
	output = re.sub(u'([\u1000-\u1021])\u00D0', u'\u0046\\1\u102e', output)
	output = re.sub(u'([\u1000-\u1021])\u00F8', u'\u0046\\1\u1036', output)
	output = re.sub(u'\u00F0', u'\u102d\u1036', output)
	return output


def convert(input):

	output = input

	output = replace(input)
	output = decompose(output)
	output = visual2logical(output)

	return output
