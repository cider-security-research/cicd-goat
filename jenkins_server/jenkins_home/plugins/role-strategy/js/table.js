/*
 * The MIT License
 *
 * Copyright (c) 2010, Manufacture Française des Pneumatiques Michelin, Thomas Maurel
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */

TableHighlighter = Class.create();
TableHighlighter.prototype = {

    initialize: function(id, decalx, decaly) {
        this.table = $(id);
        this.decalx = decalx;
        this.decaly = decaly;
        var trs = $$('#'+this.table.id+' tr');
        for (p=this.decaly;p<trs.length;++p){
            this.scan(trs[p]);
        }
    },

    scan: function(tr) {
        var element = $(tr);
        var descendants = element.getElementsByTagName('input');
        for(q=0;q<descendants.length;++q) {
            var td = $(descendants[q]);
            td.observe('mouseover', this.highlight.bind(this));
            td.observe('mouseout', this.highlight.bind(this));
        }
    },

    highlight: function(e) {
        var td = Event.element(e).parentNode;
        var tr = td.parentNode;
        var trs = $$('#'+this.table.id+' tr');
        var position = td.previousSiblings().length;

        for (p=this.decaly-1;p<trs.length;++p){
            var element = $(trs[p]);
            var num = position;
            if(p==1) num = num - this.decalx;
            element.immediateDescendants()[num ].toggleClassName('highlighted');
        }
        tr.toggleClassName('highlighted');
    }

};