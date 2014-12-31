function LimitDrag(id){
	Drag.call(this,id);//构造函数伪装继承属性
}

for(var i in Drag.prototype){
	LimitDrag.prototype[i]=Drag.prototype[i];//把父级的方法继承过来
}
LimitDrag.prototype.fnMove=function (ev){//覆盖从父级继承过来的fnMove方法
			var oEvent=ev||event;
			var l=oEvent.clientX-this.disX;
			var t=oEvent.clientY-this.disY;

			if (l<0) {
				l=0;
			}
			else if (l>document.documentElement.clientWidth-this.oDiv.offsetWidth) {
				l=document.documentElement.clientWidth-this.oDiv.offsetWidth;
			};

			if (t<0) {
				t=0;
			}
			else if (t>document.documentElement.clientHeight-this.oDiv.offsetHeight) {
				t=document.documentElement.clientHeight-this.oDiv.offsetHeight;
			};

			this.oDiv.style.left=l+'px';
			this.oDiv.style.top=t+'px';
		}