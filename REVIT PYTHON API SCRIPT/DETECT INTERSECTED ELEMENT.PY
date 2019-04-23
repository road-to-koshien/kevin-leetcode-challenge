# This python script is written to use with Dynamo. The input is single Element which is selected in Revit model.
# After running, the output will indicate all the intersected elements with the element mentioned above.
# If you have any idea please contact me via mrkevinht@gmail.com or https://www.facebook.com/kevin.ht.16

import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
from System.Collections.Generic import *
clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *

doc = DocumentManager.Instance.CurrentDBDocument

input_element = UnwrapElement(IN[0])
input_normal = IN[0]
TransactionManager.Instance.EnsureInTransaction(doc)
bbbox = input_element.get_BoundingBox(doc.ActiveView)
bb_max = bbbox.Max
bb_min = bbbox.Min
opt = Options()
output = []
collector_wrap = []
outline = Outline(bb_min, bb_max)
list_category = [BuiltInCategory.OST_Floors, BuiltInCategory.OST_StructuralColumns, BuiltInCategory.OST_StructuralFraming, BuiltInCategory.OST_Walls]
get_list = List[BuiltInCategory](list_category)
fil1 = ElementMulticategoryFilter(get_list)
fil2 = BoundingBoxIntersectsFilter(outline)
filter = LogicalAndFilter(fil1, fil2)
collector = FilteredElementCollector(doc).WherePasses(filter).WhereElementIsNotElementType().ToElements()
for each in collector:
	collector_wrap.append(each.ToDSType(False))
geo_input = input_normal.Geometry()[0]
for each in collector_wrap:
	geo = each.Geometry()[0]
	if geo_input.DoesIntersect(geo) == True:
		output.append(each)
output.remove(input_normal)
if len(output) == 0:
	output = 'Khong co element nao giao'		
TransactionManager.Instance.TransactionTaskDone()

OUT = output