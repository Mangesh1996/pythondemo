
'''
we have to change parameter manually and dynamic means taking input from user.
and then creating a new text file after accepting the input.

'''

image_width = 12200
image_height = 7284
batch_size = 20
epochs_kitti = 45
arch_layers = 10

# declare string

var='''random_seed: 42
dataset_config {
  data_sources {
    tfrecords_path: "/workspace/tao-experiments/detectnet_v2/specs/tfrecords/kitti_trainval/*"
    image_directory_path: "/workspace/tao-experiments"
  }
  image_extension: "jpg"
  target_class_mapping {
    key: "headlamp" 
    value: "headlamp"
  }
  target_class_mapping {
    key: "halo_lamp" 
    value: "halo_lamp"
  }
  target_class_mapping {
    key: "horn" 
    value: "horn"
  }
  target_class_mapping {
    key: "flasher" 
    value: "flasher"
  }
  target_class_mapping {
    key: "wiring_harness" 
    value: "wiring_harness"
  }
  validation_fold: 0
}
augmentation_config {
  preprocessing {
    output_image_width:'''+str(image_width)+'''  
    output_image_height:'''+str(image_height)+'''
    min_bbox_width:
    min_bbox_height: 
    output_image_channel: 3
  }
  spatial_augmentation {
    hflip_probability: 0.5
    zoom_min: 1.0
    zoom_max: 1.0
    translate_max_x: 8.0
    translate_max_y: 8.0
  }
  color_augmentation {
    hue_rotation_max: 25.0
    saturation_shift_max: 0.20000000298
    contrast_scale_max: 0.10000000149
    contrast_center: 0.5
  }
}
postprocessing_config {
    target_class_config {
    key: "headlamp"
    value {
      clustering_config {
        clustering_algorithm: DBSCAN
        dbscan_confidence_threshold: 0.9
        coverage_threshold: 0.00499999988824
        dbscan_eps: 0.20000000298
        dbscan_min_samples: 0.0500000007451
        minimum_bounding_box_height: 20
      }
    }
  } 
    target_class_config {
    key: "halo_lamp"
    value {
      clustering_config {
        clustering_algorithm: DBSCAN
        dbscan_confidence_threshold: 0.9
        coverage_threshold: 0.00499999988824
        dbscan_eps: 0.20000000298
        dbscan_min_samples: 0.0500000007451
        minimum_bounding_box_height: 20
      }
    }
  } 
    target_class_config {
    key: "horn"
    value {
      clustering_config {
        clustering_algorithm: DBSCAN
        dbscan_confidence_threshold: 0.9
        coverage_threshold: 0.00499999988824
        dbscan_eps: 0.20000000298
        dbscan_min_samples: 0.0500000007451
        minimum_bounding_box_height: 20
      }
    }
  } 
    target_class_config {
    key: "flasher"
    value {
      clustering_config {
        clustering_algorithm: DBSCAN
        dbscan_confidence_threshold: 0.9
        coverage_threshold: 0.00499999988824
        dbscan_eps: 0.20000000298
        dbscan_min_samples: 0.0500000007451
        minimum_bounding_box_height: 20
      }
    }
  } 
    target_class_config {
    key: "wiring_harness"
    value {
      clustering_config {
        clustering_algorithm: DBSCAN
        dbscan_confidence_threshold: 0.9
        coverage_threshold: 0.00499999988824
        dbscan_eps: 0.20000000298
        dbscan_min_samples: 0.0500000007451
        minimum_bounding_box_height: 20
      }
    }
  } 
}
model_config {
  pretrained_model_file: "/workspace/tao-experiments/detectnet_v2/specs/resnet18.hdf5"
  num_layers: 18
  use_batch_norm: true
  objective_set {
    bbox {
      scale: 35.0
      offset: 0.5
    }
    cov {
    }
  }
  arch_layers: '''+str(arch_layers)+'''
}
evaluation_config {
  validation_period_during_training: 10
  first_validation_epoch: 30
  minimum_detection_ground_truth_overlap {
     key: "headlamp"
    value: 0.399999988079 
  }
  minimum_detection_ground_truth_overlap {
     key: "halo_lamp"
    value: 0.399999988079 
  }
  minimum_detection_ground_truth_overlap {
     key: "horn"
    value: 0.399999988079 
  }
  minimum_detection_ground_truth_overlap {
     key: "flasher"
    value: 0.399999988079 
  }
  minimum_detection_ground_truth_overlap {
     key: "wiring_harness"
    value: 0.399999988079 
  }
  evaluation_box_config {
    key:  "headlamp"
    value {
      minimum_height: 10
      maximum_height: 9999
      minimum_width: 10
      maximum_width: 9999
    }
  }
  evaluation_box_config {
    key:  "halo_lamp"
    value {
      minimum_height: 10
      maximum_height: 9999
      minimum_width: 10
      maximum_width: 9999
    }
  }
  evaluation_box_config {
    key:  "horn"
    value {
      minimum_height: 10
      maximum_height: 9999
      minimum_width: 10
      maximum_width: 9999
    }
  }
  evaluation_box_config {
    key:  "flasher"
    value {
      minimum_height: 10
      maximum_height: 9999
      minimum_width: 10
      maximum_width: 9999
    }
  }
  evaluation_box_config {
    key:  "wiring_harness"
    value {
      minimum_height: 10
      maximum_height: 9999
      minimum_width: 10
      maximum_width: 9999
    }
  }
  average_precision_mode: INTEGRATE
}
cost_function_config {
  target_classes {
    name: "headlamp"
    class_weight: 10.0
    coverage_foreground_weight: 0.0500000007451
    objectives {
      name: "cov"
      initial_weight: 1.0
      weight_target: 1.0
    }
    objectives {
      name: "bbox"
      initial_weight: 10.0
      weight_target: 10.0
    }
  }
  target_classes {
    name: "halo_lamp"
    class_weight: 10.0
    coverage_foreground_weight: 0.0500000007451
    objectives {
      name: "cov"
      initial_weight: 1.0
      weight_target: 1.0
    }
    objectives {
      name: "bbox"
      initial_weight: 10.0
      weight_target: 10.0
    }
  }
  target_classes {
    name: "horn"
    class_weight: 10.0
    coverage_foreground_weight: 0.0500000007451
    objectives {
      name: "cov"
      initial_weight: 1.0
      weight_target: 1.0
    }
    objectives {
      name: "bbox"
      initial_weight: 10.0
      weight_target: 10.0
    }
  }
  target_classes {
    name: "flasher"
    class_weight: 10.0
    coverage_foreground_weight: 0.0500000007451
    objectives {
      name: "cov"
      initial_weight: 1.0
      weight_target: 1.0
    }
    objectives {
      name: "bbox"
      initial_weight: 10.0
      weight_target: 10.0
    }
  }
  target_classes {
    name: "wiring_harness"
    class_weight: 10.0
    coverage_foreground_weight: 0.0500000007451
    objectives {
      name: "cov"
      initial_weight: 1.0
      weight_target: 1.0
    }
    objectives {
      name: "bbox"
      initial_weight: 10.0
      weight_target: 10.0
    }
  }
  enable_autoweighting: true
  max_objective_weight: 0.999899983406
  min_objective_weight: 9.99999974738e-05
}
training_config {
  batch_size_per_gpu:'''+str(batch_size)+'''
  num_epochs :'''+str(epochs_kitti)+'''
  learning_rate {
    soft_start_annealing_schedule {
      min_learning_rate: 5e-06
      max_learning_rate: 5e-04
      soft_start: 0.10000000149
      annealing: 0.699999988079
    }
  }
  regularizer {
    type: L1
    weight: 3.00000002618e-09
  }
  optimizer {
    adam {
      epsilon: 9.99999993923e-09
      beta1: 0.899999976158
      beta2: 0.999000012875
    }
  }
  cost_scaling {
    initial_exponent: 20.0
    increment: 0.005
    decrement: 1.0
  }
  checkpoint_interval: 10
}
bbox_rasterizer_config {
  target_class_config {
    key: "headlamp"
    value {
      cov_center_x: 0.5
      cov_center_y: 0.5
      cov_radius_x: 0.80000000596
      cov_radius_y: 0.80000000596
      bbox_min_radius: 1.0
    }
  }
  target_class_config {
    key: "halo_lamp"
    value {
      cov_center_x: 0.5
      cov_center_y: 0.5
      cov_radius_x: 0.80000000596
      cov_radius_y: 0.80000000596
      bbox_min_radius: 1.0
    }
  }
  target_class_config {
    key: "horn"
    value {
      cov_center_x: 0.5
      cov_center_y: 0.5
      cov_radius_x: 0.80000000596
      cov_radius_y: 0.80000000596
      bbox_min_radius: 1.0
    }
  }
  target_class_config {
    key: "flasher"
    value {
      cov_center_x: 0.5
      cov_center_y: 0.5
      cov_radius_x: 0.80000000596
      cov_radius_y: 0.80000000596
      bbox_min_radius: 1.0
    }
  }
  target_class_config {
    key: "wiring_harness"
    value {
      cov_center_x: 0.5
      cov_center_y: 0.5
      cov_radius_x: 0.80000000596
      cov_radius_y: 0.80000000596
      bbox_min_radius: 1.0
    }
  }
  deadzone_radius: 0.400000154972
}
'''


with open("data.txt","w")as wr:
    wr.write(var)