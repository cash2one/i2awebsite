<?php 
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
              k='<img src="<?php print base_path().path_to_theme() ?>/images/menu-li.png" alt="" />';
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
        echo'<div class="login-box"><a href="./logout" title="Customer Login">Logout</a></div>';
    ?>
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
          <div class="slide">
            <?php
              if(!empty($advert_data)){
                foreach($advert_data as $ad){
                  echo'<div>
                        <div class="left" style="background:url('. base_path() .'/'.$ad['filepath'].') top left no-repeat;">&nbsp;</div>
                        <div class="right">
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
  <div class="clear"></div>
  <div class="footer">
    <div class="main">
      <ul class="f-left">
        <li class="m1">&copy; <a href="<?php print base_path()?>" title="I2A Solutions, Inc.">I2A Solutions, Inc.</a> All Rights Reserved</li>
        <li><a href="<?php print base_path()?>terms-of-use" title="Terms of Use">Terms of Use</a><span>|</span></li>
        <li><a href="<?php print base_path()?>privacy-policy" title="Privacy Policy">Privacy Policy</a></li>
      </ul>
      
      <ul class="f-right">
        <li><a href="<?php print base_path()?>sitemap" title="Site Map">Site Map</a></li>
        <li><a href="<?php print base_path()?>contact-us" title="Contact Us">Contact Us</a><span>|</span></li>
        <li><a href="<?php print base_path()?>careers" title="Careers">Careers</a><span>|</span></li>
        <li><a href="<?php print base_path()?>portfolio" title="Portfolio">Portfolio</a><span>|</span></li>
        <li><a href="<?php print base_path()?>expertise" title="Expertise">Expertise</a><span>|</span></li>
        <li><a href="<?php print base_path()?>about-us" title="About Us">About Us</a><span>|</span></li>
        <li><a href="<?php print base_path()?>" title="Home">Home</a><span>|</span></li>
      </ul>
      <div class="clear"></div>
    </div>
  </div>
 <!-- end footer -->
  
  
  
  




  <?php print $closure ?>
  </body>
</html>
