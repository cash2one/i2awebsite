<?php 
  $social=array();
  $type="'social_links'";
  $sql = "SELECT * FROM {node} WHERE type = $type";
  $result = db_query($sql); 
  while($row = db_fetch_object($result)){              
    $node = node_load(array('nid'=>$row->nid));
    if($node->status){
      array_push($social,array('nid'=>$node->nid,'title'=>$node->title,'body'=>$node->body,'url'=>$node->field_url[0]['value'],'filepath'=>$node->field_icon[0]['filepath'],'filename'=>$node->field_icon[0]['filename']));
    }
  }
  if(!empty($social)){
    echo'<h2 class="follow">Follow us</h2>';
    echo'<ul class="follow">';
    foreach($social as $ss)
        echo'<li><a href="'.$ss['url'].'" title="'.$ss['name'].'" ><img src="'.base_path().$ss['filepath'].'" alt="'.$ss['name'].'" /></a></li>';
    echo'</ul><div class="clear"></div>';  
  }            
?>