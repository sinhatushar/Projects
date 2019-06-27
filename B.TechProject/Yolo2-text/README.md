# YOLOv2 for text data for predicting RDF triples
{ 
    
    See Training-ipython folder for ipython notebooks containing traning and detection

    Also, the trained weights can be downloaded from :

    Trained weights for 416x416 : https://drive.google.com/open?id=1j_qfREngdZJl85mjf4y74vxUTxU6gUEW

    Trained weights for 64x320 : https://drive.google.com/drive/folders/1WyuWaIipkLfGPc2Pks9ndg7DAMfEQMGX

    Please see the BTP1/Dataset to understand the dataset which has been used for yolo2. 
    
}

### 1. Requirement

python 2.7 or python 3.x

opencv

tqdm

keras >= 2.0.8

imgaug


### 2. Edit the configuration file
The configuration file is a json file, which looks like this:

```python
{
    "model" : {
        "backend":              "Full Yolo",    # "Tiny Yolo" or "Full Yolo" or "MobileNet" or "SqueezeNet" or "Inception3"
        "input_size_w":         416,
        "input_size_h":         416,
        "gray_mode":            false,
        "anchors":              [0.00000,0.00000, 23.07692,3.29057, 23.07692,1.53049, 23.07692,0.92308, 23.07692,0.46154],
        "max_box_per_image":    3,        
        "labels":               ["subject","relation","object"]
    },

    "parser_annotation_type":    "csv",

    "train": {
        "train_csv_file":       "/content/drive/My Drive/yolo2/1747-annotation.csv",
        "train_csv_base_path":  "/content/drive/My Drive/yolo2/1747-train-images-416*416/",
        "train_image_folder":   "",   
        "train_annot_folder":   "",      

        "callback":             null,           # a specific callback to apply into image augmentation
        "train_times":          10,             # the number of time to cycle through the training set, useful for small datasets
        "pretrained_weights":   "",             # specify the path of the pretrained weights, but it's fine to start from scratch
        "batch_size":           16,             # the number of images to read in each batch
        "learning_rate":        1e-4,           # the base learning rate of the default Adam rate scheduler
        "nb_epoch":             50,             # number of epoches
        "warmup_epochs":        3,              # the number of initial epochs during which the sizes of the 5 boxes in each cell is forced to match the sizes of the 5 anchors, this trick seems to improve precision emperically

        "workers":              3,
        "max_queue_size":       8,
        "early_stop":           true,
        "tensorboard_log_dir":  "./logs/example",

        "object_scale":         5.0 ,           # determine how much to penalize wrong prediction of confidence of object predictors
        "no_object_scale":      1.0,            # determine how much to penalize wrong prediction of confidence of non-object predictors
        "coord_scale":          1.0,            # determine how much to penalize wrong position and size predictions (x, y, w, h)
        "class_scale":          1.0,            # determine how much to penalize wrong class prediction

        "saved_weights_name":   "pre-weights-not-loaded-416*416-iou-point-one.h5",
        "debug":                false
    },

    "valid": {
        "iou_threshold":        0.5,
        "score_threshold":      0.2,
        "valid_csv_file":       "",
        "valid_csv_base_path":  "",
        "valid_image_folder":   "",
        "valid_annot_folder":   "",

        "valid_times":          1
    },

    "backup":{
        "create_backup":        false, 
        "redirect_model":       true,           # if true, will rename tensorboard_log_dir and saved_weights_name to keep in same directory
        "backup_path":          "../backup",
        "backup_prefix":        "Full_yolo_VOC"
    }
}


```

## 3. Training custom dataset

 the CSV files must be used in this way
 ```
    file_path,xMin,yMin,xMax,yMax,objectCLass
 ```
 example:
 ```
    A_Series_of_Unfortunate_Events_6.jpg,5,1,315,2,subject
    A_Series_of_Unfortunate_Events_6.jpg,5,2,315,5,relation
    A_Series_of_Unfortunate_Events_6.jpg,5,5,315,7,object
 ```

 ``` train_csv_base_path``` is a base path for the directory that contains the images in the csv file, and not the base path for the CSV file, it is usefull to keep just the relative path in the csv file

### 4. Generate anchors for custom dataset 

`python gen_anchors.py -c config.json`

Copy the generated anchors printed on the terminal to the ```anchors``` setting in ```config.json```.

### 5. Start the training process

`python train.py -c config.json`

By the end of this process, the code will write the weights of the best model to file best_weights.h5 (or whatever name specified in the setting "saved_weights_name" in the config.json file). 

### 6. Perform detection using trained weights on an image by running
`python predict.py -c config.json -w /path/to/best_weights.h5 -i /path/to/image/or/video`

It carries out detection on the image and write the image with detected bounding boxes to the same folder.

### 7. Using a custom backend or generator callback

It is possible to use a customizable backend doing a dynamically import
to do it, change the architecture in the config file, like this:
```
"architecture":         "./examples/custom_backend.SuperTinyYoloFeature",
```
if the custom_backend file are in the root directory you must use ```./``` in order to indicate that you are using a file instead a known backend

for the generator callback specified into json config, it works in the same way than the custom backend, check the examples into ./examples/generator_callback.py
