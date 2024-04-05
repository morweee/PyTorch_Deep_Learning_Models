from code.MLP_code.Dataset_Loader import Dataset_Loader
from code.MLP_code.Method_MLP import Method_MLP
from code.MLP_code.Result_Saver import Result_Saver
from code.MLP_code.Setting_KFold_CV import Setting_KFold_CV
from code.MLP_code.Setting_Train_Test_Split import Setting_Train_Test_Split
from code.MLP_code.Evaluate_Accuracy import Evaluate_Accuracy
import numpy as np
import torch


#---- Multi-Layer Perceptron script ----
if 1:
    #---- parameter section -------------------------------
    np.random.seed(2)
    torch.manual_seed(2)
    #------------------------------------------------------

    # ---- objection initialization setction ---------------
    data_obj = Dataset_Loader('stage 2', '')
    data_obj.dataset_train_source_folder_path = '../../data/MLP_data/'
    data_obj.dataset_train_source_file_name = 'train.csv'
    data_obj.dataset_test_source_folder_path = '../../data/MLP_data/'
    data_obj.dataset_test_source_file_name = 'test.csv'

    method_obj = Method_MLP('multi-layer perceptron', '')

    result_obj = Result_Saver('saver', '')
    result_obj.result_destination_folder_path = '../../result/MLP_result/MLP_'
    result_obj.result_destination_file_name = 'prediction_result'

    setting_obj = Setting_Train_Test_Split('k fold cross validation', '')
    #setting_obj = Setting_Tra
    # in_Test_Split('train test split', '')

    evaluate_obj = Evaluate_Accuracy('accuracy', '')
    # ------------------------------------------------------

    # ---- running section ---------------------------------
    print('************ Start ************')
    setting_obj.prepare(data_obj, method_obj, result_obj, evaluate_obj)
    setting_obj.print_setup_summary()
    mean_score, std_score = setting_obj.load_run_save_evaluate()
    print('************ Overall Performance ************')
    print('MLP Accuracy: ' + str(mean_score) + ' +/- ' + str(std_score))
    print('************ Finish ************')
    # ------------------------------------------------------
    

    