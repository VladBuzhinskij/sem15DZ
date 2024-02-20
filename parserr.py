from collections import namedtuple
import os
import logging
logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")


def check_dir(dir):
    return os.path.exists(dir)



def pars_dir(dir):
    dir = os.path.normpath(dir)
    if check_dir(dir):
        listt=os.listdir(dir)
        nt=namedtuple("nt","name type dir name_high_dir")
        res=()
        for direct in listt:
            typef=os.path.splitext(direct)
            high_dir=(os.path.split(dir))
            if_file=os.path.isfile(os.path.join(dir, direct))
            flag_dir=True
            if if_file: 
                flag_dir=False
            else: pars_dir(os.path.join(dir, direct))
            res=nt(direct,typef[1],flag_dir,high_dir[1])
            logging.info(res)
        return "Логи сохранены в файл py_log.log"
    else: return "Директории не существует"


def parser():
    dir=input("Ведите путь к директории: ")
    print(pars_dir(dir))





