#region Namespaces
using System.Collections.Generic;
using Autodesk.Revit.ApplicationServices;
using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using Autodesk.Revit.UI.Selection;
using System.Linq;
using Autodesk.Revit.DB.Structure;
#endregion

namespace dimthepsan
{
    [Transaction(TransactionMode.Manual)]
    public class Command : IExternalCommand
    {
        public Result Execute(
          ExternalCommandData commandData,
          ref string message,
          ElementSet elements)
        {  
            UIApplication uiapp = commandData.Application;
            UIDocument uidoc = uiapp.ActiveUIDocument;
            Application app = uiapp.Application;
            Document doc = uidoc.Document;

            string thongbao = "";
            bool kiemtrathep = true;
            bool kiemtraopening = true;
            List<Opening> flooropening = null;
            List<Rebar> getrebar = null;
            List<Line> listline = new List<Line>();
            List<Line> linedim = new List<Line>();
            List<Rebar> floorrebar = null;
            List<Rebar> vidu = new List<Rebar>();
            List<Rebar> checkedrebar = new List<Rebar>();
           

            Reference pick = uidoc.Selection.PickObject(ObjectType.Element, "Chon phan tu san");
            Element floor = doc.GetElement(pick);
            var rebardata = Autodesk.Revit.DB.Structure.RebarHostData.GetRebarHostData(floor);
            getrebar = rebardata.GetRebarsInHost().Cast<Autodesk.Revit.DB.Structure.Rebar>().ToList();
            if (getrebar.Count == 0)
            {
                kiemtrathep = false;
                thongbao = "Phan tu san nay khong co thep. Vui long them thep hoac chon san khac";
            }

            if (kiemtrathep)
            {
                BoundingBoxXYZ b = floor.get_BoundingBox(doc.ActiveView);
                Outline outline = new Outline(b.Min, b.Max);
                BoundingBoxIntersectsFilter bbfilter = new BoundingBoxIntersectsFilter(outline);
                FilteredElementCollector collector = new FilteredElementCollector(doc).WherePasses(bbfilter).OfCategory(BuiltInCategory.OST_FloorOpening);
                flooropening = collector.WhereElementIsNotElementType().Cast<Autodesk.Revit.DB.Opening>().ToList();
                if (flooropening.Count == 0)
                {
                    kiemtraopening = false;
                    thongbao = "San nay khong co opening. Xin vui long them opening hoac chon san khac";
                }
            }
            if (kiemtrathep && kiemtraopening)
            {
                foreach (Opening line in flooropening)
                {
                    foreach (Line l in line.BoundaryCurves)
                    {
                        listline.Add(l);
                    }
                }
                List<Line> result = removeduplicate(listline);
  
               foreach (Rebar r in getrebar)
                {
                    List<Curve> rebarcurve = r.GetCenterlineCurves(false, false, false, MultiplanarOption.IncludeAllMultiplanarCurves, 0).ToList();
                    if (rebarcurve.Count > 1)
                    {
                        continue;
                    }
                    else
                    {
                        vidu.Add(r);
                    }
                }
               foreach (Rebar r in vidu)
                {
                    bool check = true;
                    foreach (Line l in result)
                    {
                        var j = r.GetCenterlineCurves(false, false, false, MultiplanarOption.IncludeAllMultiplanarCurves, 0).First() as Line;
                        if (System.Math.Abs(j.Direction.DotProduct(l.Direction)) < 0.01)
                        {
                            check = false;
                            break;
                        }
                    }
                    if (check == true)
                    {
                        checkedrebar.Add(r);
                    }
                  
                }
                List<Point> listpoint = new List<Point>();
                List<double> listx = new List<double>();
                List<double> listy = new List<double>();
                double maxZ_global = float.NegativeInfinity;
                double minZ_global =  float.PositiveInfinity;
                foreach (Line l in listline)
                {
                    XYZ p1 = l.GetEndPoint(0);
                    XYZ p2 = l.GetEndPoint(1);
                    double maxZ_cur = System.Math.Max((p1.Z), p2.Z);
                    if (maxZ_cur > maxZ_global)
                    {
                        maxZ_global = maxZ_cur;
                    }
                    double minZ_cur = System.Math.Min((p1.Z), (p2.Z));
                    if (minZ_cur < minZ_global)
                    {
                        minZ_global = minZ_cur;
                    }
                    listx.Add(p1.X);
                    listx.Add(p2.X);
                    listy.Add(p1.Y);
                    listy.Add(p2.Y);
                }
                XYZ maxpoint = new XYZ(listx.Max(), listy.Max(), maxZ_global);
                XYZ minpoint = new XYZ(listx.Min(), listy.Min(), maxZ_global);
                double mindistance = float.PositiveInfinity;
                Rebar res = null;
                foreach (Rebar r in checkedrebar)
                {
                    var linerebar = r.GetCenterlineCurves(false, false, false, MultiplanarOption.IncludeAllMultiplanarCurves, 0).First() as Line;
                    double min_cur = linerebar.Distance(maxpoint);
                    if (min_cur < mindistance)
                    {
                        mindistance = min_cur;
                        res = r;
                    }
                }
                if (res != null)
                {
                    using (Transaction tx = new Transaction(doc))
                    {
                        tx.Start("Transaction Name");
                    Options ropt = new Options();
                    ropt.ComputeReferences = true;
                    ropt.View = doc.ActiveView;

                    ropt.IncludeNonVisibleObjects = false;

                        Line liner = res.GetCenterlineCurves(false, false, false, MultiplanarOption.IncludeAllMultiplanarCurves, 0).First() as Line;

                        
                    ReferenceArray secRefarr = new ReferenceArray();

                    //get References for end points of rebars Line
                    secRefarr.Append((liner as Line).GetEndPointReference(0));
                    secRefarr.Append((liner as Line).GetEndPointReference(1));
                        //XYZ p1 = liner.GetEndPoint(0);
                        //XYZ p2 = liner.GetEndPoint(1);
                        //ReferenceArray ra = new ReferenceArray();
                        //    //Line dimension = Line.CreateBound(p1, p2);
                        //    //Line dimensionoffset =  dimension.CreateOffset(-3, XYZ.BasisZ) as Line;
                        //DetailLine line1 = doc.Create.NewDetailCurve(doc.ActiveView, liner) as DetailLine;
                        //ra.Append(liner.Reference);

                        //    var k = liner.Reference;
                        //    foreach (var ki in liner.Reference)
                        //    {

                        //    }
                        Dimension dim = doc.Create.NewDimension(doc.ActiveView, liner, secRefarr);
                        
                        tx.Commit();
                    }
                }
            }
            return Result.Succeeded;
        }

        public List<Line> removeduplicate(List<Line> listline)
        {
            if (listline.Count() == 1)
            {
                return listline;
            }
            List<Line> result = new List<Line>();
            result.Add(listline[0]);
            for (int i = 1; i < listline.Count(); i++)
            {
                bool check = true;
                foreach (Line l in result)
                {
                    if (System.Math.Abs(l.Direction.DotProduct(listline[i].Direction)) > 0.01)
                    {
                        check = false;
                        break;
                    }
                }
                if (check == true)
                {
                    result.Add(listline[i]);
                }
            }
            return result;
        }
    }
}

