<?php 
  if($node->nid==8){
    $portfolio_data=array();
    $type="'portfolio'";
    $sql = "SELECT * FROM {node} WHERE type = $type";
    $result = db_query($sql); 
    while($row = db_fetch_object($result)){              
      $port_node = node_load(array('nid'=>$row->nid));
      if($port_node->status){ 
        array_push($portfolio_data,array('nid'=>$port_node->nid,'title'=>$port_node->title,'body'=>$port_node->body,'filepath'=>$port_node->field_image[0]['filepath'],'filepath'=>$port_node->field_screen_image[0]['filepath'],'www'=>$port_node->field_www[0]['value'],'short_description'=>$port_node->field_short_desc[0]['value']));
      }
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
  </head>

  <body<?php print phptemplate_body_class($left, $right); ?>>
  <div id="dialog"></div>
  <div class="main">
    <?php
      if(!$user->uid)
        echo'<div class="login-box" id="log-in"><a title="Customer Login">Customer Login</a></div>';  
      else
        echo'<div class="login-box"><a href="'.base_path().'logout" title="Customer Login">Logout</a></div>';
    ?>
    <div class="call-us"><span>Call Us:</span> 1-800-555-5555</div>
    <div class="clear"></div>
    <ul class="header">
      <li><a href="<?php print base_path(); ?>" title=""><img src="<?php print base_path().path_to_theme() ?>/images/logo.gif" alt="" /></a></li>
      <li><h1>Transforming Ideas Into <b>Successful Applications</b></h1></li>
    </ul>
    <div class="clear"></div>
  </div>
  
  <div class="slider-bg">
      <div class="main">
        <div class="menu-out">
          <?php if (isset($primary_links)) : ?>
            <?php print theme('links', $primary_links, array('class' => 'links primary-links')) ?>
          <?php endif; ?>
          <?php if (isset($secondary_links)) : ?>
            <?php print theme('links', $secondary_links, array('class' => 'links secondary-links')) ?>
          <?php endif; ?>
          <div class="clear"></div>
        </div>
        <?php 
          if(!empty($node->field_baner[0]['filepath']))
            $baner=base_path().$node->field_baner[0]['filepath'];
          elseif($node->nid==26)
            $baner=base_path().path_to_theme().'/images/baner-contact.png';
          else
            $baner=base_path().path_to_theme().'/images/baner.png';
        ?>
        <div class="baner" style="background:url(<?php print $baner; ?>) top left no-repeat">  
          
          <h1 id="breadcrumbs"><?php echo $node->title ?> > <b>Web to Mobile</b></h1>
          <?php if($node->type=='job'){ ?>
            <script type="text/javascript">
              $(function(){
                $("#breadcrumbs").html('<b style="color: rgb(0, 138, 173);">Home</b> &raquo; Careers &raquo <?php echo $node->title; ?></h1>')
              });
            </script>
          <?php }?>
        </div>  
      
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
       
          
          <?php if ($mission): print '<div id="mission">'. $mission .'</div>'; endif; ?>
          <?php if ($tabs): print '<div id="tabs-wrapper" class="clear-block">'; endif; ?>
          <?php if ($title): print '<h2'. ($tabs ? ' class="with-tabs"' : '') .'>'. $title .'</h2>'; endif; ?>
          <?php if ($tabs): print '<ul class="tabs primary">'. $tabs .'</ul></div>'; endif; ?>
          <?php if ($tabs2): print '<ul class="tabs secondary">'. $tabs2 .'</ul>'; endif; ?>
          <?php if ($show_messages && $messages): print $messages; endif; ?>
          <?php print $help; ?>
          <?php print $breadcrumb ?>
          <div class="clear-block">
            <?php
              
              $u=strstr($_SERVER['REQUEST_URI'],'/edit');
              if($node->nid==8 && !strlen($u) && $node->type!='portfolio'){
                include('portfolio.php'); 
              }
              elseif($node->type=='portfolio' && $node->nid>8 && !strlen($u)){
                include('portfolio-node.php');
              }
              else{
                print $content;
              } 
              //array_push($job_data,array('nid'=>$job_node->nid,'title'=>$job_node->title,'short_description'=>$job_node->field_short_body[0]['value'],'body'=>$job_node->body,'reference'=>$job_node->field_reference_number[0]['value']));
              
              //<a href="'.base_path().drupal_lookup_path('alias',"node/".$pd['nid']).'" title="'.$pd['title'].'" class="more-link">more</a>
            ?>
            
            
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
          <?php
            $menu = module_find_lowest_menu(menu_tree_page_data('primary-links'));
            $menu_a=array();
            foreach($menu as $mm){
              if($mm['link']['depth']>1)
                array_push($menu_a, $mm);
            }
            if($menu_a && $node->type!='job'){
              $content =  menu_tree_output($menu_a);
              echo'<h1 class="menu-left">'.$title.'</h1>';
              print($content);
              echo'<br />';
            } 
            /*else{
              echo'<div class="follow-us">';
              include('social.php');
              echo'</div>';
            }*/
          ?>
          
          
          <div class="contact-us">
            <!--<h1>Contact Us Today!</h1>
            619.999.1212<br />
            <a href="" title="">info@i2asolutions.com</a>-->
          </div>
          
        </div>
        
        <?php 
          $footer=true;
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
