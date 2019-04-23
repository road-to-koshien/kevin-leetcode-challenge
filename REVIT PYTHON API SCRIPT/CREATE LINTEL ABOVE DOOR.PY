#This python script is written to be used with Dynamo.
#This script will create the lintel above each door in the whole project. 
#The input IN[0] is the distance from the edge of the door to the end of the lintel.
#The input IN[1] is family symbol (Family Type) of the Lintel beam which is defined in model.
#The input IN[2] is the door frame width.
#If you have any idea please contact me via mrkevinht@gmail.com or https://www.facebook.com/kevin.ht.16

import clr
clr.AddReference("RevitNodes")

import Revit
clr.ImportExtensions(Revit.Elements)

import System
from System.Collections.Generic import *

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument

direction = []
location = []
half = []
curve_list = []
result = []
level_list = []
distance = IN[0]
symbol = UnwrapElement(IN[1])
frame = IN[2]

doorlist = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Doors).WhereElementIsNotElementType().ToElements()
level = doc.ActiveView.GenLevel

for each in doorlist:
	x = each.Host.Location.Curve.Direction
	direction.append(x)
	y = each.Location.Point
	location.append(y)
	z = each.Symbol.get_Parameter(BuiltInParameter.DOOR_WIDTH).AsDouble()
	m = z/2 + distance/304.8
	half.append(m)
	a = each.get_Parameter(BuiltInParameter.INSTANCE_SILL_HEIGHT_PARAM).AsDouble()
	b = each.get_Parameter(BuiltInParameter.INSTANCE_HEAD_HEIGHT_PARAM).AsDouble()
	c = a + b + frame/304.8
	level_list.append(c)
i = 0
for item in location:
	p1 = location[i] + half[i]*direction[i]
	p2 = location[i] - half[i]*direction[i]
	i = i + 1
	curve = Line.CreateBound(p1, p2)
	curve_list.append(curve)

TransactionManager.Instance.EnsureInTransaction(doc)

k = 0
for one in curve_list:
	beam = doc.Create.NewFamilyInstance(one, symbol, level, Structure.StructuralType.Beam)
	beam.get_Parameter(BuiltInParameter.Z_OFFSET_VALUE).Set(level_list[k])
	beam.get_Parameter(BuiltInParameter.BEAM_V_JUSTIFICATION).Set(2)
	k = k + 1
	result.append(beam)

TransactionManager.Instance.TransactionTaskDone()

OUT = result