


$(function(){
  
  $("#hoverNav").corner();
  $(".portfolio-box").corner();
  $(".in-portfolio").corner();
  
  $(".contact-us").html($("#block-block-1").html());
  
 

  $(".portfolio-box").hover(function(){
      $("."+$(this).attr('id')).fadeIn("slow");  
    },function(){
      $("."+$(this).attr('id')).fadeOut("slow");  
  });
  
  
  itemsPerPage = 4;
  paginatorStyle = 1;
  paginatorPosition = 'bottom';
  enableGoToPage = false;
  ;//$("#result").pagination();

  $("#result .portfolio-box").click(function(){
    cnt=$(this).html();
    
  });

  //corners
  $(".login-box").corner("5px br bl");
  
  
  $(".slide .left").corner("10px");
  $(".main-adv").corner("5px");
  $(".menu-adv").corner("tl tr");
  $(".orange-button").corner("5px");
  $(".contact-us").corner("5px");
  $(".follow-us").corner("5px");


  $('.slide') 
    .cycle({ 
        fx:     'turnDown', 
        speed:  'fast', 
        timeout: 4000,
        pager:  '.menu-adv' 
  });
   
  	
  	$("#user-login-form").validate({
  		rules: {			
  			name: {
  				required: true
  			},
  			pass: {
  				required: true
  			}
  		},
  		messages: {
  		  name: "Please enter a valid name",
        pass: "Please enter a valid password"
  		}
  	});
  	
  	$("#log-in").click(function(){
      $("#dialog").dialog({
  			height: 210,
  			width: 340,
  			position: 'center',
  			title:'Customer Login',
  			resizable:false,
  			modal: true
  		});
  		$("#dialog").html($("#block-user-0").html());
  		$("#user-login-form input[type=submit]").val('');
    });
    
    //contact-form validation
    $("#webform-client-form-26").validate({
  		rules: {			
  			'webform-component-email': {
  				required: true,
				  email:true
  			},
  			'webform-component-name':{
          required: true
        },
  			'webform-component-message':{
          required: true
        }
  		},
  		messages: {
  		  'webform-component-email': "Please enter a valid Email Address",
  		  'webform-component-message': "Please enter a Message",
  		  'webform-component-name': "Please enter a Name"
  		}
  	}); 
  	
  	//contact-us-today
  	content=$(".node").find("p:last").next().parent().html();
    $("#contact-us-today").html(content);
    $(".content form#webform-client-form-29").remove();
  	
    //contact-us-today validation
    $("#webform-client-form-29").validate({
  		rules: {			
  			'edit-submitted-email': {
  				required: true,
				  email:true
  			}
  		},
  		messages: {
  		  'edit-submitted-email': "Please enter a valid email address"
  		}
  	});  	
  	
  
  //setup a job validation
  //contact-us-today validation
    $("#webform-client-form-27").validate({
  		rules: {			
  			'edit-submitted-name': {
  				required: true
  			},
  			'edit-submitted-phone': {
  				required: true
  			},
  			'edit-submitted-email': {
  				required: true,
  				email:true
  			}
  		},
  		messages: {
  		  'edit-submitted-email': "Please enter a valid email address",
  		  'edit-submitted-name': "Please enter your name",
  		  'edit-submitted-phone': "Please enter phone number"
  		}
  	});  
    
    //del text
  $('#webform-client-form-26 input[type=submit]').val('');
  $('#webform-client-form-27 input[type=submit]').val('');
  $("#contact-us-today div").each(function(){
    $(this).append('<div class="clear"></div>');
  });
  $('#contact-us-today input[type=submit]').val('');
  
  
  //menu
  $(".menu-out").html($("#block-nice_menus-2 .content").html());
  $(".menu-out ul").after('<div class="clear"></div>');
  
  $("#block-nice_menus-2").remove(); 
  
  //breadcrumbs
  
  br=$(".breadcrumb").text();
  if(br){
    breadcrumbs=br.replace(/&raquo;/gi,'&gt;');
    breadcrumbs=breadcrumbs.replace(/&amp;/gi,'&');
    breadcrumbs=breadcrumbs.replace(/Home » Home/gi,'Home');
    breadcrumbs=breadcrumbs.replace(/\//gi,' &raquo; ');
    breadcrumbs=breadcrumbs.replace(/Home/gi,'<b>Home</b>');
    $("#breadcrumbs").html(breadcrumbs);
    $("#breadcrumbs :first(a)").css('color','#008AAD');
   }
   $(".breadcrumb").remove();
   
});                  

