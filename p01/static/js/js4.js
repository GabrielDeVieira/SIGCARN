/*
 Highcharts JS v10.2.1 (2022-08-29)

 Exporting module

 (c) 2010-2021 Torstein Honsi

 License: www.highcharts.com/license
*/
(function(a){"object"===typeof module&&module.exports?(a["default"]=a,module.exports=a):"function"===typeof define&&define.amd?define("highcharts/modules/export-data",["highcharts","highcharts/modules/exporting"],function(n){a(n);a.Highcharts=n;return a}):a("undefined"!==typeof Highcharts?Highcharts:void 0)})(function(a){function n(a,e,c,v){a.hasOwnProperty(e)||(a[e]=v.apply(null,c),"function"===typeof CustomEvent&&window.dispatchEvent(new CustomEvent("HighchartsModuleLoaded",{detail:{path:e,module:a[e]}})))}
a=a?a._modules:{};n(a,"Extensions/ExportData/ExportDataDefaults.js",[],function(){"";return{exporting:{csv:{annotations:{itemDelimiter:"; ",join:!1},columnHeaderFormatter:null,dateFormat:"%Y-%m-%d %H:%M:%S",decimalPoint:null,itemDelimiter:null,lineDelimiter:"\n"},showTable:!1,useMultiLevelHeaders:!0,useRowspanHeaders:!0},lang:{downloadCSV:"Baixar CSV",downloadXLS:"Baixar XLS",exportData:{annotationHeader:"Annotations",categoryHeader:"Category",categoryDatetimeHeader:"DateTime"},viewData:"Ver tabela de dados",
hideData:"Ocultar tabela de dados"}}});n(a,"Extensions/DownloadURL.js",[a["Core/Globals.js"]],function(a){var e=a.isSafari,c=a.win,v=c.document,n=c.URL||c.webkitURL||c,C=a.dataURLtoBlob=function(a){if((a=a.replace(/filename=.*;/,"").match(/data:([^;]*)(;base64)?,([0-9A-Za-z+/]+)/))&&3<a.length&&c.atob&&c.ArrayBuffer&&c.Uint8Array&&c.Blob&&n.createObjectURL){var p=c.atob(a[3]),q=new c.ArrayBuffer(p.length);q=new c.Uint8Array(q);for(var k=0;k<q.length;++k)q[k]=p.charCodeAt(k);a=new c.Blob([q],{type:a[1]});
return n.createObjectURL(a)}};a=a.downloadURL=function(a,n){var q=c.navigator,k=v.createElement("a");if("string"===typeof a||a instanceof String||!q.msSaveOrOpenBlob){a="".concat(a);q=/Edge\/\d+/.test(q.userAgent);if(e&&"string"===typeof a&&0===a.indexOf("data:application/pdf")||q||2E6<a.length)if(a=C(a)||"",!a)throw Error("Failed to convert to blob");if("undefined"!==typeof k.download)k.href=a,k.download=n,v.body.appendChild(k),k.click(),v.body.removeChild(k);else try{var p=c.open(a,"chart");if("undefined"===
typeof p||null===p)throw Error("Falha ao abrir a janela");}catch(N){c.location.href=a}}else q.msSaveOrOpenBlob(a,n)};return{dataURLtoBlob:C,downloadURL:a}});n(a,"Extensions/ExportData/ExportData.js",[a["Core/Renderer/HTML/AST.js"],a["Extensions/ExportData/ExportDataDefaults.js"],a["Core/Globals.js"],a["Core/DefaultOptions.js"],a["Extensions/DownloadURL.js"],a["Core/Series/SeriesRegistry.js"],a["Core/Utilities.js"]],function(a,n,c,v,U,M,p){function e(){var b=this.getCSV(!0);O(P(b,"text/csv")||"data:text/csv,\ufeff"+
encodeURIComponent(b),this.getFilename()+".csv")}function q(){var b='<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40"><head>\x3c!--[if gte mso 9]><xml><x:ExcelWorkbook><x:ExcelWorksheets><x:ExcelWorksheet><x:Name>Ark1</x:Name><x:WorksheetOptions><x:DisplayGridlines/></x:WorksheetOptions></x:ExcelWorksheet></x:ExcelWorksheets></x:ExcelWorkbook></xml><![endif]--\x3e<style>td{border:none;font-family: Calibri, sans-serif;} .number{mso-number-format:"0.00";} .text{ mso-number-format:"@";}</style><meta name=ProgId content=Excel.Sheet><meta charset=UTF-8></head><body>'+
this.getTable(!0)+"</body></html>";O(P(b,"application/vnd.ms-excel")||"data:application/vnd.ms-excel;base64,"+w.btoa(unescape(encodeURIComponent(b))),this.getFilename()+".xls")}function k(b){var a="",d=this.getDataRows(),f=this.options.exporting.csv,A=x(f.decimalPoint,","!==f.itemDelimiter&&b?(1.1).toLocaleString()[1]:"."),g=x(f.itemDelimiter,","===A?";":","),c=f.lineDelimiter;d.forEach(function(b,f){for(var h,r=b.length;r--;)h=b[r],"string"===typeof h&&(h='"'+h+'"'),"number"===typeof h&&"."!==A&&
(h=h.toString().replace(".",A)),b[r]=h;b.length=d.length?d[0].length:0;a+=b.join(g);f<d.length-1&&(a+=c)});return a}function C(b){var a=this.hasParallelCoordinates,d=this.time,f=this.options.exporting&&this.options.exporting.csv||{},c=this.xAxis,g={},u=[],n=[],I=[],h=this.options.lang.exportData,l=h.categoryHeader,p=h.categoryDatetimeHeader,q=function(a,d,g){if(f.columnHeaderFormatter){var m=f.columnHeaderFormatter(a,d,g);if(!1!==m)return m}return a?a instanceof V?b?{columnTitle:1<g?d:a.name,topLevelColumnTitle:a.name}:
a.name+(1<g?" ("+d+")":""):a.options.title&&a.options.title.text||(a.dateTime?p:l):l},Q=function(a,b,d){var m={},g={};b.forEach(function(b){var f=(a.keyToAxis&&a.keyToAxis[b]||b)+"Axis";f=W(d)?a.chart[f][d]:a[f];m[b]=f&&f.categories||[];g[b]=f&&f.dateTime});return{categoryMap:m,dateTimeValueAxisMap:g}},X=function(a,b){return a.data.filter(function(a){return"undefined"!==typeof a.y&&a.name}).length&&b&&!b.categories&&!a.keyToAxis?a.pointArrayMap&&a.pointArrayMap.filter(function(a){return"x"===a}).length?
(a.pointArrayMap.unshift("x"),a.pointArrayMap):["x","y"]:a.pointArrayMap||["y"]},k=[],t,y=0;this.series.forEach(function(m){var r=m.xAxis,h=m.options.keys||X(m,r),A=h.length,z=!m.requireSorting&&{},u=c.indexOf(r),l=Q(m,h),e;if(!1!==m.options.includeInDataExport&&!m.options.isInternal&&!1!==m.visible){Y(k,function(a){return a[0]===u})||k.push([u,y]);for(e=0;e<A;)t=q(m,h[e],h.length),I.push(t.columnTitle||t),b&&n.push(t.topLevelColumnTitle||t),e++;var p={chart:m.chart,autoIncrement:m.autoIncrement,
options:m.options,pointArrayMap:m.pointArrayMap};m.options.data.forEach(function(b,c){var t={series:p};a&&(l=Q(m,h,c));m.pointClass.prototype.applyOptions.apply(t,[b]);b=t.x;var k=m.data[c]&&m.data[c].name;e=0;if(!r||"name"===m.exportKey||!a&&r&&r.hasNames&&k)b=k;z&&(z[b]&&(b+="|"+c),z[b]=!0);g[b]||(g[b]=[],g[b].xValues=[]);g[b].x=t.x;g[b].name=k;for(g[b].xValues[u]=t.x;e<A;)c=h[e],k=t[c],g[b][y+e]=x(l.categoryMap[c][k],l.dateTimeValueAxisMap[c]?d.dateFormat(f.dateFormat,k):null,k),e++});y+=e}});
for(e in g)Object.hasOwnProperty.call(g,e)&&u.push(g[e]);h=b?[n,I]:[I];for(y=k.length;y--;){var z=k[y][0];var J=k[y][1];var B=c[z];u.sort(function(a,b){return a.xValues[z]-b.xValues[z]});var e=q(B);h[0].splice(J,0,e);b&&h[1]&&h[1].splice(J,0,e);u.forEach(function(a){var b=a.name;B&&!Z(b)&&(B.dateTime?(a.x instanceof Date&&(a.x=a.x.getTime()),b=d.dateFormat(f.dateFormat,a.x)):b=B.categories?x(B.names[a.x],B.categories[a.x],a.x):a.x);a.splice(J,0,b)})}h=h.concat(u);K(this,"exportData",{dataRows:h});
return h}function N(a){var b=function(a){if(!a.tagName||"#text"===a.tagName)return a.textContent||"";var f=a.attributes,c="<".concat(a.tagName);f&&Object.keys(f).forEach(function(a){var b=f[a];c+=" ".concat(a,'="').concat(b,'"')});c+=">";c+=a.textContent||"";(a.children||[]).forEach(function(a){c+=b(a)});return c+="</".concat(a.tagName,">")};a=this.getTableAST(a);return b(a)}function aa(a){var b=0,c=[],f=this.options,e=a?(1.1).toLocaleString()[1]:".",g=x(f.exporting.useMultiLevelHeaders,!0);a=this.getDataRows(g);
var k=g?a.shift():null,l=a.shift(),n=function(a,b,c,f){var g=x(f,"");b="highcharts-text"+(b?" "+b:"");"number"===typeof g?(g=g.toString(),","===e&&(g=g.replace(".",e)),b="highcharts-number"):f||(b="highcharts-empty");c=R({"class":b},c);return{tagName:a,attributes:c,textContent:g}};!1!==f.exporting.tableCaption&&c.push({tagName:"caption",attributes:{"class":"highcharts-table-caption"},textContent:x(f.exporting.tableCaption,f.title.text?f.title.text:"Chart")});for(var h=0,p=a.length;h<p;++h)a[h].length>
b&&(b=a[h].length);c.push(function(a,b,c){var h=[],e=0;c=c||b&&b.length;var k=0,d;if(d=g&&a&&b){a:if(d=a.length,b.length===d){for(;d--;)if(a[d]!==b[d]){d=!1;break a}d=!0}else d=!1;d=!d}if(d){for(d=[];e<c;++e){var r=a[e];var l=a[e+1];r===l?++k:k?(d.push(n("th","highcharts-table-topheading",{scope:"col",colspan:k+1},r)),k=0):(r===b[e]?f.exporting.useRowspanHeaders?(l=2,delete b[e]):(l=1,b[e]=""):l=1,r=n("th","highcharts-table-topheading",{scope:"col"},r),1<l&&r.attributes&&(r.attributes.valign="top",
r.attributes.rowspan=l),d.push(r))}h.push({tagName:"tr",children:d})}if(b){d=[];e=0;for(c=b.length;e<c;++e)"undefined"!==typeof b[e]&&d.push(n("th",null,{scope:"col"},b[e]));h.push({tagName:"tr",children:d})}return{tagName:"thead",children:h}}(k,l,Math.max(b,l.length)));var q=[];a.forEach(function(a){for(var c=[],d=0;d<b;d++)c.push(n(d?"td":"th",null,d?{}:{scope:"row"},a[d]));q.push({tagName:"tr",children:c})});c.push({tagName:"tbody",children:q});c={tree:{tagName:"table",id:"highcharts-data-table-".concat(this.index),
children:c}};K(this,"aftergetTableAST",c);return c.tree}function ba(){this.toggleDataTable(!1)}function ca(b){(b=x(b,!this.isDataTableVisible))&&!this.dataTableDiv&&(this.dataTableDiv=da.createElement("div"),this.dataTableDiv.className="highcharts-data-table",this.renderTo.parentNode.insertBefore(this.dataTableDiv,this.renderTo.nextSibling));this.dataTableDiv&&(this.dataTableDiv.style.display=b?"block":"none",b&&(this.dataTableDiv.innerHTML=a.emptyHTML,(new a([this.getTableAST()])).addToDOM(this.dataTableDiv),
K(this,"afterViewData",this.dataTableDiv)));this.isDataTableVisible=b;var c=this.exportDivElements,d=this.options.exporting,f=d&&d.buttons&&d.buttons.contextButton.menuItems;b=this.options.lang;d&&d.menuItemDefinitions&&b&&b.viewData&&b.hideData&&f&&c&&(c=c[f.indexOf("viewData")])&&a.setElementHTML(c,this.isDataTableVisible?b.hideData:b.viewData)}function ea(){this.toggleDataTable(!0)}function P(a,c){var b=w.navigator,f=-1<b.userAgent.indexOf("WebKit")&&0>b.userAgent.indexOf("Chrome"),e=w.URL||w.webkitURL||
w;try{if(b.msSaveOrOpenBlob&&w.MSBlobBuilder){var g=new w.MSBlobBuilder;g.append(a);return g.getBlob("image/svg+xml")}if(!f)return e.createObjectURL(new w.Blob(["\ufeff"+a],{type:c}))}catch(u){}}function fa(){var a=this,c=a.dataTableDiv,d=document.querySelectorAll("thead")[0].querySelectorAll("tr")[0],f=function(a,b){return function(c,d){var f=(b?c:d).children[a].textContent;c=(b?d:c).children[a].textContent;return""===f||""===c||isNaN(f)||isNaN(c)?f.toString().localeCompare(c):f-c}};c&&d.childNodes.forEach(function(b){var d=
b.closest("table");b.addEventListener("click",function(){var e=S([],c.querySelectorAll("tr:not(thead tr)"),!0),g=S([],b.parentNode.children,!0);e.sort(f(g.indexOf(b),a.ascendingOrderInTable=!a.ascendingOrderInTable)).forEach(function(a){d.appendChild(a)});g.forEach(function(a){["highcharts-sort-ascending","highcharts-sort-descending"].forEach(function(b){a.classList.contains(b)&&a.classList.remove(b)})});b.classList.add(a.ascendingOrderInTable?"highcharts-sort-ascending":"highcharts-sort-descending")})})}
function ha(){this.options&&this.options.exporting&&this.options.exporting.showTable&&!this.options.chart.forExport&&this.viewData()}var S=this&&this.__spreadArray||function(a,c,d){if(d||2===arguments.length)for(var b=0,e=c.length,g;b<e;b++)!g&&b in c||(g||(g=Array.prototype.slice.call(c,0,b)),g[b]=c[b]);return a.concat(g||Array.prototype.slice.call(c))},da=c.doc,w=c.win,ia=v.getOptions,L=v.setOptions,O=U.downloadURL,V=M.series;c=M.seriesTypes;var D=c.arearange,E=c.gantt,F=c.map,G=c.mapbubble,H=c.treemap,
T=p.addEvent,Z=p.defined,R=p.extend,Y=p.find,K=p.fireEvent,W=p.isNumber,x=p.pick,l=[];"";return{compose:function(a){-1===l.indexOf(a)&&(l.push(a),T(a,"afterViewData",fa),T(a,"render",ha),a=a.prototype,a.downloadCSV=e,a.downloadXLS=q,a.getCSV=k,a.getDataRows=C,a.getTable=N,a.getTableAST=aa,a.hideData=ba,a.toggleDataTable=ca,a.viewData=ea);if(-1===l.indexOf(L)){l.push(L);if(a=ia().exporting)R(a.menuItemDefinitions,{downloadCSV:{textKey:"downloadCSV",onclick:function(){this.downloadCSV()}},downloadXLS:{textKey:"downloadXLS",
onclick:function(){this.downloadXLS()}},viewData:{textKey:"viewData",onclick:function(){this.toggleDataTable()}}}),a.buttons&&a.buttons.contextButton.menuItems&&a.buttons.contextButton.menuItems.push("separator","downloadCSV","downloadXLS","viewData");L(n)}D&&-1===l.indexOf(D)&&(l.push(D),D.prototype.keyToAxis={low:"y",high:"y"});E&&-1===l.indexOf(E)&&(l.push(E),E.prototype.keyToAxis={start:"x",end:"x"});F&&-1===l.indexOf(F)&&(l.push(F),F.prototype.exportKey="name");G&&-1===l.indexOf(G)&&(l.push(G),
G.prototype.exportKey="name");H&&-1===l.indexOf(H)&&(l.push(H),H.prototype.exportKey="name")}}});n(a,"masters/modules/export-data.src.js",[a["Core/Globals.js"],a["Extensions/ExportData/ExportData.js"]],function(a,e){e.compose(a.Chart)})});
//# sourceMappingURL=export-data.js.map