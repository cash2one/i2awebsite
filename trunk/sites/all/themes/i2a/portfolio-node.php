<?php
  $main_node = node_load(array('nid'=>'8'));
  $pnode=node_load(array('nid'=>$node->nid));
  //print_r($pnode); 
?>

<?php
  if(strlen($main_node->body)){
    echo'<div class="col-left">'.$main_node->body.'</div>';
  }
  echo'<div class="col-right project">';
    echo'<h1 id="project-name">'.$pnode->title.'</h1>';
    echo'<div>'.$pnode->body.'</div>';
    echo'<div id="project-gallery">';
      if(!empty($pnode->field_screen_image[0])){
        foreach($pnode->field_screen_image as $image){
          echo'<a href="'.base_path().$image['filepath'].'" title="'.$pnode->title.'"><img src="'.base_path().$image['filepath'].'" alt="'.$pnode->title.'" class="lightbox" style="width:120px;" /></a>';
        }
      }
    echo'<div class="clear"></div>';
  echo'</div>';
                 
  if(!empty($pnode->field_www[0]['value']))
    echo'<br /><b>See online:</b> <a href="'.$pnode->field_www[0]['value'].'" title="See onlline: '.$pnode->title.'">'.$pnode->field_www[0]['value'].'</a>';
  echo'<br /><br />';
  echo'<a href="'.base_path().drupal_lookup_path('alias',"node/8").'" title="back" class="back-link"> back</a>';
  echo'</div>';
  
  echo'<div class="clear"></div>';
  
?>