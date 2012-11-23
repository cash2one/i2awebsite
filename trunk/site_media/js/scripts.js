$(function(){
	$('#slider').nivoSlider({effect:'fade,fold', pauseTime:7000});
	$('.tooltip').tipsy({gravity: 's'}); // nw | n | ne | w | e | sw | s | se
	$('.technologies_used a.tooltip ').hover(function(){
		$(this).animate({"opacity":1},200);
	},function(){
		$(this).animate({"opacity":0.8},200);
	});
	
	$(window).scroll(function() {
		if($(this).scrollTop() > 1400) {
			$('#back_to_top').fadeIn();    
		} else {
			$('#back_to_top').fadeOut();
		}
	});
	
	$('#footer_back_to_top').click(function(){
		$('body,html').animate({scrollTop:0},800);
	});
	
	$('#menu_solutions').click(function(e){
		e.preventDefault();
		$(this).toggleClass('toggle');
		$('.menu_toggle_bg').slideToggle();
	});
	
	$('.social_icon').hover(function(){
		$(this).animate({"opacity":"1"},400);
	},function(){
		$(this).animate({"opacity":"0.6"},400);
	});
	
	$('.project_hover').hover(function() {
		$(this).css({"background-position":"82 -50","opacity":"0"});
		$(this).css({"background-color":"rgba(0,138,173,0.7)"});
		$(this).stop().animate({"background-position":"82 26","opacity":"1"},300);
		$(this).siblings(".project_caption").stop().animate({"bottom":"0px"},300);
		$(this).siblings("img").stop().animate({"width":"218","height":"116","margin-left":"-5px","margin-top":"-5px"},300);
	},function(){
		$(this).stop().animate({"background-position":"82 -50","opacity":"0"},300);
		$(this).siblings(".project_caption").stop().animate({"bottom":"-30px"},300);
		$(this).siblings("img").stop().animate({"width":"198","height":"96","margin-left":"0px","margin-top":"0px"},300);
	});
	
	$('.menu_item').hover(function(){
		var x = $(this).position().left;
		var w = $(this).width();
		$('.moving_bar').show();
		$('.menu_item').removeClass('active');
		$('.moving_bar').stop().animate({"width":w,"left":x},300, "easeInSine");
	});
});