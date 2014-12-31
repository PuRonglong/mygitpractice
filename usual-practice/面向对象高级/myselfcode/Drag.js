function Drag(id){
				var _this=this;//把this存一下,因为在事件和定时器中this会有所不同

				this.oDiv=null;
				this.disX=0;
				this.disY=0;
				this.oDiv=document.getElementById(id);

				this.oDiv.onmousedown=function(ev){
					_this.fnDown(ev);

					return false;
				}
			}
		
			Drag.prototype.fnMove=function (ev){
				var oEvent=ev||event;
				this.oDiv.style.left=oEvent.clientX-this.disX+'px';
				this.oDiv.style.top=oEvent.clientY-this.disY+'px';
			}

			Drag.prototype.fnUp=function (){
						document.onmousemove=null;
						document.onmouseup=null;
					}
			Drag.prototype.fnDown=function (ev){
					var _this=this;
					var oEvent=ev||event;
					this.disX=oEvent.clientX-this.oDiv.offsetLeft;
					this.disY=oEvent.clientY-this.oDiv.offsetTop;

					document.onmousemove=function(ev){
						_this.fnMove(ev);
					}

					document.onmouseup=function(){
						_this.fnUp();
					}
				}
				//继承最大的好处就是父类变了子类也跟着变