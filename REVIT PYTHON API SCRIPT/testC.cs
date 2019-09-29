using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


double[] listtest = {3,1,2,5,0};
string[] stringtest = {"a","b","c","d","e"};

var orderedZip = listtest.Zip(stringtest, (x, y) => new { x, y }).OrderBy(pair => pair.x).ToList();

// docs = docs.OrderBy(d => docsIds.IndexOf(d.Id)).ToList();

Console.WriteLine()