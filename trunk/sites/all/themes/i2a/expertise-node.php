<?php
  $main_node = node_load(array('nid'=>'8'));
  $pnode=node_load(array('nid'=>$node->nid)); 
  $ex=node_load(array('nid'=>$pnode->field_expertise[0]['nid']));
  
?>

<?php
  echo'<div class="col-right project">';
    //echo'<h1 id="project-name">'.$pnode->title.'</h1>';
    echo'<div>'.$pnode->body.'</div>';
    echo'<div id="project-gallery">';
      if(!empty($pnode->field_image_file[0])){
        foreach($pnode->field_image_file as $image){
              echo'<div>';
                //$image_file=imagecache_create_url($pnode->field_th_scale[0]['value'], $image['filepath']);
                //$file_size=getimagesize($image_file);
                //$css='style="padding-top:'.((120-$file_size[1])/2).'px;"';
                echo'<a href="'.imagecache_create_url('portfolio-lightbox', $image['filepath']).'" title="'.$pnode->title.'">
                        <img  src="'.$image_file.'" alt="'.$pnode->title.'" class="lightbox" />
                    </a>';
              echo'</div>';
        }
      }
  echo'</div>';
  echo'<div class="clear"></div>';
                 
  if(!empty($pnode->field_online[0]['value']))
    echo'<br /><b>See online:</b> <a href="'.$pnode->field_online[0]['value'].'" title="See onlline: '.$pnode->title.'">'.$pnode->field_online[0]['value'].'</a>';
  echo'<br /><br />';
  echo'<a href="'.base_path().drupal_lookup_path('alias',"node/3").'" title="back" class="back-link"> back</a>';
  echo'</div>';
  
  echo'<div class="clear"></div>';  
?>

<script type="text/javascript">
  $(function(){
    $("#breadcrumbs").html('<b style="color: rgb(0, 138, 173);">Home</b> &raquo; <?php echo $ex->title?> &raquo <?php echo $pnode->title; ?></h1>')
  });
</script>