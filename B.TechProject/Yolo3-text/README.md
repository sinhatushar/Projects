#  Yolo3 for text

{ 
    
    See Training-ipython folder for ipython notebooks containing traning and detection

    Also, the trained weights can be downloaded from :

    Trained weights for 416x416 : https://drive.google.com/open?id=1k1G9KNDNrJl61dkLUMEqEunqSNz-qDC0

    Trained weights for 64x320 : https://drive.google.com/open?id=1-FhUlym0t9LU6tnPvKvlfFMY6zvcvzTb

    Please see the BTP1/Dataset to understand the dataset which has been used for yolo3. 
    
}

### 1. Requirements

- works only with python2
- tensorflow >= 1.8.0 (lower versions may work too)
- opencv-python

### 2. Weights convertion

The pretrained darknet weights file can be downloaded [here](https://pjreddie.com/media/files/yolov3.weights). Place this weights file under directory `./data/darknet_weights/` and then run:

```shell
python convert_weight.py
```

Then the converted TensorFlow checkpoint file will be saved to `./data/darknet_weights/` directory. This step is compulsory.


### 3. Training

#### 3.1 Data preparation 

(1) annotation file

Generate `train.txt/val.txt/test.txt` files under `./data/my_data/` directory. One line for one image, in the format like `image_absolute_path box_1 box_2 ... box_n`. Box_format: `label_index x_min y_min x_max y_max`.(The origin of coordinates is at the left top corner.)

For example:

```
/content/gdrive/My Drive/BTP1/YOLOv3-TensorFlow/1747-train-images-416*416/Alice_and_Martin_3.jpg 0 0 0 300 6 1 0 6 300 12 2 0 12 300 66 
/content/gdrive/My Drive/BTP1/YOLOv3-TensorFlow/1747-train-images-416*416/Atsimo-Atsinanana_4.jpg 0 0 6 300 12 1 0 12 300 24 2 0 30 300 54 
/content/gdrive/My Drive/BTP1/YOLOv3-TensorFlow/1747-train-images-416*416/Ashton_Nyte_1.jpg 0 0 6 300 12 1 0 12 300 18 2 0 30 300 36 
/content/gdrive/My Drive/BTP1/YOLOv3-TensorFlow/1747-train-images-416*416/Arie_Alter_1.jpg 0 0 0 300 12 1 0 12 300 36 2 0 48 300 60 
/content/gdrive/My Drive/BTP1/YOLOv3-TensorFlow/1747-train-images-416*416/Anthony_Basso_1.jpg 0 0 6 300 12 1 0 36 300 42 2 0 48 300 54 
/content/gdrive/My Drive/BTP1/YOLOv3-TensorFlow/1747-train-images-416*416/Ashley_Judd_5.jpg 0 0 24 300 30 1 0 138 300 144 2 0 168 300 174 
/content/gdrive/My Drive/BTP1/YOLOv3-TensorFlow/1747-train-images-416*416/Álvaro_Rudolphy_14.jpg 0 0 72 300 84 1 0 48 300 60 2 0 90 300 96 
...
```

**NOTE**: **You should leave a blank line at the end of each txt file.**

(2)  class_names file:

Generate the `data.names` file under `./data/my_data/` directory. Each line represents a class name.

For example:

```
subject 
relation
object
...
```

(3) prior anchor file:

Using the kmeans algorithm to get the prior anchors:

```
python get_kmeans.py
```

Then we get 9 anchors and the average IOU. Save the anchors to a txt file.

The anchors need to be placed at `./data/yolo_anchors.txt`,. Currently they contain the anchors set for text data.

**NOTE: The yolo anchors should be scaled to the rescaled new image size. Suppose the image size is [W, H], and the image will be rescale to 416*416 as input, for each generated anchor [anchor_w, anchor_h], you should apply the transformation anchor_w = anchor_w / W * 416, anchor_h = anchor_g / H * 416.**

#### 3.2 Training

Using `train.py`. The parameters are as following:

```shell
$ python train.py -h
usage: train.py [-h] [--train_file TRAIN_FILE] [--val_file VAL_FILE]
                [--restore_path RESTORE_PATH] 
                [--save_dir SAVE_DIR]
                [--log_dir LOG_DIR] 
                [--progress_log_path PROGRESS_LOG_PATH]
                [--anchor_path ANCHOR_PATH]
                [--class_name_path CLASS_NAME_PATH] [--batch_size BATCH_SIZE]
                [--img_size [IMG_SIZE [IMG_SIZE ...]]]
                [--total_epoches TOTAL_EPOCHES]
                [--train_evaluation_freq TRAIN_EVALUATION_FREQ]
                [--val_evaluation_freq VAL_EVALUATION_FREQ]
                [--save_freq SAVE_FREQ] [--num_threads NUM_THREADS]
                [--prefetech_buffer PREFETECH_BUFFER]
                [--optimizer_name OPTIMIZER_NAME]
                [--save_optimizer SAVE_OPTIMIZER]
                [--learning_rate_init LEARNING_RATE_INIT] [--lr_type LR_TYPE]
                [--lr_decay_freq LR_DECAY_FREQ]
                [--lr_decay_factor LR_DECAY_FACTOR]
                [--lr_lower_bound LR_LOWER_BOUND]
                [--restore_part [RESTORE_PART [RESTORE_PART ...]]]
                [--update_part [UPDATE_PART [UPDATE_PART ...]]]
                [--update_part [UPDATE_PART [UPDATE_PART ...]]]
                [--use_warm_up USE_WARM_UP] [--warm_up_lr WARM_UP_LR]
                [--warm_up_epoch WARM_UP_EPOCH]
```

Check the `train.py` for more details. You should set the parameters theself. 

### 4. Evaluation

Using `eval.py` to evaluate the validation or test dataset. The parameters are as following:

```shell
$ python eval.py -h
usage: eval.py [-h] [--eval_file EVAL_FILE] [--restore_path RESTORE_PATH]
               [--anchor_path ANCHOR_PATH] 
               [--class_name_path CLASS_NAME_PATH]
               [--batch_size BATCH_SIZE]
               [--img_size [IMG_SIZE [IMG_SIZE ...]]]
               [--num_threads NUM_THREADS]
               [--prefetech_buffer PREFETECH_BUFFER]
```

Check the `eval.py` for more details. You should set the parameters theself. 

You will get the loss, recall and precision metrics results, like:

```shell
recall: 0.927, precision: 0.945
total_loss: 0.210, loss_xy: 0.010, loss_wh: 0.025, loss_conf: 0.125, loss_class: 0.050
```

### 5. Testing

Single image testing:

```shell
python test_single_image.py /path/to/image --restore_path /path/to/trained/weights

```

More parameters can be set under test_single_image.py. Please check it once. 