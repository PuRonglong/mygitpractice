$(function(){
				var $li = $("body ul.elected-list li");
				$li.live("click",function(event) {
					$(this).toggleClass('selected');//点击时给当前目标添加选中样式
				});
				$(".pass").click(function(event) {
					$("li[class=selected]").appendTo('#selected-list2');//左边移到右边
					$("#selected-list2 li a").remove();//移除X符号
					$("#selected-list2 li").removeClass("selected");//移除右边选中的样式                 
				});
				$(".cancle").click(function(event) {
					$("li[class=selected]").appendTo("#selected-list1");//右边移到左边
					$("<a>X</a>").appendTo('#selected-list1 li');       //添加X符号
				});
				$(".add").click(function(event) {
					if ($(".add-input").val()!=="") {
						$("<li>" + $(".add-input").val() + "<a>X</a></li>").appendTo('#selected-list1');
						$(".add-input").val() == $(".add-input").val("");
					};
				});//点击时在左边添加内容，并清空输入框的值
				$("#selected-list1 li a").live("click",function(event) {
					$(this).parent().remove();
				});//点击X符号的时候将此行删除
			})