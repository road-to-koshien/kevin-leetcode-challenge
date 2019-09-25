#region Namespaces
using System;
using System.Collections.Generic;
using System.Diagnostics;
using Autodesk.Revit.ApplicationServices;
using Autodesk.Revit.Attributes;
using Autodesk.Revit.DB;
using Autodesk.Revit.UI;
using System.Text;
using System.Linq;
using Autodesk.Revit.UI.Selection;
#endregion

namespace get_part_length
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
            List<double> res = new List<double>();
            ISelectionFilter partsfilsel = new partsselectionfilter();
            IList<Reference> rels = uidoc.Selection.PickObjects(ObjectType.Element, partsfilsel, "Please pick object (parts only)");
            /*Reference rel = uidoc.Selection.PickObject(ObjectType.Element, partsfilsel, "PLEASE PICK OBJECTS (YOU CAN SELECT PART ONLY)");*/
            double val = 0;
            int count = 0;
            using (Transaction t = new Transaction(doc, "Set part length"))
            {
                t.Start();
                foreach (Reference rel in rels)
                {
                    Part tmp = doc.GetElement(rel) as Part;
                    if (checkcol(tmp))
                    {
                        val = getmaxedge(tmp);
                        Parameter param_tmp = tmp.LookupParameter("PART_LENGTH");
                        param_tmp.Set(val);
                        count++;
                        
                    }
                    if (checkbeam(tmp))
                    {
                        val = getmaxedge(tmp);
                        Parameter param_tmp = tmp.LookupParameter("PART_LENGTH");
                        param_tmp.Set(val);
                        count++;
                        
                    }
                }
                t.Commit();
            }
            message = "Number of parts which has been set length value: " + count.ToString();
            TaskDialog.Show("revit", message);
            return Result.Succeeded;
        }
        public bool checkcol(Part p)
        {
            Parameter param = p.get_Parameter(BuiltInParameter.DPART_ORIGINAL_CATEGORY);
            string a = param.AsString();
            if (a == "Structural Columns")
            {
                return true;
            }
            return false;
        }
        public bool checkbeam(Part p)
        {
            Parameter param = p.get_Parameter(BuiltInParameter.DPART_ORIGINAL_CATEGORY);
            string a = param.AsString();
            if (a == "Structural Framing")
            {
                return true;
            }
            return false;
        }
        public double getmaxedge(Part p)
        {
            Options opt = new Options();
            GeometryElement geoele = p.get_Geometry(opt);
            double max = 0;
            double tmp = 0;
            foreach (GeometryObject geoobj in geoele)
            {
                Solid geosolid = geoobj as Solid;
                if (geosolid != null)
                {
                    foreach (Edge ed in geosolid.Edges)
                    {
                        tmp = ed.ApproximateLength;
                        if (tmp > max)
                        {
                            max = tmp;
                        }
                    }
                }
            }
            return max;
        }
    }
}
public class partsselectionfilter : ISelectionFilter
{
    public bool AllowElement(Element ele)
    {
        if (ele.Category.Name == "Parts")
        {
            return true;
        }
        else
        {
            return false;
        }
    }
    public bool AllowReference(Reference rel, XYZ point)
    {
        return false;
    }
}





