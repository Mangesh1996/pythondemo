'''
requirefiles :-  specs directory with resnet_18.hdf5
                workspace/tao-experiments/data

usage:- app.py
'''


import os
import json
# import wget
from zipfile import ZipFile
import subprocess


def configruation_docker_path():
    #defineing variable
    try:
        os.environ['KEY']="diycam_models"
        os.environ['NUM_GPUS']="1"

        #local paths
        os.environ["LOCAL_PROJECT_DIR"]=os.path.join(os.getcwd(),"workspace/tao-experiments")
        os.environ["LOCAL_SPECS_DIR"]=os.path.join(os.getcwd(),"specs")
        
        #docker path
        os.environ["SPECS_DIR"]="/workspace/specs/detectnet_v2/specs"

        mounts_file=os.path.expanduser("~/.tao_mounts.json")

        drive_map={
            "Mounts":[
                {
                    "source":os.environ["LOCAL_PROJECT_DIR"],
                    "destination":"/workspace/tao-experiments"
                },
                {
                    "source": os.environ["LOCAL_SPECS_DIR"],
                    "destination": os.environ["SPECS_DIR"]
                },
            ]
        }
        with open(mounts_file,"w") as mfile:
            json.dump(drive_map,mfile,indent=4)
        return True
    except:
        return False


def down_pretrain_model():
    ngc=os.path.join(os.getcwd(),"ngccl")
    if not os.path.exists(ngc):
        os.mkdir(ngc)
    url="https://ngc.nvidia.com/downloads/ngccli_cat_linux.zip"
    wget.download(url,out=ngc)
    print("\n")
    with ZipFile(os.path.join(os.getcwd(),"ngccl/ngccli_cat_linux.zip"),"r") as zop:
        zop.extractall(os.path.join(os.getcwd(),"ngccl"))
        os.remove(os.path.join(os.getcwd(),"ngccl/ngccli_cat_linux.zip"))
    
# down_pretrain_model()



def train_mode():
    try:
        print("-------------  train model start -------------------\n")
        # tao classification train -e $SPECS_DIR/classification_spec.cfg -r $USER_EXPERIMENT_DIR/output -k $KEY
        p=subprocess.Popen(["tao","classification","train","-e $SPECS_DIR/classification_spec.cfg","-r $SPECS_DIR/output","-k $KEY"])
        p.wait()
        print("------------- done the train model -------------------\n")
    except Exception as e:
        print(e)

def evaluate():
    try:
        print("-------------  evaluate start -------------------\n")
        #!tao classification evaluate -e $SPECS_DIR/classification_spec.cfg -k $KEY
        p1=subprocess.Popen(["tao","classification","evaluate","-e $SPECS_DIR/classification_spec.cfg","-k $KEY"])
        p1.wait()
        print("------------done evaluate ------------------\n")
    except Exception as e:
        print(e)


def prune_train_model(epochs):
    try:
        print("-------------  prune train model start -------------------\n")
        resnet=os.path.join(os.getcwd(),"$LOCAL_SPECS_DIR/output/resnet_pruned")
        # p1=subprocess.Popen(["mkdir","-p $LOCAL_EXPERIMENT_DIR/output/resnet_pruned"])
        
        # os.makedirs(os.path.join(os.environ["SPECS_DIR"],"output","resnet_pruned"))
        os.system("sudo mkdir -p specs/output/resnet_pruned")
        p2=subprocess.Popen([f"tao","classification","prune",f"-m $SPECS_DIR/output/weights/resnet_{epochs}.tlt","-o $SPECS_DIR/output/resnet_pruned/resnet18_nopool_bn_pruned.tlt","-eq union","-pth 0.4","-k $KEY"])
        p2.wait()
        print("--------------end prune train model -----------------\n")
    except Exception as e:
        print(e)

def retrain_prune_model():
    # !tao classification train -e $SPECS_DIR/classification_retrain_spec.cfg \
    #                   -r $USER_EXPERIMENT_DIR/output_retrain \
    #                   -k $KEY
    try:
        print("------------- start Retrain model start -------------------\n")

        p1=subprocess.Popen(["tao","classification","train","-e $SPECS_DIR/classification_retrain_spec.cfg","-r $SPECS_DIR/output_retrain","-k $KEY"])
        p1.wait()
        print("---------end retrain prune model -------------\n")
    except Exception as e:
        print(e)
    return 0

def test_model():
    #!tao classification evaluate -e $SPECS_DIR/classification_retrain_spec.cfg -k $KEY
    try:
        print("------------- test model start -------------------\n")

        p1=subprocess.Popen(["tao","classification","evaluate","-e $SPECS_DIR/classification_retrain_spec.cfg","-k $KEY"])
        p1.wait()
        print("------------------test model complete------------\n")
    except Exception as e:
        print(e)
    return 0



def export_model():
    #!tao classification export \
            # -m $USER_EXPERIMENT_DIR/output_retrain/weights/resnet_$EPOCH.tlt \
            # -o $USER_EXPERIMENT_DIR/export/final_model.etlt \
            # -k $KEY
    try:
        EPOCH="010"
        print("------------- export start -------------------\n")

        p1=subprocess.Popen(["tao","classification","export",f"-m $SPECS_DIR/output_retrain/weights/resnet_{EPOCH}.tlt","-o $SPECS_DIR/export/final_model.etlt","-k $KEY"])
        p1.wait()
        print("-------------------expot model -----------------\n")
    except Exception as e:
        print(e)
    return 0




    
configruation_docker_path()
train_mode()
evaluate()
prune_train_model("010")
retrain_prune_model()
test_model()
export_model()