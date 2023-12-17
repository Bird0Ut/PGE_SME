import plantuml
import sys
import os

def pr_red(skk): print("\033[91m {}\033[00m" .format(skk)) 
def pr_green(skk): print("\033[92m {}\033[00m" .format(skk))

def get_current_directory():
    script_path = os.path.realpath(__file__)
    script_directory = os.path.dirname(script_path)
    return script_directory

def generate_images(filename, outdir, server='http://www.plantuml.com/plantuml/img/'):
    pl = plantuml.PlantUML(server)
    result = pl.processes_file(filename, outfile=None, errorfile=None, directory=outdir)
    return result

def get_txt_files(directory):
    txt_files = []
    
    for file in os.listdir(directory):
        if file.endswith(".txt") and os.path.isfile(os.path.join(directory, file)):
            txt_files.append(file)
            
    return txt_files

umlfiles = get_txt_files(get_current_directory()+"/memory")

for umlfile in umlfiles :
    if generate_images(get_current_directory()+"/memory"+ "/" + umlfile , get_current_directory()):
        pr_green(umlfile)
    else:
        pr_red(umlfile)
