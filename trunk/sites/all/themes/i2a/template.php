<?php
// $Id: template.php,v 1.16.2.3 2010/05/11 09:41:22 goba Exp $

/**
 * Sets the body-tag class attribute.
 *
 * Adds 'sidebar-left', 'sidebar-right' or 'sidebars' classes as needed.
 */
 
 
function get_title_magically($nid)
{
  $node = node_load(array('nid'=>$nid));
  return $node->title;
} 
 
function contact_plugin(){
  $form_email='';
  $sql = "SELECT email FROM {webform_emails} WHERE from_address='default'  LIMIT 1";
  $result = db_query($sql); 
  while($row = db_fetch_object($result)){              
    $form_email=$row->email;
  }
  
  $txt='<img usemap="#contactplugin" src="'. base_path().path_to_theme() .'/images/contact-us-plugin.png" alt="CONTACT US" class="plugin-right" />';
  $txt.='<map name="contactplugin" id="contactplugin">
    <area shape="rect" coords="15,50,115,87" href="'.base_path().drupal_get_path_alias('node/26').'" alt="FILL OUT OUR FORM" />
    <area shape="rect" coords="115,40,225,75" href="mailto:'.$form_email.'" alt="FILL OUT OUR FORM" />
  </map>';
  return $txt;
}
 
function module_find_lowest_menu($menu) {
  foreach ($menu as $id => $item) {
    if (!empty($item['below'])) {
      foreach ($item['below'] as $id_new => $item_new) {
          $next[$id_new] = $item_new;
      }
    }
  }
  if (!empty($next)) {
    return module_find_lowest_menu($next);
  }

  return $menu;
} 
 
function phptemplate_body_class($left, $right) {
  if ($left != '' && $right != '') {
    $class = 'sidebars';
  }
  else {
    if ($left != '') {
      $class = 'sidebar-left';
    }
    if ($right != '') {
      $class = 'sidebar-right';
    }
  }

  if (isset($class)) {
    print ' class="'. $class .'"';
  }
}

/**
 * Return a themed breadcrumb trail.
 *
 * @param $breadcrumb
 *   An array containing the breadcrumb links.
 * @return a string containing the breadcrumb output.
 */
 
function phptemplate_breadcrumb($breadcrumb) {
  if (!empty($breadcrumb)) {
    return '<div class="breadcrumb">'. implode(' &raquo; ', $breadcrumb) .'</div>';
  }
}
 
 

/**
 * Override or insert PHPTemplate variables into the templates.
 */
function phptemplate_preprocess_page(&$vars) {
  $vars['tabs2'] = menu_secondary_local_tasks();

  // Hook into color.module
  if (module_exists('color')) {
    _color_page_alter($vars);
  }
}

/**
 * Add a "Comments" heading above comments except on forum pages.
 */
function garland_preprocess_comment_wrapper(&$vars) {
  if ($vars['content'] && $vars['node']->type != 'forum') {
    $vars['content'] = '<h2 class="comments">'. t('Comments') .'</h2>'.  $vars['content'];
  }
}

/**
 * Returns the rendered local tasks. The default implementation renders
 * them as tabs. Overridden to split the secondary tasks.
 *
 * @ingroup themeable
 */
function phptemplate_menu_local_tasks() {
  return menu_primary_local_tasks();
}

/**
 * Returns the themed submitted-by string for the comment.
 */
function phptemplate_comment_submitted($comment) {
  return t('!datetime — !username',
    array(
      '!username' => theme('username', $comment),
      '!datetime' => format_date($comment->timestamp)
    ));
}

/**
 * Returns the themed submitted-by string for the node.
 */
function phptemplate_node_submitted($node) {
  return t('!datetime — !username',
    array(
      '!username' => theme('username', $node),
      '!datetime' => format_date($node->created),
    ));
}

/**
 * Generates IE CSS links for LTR and RTL languages.
 */
function phptemplate_get_ie_styles() {
  global $language;

  $iecss = '<link type="text/css" rel="stylesheet" media="all" href="'. base_path() . path_to_theme() .'/fix-ie.css" />';
  if ($language->direction == LANGUAGE_RTL) {
    $iecss .= '<style type="text/css" media="all">@import "'. base_path() . path_to_theme() .'/fix-ie-rtl.css";</style>';
  }

  return $iecss;
}


drupal_add_js('misc/jquery-1.4.2.min.js');
drupal_add_js('misc/jquery-ui-1.8.5.custom.min.js');
drupal_add_js('misc/jquery.tooltip.js');
drupal_add_js('misc/jquery.validate.js');
drupal_add_js('misc/jquery.corner.js');
drupal_add_js('misc/paginator.js');

drupal_add_js('misc/chili-1.7.pack.js');
drupal_add_js('misc/jquery.cycle.all.js');
drupal_add_js('misc/functions.js');


drupal_add_css('misc/custom-theme/jquery-ui-1.8.5.custom.css');



