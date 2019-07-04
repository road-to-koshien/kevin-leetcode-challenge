#Script to create the beam above door:
import clr
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

import Revit
clr.ImportExtensions(Revit.Elements)

import System
from System.Collections.Generic import *

clr.AddReference("RevitAPI")
import Autodesk
from Autodesk.Revit.DB import *
from Autodesk.Revit.DB.Structure import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

doc = DocumentManager.Instance.CurrentDBDocument
view = doc.ActiveView
floor = UnwrapElement(IN[0])

kiemtrathep = True
kiemtraopening = True
mpo = MultiplanarOption.IncludeAllMultiplanarCurves

rebardata = Autodesk.Revit.DB.Structure.RebarHostData.GetRebarHostData(floor);
getrebar = rebardata.GetRebarsInHost()

tmp  = []
tmp2 = []

if len(getrebar) == 0:
	kiemtrathep = False
	thongbao = "San nay khong co thep. Vui long chon san khac hoac them thep"

b = floor.get_BoundingBox(doc.ActiveView);
outline = Outline(b.Min, b.Max);
bbfilter = BoundingBoxIntersectsFilter(outline);
flooropening = FilteredElementCollector(doc).WherePasses(bbfilter).OfCategory(BuiltInCategory.OST_FloorOpening).WhereElementIsNotElementType().ToElements()

if len(flooropening) == 0:
	kiemtraopening = False
	thongbao = "San nay khong co opening. Vui long them opening hoac chon san khac"
	
if kiemtrathep and kiemtraopening:
	openingline = flooropening[0].BoundaryCurves
	for rebar in getrebar:
		rebarShp = rebar.GetShapeDrivenAccessor()
		numOfBars = rebar.NumberOfBarPositions
		quantity = rebar.Quantity
		layoutRule = rebar.LayoutRule
		check = True
		if numOfBars > 1:
			for i in range(numOfBars):
				if not rebar.IsBarHidden(view,i):
					posTransform = rebarShp.GetBarPositionTransform(i)
					revitCurve = [rebar.GetCenterlineCurves(0,0,0,mpo,0)]
				tmp2.append(revitCurve[0][0])
				for each in openingline:
					if each.Direction.DotProduct(revitCurve[0][0].Direction) == 0:
						check = False
						break
		else:
			revitCurve = [rebar.GetCenterlineCurves(0,0,0,mpo,0)]
			for each in openingline:
				if each.Direction.DotProduct(revitCurve[0][0].Direction) == 0:
					check = False
					break
		if check:
			tmp.append(rebar)
OUT = tmp