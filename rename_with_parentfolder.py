import os 
import shutil





my_path="/media/sf_vboxshare/videos/vids/"
new_path="/media/sf_vboxshare/videos/images2/"

my_files=os.listdir(my_path)
print("\nList of files in my path: ")
print(my_files)

for this_folder in my_files:
    if os.path.isdir(my_path+this_folder):  
        this_path=my_path+this_folder
        files_in_path=os.listdir(this_path)
        print(f'there are {len(files_in_path)} files in {this_path} \n')
        for this_file in files_in_path:
            my_src=this_path+"/"+this_file
            my_dst=new_path+this_folder[:17]+" -"+this_file
            print(f'copying {my_src} into {my_dst} \n')
            #os.rename(my_src, my_dst)
            shutil.copyfile(my_src, my_dst)

