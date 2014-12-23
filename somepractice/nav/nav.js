(function($){
		/*$(".navList span").toggle(function(){
			$(this).next().slideUp("slow");
		},function(){
			$(this).next().slideDown("slow");
		})*/							//可简化如下:
		
		var $navList_li=$(".navList > li");
		
		$navList_li.on("click",function(){
			$(this).children("ul").stop().slideToggle("slow").end()
				.siblings().children("ul").slideUp("slow");
		});

		/*$navList_li.on("click",function(){			
			$(this).children("ul").hasClass("none")?show():hide();
		});
*/
})(jQuery)