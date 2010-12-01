<?php 
  if($node->nid==29){
    $main_node = node_load(array('nid'=>29));
    $period_type=$main_node->field_type[0]['value'];
    $period=1000*$main_node->field_period[0]['value'];
  }

  $advert_data=array();
  $type="'main_page_adverts'";
  $sql = "SELECT * FROM {node} WHERE type = $type";
  $result = db_query($sql); 
  while($row = db_fetch_object($result)){              
    $node = node_load(array('nid'=>$row->nid));
    if($node->status){
      array_push($advert_data,array('nid'=>$node->nid,'title'=>$node->title,'body'=>$node->body,'position'=>$node->position,'filepath'=>$node->field_image[0]['filepath'],'filename'=>$node->field_image[0]['filename'],'more'=>$node->field_more[0]['value']));
    }
  }
  
  
  
?>

<?php
// $Id: page.tpl.php,v 1.18.2.1 2009/04/30 00:13:31 goba Exp $
?><!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="<?php print $language->language ?>" lang="<?php print $language->language ?>" dir="<?php print $language->dir ?>">
  <head>
    <?php print $head ?>
    <title><?php print $head_title ?></title>
    <?php print $styles ?>
    <?php print $scripts ?>
    <!--[if lt IE 7]>
      <?php print phptemplate_get_ie_styles(); ?>
    <![endif]-->
    <link type="text/css" rel="stylesheet" media="all" href="<?php print base_path().path_to_theme() ?>/style-i2a.css" />
    
    <script type="text/javascript">
      /*<![CDATA[*/ 	
    	  $(function(){
    	   $('.slide') 
            .cycle({ 
                fx:     '<?php echo $period_type; ?>', 
                speed:  'fast', 
                timeout: <?php echo $period; ?>,
                pager:  '.menu-adv' 
          });
    	  
    	    <?php
    	      $str='';
            for($i=0,$ii=count($advert_data);$i<$ii;$i++){
              $str.="'".$advert_data[$i]['title']."'";
              if($i<($ii-1)) $str.=',';
            }
            echo 'tab=Array('.$str.');';
          ?>
        	
        	$(".menu-adv").children().each(function(){
            i=$(this).html()-1;
            if(!i)
              $(this).css('margin-left','100px');
            if(i<3)
              //k='<img src="<?php print base_path().path_to_theme() ?>/images/menu-li.png" alt="" />';
              k='<span>&rsaquo;</span>';
            else
              k='';
            if(tab[i])
              $(this).html(tab[i]+k);  
          });
          
        });
      	
      /*]]>*/
    </script>
  
  </head>
  
  
  <body<?php print phptemplate_body_class($left, $right); ?>>
  <div id="dialog"></div>
  <div class="main">
    <?php
      if(!$user->uid)
        echo'<div class="login-box"  id="log-in"><a title="Customer Login">Customer Login</a></div>';  
      else
        echo'<div class="login-box"><a href="'.base_path().'logout" title="Customer Login">Logout</a></div>';
    ?>
    <div class="call-us"><span>Call Us:</span> 1-855-422-2777</div>
    <div class="clear"></div>
    <ul class="header">
      <li><a href="<?php print base_path(); ?>" title=""><img src="<?php print base_path().path_to_theme() ?>/images/logo.gif" alt="" /></a></li>
      <li><h1>Transforming Ideas Into <b>Successful Applications</b></h1></li>
    </ul>
    <div class="clear"></div>
  </div>
  
  <div class="slider-bg">
      <div class="main">
        <div class="menu-out"></div>
        <!--<div class="menu-out">
          <?php if (isset($primary_links)) : ?>
            <?php print theme('links', $primary_links, array('class' => 'links primary-links')) ?>
          <?php endif; ?>
          <?php if (isset($secondary_links)) : ?>
            <?php print theme('links', $secondary_links, array('class' => 'links secondary-links')) ?>
          <?php endif; ?>
          <div class="clear"></div>
        </div>-->
        <!-- advert -->
        <div class="main-adv">
          <div class="menu-adv"></div>
          <div class="slide" >
            <?php
              if(!empty($advert_data)){
                foreach($advert_data as $ad){
                  echo'<div>
                        <div class="left" style="background:url('. base_path() .'/'.$ad['filepath'].') top left no-repeat;">&nbsp;</div>
                        <div class="right" style="width:250px;position:absolute;margin:10px 0 0 670px;">
                          <h1>'.$ad['title'].'</h1>
                            '.$ad['body'];
                          
                          if($ad['more']){
                            echo'<div class="orange-button main-orange">';
                            echo'<a href="'.$ad['more'].'" title="'.$ad['title'].'">Learn more &raquo;</a>';
                            echo'</div>';
                          }
                        
                        echo'</div>   
                      </div>';
                }
              }
            ?>
          </div>  
        </div>
        <!-- end advert -->
      
      <div class="clear"></div>
    </div>
  </div>
 
 
 <!-- main content -->
 
 <!-- end main content -->
  <div>
    <div class="main">
               
    <div class="txt">
      <div class="clear"></div>
      <div class="left">
       
          <?php print '';//$breadcrumb; ?>
          <?php if ($mission): print '<div id="mission">'. $mission .'</div>'; endif; ?>
          <?php if ($tabs): print '<div id="tabs-wrapper" class="clear-block">'; endif; ?>
          <?php if ($title): print '<h2'. ($tabs ? ' class="with-tabs"' : '') .'>'. $title .'</h2>'; endif; ?>
          <?php if ($tabs): print '<ul class="tabs primary">'. $tabs .'</ul></div>'; endif; ?>
          <?php if ($tabs2): print '<ul class="tabs secondary">'. $tabs2 .'</ul>'; endif; ?>
          <?php if ($show_messages && $messages): print $messages; endif; ?>
          <?php print $help; ?>
          <div class="clear-block">
            <?php print $content ?>
          </div>
          <?php print $feed_icons ?>
          <div id="footer"><?php print $footer_message . $footer ?></div>
       
      
      <?php if ($right): ?>
        <div id="sidebar-right" class="sidebar">
          <?php print $right ?>
        </div>
      <?php endif; ?>
       
      
       
       <div class="clear"></div>
      </div>
      <div class="right">
        <h1 class="orange">Contact Us Today!</h1>
        <div class="main-form">
          <div id="contact-us-today"></div>
        </div>    
        <br />
      </div>
      
      <?php
        //$front=1; 
        include('social.php');
      ?>
    </div>
    
    </div>
  </div>
 <!-- end main_content --> 
 
 <!-- footer -->
 <?php 
    include('footer.tpl.php'); 
 ?>
 <!-- end footer -->

  <?php print $closure ?>
  </body>
</html>
